from pathlib import Path
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import seaborn as sns
except Exception:
    sns = None


ROOT = Path(".").resolve()
RESULTS = ROOT / "docs" / "results"
SUMMARY = RESULTS / "summary_figures"
NAIVE_PATTERN = re.compile(r"naive", re.IGNORECASE)


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    return path


def remove_naive(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    out = df.copy()

    keep_cols = [c for c in out.columns if not NAIVE_PATTERN.search(str(c))]
    out = out[keep_cols]

    obj_cols = out.select_dtypes(include="object").columns
    if len(obj_cols) > 0:
        mask = out[obj_cols].astype(str).apply(
            lambda r: r.str.contains(NAIVE_PATTERN, na=False).any(), axis=1
        )
        out = out[~mask]

    return out.reset_index(drop=True)


def read_csv(name: str) -> pd.DataFrame:
    path = RESULTS / name
    if not path.exists():
        return pd.DataFrame()
    return remove_naive(pd.read_csv(path))


def format_value(x) -> str:
    if pd.isna(x):
        return ""

    try:
        x = float(x)
    except Exception:
        return str(x)

    if x == 0:
        return "0"

    ax = abs(x)

    if ax < 0.0001:
        return f"{x:.2e}"
    if ax < 0.001:
        return f"{x:.1e}"
    if ax < 0.01:
        return f"{x:.4f}"
    if ax < 1:
        return f"{x:.3f}"
    if ax < 10:
        return f"{x:.3g}"
    if ax < 100:
        return f"{x:.3g}"

    return f"{x:.2e}"


def text_color_for_value(value, mappable):
    try:
        rgba = mappable.cmap(mappable.norm(value))
        brightness = 0.299 * rgba[0] + 0.587 * rgba[1] + 0.114 * rgba[2]
        return "black" if brightness > 0.58 else "white"
    except Exception:
        return "black"


def add_80pct_annotations(ax, fig, pivot: pd.DataFrame, mappable):
    rows, cols = pivot.shape

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    bbox = ax.get_window_extent(renderer=renderer)

    cell_w_px = bbox.width / max(cols, 1)
    cell_h_px = bbox.height / max(rows, 1)

    max_text_w = 0.80 * cell_w_px
    max_text_h = 0.80 * cell_h_px

    for i in range(rows):
        for j in range(cols):
            value = pivot.iloc[i, j]
            label = format_value(value)

            if label == "":
                continue

            # Start reasonably large, then shrink until it fits 80% of the cell.
            fontsize = min(16.0, max_text_h * 72.0 / fig.dpi)

            txt = ax.text(
                j + 0.5,
                i + 0.5,
                label,
                ha="center",
                va="center",
                fontsize=fontsize,
                color=text_color_for_value(value, mappable),
            )

            fig.canvas.draw()
            tb = txt.get_window_extent(renderer=renderer)

            while (
                (tb.width > max_text_w or tb.height > max_text_h)
                and fontsize > 2.0
            ):
                fontsize *= 0.92
                txt.set_fontsize(fontsize)
                fig.canvas.draw()
                tb = txt.get_window_extent(renderer=renderer)


def heatmap_80pct(pivot: pd.DataFrame, title: str, path: Path, cmap: str):
    if pivot.empty:
        return

    pivot = pivot.copy()
    pivot = pivot.apply(pd.to_numeric, errors="coerce")

    rows, cols = pivot.shape

    fig_w = max(13.5, min(36, 4.0 + 1.55 * cols))
    fig_h = max(5.5, min(22, 2.6 + 0.95 * rows))

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))

    if sns is not None:
        hm = sns.heatmap(
            pivot,
            ax=ax,
            annot=False,
            cmap=cmap,
            linewidths=0.65,
            linecolor="white",
            cbar_kws={"shrink": 0.72, "pad": 0.02},
        )
        mappable = hm.collections[0]
    else:
        mappable = ax.imshow(pivot.values, aspect="auto")
        fig.colorbar(mappable, ax=ax, shrink=0.72)

    # Keep title and axis/tick labels visually consistent with the other plots.
    ax.set_title(title, fontsize=18, fontweight="bold", pad=18)
    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.set_xticks(np.arange(cols) + 0.5)
    ax.set_yticks(np.arange(rows) + 0.5)
    ax.set_xticklabels(pivot.columns, rotation=45, ha="right", fontsize=12)
    ax.set_yticklabels(pivot.index, rotation=0, fontsize=12)

    ax.tick_params(axis="both", which="major", labelsize=12)

    # Keep colorbar labels readable as well.
    try:
        cbar = mappable.colorbar
        cbar.ax.tick_params(labelsize=11)
    except Exception:
        pass

    add_80pct_annotations(ax, fig, pivot, mappable)

    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=240, bbox_inches="tight")
    plt.close(fig)


def rebuild_summary_heatmaps():
    ensure_dir(SUMMARY)

    for p in SUMMARY.glob("*heatmap*.png"):
        p.unlink()

    metrics = read_csv("all_forecast_metrics.csv")
    risk = read_csv("all_risk_metrics.csv")
    tests = read_csv("all_statistical_tests.csv")

    if not metrics.empty and {"Dataset", "Model"}.issubset(metrics.columns):
        if "RMSE" in metrics.columns:
            top_models = (
                metrics.groupby("Model")["RMSE"]
                .mean(numeric_only=True)
                .sort_values()
                .head(16)
                .index
                .tolist()
            )
        else:
            top_models = metrics["Model"].drop_duplicates().head(16).tolist()

        m = metrics[metrics["Model"].isin(top_models)].copy()

        for col, title, filename in [
            ("RMSE", "Forecast Accuracy Heatmap: RMSE", "summary_rmse_heatmap.png"),
            ("MAE", "Forecast Accuracy Heatmap: MAE", "summary_mae_heatmap.png"),
            ("QLIKE", "Forecast Accuracy Heatmap: QLIKE", "summary_qlike_heatmap.png"),
        ]:
            if col in m.columns:
                pivot = m.pivot_table(index="Dataset", columns="Model", values=col, aggfunc="mean")
                heatmap_80pct(pivot, title, SUMMARY / filename, cmap="viridis")

    if not risk.empty and {"Dataset", "Model"}.issubset(risk.columns):
        r = risk.copy()

        if "CovP" in r.columns:
            r["Coverage_Error"] = (pd.to_numeric(r["CovP"], errors="coerce") - 0.95).abs()

        if "CRPS" in r.columns:
            top_models = (
                r.groupby("Model")["CRPS"]
                .mean(numeric_only=True)
                .sort_values()
                .head(16)
                .index
                .tolist()
            )
        else:
            top_models = r["Model"].drop_duplicates().head(16).tolist()

        r = r[r["Model"].isin(top_models)]

        for col, title, filename in [
            ("CRPS", "Risk Forecasting Heatmap: CRPS", "summary_crps_heatmap.png"),
            ("Coverage_Error", "Risk Calibration Heatmap: |CovP - 0.95|", "summary_coverage_error_heatmap.png"),
            ("CovP", "VaR Coverage Probability Heatmap", "summary_covp_heatmap.png"),
        ]:
            if col in r.columns:
                pivot = r.pivot_table(index="Dataset", columns="Model", values=col, aggfunc="mean")
                heatmap_80pct(pivot, title, SUMMARY / filename, cmap="magma")

    if not tests.empty and {"Dataset", "Model"}.issubset(tests.columns):
        pvalue_cols = [
            c for c in tests.columns
            if "pvalue" in c.lower() or "p_value" in c.lower()
        ]

        for col in pvalue_cols:
            tests[col] = pd.to_numeric(tests[col], errors="coerce")

        if pvalue_cols:
            valid = tests.dropna(subset=[pvalue_cols[0]])
            top_models = (
                valid.groupby("Model")[pvalue_cols[0]]
                .mean(numeric_only=True)
                .sort_values(ascending=False)
                .head(16)
                .index
                .tolist()
            )
            t = tests[tests["Model"].isin(top_models)].copy()
        else:
            t = tests.copy()

        for col in pvalue_cols:
            pivot = t.pivot_table(index="Dataset", columns="Model", values=col, aggfunc="mean")
            readable = col.replace("_", " ").title()
            filename = f"summary_{col.lower()}_heatmap.png"
            heatmap_80pct(pivot, f"Statistical Test Heatmap: {readable}", SUMMARY / filename, cmap="cividis")


def main():
    if not RESULTS.exists():
        raise SystemExit("docs/results not found. Run this from the repo root.")

    rebuild_summary_heatmaps()

    print("Done.")
    print("All summary heatmap values now dynamically fit inside 80% of each cell.")
    print("No benchmark results were rerun.")


if __name__ == "__main__":
    main()
