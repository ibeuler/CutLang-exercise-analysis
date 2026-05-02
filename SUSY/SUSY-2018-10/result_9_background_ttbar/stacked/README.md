# stacked (ttbar vs SUSY signal)

This folder contains a small ROOT/PyROOT plotting workflow that plots `ttbar` (background) and overlays a SUSY signal (as a dashed line) for several analysis regions. Log-scale plots use fixed y-axis limits (10^-1 to 10^6) for consistent cross-region comparison, except for cutflows.

## Inputs

Place ROOT files under `inputs/`:

- `inputs/ttbar.root`
- `inputs/susy-signal.root`
- (optional) `inputs/data.root`

The script expects these histogram paths to exist in both ROOT files:

- Cutflow: `{region}/cutflow`
- Meff: `{region}/bincounts`
- MTL: `{region}/hist_mtl`

Regions used by default:

- `2JB`, `2JBveto`, `4JLowxB`, `4JLowxBveto`, `4JHighxB`, `4JHighxBveto`, `6JB`, `6JBveto`

## Run

From this directory:

- Generate multipage plot PDFs + CSV summaries:
  - `python Stack_plot.py`
- Render CSV summaries into PDF tables:
  - `python render_pdf_tables_from_csv.py`

## Outputs

- Final PDFs (paper deliverables):
  - `out/pdfs/`: Multipage plots (linear scale) for cutflows, Meff, and MTL, as well as rendered PDF tables (cutflows, final yields, histogram integrals).
  - `out/logscale/pdfs/`: Log-scale versions of the plots.
- Intermediate CSVs: `out/csv/` (cutflow tables, final yields, and integrals).
- Optional snapshot artifacts: `artifacts/`

### Features of Plot Outputs
- **Signal Overlay:** The SUSY signal is overlaid as a dashed line with no fill (rather than stacked) on top of the solid `ttbar` background to prevent it from being hidden.
- **Log-Scale Consistency:** Fixed y-axis scaling (10^-1 to 10^6) is applied to all log-scale kinematic plots (Meff, MTL) to allow easy visual comparison across regions. Cutflow log plots retain dynamic scaling.
