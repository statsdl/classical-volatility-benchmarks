import importlib.util
import sys
from pathlib import Path


def load_benchmark_module():
    path = Path(__file__).resolve().parents[1] / "examples" / "run_classical_volatility_benchmarks.py"
    spec = importlib.util.spec_from_file_location("benchmark", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_synthetic_realized_measures_smoke():
    bm = load_benchmark_module()
    df = bm.synthetic_sv_jump_t(n=180, seed=0)
    measures = bm.realized_measures(df, window=10)
    assert {"RV", "RBV", "RTV", "TrueSD", "target"}.issubset(measures.columns)
    assert len(measures) > 50


def test_metrics_smoke():
    bm = load_benchmark_module()
    df = bm.synthetic_regime_garch(n=180, seed=1)
    measures = bm.realized_measures(df, window=10)
    target = measures["target"].iloc[80:]
    pred = measures["RV"].shift(1).iloc[80:].clip(lower=bm.EPS)
    y, f = bm.align_forecasts(target, pred)
    metrics = bm.forecast_metrics(y, f)
    assert "RMSE" in metrics
    assert metrics["RMSE"] >= 0
