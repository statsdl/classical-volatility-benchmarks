# Volatility Benchmark Results

Run the benchmark with `--outdir docs/results --github-report` to populate this folder with GitHub-rendered tables and visualizations.

Example:

```bash
python examples/run_classical_volatility_benchmarks.py \
  --mode synthetic \
  --synthetic-n 2200 \
  --realized-window 22 \
  --train-fraction 0.70 \
  --alpha 0.05 \
  --run-sensitivity \
  --outdir docs/results \
  --github-report
```
