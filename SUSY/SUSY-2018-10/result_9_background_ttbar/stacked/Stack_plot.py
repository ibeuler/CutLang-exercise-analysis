import ROOT
import os
import ctypes
import csv
from pathlib import Path

# Avoid ROOT's web-based canvas (needs a browser to export images).
ROOT.gROOT.SetBatch(True)
ROOT.gEnv.SetValue("Canvas.Name", "TRootCanvas")
ROOT.gStyle.SetOptStat(0)

BASE_DIR = Path(__file__).resolve().parent
INPUTS_DIR = BASE_DIR / "inputs"
OUT_DIR = BASE_DIR / "out"
OUT_PDFS_DIR = OUT_DIR / "pdfs"
OUT_CSV_DIR = OUT_DIR / "csv"
OUT_LOG_DIR = OUT_DIR / "logscale"
OUT_LOG_PDFS_DIR = OUT_LOG_DIR / "pdfs"


def _pick_input_file(filename: str) -> str:
	"""Prefer inputs/<filename> if present; fall back to <filename> in base dir."""
	candidate = INPUTS_DIR / filename
	if candidate.exists():
		return str(candidate)
	return str(BASE_DIR / filename)


OUT_PDFS_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV_DIR.mkdir(parents=True, exist_ok=True)
OUT_LOG_PDFS_DIR.mkdir(parents=True, exist_ok=True)

ttbar = ROOT.TFile(_pick_input_file("ttbar.root"), "READ")
signal = ROOT.TFile(_pick_input_file("susy-signal.root"), "READ")

data = None
data_path = Path(_pick_input_file("data.root"))
if data_path.exists():
	data = ROOT.TFile(str(data_path), "READ")

regions = [
	"2JB",
	"2JBveto",
	"4JLowxB",
	"4JLowxBveto",
	"4JHighxB",
	"4JHighxBveto",
	"6JB",
	"6JBveto",
]


def _get_hist(root_file, hist_path: str):
	hist = root_file.Get(hist_path)
	if not hist:
		raise RuntimeError(f"Missing histogram: {hist_path}")
	# Work with a detached copy so styling doesn't mutate the file-owned object.
	cloned = hist.Clone(f"{hist.GetName()}__clone")
	cloned.SetDirectory(0)
	return cloned


def _style_hist(hist, *, fill_color: int, line_color: int = 1):
	hist.SetFillColor(fill_color)
	hist.SetLineColor(line_color)
	hist.SetLineWidth(2)


def _positive_min(hist) -> float | None:
	min_pos = None
	for i in range(1, hist.GetNbinsX() + 1):
		val = float(hist.GetBinContent(i))
		if val <= 0:
			continue
		if min_pos is None or val < min_pos:
			min_pos = val
	return min_pos


def _draw_stack_on_canvas(*, canvas, title: str, x_title: str, y_title: str, region: str, ttbar_hist, signal_hist, logy: bool = False):
	canvas.Clear()
	canvas.cd()
	canvas.SetTicks(1, 1)
	canvas.SetLogy(bool(logy))

	# Colors chosen to be readable in print.
	_style_hist(ttbar_hist, fill_color=ROOT.kOrange - 2, line_color=ROOT.kOrange + 3)
	_style_hist(signal_hist, fill_color=ROOT.kAzure - 9, line_color=ROOT.kAzure + 2)

	stack = ROOT.THStack(
		f"stack_{region}",
		f"{title} - {region};{x_title};{y_title}",
	)
	# Draw background first, then signal on top.
	stack.Add(ttbar_hist)
	stack.Add(signal_hist)

	max_val = max(float(ttbar_hist.GetMaximum()), float(signal_hist.GetMaximum()))
	if logy:
		min_tt = _positive_min(ttbar_hist)
		min_sig = _positive_min(signal_hist)
		mins = [v for v in (min_tt, min_sig) if v is not None]
		min_val = min(mins) if mins else 1e-3
		stack.SetMinimum(max(min_val * 0.5, 1e-6))
		stack.SetMaximum(max(max_val * 50.0, 1.0))
	else:
		stack.SetMinimum(0.0)
		stack.SetMaximum(max_val * 1.35)

	stack.Draw("hist")

	leg = ROOT.TLegend(0.62, 0.72, 0.88, 0.88)
	leg.SetBorderSize(0)
	leg.SetFillStyle(0)
	leg.SetHeader(f"Region: {region}")
	leg.AddEntry(ttbar_hist, "t#bar{t} (BG)", "f")
	leg.AddEntry(signal_hist, "SUSY signal", "f")
	leg.Draw()

	canvas.Modified()
	canvas.Update()

	# IMPORTANT: return references so PyROOT doesn't garbage-collect the
	# stack/legend before the caller prints the canvas to PDF.
	return stack, leg


def _make_multipage_pdf(*, out_pdf: str, title: str, x_title: str, y_title: str, ttbar_path: str, signal_path: str, logy: bool = False):
	canvas = ROOT.TCanvas("c", "c", 900, 700)
	canvas.Print(out_pdf + "[")

	for region in regions:
		ttbar_hist = _get_hist(ttbar, ttbar_path.format(region=region))
		signal_hist = _get_hist(signal, signal_path.format(region=region))
		stack, leg = _draw_stack_on_canvas(
			canvas=canvas,
			title=title,
			x_title=x_title,
			y_title=y_title,
			region=region,
			ttbar_hist=ttbar_hist,
			signal_hist=signal_hist,
			logy=logy,
		)
		# Keep stack/legend alive until AFTER printing this page.
		canvas.Print(out_pdf)
		del stack, leg

	canvas.Print(out_pdf + "]")
	canvas.Close()


def _integral_and_error(hist):
	err = ctypes.c_double(0.0)
	val = hist.IntegralAndError(1, hist.GetNbinsX(), err)
	return float(val), float(err.value)


def _print_cutflow_table(*, region: str, data_cutflow=None, ttbar_cutflow=None, signal_cutflow=None):
	col_names = ["Cut Name"]
	if data_cutflow is not None:
		col_names.append("DATA")
	if ttbar_cutflow is not None:
		col_names.append("ttbar")
	if signal_cutflow is not None:
		col_names.append("signal")

	print("_")
	print(f"Region: {region}")
	print("{:<30} {:<20} {:<20} {:<20}".format(*(col_names + [""] * (4 - len(col_names)))))
	print(" ")

	# Use whichever cutflow exists to define the bin labels.
	ref = data_cutflow or ttbar_cutflow or signal_cutflow
	if ref is None:
		print("(no cutflow histograms found)")
		return

	last_label = None
	last_bin = None
	for i in range(1, ref.GetNbinsX() + 1):
		cut_name = ref.GetXaxis().GetBinLabel(i)
		if not cut_name:
			continue
		if "Histo" in cut_name:
			continue

		row_vals = [cut_name]
		if data_cutflow is not None:
			row_vals.append((data_cutflow.GetBinContent(i), data_cutflow.GetBinError(i)))
		if ttbar_cutflow is not None:
			row_vals.append((ttbar_cutflow.GetBinContent(i), ttbar_cutflow.GetBinError(i)))
		if signal_cutflow is not None:
			row_vals.append((signal_cutflow.GetBinContent(i), signal_cutflow.GetBinError(i)))

		# Print in scientific notation like your example.
		line = "{:<30} ".format(row_vals[0])
		for (val, err) in row_vals[1:]:
			line += "{:.2e} +- {:.2e}     ".format(val, err)
			
		print(line.rstrip())

		last_label = cut_name
		last_bin = i

	print(" ")
	print("")
	print(f"{region} Region Final Yields:")
	if last_bin is not None:
		print(f"Final cut ({last_label}):")
		if data_cutflow is not None:
			print("  Data:   {:.4g} +- {:.4g}".format(data_cutflow.GetBinContent(last_bin), data_cutflow.GetBinError(last_bin)))
		if ttbar_cutflow is not None:
			print("  ttbar:  {:.4g} +- {:.4g}".format(ttbar_cutflow.GetBinContent(last_bin), ttbar_cutflow.GetBinError(last_bin)))
		if signal_cutflow is not None:
			print("  signal: {:.4g} +- {:.4g}".format(signal_cutflow.GetBinContent(last_bin), signal_cutflow.GetBinError(last_bin)))


def _print_region_summaries():
	cutflow_rows = []
	final_rows = []
	integral_rows = []

	for region in regions:
		data_cutflow = _get_hist(data, f"{region}/cutflow") if data is not None else None
		ttbar_cutflow = _get_hist(ttbar, f"{region}/cutflow")
		signal_cutflow = _get_hist(signal, f"{region}/cutflow")

		_print_cutflow_table(
			region=region,
			data_cutflow=data_cutflow,
			ttbar_cutflow=ttbar_cutflow,
			signal_cutflow=signal_cutflow,
		)

		# Collect cutflow rows for CSV (wide format).
		ref = data_cutflow or ttbar_cutflow or signal_cutflow
		last_label = None
		last_bin = None
		for i in range(1, ref.GetNbinsX() + 1):
			cut_name = ref.GetXaxis().GetBinLabel(i)
			if not cut_name:
				continue
			if "Histo" in cut_name:
				continue

			row = {
				"region": region,
				"bin": i,
				"cut": cut_name,
				"data": (data_cutflow.GetBinContent(i) if data_cutflow is not None else ""),
				"data_err": (data_cutflow.GetBinError(i) if data_cutflow is not None else ""),
				"ttbar": (ttbar_cutflow.GetBinContent(i) if ttbar_cutflow is not None else ""),
				"ttbar_err": (ttbar_cutflow.GetBinError(i) if ttbar_cutflow is not None else ""),
				"signal": (signal_cutflow.GetBinContent(i) if signal_cutflow is not None else ""),
				"signal_err": (signal_cutflow.GetBinError(i) if signal_cutflow is not None else ""),
			}
			cutflow_rows.append(row)
			last_label = cut_name
			last_bin = i

		if last_bin is not None:
			final_rows.append(
				{
					"region": region,
					"final_cut": last_label,
					"data": (data_cutflow.GetBinContent(last_bin) if data_cutflow is not None else ""),
					"data_err": (data_cutflow.GetBinError(last_bin) if data_cutflow is not None else ""),
					"ttbar": (ttbar_cutflow.GetBinContent(last_bin) if ttbar_cutflow is not None else ""),
					"ttbar_err": (ttbar_cutflow.GetBinError(last_bin) if ttbar_cutflow is not None else ""),
					"signal": (signal_cutflow.GetBinContent(last_bin) if signal_cutflow is not None else ""),
					"signal_err": (signal_cutflow.GetBinError(last_bin) if signal_cutflow is not None else ""),
				}
			)

		# Also print integrals of the plotted histograms (useful sanity check).
		meff_tt = _get_hist(ttbar, f"{region}/bincounts")
		meff_sig = _get_hist(signal, f"{region}/bincounts")
		mtl_tt = _get_hist(ttbar, f"{region}/hist_mtl")
		mtl_sig = _get_hist(signal, f"{region}/hist_mtl")

		meff_tt_val, meff_tt_err = _integral_and_error(meff_tt)
		meff_sig_val, meff_sig_err = _integral_and_error(meff_sig)
		mtl_tt_val, mtl_tt_err = _integral_and_error(mtl_tt)
		mtl_sig_val, mtl_sig_err = _integral_and_error(mtl_sig)

		print("Histogram integrals:")
		print("  Meff  ttbar:  {:.4g} +- {:.4g} | signal: {:.4g} +- {:.4g}".format(meff_tt_val, meff_tt_err, meff_sig_val, meff_sig_err))
		print("  MTL   ttbar:  {:.4g} +- {:.4g} | signal: {:.4g} +- {:.4g}".format(mtl_tt_val, mtl_tt_err, mtl_sig_val, mtl_sig_err))
		print("")

		integral_rows.extend(
			[
				{
					"region": region,
					"hist": "Meff",
					"sample": "ttbar",
					"value": meff_tt_val,
					"error": meff_tt_err,
				},
				{
					"region": region,
					"hist": "Meff",
					"sample": "signal",
					"value": meff_sig_val,
					"error": meff_sig_err,
				},
				{
					"region": region,
					"hist": "MTL",
					"sample": "ttbar",
					"value": mtl_tt_val,
					"error": mtl_tt_err,
				},
				{
					"region": region,
					"hist": "MTL",
					"sample": "signal",
					"value": mtl_sig_val,
					"error": mtl_sig_err,
				},
			]
		)

	# Write CSV outputs.
	with open(OUT_CSV_DIR / "cutflow_table.csv", "w", newline="") as f:
		writer = csv.DictWriter(
			f,
			fieldnames=["region", "bin", "cut", "data", "data_err", "ttbar", "ttbar_err", "signal", "signal_err"],
		)
		writer.writeheader()
		writer.writerows(cutflow_rows)

	with open(OUT_CSV_DIR / "final_yields_summary.csv", "w", newline="") as f:
		writer = csv.DictWriter(
			f,
			fieldnames=["region", "final_cut", "data", "data_err", "ttbar", "ttbar_err", "signal", "signal_err"],
		)
		writer.writeheader()
		writer.writerows(final_rows)

	with open(OUT_CSV_DIR / "hist_integrals_summary.csv", "w", newline="") as f:
		writer = csv.DictWriter(
			f,
			fieldnames=["region", "hist", "sample", "value", "error"],
		)
		writer.writeheader()
		writer.writerows(integral_rows)


_print_region_summaries()

_make_multipage_pdf(
	out_pdf=str(OUT_PDFS_DIR / "cutflow_plots.pdf"),
	title="Cutflow",
	x_title="Cutflow step",
	y_title="Events",
	ttbar_path="{region}/cutflow",
	signal_path="{region}/cutflow",
)

_make_multipage_pdf(
	out_pdf=str(OUT_LOG_PDFS_DIR / "cutflow_plots.pdf"),
	title="Cutflow",
	x_title="Cutflow step",
	y_title="Events",
	ttbar_path="{region}/cutflow",
	signal_path="{region}/cutflow",
	logy=True,
)

_make_multipage_pdf(
	out_pdf=str(OUT_PDFS_DIR / "Meff_plots.pdf"),
	title="M_{eff}",
	x_title="M_{eff} [GeV]",
	y_title="Events",
	ttbar_path="{region}/bincounts",
	signal_path="{region}/bincounts",
)

_make_multipage_pdf(
	out_pdf=str(OUT_LOG_PDFS_DIR / "Meff_plots.pdf"),
	title="M_{eff}",
	x_title="M_{eff} [GeV]",
	y_title="Events",
	ttbar_path="{region}/bincounts",
	signal_path="{region}/bincounts",
	logy=True,
)

_make_multipage_pdf(
	out_pdf=str(OUT_PDFS_DIR / "MTL_plots.pdf"),
	title=r"M_{T}^{\\ell}",
	x_title=r"M_{T}^{\\ell} [GeV]",
	y_title="Events",
	ttbar_path="{region}/hist_mtl",
	signal_path="{region}/hist_mtl",
)

_make_multipage_pdf(
	out_pdf=str(OUT_LOG_PDFS_DIR / "MTL_plots.pdf"),
	title=r"M_{T}^{\\ell}",
	x_title=r"M_{T}^{\\ell} [GeV]",
	y_title="Events",
	ttbar_path="{region}/hist_mtl",
	signal_path="{region}/hist_mtl",
	logy=True,
)

ttbar.Close()
signal.Close()

if data is not None:
	data.Close()
