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
SENS = RESULTS / "sensitivity_figures"
NAIVE_PATTERN = re.compile(r"naive", re.IGNORECASE)


def ensure_dir(path: Path) -> Path:
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


def clean_csvs():
    for p in RESULTS.rglob("*.csv"):
        try:
            df = pd.read_csv(p)
        except Exception:
            continue
        remove_naive(df).to_csv(p, index=False)


def read_csv(name: str) -> pd.DataFrame:
    p = RESULTS / name
    if not p.exists():
        return pd.DataFrame()
    try:
        return remove_naive(pd.read_csv(p))
    except Exception:
        return pd.DataFrame()


def savefig(path: Path):
    ensure_dir(path.parent)
    plt.tight_layout()
    plt.savefig(path, dpi=220, bbox_inches="tight")
    plt.close()


def heatmap_plot(pivot: pd.DataFrame, title: str, path: Path, cmap: str = "viridis"):
    if pivot.empty:
        return

    rows, cols = pivot.shape
    fig_w = max(11, min(28, 2.2 + 0.95 * cols))
    fig_h = max(4.5, min(18, 2.0 + 0.62 * rows))

    annot_size = max(4.5, min(8.0, 80 / max(cols + rows, 1)))
    tick_size = max(6.0, min(9.0, 95 / max(cols, 1)))

    plt.figure(figsize=(fig_w, fig_h))

    if sns is not None:
        sns.heatmap(
            pivot,
            annot=True,
            fmt=".3g",
            cmap=cmap,
            linewidths=0.45,
            linecolor="white",
            annot_kws={"size": annot_size},
            cbar_kws={"shrink": 0.72, "pad": 0.02},
        )
    else:
        plt.imshow(pivot.values, aspect="auto")
        plt.colorbar(shrink=0.72)
        for i in range(rows):
            for j in range(cols):
                val = pivot.iloc[i, j]
                if pd.notna(val):
                    plt.text(j, i, f"{val:.3g}", ha="center", va="center", fontsize=annot_size)
        plt.xticks(range(cols), pivot.columns, rotation=45, ha="right")
        plt.yticks(range(rows), pivot.index)

    plt.title(title, fontsize=13)
    plt.xlabel("")
    plt.ylabel("")
    plt.xticks(rotation=45, ha="right", fontsize=tick_size)
    plt.yticks(rotation=0, fontsize=8)
    savefig(path)


def line_plot(df: pd.DataFrame, x: str, y: str, title: str, path: Path):
    if df.empty or x not in df.columns or y not in df.columns or "Model" not in df.columns:
        return

    top_models = (
        df.groupby("Model")[y]
        .mean(numeric_only=True)
        .sort_values()
        .head(12)
        .index
        .tolist()
    )
    d = df[df["Model"].isin(top_models)].copy()
    if d.empty:
        return

    plt.figure(figsize=(11, 6))
    if sns is not None:
        sns.lineplot(data=d, x=x, y=y, hue="Model", marker="o", estimator="mean", errorbar=None)
    else:
        for model, sub in d.groupby("Model"):
            sub.groupby(x)[y].mean().plot(marker="o", label=model)
        plt.legend(fontsize=8)

    plt.title(title)
    plt.xlabel(x.replace("_", " ").title())
    plt.ylabel(y)
    plt.legend(fontsize=8, ncol=2)
    savefig(path)


def rebuild_summary_heatmaps(metrics: pd.DataFrame, risk: pd.DataFrame, tests: pd.DataFrame):
    ensure_dir(SUMMARY)

    for p in SUMMARY.glob("*heatmap*.png"):
        p.unlink()
    for p in SUMMARY.glob("*rank*.png"):
        p.unlink()

    if not metrics.empty and {"Dataset", "Model"}.issubset(metrics.columns):
        top_models = (
            metrics.groupby("Model")["RMSE"]
            .mean(numeric_only=True)
            .sort_values()
            .head(16)
            .index
            .tolist()
            if "RMSE" in metrics.columns
            else metrics["Model"].drop_duplicates().head(16).tolist()
        )

        m = metrics[metrics["Model"].isin(top_models)].copy()

        for col, title, file in [
            ("RMSE", "Forecast Accuracy Heatmap: RMSE", "summary_rmse_heatmap.png"),
            ("MAE", "Forecast Accuracy Heatmap: MAE", "summary_mae_heatmap.png"),
            ("QLIKE", "Forecast Accuracy Heatmap: QLIKE", "summary_qlike_heatmap.png"),
        ]:
            if col in m.columns:
                pivot = m.pivot_table(index="Dataset", columns="Model", values=col, aggfunc="mean")
                heatmap_plot(pivot, title, SUMMARY / file, cmap="viridis")

    if not risk.empty and {"Dataset", "Model"}.issubset(risk.columns):
        r = risk.copy()

        if "CovP" in r.columns:
            r["Coverage_Error"] = (pd.to_numeric(r["CovP"], errors="coerce") - 0.95).abs()

        top_models = (
            r.groupby("Model")["CRPS"]
            .mean(numeric_only=True)
            .sort_values()
            .head(16)
            .index
            .tolist()
            if "CRPS" in r.columns
            else r["Model"].drop_duplicates().head(16).tolist()
        )

        r = r[r["Model"].isin(top_models)]

        for col, title, file in [
            ("CRPS", "Risk Forecasting Heatmap: CRPS", "summary_crps_heatmap.png"),
            ("Coverage_Error", "Risk Calibration Heatmap: |CovP - 0.95|", "summary_coverage_error_heatmap.png"),
            ("CovP", "VaR Coverage Probability Heatmap", "summary_covp_heatmap.png"),
        ]:
            if col in r.columns:
                pivot = r.pivot_table(index="Dataset", columns="Model", values=col, aggfunc="mean")
                heatmap_plot(pivot, title, SUMMARY / file, cmap="magma")

    if not tests.empty and {"Dataset", "Model"}.issubset(tests.columns):
        t = tests.copy()
        pvalue_cols = [c for c in t.columns if "pvalue" in c.lower() or "p_value" in c.lower()]
        for col in pvalue_cols[:3]:
            t[col] = pd.to_numeric(t[col], errors="coerce")

        if pvalue_cols:
            valid = t.dropna(subset=[pvalue_cols[0]])
            top_models = (
                valid.groupby("Model")[pvalue_cols[0]]
                .mean(numeric_only=True)
                .sort_values(ascending=False)
                .head(16)
                .index
                .tolist()
            )
            t = t[t["Model"].isin(top_models)]

        for col in pvalue_cols[:3]:
            pivot = t.pivot_table(index="Dataset", columns="Model", values=col, aggfunc="mean")
            readable = col.replace("_", " ").title()
            heatmap_plot(
                pivot,
                f"Statistical Test Heatmap: {readable}",
                SUMMARY / f"summary_{col.lower()}_heatmap.png",
                cmap="cividis",
            )


def rebuild_sensitivity_figures(sens: pd.DataFrame):
    ensure_dir(SENS)

    for p in SENS.glob("*.png"):
        p.unlink()

    if sens.empty:
        return

    line_plot(
        sens,
        "realized_window",
        "RMSE",
        "Sensitivity of RMSE to Realized-Volatility Window",
        SENS / "sensitivity_rmse_by_window.png",
    )

    line_plot(
        sens,
        "alpha",
        "CovP",
        "Sensitivity of VaR Coverage to Tail Probability",
        SENS / "sensitivity_covp_by_alpha.png",
    )

    line_plot(
        sens,
        "train_fraction",
        "CRPS",
        "Sensitivity of CRPS to Training Fraction",
        SENS / "sensitivity_crps_by_train_fraction.png",
    )


def rank_within_dataset(df: pd.DataFrame, metric: str, ascending: bool = True) -> pd.DataFrame:
    if df.empty or metric not in df.columns or not {"Dataset", "Model"}.issubset(df.columns):
        return pd.DataFrame()

    d = df[["Dataset", "Model", metric]].copy()
    d[metric] = pd.to_numeric(d[metric], errors="coerce")
    d = d.dropna(subset=[metric])
    if d.empty:
        return pd.DataFrame()

    d[f"{metric}_rank"] = d.groupby("Dataset")[metric].rank(method="average", ascending=ascending)
    return d[["Dataset", "Model", f"{metric}_rank"]]


def compute_average_ranks(metrics: pd.DataFrame, risk: pd.DataFrame, tests: pd.DataFrame) -> pd.DataFrame:
    rank_frames = []

    accuracy_metrics = ["RMSE", "MAE", "MAPE", "NMAE", "QLIKE"]
    for col in accuracy_metrics:
        r = rank_within_dataset(metrics, col, ascending=True)
        if not r.empty:
            r = r.rename(columns={f"{col}_rank": f"Accuracy_{col}_rank"})
            rank_frames.append(r)

    if not risk.empty:
        risk = risk.copy()
        if "CovP" in risk.columns:
            risk["Coverage_Error"] = (pd.to_numeric(risk["CovP"], errors="coerce") - 0.95).abs()

        for col in ["CRPS", "Coverage_Error"]:
            r = rank_within_dataset(risk, col, ascending=True)
            if not r.empty:
                r = r.rename(columns={f"{col}_rank": f"Risk_{col}_rank"})
                rank_frames.append(r)

    if not tests.empty:
        pvalue_cols = [c for c in tests.columns if "pvalue" in c.lower() or "p_value" in c.lower()]
        stat_cols = [c for c in tests.columns if c.lower().endswith("_lr") or c.lower().endswith("_stat")]

        for col in pvalue_cols:
            r = rank_within_dataset(tests, col, ascending=False)
            if not r.empty:
                r = r.rename(columns={f"{col}_rank": f"Statistical_{col}_rank"})
                rank_frames.append(r)

        for col in stat_cols:
            r = rank_within_dataset(tests, col, ascending=True)
            if not r.empty:
                r = r.rename(columns={f"{col}_rank": f"Statistical_{col}_rank"})
                rank_frames.append(r)

    if not rank_frames:
        return pd.DataFrame()

    merged = rank_frames[0]
    for r in rank_frames[1:]:
        merged = pd.merge(merged, r, on=["Dataset", "Model"], how="outer")

    rank_cols = [c for c in merged.columns if c.endswith("_rank")]

    accuracy_cols = [c for c in rank_cols if c.startswith("Accuracy_")]
    risk_cols = [c for c in rank_cols if c.startswith("Risk_")]
    stat_cols = [c for c in rank_cols if c.startswith("Statistical_")]

    out = merged[["Dataset", "Model"]].copy()

    if accuracy_cols:
        out["Accuracy Rank"] = merged[accuracy_cols].mean(axis=1)
    if risk_cols:
        out["Risk Rank"] = merged[risk_cols].mean(axis=1)
    if stat_cols:
        out["Statistical Rank"] = merged[stat_cols].mean(axis=1)

    component_cols = [c for c in ["Accuracy Rank", "Risk Rank", "Statistical Rank"] if c in out.columns]
    out["Overall Average Rank"] = out[component_cols].mean(axis=1)

    final = out.groupby("Model", as_index=False)[component_cols + ["Overall Average Rank"]].mean()
    final = final.sort_values("Overall Average Rank").reset_index(drop=True)
    final.insert(0, "Final Rank", np.arange(1, len(final) + 1))

    for c in final.columns:
        if c != "Model":
            final[c] = pd.to_numeric(final[c], errors="coerce").round(3)

    final.to_csv(RESULTS / "average_model_ranks.csv", index=False)
    return final


def markdown_table(df: pd.DataFrame, max_rows: int = 20) -> str:
    if df.empty:
        return "No average-rank table was available."

    d = df.head(max_rows).copy()
    cols = list(d.columns)

    def fmt(x):
        if pd.isna(x):
            return ""
        if isinstance(x, (float, np.floating)):
            return f"{x:.3f}"
        return str(x)

    lines = []
    lines.append("| " + " | ".join(cols) + " |")
    lines.append("| " + " | ".join(["---"] * len(cols)) + " |")
    for _, row in d.iterrows():
        lines.append("| " + " | ".join(fmt(row[c]) for c in cols) + " |")
    return "\n".join(lines)


def figure_block(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    title = path.stem.replace("_", " ").title()

    discussion = "This figure summarizes model behavior across datasets. Lower error-oriented values indicate stronger forecasting accuracy, while coverage-oriented plots should be interpreted relative to the nominal coverage level."

    lower = path.stem.lower()
    if "rmse" in lower or "mae" in lower or "qlike" in lower:
        discussion = "This accuracy diagram compares forecasting errors across datasets and models. Models with consistently smaller annotated values are more stable and accurate across volatility regimes."
    elif "crps" in lower:
        discussion = "This risk-scoring diagram summarizes the sharpness and calibration of probabilistic forecasts. Smaller CRPS values indicate stronger distributional forecasting performance."
    elif "coverage" in lower or "covp" in lower:
        discussion = "This coverage diagram evaluates VaR calibration. Values closer to the target coverage level indicate better risk-model reliability."
    elif "pvalue" in lower or "kupiec" in lower or "christoffersen" in lower:
        discussion = "This statistical-test diagram summarizes whether forecast violations are consistent with the expected risk level. Larger p-values generally indicate fewer signs of misspecification."
    elif "sensitivity" in lower:
        discussion = "This sensitivity diagram shows how model performance changes when the realized-volatility window, tail level, or train/test split is varied. Flatter curves indicate stronger robustness."

    return f"""### {title}

![{title}]({rel})

{discussion}
"""


def discussion_text(avg: pd.DataFrame) -> str:
    if avg.empty:
        return (
            "The overall comparison should be interpreted using the saved CSV files in `docs/results`. "
            "The README focuses on visual summaries and does not repeat the large result tables."
        )

    top = avg.head(3)["Model"].astype(str).tolist()
    top_text = ", ".join(top)

    best_accuracy = ""
    if "Accuracy Rank" in avg.columns:
        m = avg.sort_values("Accuracy Rank").iloc[0]["Model"]
        best_accuracy = f"For forecasting accuracy, `{m}` obtains the strongest average rank across the available error metrics. "

    best_risk = ""
    if "Risk Rank" in avg.columns:
        m = avg.sort_values("Risk Rank").iloc[0]["Model"]
        best_risk = f"For risk evaluation, `{m}` gives the best average risk rank after combining CRPS and coverage behavior. "

    best_stat = ""
    if "Statistical Rank" in avg.columns:
        m = avg.sort_values("Statistical Rank").iloc[0]["Model"]
        best_stat = f"For statistical-test behavior, `{m}` shows the strongest average rank across the available diagnostic tests. "

    return (
        f"Overall, the average-rank summary identifies `{top_text}` as the most competitive models across the available datasets. "
        f"{best_accuracy}{best_risk}{best_stat}"
        "The accuracy figures emphasize point-forecast precision, the risk figures evaluate VaR/ES-style calibration and probabilistic sharpness, "
        "and the statistical-test figures indicate whether exceedances and residual behavior are consistent with the model assumptions. "
        "Therefore, the preferred model is not necessarily the one with the smallest error in one dataset, but the one that remains accurate, risk-calibrated, and statistically stable across the full benchmark."
    )


def write_readme(avg: pd.DataFrame):
    figures = sorted(
        [p for p in RESULTS.rglob("*.png") if not NAIVE_PATTERN.search(p.as_posix())],
        key=lambda p: p.as_posix(),
    )

    preferred = []
    for folder in ["summary_figures", "sensitivity_figures"]:
        preferred.extend([p for p in figures if f"/{folder}/" in p.as_posix()])
    preferred.extend([p for p in figures if p not in preferred])

    lines = []

    lines.append("# Classical Volatility Benchmarks")
    lines.append("")
    lines.append("Classical volatility forecasting benchmarks for realized-volatility measures, GARCH-family models, realized GARCH-based models, risk evaluation, statistical tests, visualization, and sensitivity analysis.")
    lines.append("")
    lines.append("This README displays the generated diagrams directly in the GitHub interface. The full numerical CSV files remain available under `docs/results/`, but the large tables are intentionally not embedded here.")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("- **Realized volatility measures**: RV, RBV, RTV, and TrueSD/proxy TrueSD.")
    lines.append("- **Classical volatility models**: HAR-RV, GARCH, GJR-GARCH, Threshold-GARCH/TARCH, FIGARCH, EGARCH, Generalized GARCH, and APGARCH/APARCH.")
    lines.append("- **Realized GARCH-based models**: RGARCH, ARMA-RGARCH, REGARCH, and ARMA-REGARCH.")
    lines.append("- **Risk metrics**: VaR, ES, CRPS, and coverage probability.")
    lines.append("- **Statistical tests**: Kupiec, Christoffersen, Diebold-Mariano, and Ljung-Box tests.")
    lines.append("- **Sensitivity analysis**: realized-volatility window, tail probability, and train/test split.")
    lines.append("")
    lines.append("## Installation")
    lines.append("")
    lines.append("```bash")
    lines.append("git clone https://github.com/statsdl/classical-volatility-benchmarks.git")
    lines.append("cd classical-volatility-benchmarks")
    lines.append("python3 -m venv .venv")
    lines.append("source .venv/bin/activate")
    lines.append("python -m pip install --upgrade pip")
    lines.append("python -m pip install -e \".[dev]\"")
    lines.append("```")
    lines.append("")
    lines.append("## Visual Results and Discussion")
    lines.append("")

    for p in preferred:
        lines.append(figure_block(p))

    lines.append("## Overall Discussion")
    lines.append("")
    lines.append(discussion_text(avg))
    lines.append("")
    lines.append("The heatmaps compare models across datasets using compact annotations so that the values remain inside each cell. Accuracy metrics such as RMSE, MAE, and QLIKE should be minimized. Risk metrics such as CRPS should also be minimized, while coverage probability should remain close to the nominal level. Statistical diagnostics are interpreted jointly with the accuracy and risk metrics because a model can have low error but still produce poorly calibrated risk forecasts.")
    lines.append("")
    lines.append("## Conclusion")
    lines.append("")
    lines.append("The benchmark indicates that model choice should be based on a combined evaluation of forecasting accuracy, probabilistic risk quality, statistical validity, and robustness under sensitivity settings. The average-rank table below summarizes this combined evidence and is the compact replacement for the full tables.")
    lines.append("")
    lines.append("## Average Rank Summary")
    lines.append("")
    lines.append("Lower rank is better. The final rank combines the available accuracy, risk, and statistical-test ranks.")
    lines.append("")
    lines.append(markdown_table(avg, max_rows=25))
    lines.append("")
    lines.append("## Result Files")
    lines.append("")
    lines.append("The complete CSV tables are available in `docs/results/`:")
    lines.append("")
    lines.append("- `all_forecast_metrics.csv`")
    lines.append("- `all_risk_metrics.csv`")
    lines.append("- `all_statistical_tests.csv`")
    lines.append("- `sensitivity_results.csv`")
    lines.append("- `average_model_ranks.csv`")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("This repository is released under the MIT License.")
    lines.append("")

    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    (RESULTS / "README.md").write_text(
        "# Results\n\nThe full diagrams, discussion, conclusion, and average-rank summary are displayed in the main repository `README.md`. CSV files remain in this folder for reproducibility.\n",
        encoding="utf-8",
    )


def main():
    if not RESULTS.exists():
        raise SystemExit("docs/results was not found. Run this from the repository root after results already exist.")

    clean_csvs()

    metrics = read_csv("all_forecast_metrics.csv")
    risk = read_csv("all_risk_metrics.csv")
    tests = read_csv("all_statistical_tests.csv")
    sens = read_csv("sensitivity_results.csv")

    rebuild_summary_heatmaps(metrics, risk, tests)
    rebuild_sensitivity_figures(sens)

    avg = compute_average_ranks(metrics, risk, tests)
    write_readme(avg)

    print("Done.")
    print("Updated README.md without large result tables.")
    print("Rebuilt heatmaps with compact annotations.")
    print("Added discussion, conclusion, and average rank summary.")
    print("Created docs/results/average_model_ranks.csv.")


if __name__ == "__main__":
    main()
