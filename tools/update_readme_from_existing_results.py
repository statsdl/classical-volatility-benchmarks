from pathlib import Path
import re
import math
import shutil

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import seaborn as sns
except Exception:
    sns = None


ROOT = Path(".").resolve()
RESULTS = ROOT / "docs" / "results"
NAIVE_PATTERN = re.compile(r"naive", re.IGNORECASE)


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def remove_naive_from_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    out = df.copy()

    # Remove Naive columns, for example from forecasts.csv
    keep_cols = [c for c in out.columns if not NAIVE_PATTERN.search(str(c))]
    out = out[keep_cols]

    # Remove rows where Model/method/estimator columns contain Naive
    for col in out.columns:
        if col.lower() in {"model", "method", "estimator", "forecast", "name"}:
            out = out[~out[col].astype(str).str.contains(NAIVE_PATTERN, na=False)]

    # Extra safety: remove rows where any text cell contains Naive
    obj_cols = out.select_dtypes(include="object").columns
    if len(obj_cols) > 0:
        mask = out[obj_cols].astype(str).apply(
            lambda row: row.str.contains(NAIVE_PATTERN, na=False).any(), axis=1
        )
        out = out[~mask]

    return out.reset_index(drop=True)


def clean_existing_csvs():
    for path in RESULTS.rglob("*.csv"):
        try:
            df = pd.read_csv(path)
        except Exception:
            continue
        cleaned = remove_naive_from_dataframe(df)
        cleaned.to_csv(path, index=False)


def clean_markdown_files():
    for path in [ROOT / "README.md", RESULTS / "README.md", ROOT / "PYPI_README.md"]:
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        lines = [line for line in lines if not NAIVE_PATTERN.search(line)]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def delete_old_pngs():
    # Old figures may still have Naive in legends.
    # Delete them and rebuild figures only from cleaned CSVs.
    for path in RESULTS.rglob("*.png"):
        path.unlink()


def savefig(path: Path):
    ensure_dir(path.parent)
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()


def numeric_table(df: pd.DataFrame, cols):
    cols = [c for c in cols if c in df.columns]
    if not cols:
        return pd.DataFrame()
    out = df[cols].copy()
    for c in out.columns:
        if pd.api.types.is_numeric_dtype(out[c]):
            out[c] = out[c].map(lambda x: "" if pd.isna(x) else float(f"{x:.6g}"))
    return out


def plot_bar(df: pd.DataFrame, value: str, outdir: Path, prefix: str, title: str, top_n: int = 20):
    if df.empty or value not in df.columns or "Model" not in df.columns:
        return
    data = df.sort_values(value).head(top_n).copy()
    data = remove_naive_from_dataframe(data)
    if data.empty:
        return

    plt.figure(figsize=(12, max(5, 0.35 * len(data))))
    if sns is not None:
        sns.barplot(data=data, x=value, y="Model", orient="h")
    else:
        plt.barh(data["Model"], data[value])
        plt.gca().invert_yaxis()
    plt.title(title)
    plt.xlabel(value)
    plt.ylabel("Model")
    savefig(outdir / f"{prefix}_{value}.png")


def plot_actual_vs_forecast(dataset_dir: Path):
    forecasts_path = dataset_dir / "forecasts.csv"
    measures_path = dataset_dir / "realized_measures.csv"
    metrics_path = dataset_dir / "forecast_metrics.csv"

    if not forecasts_path.exists() or not measures_path.exists():
        return

    forecasts = pd.read_csv(forecasts_path)
    measures = pd.read_csv(measures_path)

    forecasts = remove_naive_from_dataframe(forecasts)
    measures = remove_naive_from_dataframe(measures)

    forecasts.to_csv(forecasts_path, index=False)
    measures.to_csv(measures_path, index=False)

    if forecasts.empty or measures.empty:
        return

    target_col = None
    for c in ["target", "RV", "TrueSD", "true_sigma", "return"]:
        if c in measures.columns:
            target_col = c
            break
    if target_col is None:
        return

    metric_order = []
    if metrics_path.exists():
        metrics = remove_naive_from_dataframe(pd.read_csv(metrics_path))
        metrics.to_csv(metrics_path, index=False)
        if "Model" in metrics.columns and "RMSE" in metrics.columns:
            metric_order = metrics.sort_values("RMSE")["Model"].astype(str).tolist()

    model_cols = [c for c in forecasts.columns if c not in {"Unnamed: 0", "index", "date", "Date"}]
    model_cols = [c for c in model_cols if not NAIVE_PATTERN.search(c)]
    if metric_order:
        model_cols = [m for m in metric_order if m in model_cols] + [m for m in model_cols if m not in metric_order]

    model_cols = model_cols[:8]
    if not model_cols:
        return

    y = pd.to_numeric(measures[target_col], errors="coerce").dropna().tail(350)

    plt.figure(figsize=(14, 6))
    plt.plot(range(len(y)), y.values, label=f"Actual {target_col}", linewidth=2)

    for model in model_cols:
        s = pd.to_numeric(forecasts[model], errors="coerce").dropna().tail(len(y))
        if len(s) > 0:
            plt.plot(range(len(s)), s.values, label=model, linewidth=1.1)

    plt.title(f"{dataset_dir.name}: Actual vs Forecasted Volatility")
    plt.xlabel("Time")
    plt.ylabel("Volatility / realized measure")
    plt.legend(fontsize=8)
    savefig(dataset_dir / f"{dataset_dir.name}_actual_vs_forecast.png")


def rebuild_dataset_figures():
    for dataset_dir in RESULTS.iterdir():
        if not dataset_dir.is_dir():
            continue
        if dataset_dir.name in {"summary_figures", "sensitivity_figures"}:
            continue

        metrics_path = dataset_dir / "forecast_metrics.csv"
        risk_path = dataset_dir / "risk_metrics.csv"

        if metrics_path.exists():
            metrics = remove_naive_from_dataframe(pd.read_csv(metrics_path))
            metrics.to_csv(metrics_path, index=False)
            plot_bar(metrics, "RMSE", dataset_dir, dataset_dir.name, f"{dataset_dir.name}: RMSE comparison")
            plot_bar(metrics, "QLIKE", dataset_dir, dataset_dir.name, f"{dataset_dir.name}: QLIKE comparison")
            plot_bar(metrics, "MAE", dataset_dir, dataset_dir.name, f"{dataset_dir.name}: MAE comparison")

        if risk_path.exists():
            risk = remove_naive_from_dataframe(pd.read_csv(risk_path))
            risk.to_csv(risk_path, index=False)
            plot_bar(risk, "CRPS", dataset_dir, dataset_dir.name, f"{dataset_dir.name}: CRPS comparison")
            plot_bar(risk, "CovP", dataset_dir, dataset_dir.name, f"{dataset_dir.name}: VaR coverage probability")
            plot_bar(risk, "ES", dataset_dir, dataset_dir.name, f"{dataset_dir.name}: Expected Shortfall comparison")

        plot_actual_vs_forecast(dataset_dir)


def rebuild_summary_figures():
    figdir = ensure_dir(RESULTS / "summary_figures")

    metrics_path = RESULTS / "all_forecast_metrics.csv"
    risk_path = RESULTS / "all_risk_metrics.csv"

    metrics = pd.read_csv(metrics_path) if metrics_path.exists() else pd.DataFrame()
    risk = pd.read_csv(risk_path) if risk_path.exists() else pd.DataFrame()

    metrics = remove_naive_from_dataframe(metrics)
    risk = remove_naive_from_dataframe(risk)

    if not metrics.empty:
        metrics.to_csv(metrics_path, index=False)

        model_order = metrics.groupby("Model")["RMSE"].mean().sort_values().head(18).index.tolist()
        m = metrics[metrics["Model"].isin(model_order)]

        for value, title, filename in [
            ("RMSE", "RMSE by dataset and model", "summary_rmse_heatmap.png"),
            ("MAE", "MAE by dataset and model", "summary_mae_heatmap.png"),
            ("QLIKE", "QLIKE by dataset and model", "summary_qlike_heatmap.png"),
        ]:
            if value in m.columns:
                pivot = m.pivot_table(index="Dataset", columns="Model", values=value, aggfunc="mean")
                plt.figure(figsize=(max(12, 0.65 * len(pivot.columns)), max(4, 0.55 * len(pivot.index))))
                if sns is not None:
                    sns.heatmap(pivot, annot=True, fmt=".4g", cmap="viridis", linewidths=0.5)
                else:
                    plt.imshow(pivot.values, aspect="auto")
                    plt.colorbar(label=value)
                    plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=65, ha="right")
                    plt.yticks(range(len(pivot.index)), pivot.index)
                plt.title(title)
                savefig(figdir / filename)

        ranked = metrics.copy()
        ranked["RMSE_rank"] = ranked.groupby("Dataset")["RMSE"].rank(method="average")
        ranked = ranked[ranked["Model"].isin(model_order)]
        if not ranked.empty:
            plt.figure(figsize=(max(12, 0.65 * ranked["Model"].nunique()), 6))
            if sns is not None:
                sns.boxplot(data=ranked, x="Model", y="RMSE_rank")
                sns.stripplot(data=ranked, x="Model", y="RMSE_rank", color="black", alpha=0.45, size=3)
            else:
                ranked.boxplot(column="RMSE_rank", by="Model", rot=65)
            plt.xticks(rotation=65, ha="right")
            plt.title("Model rank distribution across datasets")
            plt.xlabel("Model")
            plt.ylabel("RMSE rank; lower is better")
            savefig(figdir / "summary_model_rank_boxplot.png")

    if not risk.empty:
        risk.to_csv(risk_path, index=False)

        model_order = risk.groupby("Model")["CRPS"].mean().sort_values().head(18).index.tolist()
        r = risk[risk["Model"].isin(model_order)]

        for value, title, filename in [
            ("CRPS", "CRPS by dataset and model", "summary_crps_heatmap.png"),
            ("CovP", "VaR coverage probability by dataset and model", "summary_covp_heatmap.png"),
            ("ES", "Expected Shortfall by dataset and model", "summary_es_heatmap.png"),
        ]:
            if value in r.columns:
                pivot = r.pivot_table(index="Dataset", columns="Model", values=value, aggfunc="mean")
                plt.figure(figsize=(max(12, 0.65 * len(pivot.columns)), max(4, 0.55 * len(pivot.index))))
                if sns is not None:
                    sns.heatmap(pivot, annot=True, fmt=".4g", cmap="magma", linewidths=0.5)
                else:
                    plt.imshow(pivot.values, aspect="auto")
                    plt.colorbar(label=value)
                    plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=65, ha="right")
                    plt.yticks(range(len(pivot.index)), pivot.index)
                plt.title(title)
                savefig(figdir / filename)

        if {"CRPS", "CovP"}.issubset(r.columns):
            plt.figure(figsize=(10, 7))
            if sns is not None:
                sns.scatterplot(data=r, x="CRPS", y="CovP", hue="Model", style="Dataset", s=85)
            else:
                for model, sub in r.groupby("Model"):
                    plt.scatter(sub["CRPS"], sub["CovP"], label=model)
                plt.legend(fontsize=8)
            plt.axhline(0.95, linestyle="--", linewidth=1, label="Nominal 95% coverage")
            plt.title("Risk trade-off: CRPS vs VaR coverage probability")
            plt.xlabel("CRPS; lower is better")
            plt.ylabel("Coverage probability")
            savefig(figdir / "summary_crps_covp_scatter.png")


def rebuild_sensitivity_figures():
    sens_path = RESULTS / "sensitivity_results.csv"
    if not sens_path.exists():
        return

    df = remove_naive_from_dataframe(pd.read_csv(sens_path))
    df.to_csv(sens_path, index=False)

    figdir = ensure_dir(RESULTS / "sensitivity_figures")
    if df.empty or "Model" not in df.columns:
        return

    if {"realized_window", "RMSE"}.issubset(df.columns):
        top = df.groupby("Model")["RMSE"].mean().sort_values().head(12).index.tolist()
        d = df[df["Model"].isin(top)]
        plt.figure(figsize=(11, 6))
        if sns is not None:
            sns.lineplot(data=d, x="realized_window", y="RMSE", hue="Model", marker="o", estimator="mean", errorbar=None)
        else:
            for model, sub in d.groupby("Model"):
                sub.groupby("realized_window")["RMSE"].mean().plot(marker="o", label=model)
            plt.legend(fontsize=8)
        plt.title("Sensitivity of RMSE to realized-volatility window")
        plt.xlabel("Realized-measure rolling window")
        plt.ylabel("Mean RMSE")
        savefig(figdir / "sensitivity_rmse_by_window.png")

    if {"alpha", "CovP"}.issubset(df.columns):
        top = df.groupby("Model")["CovP"].mean().sort_values(ascending=False).head(12).index.tolist()
        d = df[df["Model"].isin(top)]
        plt.figure(figsize=(11, 6))
        if sns is not None:
            sns.lineplot(data=d, x="alpha", y="CovP", hue="Model", marker="o", estimator="mean", errorbar=None)
        else:
            for model, sub in d.groupby("Model"):
                sub.groupby("alpha")["CovP"].mean().plot(marker="o", label=model)
            plt.legend(fontsize=8)
        plt.title("Sensitivity of VaR coverage probability to tail level")
        plt.xlabel("VaR/ES tail probability alpha")
        plt.ylabel("Coverage probability")
        savefig(figdir / "sensitivity_covp_by_alpha.png")

    if {"train_fraction", "CRPS"}.issubset(df.columns):
        top = df.groupby("Model")["CRPS"].mean().sort_values().head(12).index.tolist()
        d = df[df["Model"].isin(top)]
        plt.figure(figsize=(11, 6))
        if sns is not None:
            sns.lineplot(data=d, x="train_fraction", y="CRPS", hue="Model", marker="o", estimator="mean", errorbar=None)
        else:
            for model, sub in d.groupby("Model"):
                sub.groupby("train_fraction")["CRPS"].mean().plot(marker="o", label=model)
            plt.legend(fontsize=8)
        plt.title("Sensitivity of CRPS to train/test split")
        plt.xlabel("Training fraction")
        plt.ylabel("Mean CRPS")
        savefig(figdir / "sensitivity_crps_by_train_fraction.png")


def markdown_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "No rows available."

    out = df.copy()
    for c in out.columns:
        if pd.api.types.is_numeric_dtype(out[c]):
            out[c] = out[c].map(lambda x: "" if pd.isna(x) else f"{float(x):.6g}")

    return out.to_markdown(index=False)


def details_table(title: str, df: pd.DataFrame) -> str:
    return f"""<details open>
<summary><strong>{title}</strong></summary>

{markdown_table(df)}

</details>
"""


def collect_figures():
    pngs = sorted(RESULTS.rglob("*.png"))
    pngs = [p for p in pngs if not NAIVE_PATTERN.search(p.as_posix())]
    return pngs


def write_main_readme():
    lines = []

    lines.append("# Classical Volatility Benchmarks")
    lines.append("")
    lines.append("Classical volatility forecasting benchmarks with realized-volatility measures, GARCH-family models, realized GARCH-based models, risk evaluation, statistical tests, visualization, and sensitivity analysis.")
    lines.append("")
    lines.append("All tables and figures below are rendered directly in this README from the already-generated result files under `docs/results/`.")
    lines.append("")
    lines.append("## Main Capabilities")
    lines.append("")
    lines.append("- **Realized volatility measures**: RV, RBV, RTV, and TrueSD/proxy TrueSD.")
    lines.append("- **Classical volatility models**: HAR-RV, GARCH, GJR-GARCH, Threshold-GARCH/TARCH, FIGARCH, EGARCH, Generalized GARCH, and APGARCH/APARCH with multiple orders.")
    lines.append("- **Realized GARCH-based models**: RGARCH, ARMA-RGARCH, REGARCH, and ARMA-REGARCH under standardized Student's t innovations.")
    lines.append("- **Risk metrics**: VaR, ES, CRPS, and coverage probability.")
    lines.append("- **Statistical tests**: Kupiec unconditional coverage, Christoffersen independence/conditional coverage, Diebold-Mariano, and Ljung-Box tests.")
    lines.append("- **Synthetic datasets**: Three high-variation complex synthetic data generators.")
    lines.append("- **Visualization suite**: Forecast plots, risk plots, heatmaps, rank plots, and sensitivity plots using matplotlib and seaborn.")
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
    lines.append("## Results")
    lines.append("")

    metrics_path = RESULTS / "all_forecast_metrics.csv"
    risk_path = RESULTS / "all_risk_metrics.csv"
    tests_path = RESULTS / "all_statistical_tests.csv"
    sens_path = RESULTS / "sensitivity_results.csv"

    if metrics_path.exists():
        metrics = remove_naive_from_dataframe(pd.read_csv(metrics_path)).sort_values(["Dataset", "RMSE"])
        cols = [c for c in ["Dataset", "Model", "RMSE", "MAE", "MAPE", "NMAE", "QLIKE"] if c in metrics.columns]
        lines.append(details_table("Forecast accuracy results", numeric_table(metrics, cols)))
        lines.append("")

    if risk_path.exists():
        risk = remove_naive_from_dataframe(pd.read_csv(risk_path)).sort_values(["Dataset", "CRPS"])
        cols = [c for c in ["Dataset", "Model", "VaR", "ES", "CRPS", "CovP", "Exceptions", "N"] if c in risk.columns]
        lines.append(details_table("Risk metric results", numeric_table(risk, cols)))
        lines.append("")

    if tests_path.exists():
        tests = remove_naive_from_dataframe(pd.read_csv(tests_path))
        cols = [c for c in ["Dataset", "Model", "Kupiec_LR", "Kupiec_pvalue", "Christoffersen_LR", "Christoffersen_pvalue", "DM_stat", "DM_pvalue", "LB_stat", "LB_pvalue"] if c in tests.columns]
        lines.append(details_table("Statistical test results", numeric_table(tests, cols)))
        lines.append("")

    if sens_path.exists():
        sens = remove_naive_from_dataframe(pd.read_csv(sens_path))
        sort_cols = [c for c in ["Dataset", "realized_window", "alpha", "train_fraction", "RMSE"] if c in sens.columns]
        if sort_cols:
            sens = sens.sort_values(sort_cols)
        cols = [c for c in ["Dataset", "realized_window", "alpha", "train_fraction", "Model", "RMSE", "MAE", "QLIKE", "CRPS", "CovP"] if c in sens.columns]
        lines.append(details_table("Sensitivity analysis results", numeric_table(sens, cols)))
        lines.append("")

    lines.append("## Visual Results")
    lines.append("")
    lines.append("The following diagrams are displayed directly in the GitHub README interface.")
    lines.append("")

    figures = collect_figures()
    for png in figures:
        rel = png.relative_to(ROOT).as_posix()
        title = png.stem.replace("_", " ").title()
        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"![{title}]({rel})")
        lines.append("")

    lines.append("## Test")
    lines.append("")
    lines.append("```bash")
    lines.append("python -m pytest")
    lines.append("```")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("This repository is released under the MIT License.")
    lines.append("")

    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")

    # Keep docs/results README simple, so the root README is the main interface.
    (RESULTS / "README.md").write_text(
        "# Results\n\nAll result tables and diagrams are displayed in the main repository `README.md`.\n",
        encoding="utf-8",
    )


def remove_naive_from_future_script():
    script = ROOT / "examples" / "run_classical_volatility_benchmarks.py"
    if not script.exists():
        return

    s = script.read_text(encoding="utf-8")

    # Remove Naive from future runs without deleting the function definition.
    s = s.replace('    forecasts["Naive-RV"] = forecast_naive(measures, train_size)\n', "")

    # Remove Naive references from text if any remain.
    s = "\n".join(line for line in s.splitlines() if not NAIVE_PATTERN.search(line)) + "\n"

    script.write_text(s, encoding="utf-8")


def main():
    if not RESULTS.exists():
        raise SystemExit("docs/results does not exist. Please run this from the repo after results are already generated.")

    clean_existing_csvs()
    clean_markdown_files()
    delete_old_pngs()
    rebuild_dataset_figures()
    rebuild_summary_figures()
    rebuild_sensitivity_figures()
    write_main_readme()
    remove_naive_from_future_script()

    print("Done.")
    print("Updated main README.md with result tables and diagrams.")
    print("Removed Naive/Naive-RV from CSV files, figures, README, and future benchmark script.")


if __name__ == "__main__":
    main()
