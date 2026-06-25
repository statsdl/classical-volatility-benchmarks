#!/usr/bin/env python3
"""
Classical volatility forecasting and risk benchmark.

This script implements:
  - Realized volatility measures: RV, RBV, RTV, TrueSD/proxy TrueSD
  - HAR-RV forecasting
  - GARCH-family models: GARCH, GJR-GARCH, Threshold/TARCH, FIGARCH,
    EGARCH, Generalized GARCH orders, APGARCH/APARCH
  - Realized GARCH-based models: RGARCH, ARMA-RGARCH, REGARCH,
    ARMA-REGARCH with Student-t return innovations
  - VaR, ES, CRPS, coverage probability, Kupiec, Christoffersen,
    Diebold-Mariano, and Ljung-Box tests
  - Three high-variation synthetic datasets and optional online finance data
  - Detailed CSV outputs, visualizations, GitHub-ready reports, and sensitivity analysis

Recommended install:
  pip install numpy pandas scipy scikit-learn matplotlib seaborn statsmodels arch yfinance

Example synthetic run:
  python examples/run_classical_volatility_benchmarks.py --mode synthetic --outdir results/volatility_benchmark

Example online run:
  python examples/run_classical_volatility_benchmarks.py --mode online --tickers SPY AAPL BTC-USD --start 2018-01-01 --outdir results/volatility_benchmark_online
"""

from __future__ import annotations

import argparse
import math
import os
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from scipy import optimize, stats, special
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.diagnostic import acorr_ljungbox

import matplotlib.pyplot as plt

try:
    import seaborn as sns
except Exception:  # seaborn is optional; matplotlib fallback is used when unavailable
    sns = None

warnings.filterwarnings("ignore")

EPS = 1e-12


# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def ensure_dir(path: str | Path) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def safe_log(x: np.ndarray | pd.Series, eps: float = EPS) -> np.ndarray:
    return np.log(np.maximum(np.asarray(x, dtype=float), eps))


def clean_series(x: pd.Series) -> pd.Series:
    return pd.to_numeric(x, errors="coerce").replace([np.inf, -np.inf], np.nan).dropna()


def align_forecasts(target: pd.Series, forecast: pd.Series) -> Tuple[pd.Series, pd.Series]:
    df = pd.concat([target.rename("target"), forecast.rename("forecast")], axis=1)
    df = df.replace([np.inf, -np.inf], np.nan).dropna()
    return df["target"], df["forecast"].clip(lower=EPS)


def student_t_standardized_logpdf(z: np.ndarray, nu: float) -> np.ndarray:
    """Log pdf of standardized Student-t with variance one for nu > 2."""
    z = np.asarray(z, dtype=float)
    nu = max(float(nu), 2.05)
    return (
        special.gammaln((nu + 1.0) / 2.0)
        - special.gammaln(nu / 2.0)
        - 0.5 * np.log(np.pi * (nu - 2.0))
        - ((nu + 1.0) / 2.0) * np.log1p((z * z) / (nu - 2.0))
    )


# -----------------------------------------------------------------------------
# Synthetic datasets: three high-variation complex forms
# -----------------------------------------------------------------------------


def synthetic_sv_jump_t(n: int = 2200, seed: int = 0) -> pd.DataFrame:
    """Stochastic-volatility data with jumps and heavy-tailed innovations."""
    rng = np.random.default_rng(seed)
    log_sigma2 = np.zeros(n)
    log_sigma2[0] = np.log(0.04)
    jump_prob = 0.035
    for t in range(1, n):
        jump = rng.normal(0, 1.2) if rng.random() < jump_prob else 0.0
        log_sigma2[t] = -0.12 + 0.975 * log_sigma2[t - 1] + rng.normal(0, 0.28) + jump
    sigma = np.sqrt(np.exp(log_sigma2))
    z = rng.standard_t(df=5, size=n) / np.sqrt(5 / 3)
    jumps = rng.binomial(1, jump_prob, size=n) * rng.normal(0, 0.09, size=n)
    returns = sigma * z + jumps
    price = 100 * np.exp(np.cumsum(returns))
    return pd.DataFrame({"price": price, "return": returns, "true_sigma": sigma})


def synthetic_regime_garch(n: int = 2200, seed: int = 1) -> pd.DataFrame:
    """GARCH-like data with regime shifts and asymmetric shocks."""
    rng = np.random.default_rng(seed)
    returns = np.zeros(n)
    sigma2 = np.zeros(n)
    sigma2[0] = 0.04
    regimes = np.zeros(n)
    for t in range(1, n):
        regimes[t] = 1 if (500 < t < 900 or 1350 < t < 1700) else 0
        omega = 0.0008 if regimes[t] == 0 else 0.008
        alpha = 0.07 if regimes[t] == 0 else 0.14
        beta = 0.90 if regimes[t] == 0 else 0.80
        leverage = 0.08 * (returns[t - 1] < 0)
        sigma2[t] = omega + (alpha + leverage) * returns[t - 1] ** 2 + beta * sigma2[t - 1]
        sigma2[t] = float(np.clip(sigma2[t], 1e-6, 3.0))
        z = rng.standard_t(df=6) / np.sqrt(6 / 4)
        returns[t] = np.sqrt(sigma2[t]) * z
    price = 100 * np.exp(np.cumsum(returns))
    return pd.DataFrame({"price": price, "return": returns, "true_sigma": np.sqrt(sigma2)})


def synthetic_rough_long_memory(n: int = 2200, seed: int = 2) -> pd.DataFrame:
    """Long-memory/rough-volatility-like data with cyclic components."""
    rng = np.random.default_rng(seed)
    shocks = rng.normal(0, 1.0, n + 200)
    weights = np.array([(k + 1) ** (-0.42) for k in range(200)])
    weights = weights / np.sqrt(np.sum(weights**2))
    long_memory = np.convolve(shocks, weights, mode="valid")[:n]
    cycle = 0.8 * np.sin(np.linspace(0, 18 * np.pi, n)) + 0.5 * np.sin(np.linspace(0, 4 * np.pi, n))
    log_sigma = -2.1 + 0.42 * long_memory + 0.30 * cycle
    crisis = np.zeros(n)
    crisis[900:1100] = np.linspace(0, 1.2, 200)
    crisis[1100:1350] = np.linspace(1.2, 0, 250)
    sigma = np.exp(log_sigma + crisis)
    z = rng.standard_t(df=4.5, size=n) / np.sqrt(4.5 / 2.5)
    returns = sigma * z
    price = 100 * np.exp(np.cumsum(returns))
    return pd.DataFrame({"price": price, "return": returns, "true_sigma": sigma})


def make_synthetic_datasets(n: int, seed: int) -> Dict[str, pd.DataFrame]:
    return {
        "synthetic_sv_jump_t": synthetic_sv_jump_t(n=n, seed=seed),
        "synthetic_regime_garch": synthetic_regime_garch(n=n, seed=seed + 1),
        "synthetic_rough_long_memory": synthetic_rough_long_memory(n=n, seed=seed + 2),
    }


# -----------------------------------------------------------------------------
# Online data
# -----------------------------------------------------------------------------


def download_online_data(tickers: Sequence[str], start: str, end: Optional[str]) -> Dict[str, pd.DataFrame]:
    try:
        import yfinance as yf
    except ImportError as exc:
        raise ImportError("Install yfinance to use --mode online: pip install yfinance") from exc

    datasets: Dict[str, pd.DataFrame] = {}
    for ticker in tickers:
        raw = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
        if raw.empty:
            print(f"[WARN] No data downloaded for {ticker}")
            continue
        close = raw["Close"] if "Close" in raw else raw.iloc[:, 0]
        ret = np.log(close).diff().dropna()
        df = pd.DataFrame({"price": close.loc[ret.index], "return": ret})
        datasets[ticker.replace("/", "_").replace("-", "_")] = df.dropna()
    return datasets


# -----------------------------------------------------------------------------
# Realized volatility measures
# -----------------------------------------------------------------------------


def realized_measures(df: pd.DataFrame, window: int = 22) -> pd.DataFrame:
    """Compute RV, RBV, RTV, and TrueSD/proxy TrueSD.

    For daily online data, these are rolling realized proxies. For synthetic data,
    TrueSD uses the known latent sigma if available.
    """
    ret = clean_series(df["return"])
    out = pd.DataFrame(index=ret.index)
    out["return"] = ret

    rv = ret.pow(2).rolling(window).sum()
    rbv = (np.pi / 2.0) * (ret.abs() * ret.abs().shift(1)).rolling(window).sum()
    mu_43 = 2 ** (2 / 3) * math.gamma(7 / 6) / math.gamma(1 / 2)
    rtv = (mu_43 ** -3) * (
        ret.abs().pow(4 / 3) * ret.abs().shift(1).pow(4 / 3) * ret.abs().shift(2).pow(4 / 3)
    ).rolling(window).sum()

    out["RV"] = rv.clip(lower=EPS)
    out["RBV"] = rbv.clip(lower=EPS)
    out["RTV"] = rtv.clip(lower=EPS)
    if "true_sigma" in df.columns:
        true_sigma = pd.Series(df["true_sigma"], index=df.index).reindex(out.index)
        out["TrueSD"] = true_sigma.pow(2).rolling(window).mean().clip(lower=EPS)
    else:
        out["TrueSD"] = ret.rolling(window).std().pow(2).mul(window).clip(lower=EPS)
    out["target"] = out["RV"].shift(-1)
    return out.replace([np.inf, -np.inf], np.nan).dropna()


# -----------------------------------------------------------------------------
# Forecasting models
# -----------------------------------------------------------------------------




def forecast_har(measures: pd.DataFrame, train_size: int, ridge_alpha: float = 1e-6) -> pd.Series:
    rv = measures["RV"].clip(lower=EPS)
    features = pd.DataFrame(index=measures.index)
    features["RV_lag1"] = rv.shift(1)
    features["RV_week"] = rv.shift(1).rolling(5).mean()
    features["RV_month"] = rv.shift(1).rolling(22).mean()
    target = measures["target"]
    data = pd.concat([features, target.rename("target")], axis=1).dropna()
    train_idx = data.index[: max(20, train_size - (len(measures) - len(data)))]
    test_idx = data.index.difference(train_idx)
    model = Ridge(alpha=ridge_alpha)
    model.fit(data.loc[train_idx, features.columns], data.loc[train_idx, "target"])
    pred = pd.Series(model.predict(data.loc[test_idx, features.columns]), index=test_idx, name="HAR-RV")
    return pred.clip(lower=EPS)


def forecast_garch_family(
    returns: pd.Series,
    train_size: int,
    model_specs: Optional[List[Tuple[str, dict]]] = None,
) -> Dict[str, pd.Series]:
    try:
        from arch import arch_model
    except ImportError:
        print("[WARN] arch is not installed. Skipping GARCH-family models. Install with: pip install arch")
        return {}

    if model_specs is None:
        model_specs = [
            ("GARCH(1,1)-t", {"vol": "GARCH", "p": 1, "o": 0, "q": 1, "power": 2.0}),
            ("GARCH(1,2)-t", {"vol": "GARCH", "p": 1, "o": 0, "q": 2, "power": 2.0}),
            ("GARCH(2,1)-t", {"vol": "GARCH", "p": 2, "o": 0, "q": 1, "power": 2.0}),
            ("Generalized-GARCH(2,2)-t", {"vol": "GARCH", "p": 2, "o": 0, "q": 2, "power": 2.0}),
            ("GJR-GARCH(1,1)-t", {"vol": "GARCH", "p": 1, "o": 1, "q": 1, "power": 2.0}),
            ("Threshold-GARCH(1,1)-t", {"vol": "GARCH", "p": 1, "o": 1, "q": 1, "power": 1.0}),
            ("EGARCH(1,1)-t", {"vol": "EGARCH", "p": 1, "o": 1, "q": 1}),
            ("EGARCH(2,1)-t", {"vol": "EGARCH", "p": 2, "o": 1, "q": 1}),
            ("FIGARCH(1,1)-t", {"vol": "FIGARCH", "p": 1, "q": 1}),
            ("APGARCH/APARCH(1,1)-t", {"vol": "APARCH", "p": 1, "o": 1, "q": 1}),
            ("APGARCH/APARCH(2,1)-t", {"vol": "APARCH", "p": 2, "o": 1, "q": 1}),
        ]

    y = clean_series(returns) * 100.0
    forecasts: Dict[str, pd.Series] = {}
    for name, spec in model_specs:
        try:
            am = arch_model(y, mean="Zero", dist="StudentsT", rescale=False, **spec)
            res = am.fit(disp="off", last_obs=y.index[train_size - 1], show_warning=False)
            f = res.forecast(start=y.index[train_size], horizon=1, reindex=True)
            var = f.variance["h.1"].dropna() / 10000.0
            forecasts[name] = var.rename(name).clip(lower=EPS)
            print(f"[OK] {name}")
        except Exception as exc:
            print(f"[WARN] Skipped {name}: {exc}")
    return forecasts


# -----------------------------------------------------------------------------
# Realized GARCH-based models
# -----------------------------------------------------------------------------


@dataclass
class RealizedGarchResult:
    name: str
    params: np.ndarray
    success: bool
    loss: float
    forecast: pd.Series


def arma_residuals(y: pd.Series, train_size: int, order: Tuple[int, int]) -> pd.Series:
    p, q = order
    if p == 0 and q == 0:
        return y.copy()
    try:
        from statsmodels.tsa.statespace.sarimax import SARIMAX

        model = SARIMAX(y, order=(p, 0, q), trend="c", enforce_stationarity=False, enforce_invertibility=False)
        res = model.fit(disp=False, maxiter=300)
        resid = pd.Series(res.resid, index=y.index).dropna()
        return resid.reindex(y.index).fillna(y)
    except Exception as exc:
        print(f"[WARN] ARMA({p},{q}) residual extraction failed; using raw returns. Reason: {exc}")
        return y.copy()


def fit_rgarch_single(
    y: pd.Series,
    x: pd.Series,
    train_size: int,
    name: str = "RGARCH-t",
    arma_order: Tuple[int, int] = (0, 0),
) -> RealizedGarchResult:
    data = pd.concat([y.rename("y"), x.rename("x")], axis=1).replace([np.inf, -np.inf], np.nan).dropna()
    y0 = arma_residuals(data["y"], train_size, arma_order).reindex(data.index).fillna(data["y"]).values
    x0 = data["x"].clip(lower=EPS).values
    train_n = min(train_size, len(data) - 10)

    def unpack(theta: np.ndarray):
        omega = theta[0]
        beta = 1.0 / (1.0 + np.exp(-theta[1])) * 0.995
        gamma = theta[2]
        xi = theta[3]
        phi = theta[4]
        tau1 = theta[5]
        tau2 = theta[6]
        sigma_u = np.exp(theta[7]) + 1e-6
        nu = 2.05 + np.exp(theta[8])
        return omega, beta, gamma, xi, phi, tau1, tau2, sigma_u, nu

    def compute_logh(theta: np.ndarray, n: int) -> Tuple[np.ndarray, np.ndarray]:
        omega, beta, gamma, xi, phi, tau1, tau2, sigma_u, nu = unpack(theta)
        logx = safe_log(x0[:n])
        logh = np.zeros(n)
        z = np.zeros(n)
        logh[0] = np.mean(logx[: min(20, n)])
        for t in range(n):
            if t > 0:
                logh[t] = omega + beta * logh[t - 1] + gamma * logx[t - 1]
            h = np.exp(np.clip(logh[t], -30, 10))
            z[t] = y0[t] / np.sqrt(h + EPS)
        return logh, z

    def nll(theta: np.ndarray) -> float:
        logh, z = compute_logh(theta, train_n)
        omega, beta, gamma, xi, phi, tau1, tau2, sigma_u, nu = unpack(theta)
        h = np.exp(np.clip(logh, -30, 10))
        logx = safe_log(x0[:train_n])
        u = logx - (xi + phi * logh + tau1 * z + tau2 * (z * z - 1.0))
        ll_ret = student_t_standardized_logpdf(z, nu) - 0.5 * np.log(h)
        ll_meas = stats.norm.logpdf(u, loc=0.0, scale=sigma_u)
        loss = -np.sum(ll_ret + ll_meas)
        penalty = 1e-4 * np.sum(theta**2)
        return float(loss + penalty) if np.isfinite(loss) else 1e12

    init = np.array([
        -0.05,
        2.5,
        0.10,
        np.mean(safe_log(x0[:train_n])),
        0.80,
        -0.05,
        0.05,
        -2.0,
        np.log(8.0 - 2.05),
    ])
    try:
        opt = optimize.minimize(nll, init, method="Nelder-Mead", options={"maxiter": 2500, "xatol": 1e-5, "fatol": 1e-5})
        theta = opt.x
        logh, _ = compute_logh(theta, len(data))
        pred = pd.Series(np.exp(np.clip(logh, -30, 10)), index=data.index, name=name).shift(1).iloc[train_n:]
        return RealizedGarchResult(name, theta, bool(opt.success), float(opt.fun), pred.clip(lower=EPS))
    except Exception as exc:
        print(f"[WARN] {name} failed: {exc}")
        empty = pd.Series(dtype=float, name=name)
        return RealizedGarchResult(name, init, False, np.inf, empty)


def fit_regarch_multi(
    y: pd.Series,
    X: pd.DataFrame,
    train_size: int,
    name: str = "REGARCH-t",
    arma_order: Tuple[int, int] = (0, 0),
) -> RealizedGarchResult:
    data = pd.concat([y.rename("y"), X], axis=1).replace([np.inf, -np.inf], np.nan).dropna()
    measure_cols = list(X.columns)
    K = len(measure_cols)
    y0 = arma_residuals(data["y"], train_size, arma_order).reindex(data.index).fillna(data["y"]).values
    X0 = data[measure_cols].clip(lower=EPS).values
    train_n = min(train_size, len(data) - 10)

    def unpack(theta: np.ndarray):
        idx = 0
        omega = theta[idx]; idx += 1
        beta = 1.0 / (1.0 + np.exp(-theta[idx])) * 0.995; idx += 1
        tau1 = theta[idx]; tau2 = theta[idx + 1]; idx += 2
        gamma = theta[idx: idx + K]; idx += K
        xi = theta[idx: idx + K]; idx += K
        phi = theta[idx: idx + K]; idx += K
        delta1 = theta[idx: idx + K]; idx += K
        delta2 = theta[idx: idx + K]; idx += K
        sigma_u = np.exp(theta[idx: idx + K]) + 1e-6; idx += K
        nu = 2.05 + np.exp(theta[idx])
        return omega, beta, tau1, tau2, gamma, xi, phi, delta1, delta2, sigma_u, nu

    def compute(theta: np.ndarray, n: int):
        omega, beta, tau1, tau2, gamma, xi, phi, delta1, delta2, sigma_u, nu = unpack(theta)
        logX = safe_log(X0[:n])
        logh = np.zeros(n)
        z = np.zeros(n)
        U = np.zeros((n, K))
        logh[0] = np.mean(logX[: min(20, n), 0])
        for t in range(n):
            if t > 0:
                leverage_prev = tau1 * z[t - 1] + tau2 * (z[t - 1] ** 2 - 1.0)
                logh[t] = omega + beta * logh[t - 1] + leverage_prev + float(np.dot(gamma, U[t - 1]))
            h = np.exp(np.clip(logh[t], -30, 10))
            z[t] = y0[t] / np.sqrt(h + EPS)
            U[t] = logX[t] - (xi + phi * logh[t] + delta1 * z[t] + delta2 * (z[t] ** 2 - 1.0))
        return logh, z, U

    def nll(theta: np.ndarray) -> float:
        logh, z, U = compute(theta, train_n)
        omega, beta, tau1, tau2, gamma, xi, phi, delta1, delta2, sigma_u, nu = unpack(theta)
        h = np.exp(np.clip(logh, -30, 10))
        ll_ret = student_t_standardized_logpdf(z, nu) - 0.5 * np.log(h)
        ll_meas = np.sum(stats.norm.logpdf(U, loc=0.0, scale=sigma_u), axis=1)
        loss = -np.sum(ll_ret + ll_meas)
        penalty = 1e-4 * np.sum(theta**2) + 1e-3 * np.sum(gamma**2)
        return float(loss + penalty) if np.isfinite(loss) else 1e12

    init = []
    init.extend([-0.05, 2.5, -0.03, 0.03])
    init.extend([0.04] * K)
    init.extend(list(np.mean(safe_log(X0[:train_n]), axis=0)))
    init.extend([0.80] * K)
    init.extend([-0.03] * K)
    init.extend([0.03] * K)
    init.extend([-2.0] * K)
    init.append(np.log(8.0 - 2.05))
    init = np.array(init, dtype=float)

    try:
        opt = optimize.minimize(nll, init, method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-5, "fatol": 1e-5})
        theta = opt.x
        logh, _, _ = compute(theta, len(data))
        pred = pd.Series(np.exp(np.clip(logh, -30, 10)), index=data.index, name=name).shift(1).iloc[train_n:]
        return RealizedGarchResult(name, theta, bool(opt.success), float(opt.fun), pred.clip(lower=EPS))
    except Exception as exc:
        print(f"[WARN] {name} failed: {exc}")
        empty = pd.Series(dtype=float, name=name)
        return RealizedGarchResult(name, init, False, np.inf, empty)


def forecast_realized_garch_models(measures: pd.DataFrame, train_size: int) -> Dict[str, pd.Series]:
    y = measures["return"]
    single_x = measures["RV"]
    X_multi = measures[["RV", "RBV", "RTV", "TrueSD"]].copy()
    models = [
        fit_rgarch_single(y, single_x, train_size, name="RGARCH-t", arma_order=(0, 0)),
        fit_rgarch_single(y, single_x, train_size, name="ARMA(1,1)-RGARCH-t", arma_order=(1, 1)),
        fit_regarch_multi(y, X_multi, train_size, name="REGARCH-t", arma_order=(0, 0)),
        fit_regarch_multi(y, X_multi, train_size, name="ARMA(1,1)-REGARCH-t", arma_order=(1, 1)),
    ]
    out = {}
    for result in models:
        if not result.forecast.empty:
            out[result.name] = result.forecast
            print(f"[OK] {result.name}, success={result.success}, loss={result.loss:.3f}")
    return out


# -----------------------------------------------------------------------------
# Forecast and risk metrics
# -----------------------------------------------------------------------------


def forecast_metrics(target: pd.Series, forecast: pd.Series) -> Dict[str, float]:
    y, f = align_forecasts(target, forecast)
    err = f - y
    return {
        "RMSE": float(np.sqrt(np.mean(err**2))),
        "MAE": float(np.mean(np.abs(err))),
        "MAPE": float(np.mean(np.abs(err) / np.maximum(np.abs(y), EPS)) * 100),
        "QLIKE": float(np.mean(np.log(f) + y / f)),
    }


def normal_crps(y: np.ndarray, mu: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    sigma = np.maximum(sigma, EPS)
    z = (y - mu) / sigma
    return sigma * (z * (2 * stats.norm.cdf(z) - 1) + 2 * stats.norm.pdf(z) - 1 / np.sqrt(np.pi))


def risk_metrics(
    returns: pd.Series,
    variance_forecast: pd.Series,
    train_returns: pd.Series,
    alpha: float = 0.05,
) -> Dict[str, float]:
    df = pd.concat([returns.rename("r"), variance_forecast.rename("v")], axis=1).dropna()
    r = df["r"].values
    sigma = np.sqrt(np.maximum(df["v"].values, EPS))

    train_std = train_returns.dropna().values
    train_scale = np.std(train_std) + EPS
    std_resid = train_std / train_scale
    q = float(np.quantile(std_resid, alpha))
    es_q = float(std_resid[std_resid <= q].mean()) if np.any(std_resid <= q) else q

    var = sigma * q
    es = sigma * es_q
    violations = r < var
    crps = normal_crps(r, np.zeros_like(r), sigma)

    covp = float(np.mean(violations))
    avg_es_loss = float(np.mean(np.where(violations, np.abs(r - es), 0.0)))
    return {
        "VaR_alpha": alpha,
        "Avg_VaR": float(np.mean(var)),
        "Avg_ES": float(np.mean(es)),
        "CovP": covp,
        "ViolationRate": covp,
        "CRPS": float(np.mean(crps)),
        "ES_Loss": avg_es_loss,
        "N": int(len(r)),
        "Violations": int(np.sum(violations)),
    }


def kupiec_test(returns: pd.Series, variance_forecast: pd.Series, train_returns: pd.Series, alpha: float = 0.05) -> Dict[str, float]:
    df = pd.concat([returns.rename("r"), variance_forecast.rename("v")], axis=1).dropna()
    r = df["r"].values
    sigma = np.sqrt(np.maximum(df["v"].values, EPS))
    std_train = train_returns.dropna().values / (np.std(train_returns.dropna().values) + EPS)
    q = float(np.quantile(std_train, alpha))
    violations = r < sigma * q
    n = len(violations)
    x = int(np.sum(violations))
    phat = np.clip(x / max(n, 1), EPS, 1 - EPS)
    a = np.clip(alpha, EPS, 1 - EPS)
    log_l0 = (n - x) * np.log(1 - a) + x * np.log(a)
    log_l1 = (n - x) * np.log(1 - phat) + x * np.log(phat)
    lr_uc = -2 * (log_l0 - log_l1)
    p_uc = 1 - stats.chi2.cdf(lr_uc, df=1)
    return {"Kupiec_LRuc": float(lr_uc), "Kupiec_pvalue": float(p_uc)}


def christoffersen_test(returns: pd.Series, variance_forecast: pd.Series, train_returns: pd.Series, alpha: float = 0.05) -> Dict[str, float]:
    df = pd.concat([returns.rename("r"), variance_forecast.rename("v")], axis=1).dropna()
    r = df["r"].values
    sigma = np.sqrt(np.maximum(df["v"].values, EPS))
    std_train = train_returns.dropna().values / (np.std(train_returns.dropna().values) + EPS)
    q = float(np.quantile(std_train, alpha))
    I = (r < sigma * q).astype(int)
    if len(I) < 3:
        return {"Christoffersen_LRind": np.nan, "Christoffersen_pvalue": np.nan}
    I0, I1 = I[:-1], I[1:]
    n00 = np.sum((I0 == 0) & (I1 == 0))
    n01 = np.sum((I0 == 0) & (I1 == 1))
    n10 = np.sum((I0 == 1) & (I1 == 0))
    n11 = np.sum((I0 == 1) & (I1 == 1))
    pi01 = np.clip(n01 / max(n00 + n01, 1), EPS, 1 - EPS)
    pi11 = np.clip(n11 / max(n10 + n11, 1), EPS, 1 - EPS)
    pi = np.clip((n01 + n11) / max(n00 + n01 + n10 + n11, 1), EPS, 1 - EPS)
    log_l_ind = n00 * np.log(1 - pi01) + n01 * np.log(pi01) + n10 * np.log(1 - pi11) + n11 * np.log(pi11)
    log_l_pooled = (n00 + n10) * np.log(1 - pi) + (n01 + n11) * np.log(pi)
    lr_ind = -2 * (log_l_pooled - log_l_ind)
    p_ind = 1 - stats.chi2.cdf(lr_ind, df=1)
    return {"Christoffersen_LRind": float(lr_ind), "Christoffersen_pvalue": float(p_ind)}


def diebold_mariano(loss_a: np.ndarray, loss_b: np.ndarray) -> Dict[str, float]:
    d = np.asarray(loss_a) - np.asarray(loss_b)
    d = d[np.isfinite(d)]
    if len(d) < 5:
        return {"DM_stat": np.nan, "DM_pvalue": np.nan}
    dm = np.mean(d) / (np.std(d, ddof=1) / np.sqrt(len(d)) + EPS)
    p = 2 * (1 - stats.t.cdf(abs(dm), df=len(d) - 1))
    return {"DM_stat": float(dm), "DM_pvalue": float(p)}


def ljung_box_standardized(returns: pd.Series, variance_forecast: pd.Series, lags: int = 10) -> Dict[str, float]:
    df = pd.concat([returns.rename("r"), variance_forecast.rename("v")], axis=1).dropna()
    z = df["r"] / np.sqrt(df["v"].clip(lower=EPS))
    try:
        out = acorr_ljungbox(z.dropna(), lags=[lags], return_df=True)
        return {"LjungBox_stat": float(out["lb_stat"].iloc[0]), "LjungBox_pvalue": float(out["lb_pvalue"].iloc[0])}
    except Exception:
        return {"LjungBox_stat": np.nan, "LjungBox_pvalue": np.nan}


# -----------------------------------------------------------------------------
# Visualization
# -----------------------------------------------------------------------------


def plot_actual_vs_forecast(target: pd.Series, forecasts: Dict[str, pd.Series], outdir: Path, prefix: str, max_models: int = 8):
    metric_rows = []
    for name, pred in forecasts.items():
        try:
            m = forecast_metrics(target, pred)
            metric_rows.append((name, m["RMSE"]))
        except Exception:
            pass
    top = [name for name, _ in sorted(metric_rows, key=lambda z: z[1])[:max_models]]
    plt.figure(figsize=(14, 6))
    target_plot = target.dropna().iloc[-350:]
    plt.plot(target_plot.index, target_plot.values, label="Actual next RV", linewidth=2)
    for name in top:
        pred = forecasts[name].reindex(target_plot.index).dropna()
        plt.plot(pred.index, pred.values, label=name, alpha=0.8)
    plt.title(f"{prefix}: Actual vs Forecasted Volatility")
    plt.xlabel("Time")
    plt.ylabel("Variance / Realized Volatility")
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(outdir / f"{prefix}_actual_vs_forecast.png", dpi=180)
    plt.close()


def plot_bar(df: pd.DataFrame, value: str, outdir: Path, prefix: str, title: str, top_n: int = 20):
    if df.empty or value not in df.columns:
        return
    data = df.sort_values(value).head(top_n)
    plt.figure(figsize=(12, max(5, 0.35 * len(data))))
    plt.barh(data["Model"], data[value])
    plt.title(title)
    plt.xlabel(value)
    plt.tight_layout()
    plt.savefig(outdir / f"{prefix}_{value}.png", dpi=180)
    plt.close()


def plot_var_es(returns: pd.Series, forecast: pd.Series, train_returns: pd.Series, outdir: Path, prefix: str, model_name: str, alpha: float):
    df = pd.concat([returns.rename("r"), forecast.rename("v")], axis=1).dropna().iloc[-350:]
    if df.empty:
        return
    std_train = train_returns.dropna().values / (np.std(train_returns.dropna().values) + EPS)
    q = float(np.quantile(std_train, alpha))
    es_q = float(std_train[std_train <= q].mean()) if np.any(std_train <= q) else q
    sigma = np.sqrt(df["v"].clip(lower=EPS))
    var = sigma * q
    es = sigma * es_q
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df["r"], label="Return")
    plt.plot(df.index, var, label=f"VaR {alpha:.2f}")
    plt.plot(df.index, es, label=f"ES {alpha:.2f}")
    plt.title(f"{prefix}: VaR and ES for {model_name}")
    plt.xlabel("Time")
    plt.ylabel("Return")
    plt.legend()
    plt.tight_layout()
    safe_model = model_name.replace("/", "_").replace("(", "").replace(")", "").replace(",", "_").replace(" ", "_")
    plt.savefig(outdir / f"{prefix}_VaR_ES_{safe_model}.png", dpi=180)
    plt.close()


# -----------------------------------------------------------------------------
# Benchmark runner
# -----------------------------------------------------------------------------


def run_one_dataset(
    name: str,
    raw_df: pd.DataFrame,
    outroot: Path,
    realized_window: int,
    train_fraction: float,
    alpha: float,
) -> None:
    print(f"\n===== Dataset: {name} =====")
    outdir = ensure_dir(outroot / name)
    measures = realized_measures(raw_df, window=realized_window)
    measures.to_csv(outdir / "realized_measures.csv")

    n = len(measures)
    train_size = int(n * train_fraction)
    if train_size < 100 or n - train_size < 50:
        print(f"[WARN] Skipping {name}: not enough observations after realized-measure construction.")
        return

    target = measures["target"]
    returns = measures["return"]
    train_returns = returns.iloc[:train_size]

    forecasts: Dict[str, pd.Series] = {}
    forecasts["HAR-RV"] = forecast_har(measures, train_size)
    forecasts.update(forecast_garch_family(returns, train_size))
    forecasts.update(forecast_realized_garch_models(measures, train_size))

    # Keep only forecasts with overlap on test target.
    clean_forecasts = {}
    for model_name, pred in forecasts.items():
        y, f = align_forecasts(target.iloc[train_size:], pred)
        if len(y) >= 20:
            clean_forecasts[model_name] = f.rename(model_name)
    forecasts = clean_forecasts

    all_pred = pd.concat(forecasts.values(), axis=1) if forecasts else pd.DataFrame()
    all_pred.to_csv(outdir / "forecasts.csv")

    rows = []
    risk_rows = []
    test_rows = []
    baseline_loss = None
    baseline_name = "HAR-RV" if "HAR-RV" in forecasts else next(iter(forecasts), None)
    if baseline_name:
        yb, fb = align_forecasts(target.iloc[train_size:], forecasts[baseline_name])
        baseline_loss = (fb.values - yb.values) ** 2

    for model_name, pred in forecasts.items():
        y, f = align_forecasts(target.iloc[train_size:], pred)
        m = forecast_metrics(y, f)
        rows.append({"Dataset": name, "Model": model_name, **m})

        r_metrics = risk_metrics(returns.iloc[train_size:], f, train_returns, alpha=alpha)
        risk_rows.append({"Dataset": name, "Model": model_name, **r_metrics})

        tests = {}
        tests.update(kupiec_test(returns.iloc[train_size:], f, train_returns, alpha=alpha))
        tests.update(christoffersen_test(returns.iloc[train_size:], f, train_returns, alpha=alpha))
        tests.update(ljung_box_standardized(returns.iloc[train_size:], f, lags=10))
        if baseline_loss is not None and model_name != baseline_name:
            common = pd.concat([target.iloc[train_size:].rename("y"), f.rename("f"), forecasts[baseline_name].rename("b")], axis=1).dropna()
            if len(common) >= 20:
                loss_model = (common["f"].values - common["y"].values) ** 2
                loss_base = (common["b"].values - common["y"].values) ** 2
                tests.update(diebold_mariano(loss_model, loss_base))
            else:
                tests.update({"DM_stat": np.nan, "DM_pvalue": np.nan})
        else:
            tests.update({"DM_stat": np.nan, "DM_pvalue": np.nan})
        test_rows.append({"Dataset": name, "Model": model_name, **tests})

    metrics_df = pd.DataFrame(rows).sort_values("RMSE")
    risk_df = pd.DataFrame(risk_rows).sort_values("CRPS")
    tests_df = pd.DataFrame(test_rows)

    metrics_df.to_csv(outdir / "forecast_metrics.csv", index=False)
    risk_df.to_csv(outdir / "risk_metrics.csv", index=False)
    tests_df.to_csv(outdir / "statistical_tests.csv", index=False)

    plot_actual_vs_forecast(target.iloc[train_size:], forecasts, outdir, name)
    plot_bar(metrics_df, "RMSE", outdir, name, f"{name}: RMSE comparison")
    plot_bar(metrics_df, "QLIKE", outdir, name, f"{name}: QLIKE comparison")
    plot_bar(risk_df, "CRPS", outdir, name, f"{name}: CRPS comparison")
    plot_bar(risk_df, "CovP", outdir, name, f"{name}: VaR coverage probability")

    if not metrics_df.empty:
        best_model = metrics_df.iloc[0]["Model"]
        plot_var_es(returns.iloc[train_size:], forecasts[best_model], train_returns, outdir, name, best_model, alpha)

    print("Top forecast metrics:")
    print(metrics_df.head(10).to_string(index=False))
    print("Top risk metrics:")
    print(risk_df.head(10).to_string(index=False))
    print(f"Outputs saved to: {outdir}")


# -----------------------------------------------------------------------------
# GitHub-ready summary, visualization gallery, and sensitivity analysis
# -----------------------------------------------------------------------------


def _save_fig(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()


def plot_summary_heatmaps(outroot: Path) -> None:
    """Create cross-dataset heatmaps and tabular comparison visualizations."""
    metric_path = outroot / "all_forecast_metrics.csv"
    risk_path = outroot / "all_risk_metrics.csv"
    if not metric_path.exists():
        return
    figures = ensure_dir(outroot / "summary_figures")
    metrics = pd.read_csv(metric_path)
    risk = pd.read_csv(risk_path) if risk_path.exists() else pd.DataFrame()

    # Keep the most common/top models so plots remain readable on GitHub.
    if not metrics.empty:
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
                _save_fig(figures / filename)

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
            _save_fig(figures / "summary_model_rank_boxplot.png")

    if not risk.empty:
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
                _save_fig(figures / filename)

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
            _save_fig(figures / "summary_crps_covp_scatter.png")


def make_markdown_table(df: pd.DataFrame, max_rows: int = 15, floatfmt: str = ".5g") -> str:
    if df.empty:
        return "No rows available."
    out = df.head(max_rows).copy()
    for c in out.columns:
        if pd.api.types.is_float_dtype(out[c]):
            out[c] = out[c].map(lambda x: "" if pd.isna(x) else format(float(x), floatfmt))
    return out.to_markdown(index=False)


def generate_github_report(outroot: Path) -> None:
    """Write a GitHub-rendered Markdown report with tables and figure gallery."""
    outroot = ensure_dir(outroot)
    plot_summary_heatmaps(outroot)
    report_path = outroot / "README.md"
    lines = []
    lines.append("# Volatility Benchmark Results")
    lines.append("")
    lines.append("This folder is designed to be committed to GitHub so the tables and plots render directly in the repository.")
    lines.append("")

    metrics_path = outroot / "all_forecast_metrics.csv"
    risk_path = outroot / "all_risk_metrics.csv"
    tests_path = outroot / "all_statistical_tests.csv"

    if metrics_path.exists():
        metrics = pd.read_csv(metrics_path).sort_values(["Dataset", "RMSE"])
        lines.append("## Forecast accuracy table")
        lines.append("")
        cols = [c for c in ["Dataset", "Model", "RMSE", "MAE", "MAPE", "NMAE", "QLIKE"] if c in metrics.columns]
        lines.append(make_markdown_table(metrics[cols], max_rows=30))
        lines.append("")
    if risk_path.exists():
        risk = pd.read_csv(risk_path).sort_values(["Dataset", "CRPS"])
        lines.append("## Risk metric table")
        lines.append("")
        cols = [c for c in ["Dataset", "Model", "VaR", "ES", "CRPS", "CovP", "Exceptions", "N"] if c in risk.columns]
        lines.append(make_markdown_table(risk[cols], max_rows=30))
        lines.append("")
    if tests_path.exists():
        tests = pd.read_csv(tests_path)
        lines.append("## Statistical test table")
        lines.append("")
        cols = [c for c in ["Dataset", "Model", "Kupiec_LR", "Kupiec_pvalue", "Christoffersen_LR", "Christoffersen_pvalue", "DM_stat", "DM_pvalue", "LB_stat", "LB_pvalue"] if c in tests.columns]
        lines.append(make_markdown_table(tests[cols], max_rows=30))
        lines.append("")

    lines.append("## Visualization gallery")
    lines.append("")
    pngs = sorted(outroot.glob("**/*.png"))
    if pngs:
        for png in pngs:
            rel = png.relative_to(outroot).as_posix()
            title = png.stem.replace("_", " ").title()
            lines.append(f"### {title}")
            lines.append("")
            lines.append(f"![{title}]({rel})")
            lines.append("")
    else:
        lines.append("No figures generated yet. Run the benchmark script first.")
        lines.append("")

    sens_path = outroot / "sensitivity_results.csv"
    if sens_path.exists():
        sens = pd.read_csv(sens_path)
        lines.append("## Sensitivity analysis table")
        lines.append("")
        cols = [c for c in ["Dataset", "realized_window", "alpha", "train_fraction", "Model", "RMSE", "CRPS", "CovP"] if c in sens.columns]
        lines.append(make_markdown_table(sens[cols].sort_values(["Dataset", "RMSE"]), max_rows=40))
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"GitHub report written to: {report_path}")


def plot_sensitivity_summary(sensitivity_df: pd.DataFrame, outroot: Path) -> None:
    if sensitivity_df.empty:
        return
    figures = ensure_dir(outroot / "sensitivity_figures")
    df = sensitivity_df.copy()
    if "RMSE" in df.columns:
        top_models = df.groupby("Model")["RMSE"].mean().sort_values().head(12).index.tolist()
        d = df[df["Model"].isin(top_models)]
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
        _save_fig(figures / "sensitivity_rmse_by_window.png")

        pivot = d.pivot_table(index="realized_window", columns="Model", values="RMSE", aggfunc="mean")
        plt.figure(figsize=(max(12, 0.65 * len(pivot.columns)), 6))
        if sns is not None:
            sns.heatmap(pivot, annot=True, fmt=".4g", cmap="viridis", linewidths=0.5)
        else:
            plt.imshow(pivot.values, aspect="auto")
            plt.colorbar(label="RMSE")
            plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=65, ha="right")
            plt.yticks(range(len(pivot.index)), pivot.index)
        plt.title("Sensitivity heatmap: RMSE vs window and model")
        _save_fig(figures / "sensitivity_rmse_heatmap.png")

    if {"alpha", "CovP"}.issubset(df.columns):
        plt.figure(figsize=(11, 6))
        d = df[df["Model"].isin(df.groupby("Model")["CovP"].mean().sort_values(ascending=False).head(12).index)]
        if sns is not None:
            sns.lineplot(data=d, x="alpha", y="CovP", hue="Model", marker="o", estimator="mean", errorbar=None)
        else:
            for model, sub in d.groupby("Model"):
                sub.groupby("alpha")["CovP"].mean().plot(marker="o", label=model)
            plt.legend(fontsize=8)
        plt.title("Sensitivity of VaR coverage probability to tail level")
        plt.xlabel("VaR/ES tail probability alpha")
        plt.ylabel("Coverage probability")
        _save_fig(figures / "sensitivity_covp_by_alpha.png")

    if {"train_fraction", "CRPS"}.issubset(df.columns):
        plt.figure(figsize=(11, 6))
        d = df[df["Model"].isin(df.groupby("Model")["CRPS"].mean().sort_values().head(12).index)]
        if sns is not None:
            sns.lineplot(data=d, x="train_fraction", y="CRPS", hue="Model", marker="o", estimator="mean", errorbar=None)
        else:
            for model, sub in d.groupby("Model"):
                sub.groupby("train_fraction")["CRPS"].mean().plot(marker="o", label=model)
            plt.legend(fontsize=8)
        plt.title("Sensitivity of CRPS to train/test split")
        plt.xlabel("Training fraction")
        plt.ylabel("Mean CRPS")
        _save_fig(figures / "sensitivity_crps_by_train_fraction.png")


def run_sensitivity_suite(
    datasets: Dict[str, pd.DataFrame],
    outroot: Path,
    windows: Sequence[int],
    alphas: Sequence[float],
    train_fractions: Sequence[float],
) -> None:
    """Run sensitivity analysis and generate GitHub-ready plots/tables.

    This intentionally reuses the full benchmark pipeline so sensitivity results
    are directly comparable with the main results.
    """
    rows = []
    sens_root = ensure_dir(outroot / "sensitivity_runs")
    for realized_window in windows:
        for alpha in alphas:
            for train_fraction in train_fractions:
                combo = f"window_{realized_window}_alpha_{alpha:g}_train_{train_fraction:g}".replace(".", "p")
                combo_root = ensure_dir(sens_root / combo)
                print(f"\n[SENSITIVITY] {combo}")
                for name, df in datasets.items():
                    run_one_dataset(
                        name=name,
                        raw_df=df,
                        outroot=combo_root,
                        realized_window=int(realized_window),
                        train_fraction=float(train_fraction),
                        alpha=float(alpha),
                    )
                combine_outputs(combo_root)
                metric_path = combo_root / "all_forecast_metrics.csv"
                risk_path = combo_root / "all_risk_metrics.csv"
                if metric_path.exists():
                    met = pd.read_csv(metric_path)
                    risk = pd.read_csv(risk_path) if risk_path.exists() else pd.DataFrame()
                    merged = met.merge(risk, on=["Dataset", "Model"], how="left", suffixes=("", "_risk")) if not risk.empty else met
                    for _, r in merged.iterrows():
                        row = r.to_dict()
                        row.update({
                            "realized_window": int(realized_window),
                            "alpha": float(alpha),
                            "train_fraction": float(train_fraction),
                        })
                        rows.append(row)
    sensitivity_df = pd.DataFrame(rows)
    if not sensitivity_df.empty:
        sensitivity_df.to_csv(outroot / "sensitivity_results.csv", index=False)
        plot_sensitivity_summary(sensitivity_df, outroot)
        print(f"Sensitivity summary saved to: {outroot / 'sensitivity_results.csv'}")


def combine_outputs(outroot: Path) -> None:
    metric_files = list(outroot.glob("*/forecast_metrics.csv"))
    risk_files = list(outroot.glob("*/risk_metrics.csv"))
    test_files = list(outroot.glob("*/statistical_tests.csv"))
    if metric_files:
        pd.concat([pd.read_csv(f) for f in metric_files], ignore_index=True).to_csv(outroot / "all_forecast_metrics.csv", index=False)
    if risk_files:
        pd.concat([pd.read_csv(f) for f in risk_files], ignore_index=True).to_csv(outroot / "all_risk_metrics.csv", index=False)
    if test_files:
        pd.concat([pd.read_csv(f) for f in test_files], ignore_index=True).to_csv(outroot / "all_statistical_tests.csv", index=False)
    plot_summary_heatmaps(outroot)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Classical volatility forecasting and risk benchmark.")
    p.add_argument("--mode", choices=["synthetic", "online", "both"], default="synthetic")
    p.add_argument("--tickers", nargs="+", default=["SPY", "AAPL", "BTC-USD"], help="Tickers for online mode")
    p.add_argument("--start", default="2018-01-01", help="Start date for online mode")
    p.add_argument("--end", default=None, help="End date for online mode")
    p.add_argument("--synthetic-n", type=int, default=2200, help="Length of each synthetic dataset")
    p.add_argument("--seed", type=int, default=123, help="Random seed")
    p.add_argument("--realized-window", type=int, default=22, help="Rolling window for RV/RBV/RTV/TrueSD")
    p.add_argument("--train-fraction", type=float, default=0.70)
    p.add_argument("--alpha", type=float, default=0.05, help="VaR/ES tail probability")
    p.add_argument("--outdir", default="docs/results", help="Directory for CSV tables, figures, and GitHub report")
    p.add_argument("--github-report", action="store_true", help="Create outdir/README.md with tables and figure gallery")
    p.add_argument("--run-sensitivity", action="store_true", help="Run sensitivity analysis over windows, alpha levels, and train splits")
    p.add_argument("--sensitivity-windows", nargs="+", type=int, default=[10, 22, 44], help="Sensitivity rolling windows")
    p.add_argument("--sensitivity-alphas", nargs="+", type=float, default=[0.01, 0.025, 0.05], help="Sensitivity VaR/ES alpha levels")
    p.add_argument("--sensitivity-train-fractions", nargs="+", type=float, default=[0.60, 0.70, 0.80], help="Sensitivity train fractions")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    outroot = ensure_dir(args.outdir)

    datasets: Dict[str, pd.DataFrame] = {}
    if args.mode in {"synthetic", "both"}:
        datasets.update(make_synthetic_datasets(n=args.synthetic_n, seed=args.seed))
    if args.mode in {"online", "both"}:
        datasets.update(download_online_data(args.tickers, start=args.start, end=args.end))

    if not datasets:
        raise RuntimeError("No datasets available. Check online tickers or use --mode synthetic.")

    for name, df in datasets.items():
        run_one_dataset(
            name=name,
            raw_df=df,
            outroot=outroot,
            realized_window=args.realized_window,
            train_fraction=args.train_fraction,
            alpha=args.alpha,
        )
    combine_outputs(outroot)
    if args.run_sensitivity:
        run_sensitivity_suite(
            datasets=datasets,
            outroot=outroot,
            windows=args.sensitivity_windows,
            alphas=args.sensitivity_alphas,
            train_fractions=args.sensitivity_train_fractions,
        )
    if args.github_report or args.run_sensitivity:
        generate_github_report(outroot)
    print(f"\nAll outputs saved under: {outroot.resolve()}")


if __name__ == "__main__":
    main()
