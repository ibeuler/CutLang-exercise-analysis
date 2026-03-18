# stacked (ttbar vs SUSY signal)

This folder contains a small ROOT/PyROOT plotting workflow that stacks `ttbar` (background) and a SUSY signal for several analysis regions.

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

- Final PDFs (paper deliverables): `out/pdfs/`
- Intermediate CSVs: `out/csv/`
- Optional snapshot artifacts: `artifacts/`
