# Classical Volatility Benchmarks

A GitHub-ready repository for classical volatility forecasting benchmarks, realized-volatility modeling, realized GARCH-based models, risk evaluation, statistical testing, visualization, and sensitivity analysis.

The repository is designed so that result tables and plots can be committed directly under `docs/results/`, allowing GitHub to render the complete result report inside the repository.

## Main Capabilities

- **Realized volatility measures**: RV, RBV, RTV, and TrueSD/proxy TrueSD.
- **Classical and econometric volatility models**: HAR-RV, GARCH, GJR-GARCH, Threshold-GARCH/TARCH, FIGARCH, EGARCH, Generalized GARCH, APGARCH/APARCH with multiple orders.
- **Realized GARCH-based models**: RGARCH, ARMA-RGARCH, REGARCH, and ARMA-REGARCH under standardized Student's t innovations.
- **Risk metrics**: VaR, ES, CRPS, and coverage probability.
- **Statistical tests**: Kupiec unconditional coverage, Christoffersen independence/conditional coverage, Diebold-Mariano, and Ljung-Box tests.
- **Synthetic datasets**: Three high-variation complex synthetic data generators.
- **Online finance datasets**: Optional ticker download using `yfinance`.
- **Visualization suite**: Actual-vs-forecast plots, VaR/ES plots, heatmaps, rank boxplots, risk scatter plots, and sensitivity plots using `matplotlib` and `seaborn`.
- **Sensitivity analysis**: Realized-window sensitivity, VaR/ES alpha sensitivity, train/test split sensitivity, and model robustness summaries.

## Repository Layout

```text
.
├── README.md
├── pyproject.toml
├── requirements.txt
├── examples/
│   └── run_classical_volatility_benchmarks.py
├── docs/
│   └── results/
│       └── README.md
├── scripts/
│   └── commit_results_to_github.sh
├── tests/
│   └── test_benchmark_smoke.py
└── .github/
    └── workflows/
        └── tests.yml
```

## Installation

```bash
git clone https://github.com/statsdl/classical-volatility-benchmarks.git
cd classical-volatility-benchmarks

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Quick Synthetic Run

This runs all three synthetic datasets, produces model comparison tables, plots, statistical tests, and a GitHub-rendered report.

```bash
python examples/run_classical_volatility_benchmarks.py \
  --mode synthetic \
  --synthetic-n 2200 \
  --realized-window 22 \
  --train-fraction 0.70 \
  --alpha 0.05 \
  --outdir docs/results \
  --github-report
```

Open this file on GitHub after committing the results:

```text
docs/results/README.md
```

## Full Run with Sensitivity Analysis

This performs the main benchmark and then re-runs the benchmark over multiple realized windows, alpha levels, and train/test splits.

```bash
python examples/run_classical_volatility_benchmarks.py \
  --mode synthetic \
  --synthetic-n 2200 \
  --realized-window 22 \
  --train-fraction 0.70 \
  --alpha 0.05 \
  --run-sensitivity \
  --sensitivity-windows 10 22 44 \
  --sensitivity-alphas 0.01 0.025 0.05 \
  --sensitivity-train-fractions 0.60 0.70 0.80 \
  --outdir docs/results \
  --github-report
```

## Online Finance Run

```bash
python examples/run_classical_volatility_benchmarks.py \
  --mode online \
  --tickers SPY AAPL MSFT BTC-USD \
  --start 2018-01-01 \
  --realized-window 22 \
  --train-fraction 0.70 \
  --alpha 0.05 \
  --outdir docs/results \
  --github-report
```

## Combined Synthetic + Online Run

```bash
python examples/run_classical_volatility_benchmarks.py \
  --mode both \
  --tickers SPY AAPL MSFT BTC-USD \
  --start 2018-01-01 \
  --synthetic-n 2200 \
  --realized-window 22 \
  --train-fraction 0.70 \
  --alpha 0.05 \
  --run-sensitivity \
  --outdir docs/results \
  --github-report
```

## Output Files

After a run, the following files are created under `docs/results/`:

```text
all_forecast_metrics.csv
all_risk_metrics.csv
all_statistical_tests.csv
sensitivity_results.csv
summary_figures/*.png
sensitivity_figures/*.png
<dataset_name>/*.csv
<dataset_name>/*.png
README.md
```

The generated `docs/results/README.md` contains:

- forecast metric table,
- risk metric table,
- statistical test table,
- visualization gallery,
- sensitivity-analysis table,
- embedded plots that render directly on GitHub.

## Commit Results to GitHub

```bash
git add docs/results
git commit -m "Add classical volatility benchmarks results"
git push
```

Or use:

```bash
bash scripts/commit_results_to_github.sh
```

## Test

```bash
python -m pytest
```

## License

This repository is released under the MIT License.
