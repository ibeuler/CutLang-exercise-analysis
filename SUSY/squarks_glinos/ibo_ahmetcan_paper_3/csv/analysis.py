import os
import re
import math
import glob
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # headless backend for PNGs
import matplotlib.pyplot as plt

# Robust parser for values like "24816.0 ±157.53", "1234+/-56", plain numbers, or numeric cells
VAL_ERR_REGEX = re.compile(
    r'\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*(?:±|\+/-|\+-)\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*'
)

def parse_value_error_cell(x):
    if pd.isna(x):
        return (np.nan, np.nan)
    if isinstance(x, (int, float, np.number)):
        return (float(x), np.nan)
    s = str(x).strip()
    m = VAL_ERR_REGEX.fullmatch(s)
    if m:
        return (float(m.group(1)), float(m.group(2)))
    # try to split on ± variants anywhere in string
    for sep in ['±', '+/-', '+-']:
        if sep in s:
            parts = s.split(sep)
            try:
                v = float(parts[0].strip())
                e = float(parts[1].strip())
                return (v, e)
            except Exception:
                pass
    # plain number?
    try:
        return (float(s), np.nan)
    except Exception:
        return (np.nan, np.nan)

def parse_series_to_val_err(series: pd.Series):
    vals = []
    errs = []
    for x in series:
        v, e = parse_value_error_cell(x)
        vals.append(v)
        errs.append(e)
    vals = np.array(vals, dtype=float)
    errs = np.array(errs, dtype=float)
    # If all errs are nan or zeros, keep as nan/zero
    return vals, errs

def find_columns(df: pd.DataFrame):
    cols = [c for c in df.columns]

    paper_tokens = ['paper', 'atlas', 'reference', 'ref']
    ibrahim_tokens = ['ibeuler', 'ibrahim', 'ibo']
    ahmet_tokens = ['ahmetcan', 'ahmet']

    # Value columns
    value_cols = {}
    for c in cols:
        cl = c.lower()
        if any(t in cl for t in paper_tokens):
            value_cols['paper'] = c
        elif any(t in cl for t in ahmet_tokens) and 'selection' not in cl:
            value_cols['ahmetcan'] = c
        elif any(t in cl for t in ibrahim_tokens) and 'selection' not in cl:
            value_cols['ibrahim'] = c

    # Selection label columns
    sel_cols = {}
    for c in cols:
        cl = c.lower()
        # generic selection label like 'Selection in region X'
        if c == 'Selection' or cl == 'selection' or cl.startswith('selection '):
            sel_cols['generic'] = c
        # avoid picking numeric cutflow columns as labels
        if any(t in cl for t in ibrahim_tokens) and 'selection' in cl and 'cutflow' not in cl:
            sel_cols['ibrahim'] = c
        if any(t in cl for t in ahmet_tokens) and 'selection' in cl and 'cutflow' not in cl:
            sel_cols['ahmetcan'] = c

    # Fallbacks for selection if missing (fix: use 'ibrahim' key)
    if 'ibrahim' not in sel_cols and 'generic' in sel_cols:
        sel_cols['ibrahim'] = sel_cols['generic']
    if 'ahmetcan' not in sel_cols and 'generic' in sel_cols:
        sel_cols['ahmetcan'] = sel_cols['generic']

    # Positional fallbacks per your layout:
    # col 0: ibrahim selection, col 1: ibrahim cutflow
    # col 5: ahmetcan selection, col 6: ahmetcan cutflow
    ncols = len(cols)
    if 'ibrahim' not in value_cols and ncols >= 2:
        value_cols['ibrahim'] = cols[1]
    if 'ibrahim' not in sel_cols and ncols >= 1:
        sel_cols['ibrahim'] = cols[0]

    if 'ahmetcan' not in value_cols and ncols >= 7:
        value_cols['ahmetcan'] = cols[6]
    if 'ahmetcan' not in sel_cols and ncols >= 6:
        sel_cols['ahmetcan'] = cols[5]

    # Try to find paper if still missing (token-based only to avoid mistakes)
    # Users can add a manual mapping here if needed.

    return value_cols, sel_cols

def _pick_best_label_series(df: pd.DataFrame, sel_cols: dict, preferred=('generic','ibrahim','ahmetcan')):
    # Choose a text-like selection label column
    for key in preferred:
        col = sel_cols.get(key)
        if col is None:
            continue
        s = df.get(col)
        if s is None:
            continue
        # object dtype or clearly non-numeric looks like labels
        if s.dtype == object:
            return s
        # try detect if non-numeric strings
        try:
            _ = pd.to_numeric(s, errors='coerce')
            # if most are NaN after coercion, it's labels
            if _.isna().mean() > 0.7:
                return s.astype(str)
        except Exception:
            return s.astype(str)
    return None

def symmetric_percent(a, b):
    # Symmetric MAPE: 200*|a-b|/(|a|+|b|)
    denom = np.abs(a) + np.abs(b)
    sp = np.zeros_like(denom, dtype=float)
    # both zero -> 0, one zero -> 200%
    both_zero = (denom == 0)
    one_zero = (~both_zero) & ((np.abs(a) == 0) | (np.abs(b) == 0))
    normal = (~both_zero) & (~one_zero)
    sp[normal] = 200.0 * np.abs(a[normal] - b[normal]) / denom[normal]
    sp[one_zero] = 200.0
    sp[both_zero] = 0.0
    return sp

def analyze_pair(a_vals, a_errs, b_vals, b_errs):
    mask = np.isfinite(a_vals) & np.isfinite(b_vals)
    if not np.any(mask):
        return {
            'n': 0,
            'within_1sigma_rate': np.nan,
            'within_2sigma_rate': np.nan,
            'mean_symmetric_percent_diff': np.nan,
            'median_symmetric_percent_diff': np.nan,
            'rmse_percent_diff': np.nan,
            'mean_abs_pull': np.nan,
            'exact_match_rate': np.nan,
        }
    av = a_vals[mask]
    bv = b_vals[mask]
    ae = a_errs[mask]
    be = b_errs[mask]

    delta = av - bv
    # combined sigma; if any component is nan, treat as 0 for that side
    ae = np.nan_to_num(ae, nan=0.0)
    be = np.nan_to_num(be, nan=0.0)
    sigma = np.sqrt(ae**2 + be**2)
    with np.errstate(divide='ignore', invalid='ignore'):
        pull = np.where(sigma > 0, delta / sigma, np.nan)

    sp = symmetric_percent(av, bv)
    with np.errstate(invalid='ignore'):
        rmse = math.sqrt(np.nanmean((sp)**2)) if sp.size else np.nan

    within_1 = np.nanmean(np.abs(pull) <= 1.0) if np.any(np.isfinite(pull)) else np.nan
    within_2 = np.nanmean(np.abs(pull) <= 2.0) if np.any(np.isfinite(pull)) else np.nan
    exact = np.mean(np.isclose(av, bv, rtol=0.0, atol=1e-12))

    return {
        'n': int(mask.sum()),
        'within_1sigma_rate': within_1,
        'within_2sigma_rate': within_2,
        'mean_symmetric_percent_diff': float(np.nanmean(sp)),
        'median_symmetric_percent_diff': float(np.nanmedian(sp)),
        'rmse_percent_diff': rmse,
        'mean_abs_pull': float(np.nanmean(np.abs(pull))) if np.any(np.isfinite(pull)) else np.nan,
        'exact_match_rate': float(exact),
    }

# Text normalization for selection label matching
_norm_map = {
    '≥': '>=', '≤': '<=', '−': '-', '±': '+/-', '×': 'x',
    '&&': 'and', '||': 'or'
}
def normalize_label(s: str) -> str:
    if s is None:
        return ''
    t = str(s).lower().strip()
    for k, v in _norm_map.items():
        t = t.replace(k, v)
    # remove commas, collapse whitespace, normalize spaces around operators
    t = t.replace(',', ' ')
    t = re.sub(r'\s+', ' ', t)
    t = re.sub(r'\s*([()=<>+/*-])\s*', r'\1', t)
    return t

def compare_selections(a_sel: pd.Series, b_sel: pd.Series):
    if a_sel is None or b_sel is None:
        return np.nan, np.nan
    a = a_sel.fillna("").astype(str).str.strip()
    b = b_sel.fillna("").astype(str).str.strip()
    match_raw = float((a == b).mean())
    an = a.apply(normalize_label)
    bn = b.apply(normalize_label)
    match_norm = float((an == bn).mean())
    return match_raw, match_norm

def last_valid_val_err(vals: np.ndarray, errs: np.ndarray):
    idxs = np.where(np.isfinite(vals))[0]
    if idxs.size == 0:
        return (np.nan, np.nan, -1)
    idx = int(idxs[-1])
    v = float(vals[idx])
    e = float(errs[idx]) if idx < len(errs) and np.isfinite(errs[idx]) else np.nan
    return (v, e, idx)

def final_pair_metrics(a_val: float, a_err: float, b_val: float, b_err: float):
    if not np.isfinite(a_val) or not np.isfinite(b_val):
        return {'final_delta': np.nan, 'final_pull': np.nan, 'final_smape': np.nan, 'final_within_1sigma': np.nan}
    delta = a_val - b_val
    ae = 0.0 if not np.isfinite(a_err) else float(a_err)
    be = 0.0 if not np.isfinite(b_err) else float(b_err)
    sigma = math.sqrt(ae*ae + be*be)
    pull = (delta / sigma) if sigma > 0 else np.nan
    smape = float(symmetric_percent(np.array([a_val]), np.array([b_val]))[0])
    within1 = (abs(pull) <= 1.0) if np.isfinite(pull) else np.nan
    return {'final_delta': float(delta), 'final_pull': pull, 'final_smape': smape, 'final_within_1sigma': within1}

def analyze_file(path):
    df = pd.read_csv(path)
    value_cols, sel_cols = find_columns(df)

    # Map label -> (vals, errs, sel)
    series = {}
    generic_sel = _pick_best_label_series(df, sel_cols, preferred=('generic','ibrahim','ahmetcan'))

    if 'paper' in value_cols:
        pv, pe = parse_series_to_val_err(df[value_cols['paper']])
        paper_sel = df.get(sel_cols.get('generic')) if sel_cols.get('generic') in df.columns else generic_sel
        series['paper'] = (pv, pe, paper_sel)
    if 'ibrahim' in value_cols:
        iv, ie = parse_series_to_val_err(df[value_cols['ibrahim']])
        ib_sel = df.get(sel_cols.get('ibrahim')) if sel_cols.get('ibrahim') in df.columns else generic_sel
        series['ibrahim'] = (iv, ie, ib_sel if ib_sel is not None else generic_sel)
    else:
        print(f'[WARN] No ibrahim/ibeuler value column detected in {os.path.basename(path)}. Columns: {list(df.columns)}')
    if 'ahmetcan' in value_cols:
        av, ae = parse_series_to_val_err(df[value_cols['ahmetcan']])
        ah_sel = df.get(sel_cols.get('ahmetcan')) if sel_cols.get('ahmetcan') in df.columns else generic_sel
        series['ahmetcan'] = (av, ae, ah_sel if ah_sel is not None else generic_sel)

    pairs = [('ibrahim','paper'), ('ahmetcan','paper'), ('ibrahim','ahmetcan')]
    region = os.path.splitext(os.path.basename(path))[0].replace('cutflow_comparison_', '')
    results = []
    detail_rows = []

    # pairwise row-wise stats
    for a,b in pairs:
        if a not in series or b not in series:
            continue
        a_vals, a_errs, a_sel = series[a]
        b_vals, b_errs, b_sel = series[b]
        stats = analyze_pair(a_vals, a_errs, b_vals, b_errs)
        sel_match_raw, sel_match_norm = compare_selections(a_sel, b_sel)
        stats_row = {
            'file': os.path.basename(path),
            'region': region,
            'pair': f'{a}_vs_{b}',
            'selection_match_rate_raw': sel_match_raw,
            'selection_match_rate_norm': sel_match_norm,
            **stats
        }
        results.append(stats_row)

        # per-row details
        sel_label = generic_sel if generic_sel is not None else (a_sel if a_sel is not None else b_sel)
        ae = np.nan_to_num(a_errs, nan=0.0)
        be = np.nan_to_num(b_errs, nan=0.0)
        sigma = np.sqrt(ae**2 + be**2)
        with np.errstate(divide='ignore', invalid='ignore'):
            pull = np.where(sigma > 0, (a_vals - b_vals) / sigma, np.nan)
        sp = symmetric_percent(a_vals, b_vals)

        if a_sel is not None and b_sel is not None:
            raw_eq = a_sel.fillna("").astype(str).str.strip() == b_sel.fillna("").astype(str).str.strip()
            norm_eq = a_sel.fillna("").astype(str).apply(normalize_label) == b_sel.fillna("").astype(str).apply(normalize_label)
        else:
            raw_eq = pd.Series([np.nan]*len(a_vals))
            norm_eq = pd.Series([np.nan]*len(a_vals))

        detail = pd.DataFrame({
            'selection': sel_label,
            f'{a}_value': a_vals, f'{a}_err': a_errs,
            f'{b}_value': b_vals, f'{b}_err': b_errs,
            'delta': a_vals - b_vals,
            'pull': pull,
            'symmetric_percent_diff': sp,
            'label_match_raw': raw_eq.values,
            'label_match_norm': norm_eq.values,
        })
        detail_rows.append((f'{a}_vs_{b}', detail))

    # final yields per source + pairwise final metrics
    finals_row = {'file': os.path.basename(path), 'region': region}
    finals = {}
    for key in ('ibrahim','ahmetcan','paper'):
        if key in series:
            v, e, _ = series[key]
            fv, fe, _idx = last_valid_val_err(v, e)
            finals[key] = (fv, fe)
            finals_row[f'final_{key}_value'] = fv
            finals_row[f'final_{key}_err'] = fe
        else:
            finals_row[f'final_{key}_value'] = np.nan
            finals_row[f'final_{key}_err'] = np.nan

    # pairwise final metrics (delta, pull, sMAPE, within 1σ)
    for a,b in pairs:
        if a in finals and b in finals:
            av, ae = finals[a]
            bv, be = finals[b]
            m = final_pair_metrics(av, ae, bv, be)
            for k, v in m.items():
                finals_row[f'{a}_vs_{b}_{k}'] = v
            # ratios
            if np.isfinite(av) and np.isfinite(bv) and bv != 0:
                finals_row[f'{a}_over_{b}_ratio'] = float(av / bv)
            else:
                finals_row[f'{a}_over_{b}_ratio'] = np.nan

    # normalization reference for this file (prefer paper, else ibrahim, else ahmetcan)
    ref = None
    for cand in ('paper','ibrahim','ahmetcan'):
        v = finals_row.get(f'final_{cand}_value', np.nan)
        if np.isfinite(v) and v != 0:
            ref = cand
            break
    finals_row['final_norm_ref'] = ref if ref else ''

    if ref:
        ref_v = finals_row[f'final_{ref}_value']
        for s in ('ibrahim','ahmetcan','paper'):
            v = finals_row.get(f'final_{s}_value', np.nan)
            finals_row[f'final_{s}_norm'] = float(v / ref_v) if np.isfinite(v) and ref_v != 0 else np.nan
    else:
        for s in ('ibrahim','ahmetcan','paper'):
            finals_row[f'final_{s}_norm'] = np.nan

    return results, detail_rows, finals_row

def _plot_final_yields(df_final: pd.DataFrame, outdir: str):
    os.makedirs(outdir, exist_ok=True)

    # Grouped bars of final yields (absolute)
    sources = ['ibrahim','ahmetcan','paper']
    present = [s for s in sources if f'final_{s}_value' in df_final.columns]
    if present:
        dfp = df_final.copy().sort_values('region')
        x = np.arange(len(dfp))
        w = 0.8 / max(1, len(present))
        plt.figure(figsize=(max(9, len(dfp)*1.2), 4.5))
        for i, s in enumerate(present):
            plt.bar(x + i*w - 0.4 + w/2, dfp[f'final_{s}_value'].values, width=w, label=s)
            if f'final_{s}_err' in dfp.columns:
                yerr = dfp[f'final_{s}_err'].values
                plt.errorbar(x + i*w - 0.4 + w/2, dfp[f'final_{s}_value'].values, yerr=yerr, fmt='none', ecolor='k', capsize=2, lw=0.6)
        plt.xticks(x, dfp['region'], rotation=30, ha='right')
        plt.ylabel('Final yield (last cut)')
        plt.title('Final cutflow yields by region')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, 'final_yields_by_region.png'), dpi=150)
        plt.close()

        # Plot: all yields normalized to the final yield for each region
        # This requires reading the full cutflow for each region, not just the final summary
        # Try to load details for each region and plot normalized yields per cut
        details_dir = os.path.join(outdir, '../details')
        detail_files = glob.glob(os.path.join(details_dir, '*_ibrahim_vs_paper_details.csv'))
        if detail_files:
            for detail_path in detail_files:
                df_detail = pd.read_csv(detail_path)
                region = os.path.basename(detail_path).split('_ibrahim_vs_paper_details.csv')[0]
                # For each source, normalize all yields to the last yield
                for source in ['ibrahim', 'paper', 'ahmetcan']:
                    val_col = f'{source}_value'
                    if val_col in df_detail.columns:
                        vals = df_detail[val_col].values
                        if np.isfinite(vals).any():
                            last_idx = np.where(np.isfinite(vals))[0][-1]
                            final_val = vals[last_idx] if last_idx >= 0 else np.nan
                            norm_vals = vals / final_val if np.isfinite(final_val) and final_val != 0 else np.full_like(vals, np.nan)
                            plt.plot(norm_vals, label=source)
                plt.xlabel('Cut index')
                plt.ylabel('Yield normalized to final')
                plt.title(f'Normalized yields per cut: {region}')
                plt.legend()
                plt.tight_layout()
                plt.savefig(os.path.join(outdir, f'normalized_yields_per_cut_{region}.png'), dpi=150)
                plt.close()

        # Plot: match/agreement between all but last yield (e.g., ratio or difference)
        # For each region, plot the ratio between sources for all cuts except the last
        if detail_files:
            for detail_path in detail_files:
                df_detail = pd.read_csv(detail_path)
                region = os.path.basename(detail_path).split('_ibrahim_vs_paper_details.csv')[0]
                # Only up to the penultimate cut
                n_cuts = len(df_detail)
                if n_cuts > 1:
                    idxs = np.arange(n_cuts-1)
                    for a, b in [('ibrahim', 'paper'), ('ahmetcan', 'paper'), ('ibrahim', 'ahmetcan')]:
                        a_vals = df_detail.get(f'{a}_value', np.full(n_cuts, np.nan))
                        b_vals = df_detail.get(f'{b}_value', np.full(n_cuts, np.nan))
                        # Avoid division by zero
                        ratios = np.divide(a_vals[:n_cuts-1], b_vals[:n_cuts-1], out=np.full(n_cuts-1, np.nan), where=(b_vals[:n_cuts-1]!=0))
                        plt.plot(idxs, ratios, label=f'{a}/{b}')
                    plt.xlabel('Cut index (except last)')
                    plt.ylabel('Yield ratio')
                    plt.title(f'Yield ratios per cut (except last): {region}')
                    plt.legend()
                    plt.tight_layout()
                    plt.savefig(os.path.join(outdir, f'yield_ratios_per_cut_except_last_{region}.png'), dpi=150)
                    plt.close()
    # Normalized final yields (reference=1)
    norm_present = [s for s in sources if f'final_{s}_norm' in df_final.columns]
    if norm_present:
        dfp = df_final.copy().sort_values('region')
        x = np.arange(len(dfp))
        w = 0.8 / max(1, len(norm_present))
        plt.figure(figsize=(max(9, len(dfp)*1.2), 4.5))
        for i, s in enumerate(norm_present):
            plt.bar(x + i*w - 0.4 + w/2, dfp[f'final_{s}_norm'].values, width=w, label=s)
        # y=1 ref line
        plt.axhline(1.0, color='k', lw=1, ls='--')
        ref_lbls = dfp.get('final_norm_ref', pd.Series(['']*len(dfp)))
        # show ref label in title if mostly constant
        ref_mode = ref_lbls.mode().iat[0] if not ref_lbls.empty else ''
        ref_txt = f' (ref={ref_mode})' if isinstance(ref_mode, str) and len(ref_mode) else ''
        plt.xticks(x, dfp['region'], rotation=30, ha='right')
        plt.ylabel('Final yield (normalized to 1)')
        plt.title(f'Normalized final yields by region{ref_txt}')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, 'normalized_final_yields_by_region.png'), dpi=150)
        plt.close()

    # Ratios to paper (if paper present)
    if 'final_paper_value' in df_final.columns:
        dfp = df_final.copy().sort_values('region')
        cols = []
        labels = []
        if 'ibrahim_vs_paper_final_delta' in dfp.columns and 'ibrahim_over_paper_ratio' in dfp.columns:
            cols.append('ibrahim_over_paper_ratio'); labels.append('ibrahim/paper')
        if 'ahmetcan_vs_paper_final_delta' in dfp.columns and 'ahmetcan_over_paper_ratio' in dfp.columns:
            cols.append('ahmetcan_over_paper_ratio'); labels.append('ahmetcan/paper')
        if cols:
            x = np.arange(len(dfp))
            w = 0.8 / max(1, len(cols))
            plt.figure(figsize=(max(9, len(dfp)*1.2), 4.5))
            for i, c in enumerate(cols):
                plt.bar(x + i*w - 0.4 + w/2, dfp[c].values, width=w, label=labels[i])
            plt.axhline(1.0, color='k', lw=1, ls='--')
            plt.xticks(x, dfp['region'], rotation=30, ha='right')
            plt.ylabel('Ratio to paper (last cut)')
            plt.title('Final ratios to paper by region')
            plt.legend()
            plt.tight_layout()
            plt.savefig(os.path.join(outdir, 'final_ratios_to_paper_by_region.png'), dpi=150)
            plt.close()

    # Final sMAPE for ibrahim vs ahmetcan across regions
    if 'ibrahim_vs_ahmetcan_final_smape' in df_final.columns:
        dfp = df_final.copy().sort_values('region')
        plt.figure(figsize=(9,4))
        plt.bar(dfp['region'], dfp['ibrahim_vs_ahmetcan_final_smape'])
        plt.xticks(rotation=30, ha='right')
        plt.ylabel('Final sMAPE (%)')
        plt.title('ibrahim vs ahmetcan final symmetric % diff')
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, 'final_smape_ibrahim_vs_ahmetcan.png'), dpi=150)
        plt.close()

def _plot_summary(df_sum: pd.DataFrame, outdir: str):
    os.makedirs(outdir, exist_ok=True)
    # Plot within-1sigma rate by region for each pair (if available)
    if {'region','pair','within_1sigma_rate'}.issubset(df_sum.columns):
        pairs = sorted(df_sum['pair'].dropna().unique())
        regions = sorted(df_sum['region'].dropna().unique())
        plt.figure(figsize=(max(10, len(regions)*1.2), 4.5))
        for i, p in enumerate(pairs):
            sub = df_sum[df_sum['pair'] == p].set_index('region').reindex(regions)
            plt.plot(regions, sub['within_1sigma_rate'], marker='o', label=p)
        plt.xticks(rotation=30, ha='right')
        plt.ylim(0, 1)
        plt.ylabel('Fraction within 1σ')
        plt.title('Within-1σ rate by region')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, 'within1sigma_by_region.png'), dpi=150)
        plt.close()

    # Plot mean symmetric percent diff by region for each pair (if available)
    if {'region','pair','mean_symmetric_percent_diff'}.issubset(df_sum.columns):
        pairs = sorted(df_sum['pair'].dropna().unique())
        regions = sorted(df_sum['region'].dropna().unique())
        plt.figure(figsize=(max(10, len(regions)*1.2), 4.5))
        for i, p in enumerate(pairs):
            sub = df_sum[df_sum['pair'] == p].set_index('region').reindex(regions)
            plt.plot(regions, sub['mean_symmetric_percent_diff'], marker='o', label=p)
        plt.xticks(rotation=30, ha='right')
        plt.ylabel('Mean sMAPE (%)')
        plt.title('Mean symmetric % diff by region')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, 'smape_by_region.png'), dpi=150)
        plt.close()

def main():
    # Base directory is the directory containing this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(base_dir, 'plots'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'details'), exist_ok=True)

    # Discover input CSV files
    csv_files = sorted(glob.glob(os.path.join(base_dir, 'cutflow_comparison_*.csv')))

    all_results = []
    all_finals = []
    details_dir = os.path.join(base_dir, 'details')

    for f in csv_files:
        print(f'Analyzing: {f}')
        res, details, finals_row = analyze_file(f)
        all_results.extend(res)
        all_finals.append(finals_row)
        stem = os.path.splitext(os.path.basename(f))[0]
        for pair_name, df_detail in details:
            out_path = os.path.join(details_dir, f'{stem}_{pair_name}_details.csv')
            df_detail.to_csv(out_path, index=False)

    if all_results:
        df_sum = pd.DataFrame(all_results)
        cols = [
            'file','region','pair',
            'selection_match_rate_raw','selection_match_rate_norm',
            'n','within_1sigma_rate','within_2sigma_rate',
            'mean_symmetric_percent_diff','median_symmetric_percent_diff',
            'rmse_percent_diff','mean_abs_pull','exact_match_rate'
        ]
        cols = [c for c in cols if c in df_sum.columns] + [c for c in df_sum.columns if c not in cols]
        df_sum = df_sum[cols]
        df_sum.to_csv(os.path.join(base_dir, 'cutflow_stats_summary.csv'), index=False)
        print('Saved: cutflow_stats_summary.csv')

        _plot_summary(df_sum, outdir=os.path.join(base_dir, 'plots'))
    else:
        print('No comparable pairs found in files.')

    if all_finals:
        df_final = pd.DataFrame(all_finals)
        # stable column order
        base_cols = ['file','region',
                     'final_ibrahim_value','final_ibrahim_err',
                     'final_ahmetcan_value','final_ahmetcan_err',
                     'final_paper_value','final_paper_err']
        pair_cols = []
        for a,b in [('ibrahim','ahmetcan'),('ibrahim','paper'),('ahmetcan','paper')]:
            for k in ['final_delta','final_pull','final_smape','final_within_1sigma']:
                c = f'{a}_vs_{b}_{k}'
                if c in df_final.columns:
                    pair_cols.append(c)
        ordered = [c for c in base_cols if c in df_final.columns] + pair_cols + [c for c in df_final.columns if c not in base_cols + pair_cols]
        df_final = df_final[ordered]
        df_final.to_csv(os.path.join(base_dir, 'final_yields_summary.csv'), index=False)
        print('Saved: final_yields_summary.csv')

        _plot_final_yields(df_final, outdir=os.path.join(base_dir, 'plots'))
    else:
        print('No final yield info to summarize.')

    all_results = []
    all_finals = []
    details_dir = os.path.join(base_dir, 'details')
    os.makedirs(details_dir, exist_ok=True)

    for f in csv_files:
        print(f'Analyzing: {f}')
        res, details, finals_row = analyze_file(f)
        all_results.extend(res)
        all_finals.append(finals_row)
        stem = os.path.splitext(os.path.basename(f))[0]
        for pair_name, df_detail in details:
            out_path = os.path.join(details_dir, f'{stem}_{pair_name}_details.csv')
            df_detail.to_csv(out_path, index=False)

    if all_results:
        df_sum = pd.DataFrame(all_results)
        cols = [
            'file','region','pair',
            'selection_match_rate_raw','selection_match_rate_norm',
            'n','within_1sigma_rate','within_2sigma_rate',
            'mean_symmetric_percent_diff','median_symmetric_percent_diff',
            'rmse_percent_diff','mean_abs_pull','exact_match_rate'
        ]
        cols = [c for c in cols if c in df_sum.columns] + [c for c in df_sum.columns if c not in cols]
        df_sum = df_sum[cols]
        df_sum.to_csv('cutflow_stats_summary.csv', index=False)
        print('Saved: cutflow_stats_summary.csv')
        # optional: print compact
        # print(df_sum.to_string(index=False))

        _plot_summary(df_sum, outdir=os.path.join(base_dir, 'plots'))
    else:
        print('No comparable pairs found in files.')

    if all_finals:
        df_final = pd.DataFrame(all_finals)
        # stable column order
        base_cols = ['file','region',
                     'final_ibrahim_value','final_ibrahim_err',
                     'final_ahmetcan_value','final_ahmetcan_err',
                     'final_paper_value','final_paper_err']
        pair_cols = []
        for a,b in [('ibrahim','ahmetcan'),('ibrahim','paper'),('ahmetcan','paper')]:
            for k in ['final_delta','final_pull','final_smape','final_within_1sigma']:
                c = f'{a}_vs_{b}_{k}'
                if c in df_final.columns:
                    pair_cols.append(c)
        ordered = [c for c in base_cols if c in df_final.columns] + pair_cols + [c for c in df_final.columns if c not in base_cols + pair_cols]
        df_final = df_final[ordered]
        df_final.to_csv('final_yields_summary.csv', index=False)
        print('Saved: final_yields_summary.csv')

        _plot_final_yields(df_final, outdir=os.path.join(base_dir, 'plots'))

if __name__ == '__main__':
    main()