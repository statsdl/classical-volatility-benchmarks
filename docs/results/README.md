# Volatility Benchmark Results

This folder is designed to be committed to GitHub so the tables and plots render directly in the repository.

## Forecast accuracy table

| Dataset                     | Model                    |     RMSE |      MAE |   MAPE |     QLIKE |
|:----------------------------|:-------------------------|---------:|---------:|-------:|----------:|
| synthetic_regime_garch      | HAR-RV                   |  2.5111  | 0.69885  | 21.544 |  1.7367   |
| synthetic_regime_garch      | Naive-RV                 |  2.6524  | 0.66216  | 12.519 |  1.7267   |
| synthetic_regime_garch      | RGARCH-t                 |  4.8871  | 1.7846   | 30.016 |  1.8348   |
| synthetic_regime_garch      | ARMA(1,1)-RGARCH-t       |  5.9421  | 2.2981   | 42.278 |  1.977    |
| synthetic_regime_garch      | REGARCH-t                |  8.2     | 2.588    | 33.783 |  1.8677   |
| synthetic_regime_garch      | ARMA(1,1)-REGARCH-t      |  9.926   | 4.0174   | 74.548 |  3.7199   |
| synthetic_regime_garch      | GARCH(2,1)-t             | 10.913   | 4.5279   | 94.236 | 16.569    |
| synthetic_regime_garch      | GARCH(1,1)-t             | 10.913   | 4.5279   | 94.236 | 16.569    |
| synthetic_regime_garch      | APGARCH/APARCH(1,1)-t    | 10.913   | 4.5293   | 94.222 | 16.592    |
| synthetic_regime_garch      | APGARCH/APARCH(2,1)-t    | 10.913   | 4.5293   | 94.223 | 16.592    |
| synthetic_regime_garch      | Generalized-GARCH(2,2)-t | 10.919   | 4.5283   | 94.22  | 16.587    |
| synthetic_regime_garch      | GARCH(1,2)-t             | 10.919   | 4.5283   | 94.22  | 16.587    |
| synthetic_regime_garch      | GJR-GARCH(1,1)-t         | 10.923   | 4.5329   | 94.255 | 16.73     |
| synthetic_regime_garch      | FIGARCH(1,1)-t           | 10.952   | 4.529    | 93.617 | 15.697    |
| synthetic_regime_garch      | EGARCH(1,1)-t            | 10.981   | 4.545    | 93.961 | 16.263    |
| synthetic_regime_garch      | EGARCH(2,1)-t            | 11       | 4.5486   | 93.966 | 16.346    |
| synthetic_regime_garch      | Threshold-GARCH(1,1)-t   | 11.07    | 4.5777   | 94.06  | 17.904    |
| synthetic_rough_long_memory | HAR-RV                   |  0.13466 | 0.060035 | 18.296 | -0.1326   |
| synthetic_rough_long_memory | Naive-RV                 |  0.1378  | 0.054957 | 13.29  | -0.13728  |
| synthetic_rough_long_memory | RGARCH-t                 |  0.23059 | 0.16417  | 41.754 |  0.11202  |
| synthetic_rough_long_memory | ARMA(1,1)-REGARCH-t      |  0.2946  | 0.21129  | 85.134 |  0.012189 |
| synthetic_rough_long_memory | REGARCH-t                |  0.33692 | 0.17041  | 31.17  | -0.04921  |
| synthetic_rough_long_memory | ARMA(1,1)-RGARCH-t       |  0.45262 | 0.27167  | 44.314 |  0.23292  |
| synthetic_rough_long_memory | GJR-GARCH(1,1)-t         |  0.64356 | 0.4524   | 94.265 | 15.085    |
| synthetic_rough_long_memory | FIGARCH(1,1)-t           |  0.64374 | 0.45245  | 94.261 | 15.076    |
| synthetic_rough_long_memory | GARCH(2,1)-t             |  0.64374 | 0.45246  | 94.267 | 15.091    |
| synthetic_rough_long_memory | GARCH(1,1)-t             |  0.64374 | 0.45246  | 94.267 | 15.091    |
| synthetic_rough_long_memory | Generalized-GARCH(2,2)-t |  0.64382 | 0.45247  | 94.263 | 15.156    |
| synthetic_rough_long_memory | GARCH(1,2)-t             |  0.64382 | 0.45247  | 94.263 | 15.156    |
| synthetic_rough_long_memory | EGARCH(1,1)-t            |  0.6482  | 0.45398  | 94.215 | 15.516    |

## Risk metric table

| Dataset                     | Model                    |     CRPS |      CovP |   N |
|:----------------------------|:-------------------------|---------:|----------:|----:|
| synthetic_regime_garch      | EGARCH(2,1)-t            | 0.18498  | 0.036508  | 630 |
| synthetic_regime_garch      | Generalized-GARCH(2,2)-t | 0.18512  | 0.047619  | 630 |
| synthetic_regime_garch      | GARCH(1,2)-t             | 0.18512  | 0.047619  | 630 |
| synthetic_regime_garch      | Threshold-GARCH(1,1)-t   | 0.18577  | 0.047619  | 630 |
| synthetic_regime_garch      | EGARCH(1,1)-t            | 0.18621  | 0.044444  | 630 |
| synthetic_regime_garch      | FIGARCH(1,1)-t           | 0.18623  | 0.039683  | 630 |
| synthetic_regime_garch      | GJR-GARCH(1,1)-t         | 0.18653  | 0.052381  | 630 |
| synthetic_regime_garch      | APGARCH/APARCH(1,1)-t    | 0.18662  | 0.052381  | 630 |
| synthetic_regime_garch      | APGARCH/APARCH(2,1)-t    | 0.18662  | 0.052381  | 630 |
| synthetic_regime_garch      | GARCH(2,1)-t             | 0.1868   | 0.052381  | 630 |
| synthetic_regime_garch      | GARCH(1,1)-t             | 0.1868   | 0.052381  | 630 |
| synthetic_regime_garch      | ARMA(1,1)-REGARCH-t      | 0.25861  | 0.0045942 | 653 |
| synthetic_regime_garch      | ARMA(1,1)-RGARCH-t       | 0.35046  | 0.0015314 | 653 |
| synthetic_regime_garch      | RGARCH-t                 | 0.38001  | 0.0015314 | 653 |
| synthetic_regime_garch      | REGARCH-t                | 0.39203  | 0         | 653 |
| synthetic_regime_garch      | Naive-RV                 | 0.44145  | 0         | 653 |
| synthetic_regime_garch      | HAR-RV                   | 0.45057  | 0         | 653 |
| synthetic_rough_long_memory | EGARCH(2,1)-t            | 0.069736 | 0.034921  | 630 |
| synthetic_rough_long_memory | GARCH(1,2)-t             | 0.070684 | 0.039683  | 630 |
| synthetic_rough_long_memory | Generalized-GARCH(2,2)-t | 0.070684 | 0.039683  | 630 |
| synthetic_rough_long_memory | Threshold-GARCH(1,1)-t   | 0.070942 | 0.047619  | 630 |
| synthetic_rough_long_memory | APGARCH/APARCH(1,1)-t    | 0.070982 | 0.046032  | 630 |
| synthetic_rough_long_memory | APGARCH/APARCH(2,1)-t    | 0.070982 | 0.046032  | 630 |
| synthetic_rough_long_memory | EGARCH(1,1)-t            | 0.071114 | 0.038095  | 630 |
| synthetic_rough_long_memory | GJR-GARCH(1,1)-t         | 0.071215 | 0.04127   | 630 |
| synthetic_rough_long_memory | GARCH(1,1)-t             | 0.071217 | 0.04127   | 630 |
| synthetic_rough_long_memory | GARCH(2,1)-t             | 0.071217 | 0.04127   | 630 |
| synthetic_rough_long_memory | FIGARCH(1,1)-t           | 0.071221 | 0.04127   | 630 |
| synthetic_rough_long_memory | ARMA(1,1)-RGARCH-t       | 0.1171   | 0         | 653 |
| synthetic_rough_long_memory | RGARCH-t                 | 0.13169  | 0         | 653 |

## Statistical test table

| Dataset                | Model                    |   Kupiec_pvalue |   Christoffersen_pvalue |   DM_stat |   DM_pvalue |
|:-----------------------|:-------------------------|----------------:|------------------------:|----------:|------------:|
| synthetic_regime_garch | Naive-RV                 |      2.2204e-16 |              1          |    3.1408 |  0.0017609  |
| synthetic_regime_garch | HAR-RV                   |      2.2204e-16 |              1          |           |             |
| synthetic_regime_garch | GARCH(1,1)-t             |      0.78548    |              0.11323    |    5.4577 |  6.9461e-08 |
| synthetic_regime_garch | GARCH(1,2)-t             |      0.78231    |              0.058688   |    5.4552 |  7.0395e-08 |
| synthetic_regime_garch | GARCH(2,1)-t             |      0.78548    |              0.11323    |    5.4577 |  6.946e-08  |
| synthetic_regime_garch | Generalized-GARCH(2,2)-t |      0.78231    |              0.058688   |    5.4552 |  7.0394e-08 |
| synthetic_regime_garch | GJR-GARCH(1,1)-t         |      0.78548    |              0.028533   |    5.4634 |  6.7369e-08 |
| synthetic_regime_garch | Threshold-GARCH(1,1)-t   |      0.78231    |              0.72028    |    5.4739 |  6.367e-08  |
| synthetic_regime_garch | EGARCH(1,1)-t            |      0.51466    |              0.15696    |    5.4685 |  6.5537e-08 |
| synthetic_regime_garch | EGARCH(2,1)-t            |      0.10332    |              0.86102    |    5.4647 |  6.6908e-08 |
| synthetic_regime_garch | FIGARCH(1,1)-t           |      0.21842    |              0.35021    |    5.4496 |  7.2557e-08 |
| synthetic_regime_garch | APGARCH/APARCH(1,1)-t    |      0.78548    |              0.028533   |    5.4628 |  6.76e-08   |
| synthetic_regime_garch | APGARCH/APARCH(2,1)-t    |      0.78548    |              0.028533   |    5.4628 |  6.7599e-08 |
| synthetic_regime_garch | RGARCH-t                 |      2.7311e-14 |              0.9558     |    4.345  |  1.6149e-05 |
| synthetic_regime_garch | ARMA(1,1)-RGARCH-t       |      2.7311e-14 |              0.9558     |    4.8726 |  1.384e-06  |
| synthetic_regime_garch | REGARCH-t                |      2.2204e-16 |              1          |    4.8913 |  1.2635e-06 |
| synthetic_regime_garch | ARMA(1,1)-REGARCH-t      |      9.7818e-12 |              0.86773    |    5.4979 |  5.5203e-08 |
| synthetic_sv_jump_t    | Naive-RV                 |      6.7379e-13 |              0.91166    |   -1.8405 |  0.066153   |
| synthetic_sv_jump_t    | HAR-RV                   |      1.3703e-07 |              2.5097e-07 |           |             |
| synthetic_sv_jump_t    | GARCH(1,1)-t             |      6.5025e-06 |              0.11718    |   16.271  |  0          |
| synthetic_sv_jump_t    | GARCH(1,2)-t             |      6.5025e-06 |              0.11718    |   16.271  |  0          |
| synthetic_sv_jump_t    | GARCH(2,1)-t             |      1.5326e-06 |              0.075562   |   16.279  |  0          |
| synthetic_sv_jump_t    | Generalized-GARCH(2,2)-t |      1.5417e-07 |              0.27731    |   16.279  |  0          |
| synthetic_sv_jump_t    | GJR-GARCH(1,1)-t         |      6.5025e-06 |              0.11718    |   16.275  |  0          |
| synthetic_sv_jump_t    | Threshold-GARCH(1,1)-t   |      1.3354e-08 |              0.6876     |   16.369  |  0          |
| synthetic_sv_jump_t    | EGARCH(1,1)-t            |      0.007471   |              0.31708    |   15.713  |  0          |
| synthetic_sv_jump_t    | EGARCH(2,1)-t            |      0.066944   |              0.21742    |   15.773  |  0          |
| synthetic_sv_jump_t    | FIGARCH(1,1)-t           |      6.5025e-06 |              0.11718    |   16.269  |  0          |
| synthetic_sv_jump_t    | APGARCH/APARCH(1,1)-t    |      7.2496e-07 |              0.20161    |   16.302  |  0          |
| synthetic_sv_jump_t    | APGARCH/APARCH(2,1)-t    |      1.3354e-08 |              0.23226    |   16.305  |  0          |

## Visualization gallery

### Sensitivity Covp By Alpha

![Sensitivity Covp By Alpha](sensitivity_figures/sensitivity_covp_by_alpha.png)

### Sensitivity Crps By Train Fraction

![Sensitivity Crps By Train Fraction](sensitivity_figures/sensitivity_crps_by_train_fraction.png)

### Sensitivity Rmse By Window

![Sensitivity Rmse By Window](sensitivity_figures/sensitivity_rmse_by_window.png)

### Sensitivity Rmse Heatmap

![Sensitivity Rmse Heatmap](sensitivity_figures/sensitivity_rmse_heatmap.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p01_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p01_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p01_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p01_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p01_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p01_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p01_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Har-Rv

![Synthetic Sv Jump T Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_HAR-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p025_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p025_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p025_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p025_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p025_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p025_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p025_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Har-Rv

![Synthetic Sv Jump T Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_HAR-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p05_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p05_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p05_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p05_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_10_alpha_0p05_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_10_alpha_0p05_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_10_alpha_0p05_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Har-Rv

![Synthetic Sv Jump T Var Es Har-Rv](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_HAR-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_10_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p01_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p01_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p01_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p01_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p01_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p01_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p01_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p025_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p025_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p025_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p025_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p025_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p025_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p025_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p05_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p05_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p05_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p05_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_22_alpha_0p05_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_22_alpha_0p05_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_22_alpha_0p05_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_22_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p01_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p01_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p01_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p01_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p01_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p01_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p01_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p01_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p025_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p025_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p025_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p025_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p025_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p025_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p025_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p025_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p6/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p05_train_0p6/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p6/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p6/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p05_train_0p6/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p6/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p6/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p6/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p7/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p05_train_0p7/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p7/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p7/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p05_train_0p7/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p7/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p7/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p7/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p8/summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](sensitivity_runs/window_44_alpha_0p05_train_0p8/summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p8/summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p8/summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](sensitivity_runs/window_44_alpha_0p05_train_0p8/summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p8/summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](sensitivity_runs/window_44_alpha_0p05_train_0p8/summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Naive-Rv

![Synthetic Regime Garch Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_VaR_ES_Naive-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](sensitivity_runs/window_44_alpha_0p05_train_0p8/synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

### Summary Covp Heatmap

![Summary Covp Heatmap](summary_figures/summary_covp_heatmap.png)

### Summary Crps Covp Scatter

![Summary Crps Covp Scatter](summary_figures/summary_crps_covp_scatter.png)

### Summary Crps Heatmap

![Summary Crps Heatmap](summary_figures/summary_crps_heatmap.png)

### Summary Mae Heatmap

![Summary Mae Heatmap](summary_figures/summary_mae_heatmap.png)

### Summary Model Rank Boxplot

![Summary Model Rank Boxplot](summary_figures/summary_model_rank_boxplot.png)

### Summary Qlike Heatmap

![Summary Qlike Heatmap](summary_figures/summary_qlike_heatmap.png)

### Summary Rmse Heatmap

![Summary Rmse Heatmap](summary_figures/summary_rmse_heatmap.png)

### Synthetic Regime Garch Crps

![Synthetic Regime Garch Crps](synthetic_regime_garch/synthetic_regime_garch_CRPS.png)

### Synthetic Regime Garch Covp

![Synthetic Regime Garch Covp](synthetic_regime_garch/synthetic_regime_garch_CovP.png)

### Synthetic Regime Garch Qlike

![Synthetic Regime Garch Qlike](synthetic_regime_garch/synthetic_regime_garch_QLIKE.png)

### Synthetic Regime Garch Rmse

![Synthetic Regime Garch Rmse](synthetic_regime_garch/synthetic_regime_garch_RMSE.png)

### Synthetic Regime Garch Var Es Har-Rv

![Synthetic Regime Garch Var Es Har-Rv](synthetic_regime_garch/synthetic_regime_garch_VaR_ES_HAR-RV.png)

### Synthetic Regime Garch Actual Vs Forecast

![Synthetic Regime Garch Actual Vs Forecast](synthetic_regime_garch/synthetic_regime_garch_actual_vs_forecast.png)

### Synthetic Rough Long Memory Crps

![Synthetic Rough Long Memory Crps](synthetic_rough_long_memory/synthetic_rough_long_memory_CRPS.png)

### Synthetic Rough Long Memory Covp

![Synthetic Rough Long Memory Covp](synthetic_rough_long_memory/synthetic_rough_long_memory_CovP.png)

### Synthetic Rough Long Memory Qlike

![Synthetic Rough Long Memory Qlike](synthetic_rough_long_memory/synthetic_rough_long_memory_QLIKE.png)

### Synthetic Rough Long Memory Rmse

![Synthetic Rough Long Memory Rmse](synthetic_rough_long_memory/synthetic_rough_long_memory_RMSE.png)

### Synthetic Rough Long Memory Var Es Har-Rv

![Synthetic Rough Long Memory Var Es Har-Rv](synthetic_rough_long_memory/synthetic_rough_long_memory_VaR_ES_HAR-RV.png)

### Synthetic Rough Long Memory Actual Vs Forecast

![Synthetic Rough Long Memory Actual Vs Forecast](synthetic_rough_long_memory/synthetic_rough_long_memory_actual_vs_forecast.png)

### Synthetic Sv Jump T Crps

![Synthetic Sv Jump T Crps](synthetic_sv_jump_t/synthetic_sv_jump_t_CRPS.png)

### Synthetic Sv Jump T Covp

![Synthetic Sv Jump T Covp](synthetic_sv_jump_t/synthetic_sv_jump_t_CovP.png)

### Synthetic Sv Jump T Qlike

![Synthetic Sv Jump T Qlike](synthetic_sv_jump_t/synthetic_sv_jump_t_QLIKE.png)

### Synthetic Sv Jump T Rmse

![Synthetic Sv Jump T Rmse](synthetic_sv_jump_t/synthetic_sv_jump_t_RMSE.png)

### Synthetic Sv Jump T Var Es Naive-Rv

![Synthetic Sv Jump T Var Es Naive-Rv](synthetic_sv_jump_t/synthetic_sv_jump_t_VaR_ES_Naive-RV.png)

### Synthetic Sv Jump T Actual Vs Forecast

![Synthetic Sv Jump T Actual Vs Forecast](synthetic_sv_jump_t/synthetic_sv_jump_t_actual_vs_forecast.png)

## Sensitivity analysis table

| Dataset                |   realized_window |   alpha |   train_fraction | Model               |    RMSE |    CRPS |      CovP |
|:-----------------------|------------------:|--------:|-----------------:|:--------------------|--------:|--------:|----------:|
| synthetic_regime_garch |                10 |   0.01  |              0.8 | Naive-RV            | 0.21355 | 0.20251 | 0         |
| synthetic_regime_garch |                10 |   0.025 |              0.8 | Naive-RV            | 0.21355 | 0.20251 | 0         |
| synthetic_regime_garch |                10 |   0.05  |              0.8 | Naive-RV            | 0.21355 | 0.20251 | 0.0022831 |
| synthetic_regime_garch |                44 |   0.01  |              0.8 | Naive-RV            | 0.21938 | 0.38244 | 0         |
| synthetic_regime_garch |                44 |   0.025 |              0.8 | Naive-RV            | 0.21938 | 0.38244 | 0         |
| synthetic_regime_garch |                44 |   0.05  |              0.8 | Naive-RV            | 0.21938 | 0.38244 | 0         |
| synthetic_regime_garch |                22 |   0.01  |              0.8 | Naive-RV            | 0.22231 | 0.278   | 0         |
| synthetic_regime_garch |                22 |   0.025 |              0.8 | Naive-RV            | 0.22231 | 0.278   | 0         |
| synthetic_regime_garch |                22 |   0.05  |              0.8 | Naive-RV            | 0.22231 | 0.278   | 0         |
| synthetic_regime_garch |                10 |   0.01  |              0.8 | RGARCH-t            | 0.24994 | 0.20019 | 0         |
| synthetic_regime_garch |                10 |   0.025 |              0.8 | RGARCH-t            | 0.24994 | 0.20019 | 0         |
| synthetic_regime_garch |                10 |   0.05  |              0.8 | RGARCH-t            | 0.24994 | 0.20019 | 0.0045662 |
| synthetic_regime_garch |                10 |   0.01  |              0.8 | ARMA(1,1)-RGARCH-t  | 0.27988 | 0.18572 | 0         |
| synthetic_regime_garch |                10 |   0.025 |              0.8 | ARMA(1,1)-RGARCH-t  | 0.27988 | 0.18572 | 0         |
| synthetic_regime_garch |                10 |   0.05  |              0.8 | ARMA(1,1)-RGARCH-t  | 0.27988 | 0.18572 | 0.0068493 |
| synthetic_regime_garch |                10 |   0.01  |              0.8 | REGARCH-t           | 0.2917  | 0.22193 | 0         |
| synthetic_regime_garch |                10 |   0.025 |              0.8 | REGARCH-t           | 0.2917  | 0.22193 | 0         |
| synthetic_regime_garch |                10 |   0.05  |              0.8 | REGARCH-t           | 0.2917  | 0.22193 | 0.0022831 |
| synthetic_regime_garch |                10 |   0.01  |              0.8 | ARMA(1,1)-REGARCH-t | 0.2966  | 0.19    | 0         |
| synthetic_regime_garch |                10 |   0.025 |              0.8 | ARMA(1,1)-REGARCH-t | 0.2966  | 0.19    | 0         |
| synthetic_regime_garch |                10 |   0.05  |              0.8 | ARMA(1,1)-REGARCH-t | 0.2966  | 0.19    | 0.0022831 |
| synthetic_regime_garch |                44 |   0.01  |              0.8 | HAR-RV              | 0.29864 | 0.39751 | 0         |
| synthetic_regime_garch |                44 |   0.025 |              0.8 | HAR-RV              | 0.29864 | 0.39751 | 0         |
| synthetic_regime_garch |                44 |   0.05  |              0.8 | HAR-RV              | 0.29864 | 0.39751 | 0         |
| synthetic_regime_garch |                10 |   0.01  |              0.8 | HAR-RV              | 0.30313 | 0.23195 | 0         |
| synthetic_regime_garch |                10 |   0.025 |              0.8 | HAR-RV              | 0.30313 | 0.23195 | 0         |
| synthetic_regime_garch |                10 |   0.05  |              0.8 | HAR-RV              | 0.30313 | 0.23195 | 0.0022831 |
| synthetic_regime_garch |                22 |   0.01  |              0.8 | HAR-RV              | 0.34621 | 0.30445 | 0         |
| synthetic_regime_garch |                22 |   0.025 |              0.8 | HAR-RV              | 0.34621 | 0.30445 | 0         |
| synthetic_regime_garch |                22 |   0.05  |              0.8 | HAR-RV              | 0.34621 | 0.30445 | 0         |
| synthetic_regime_garch |                22 |   0.01  |              0.8 | RGARCH-t            | 0.47406 | 0.31698 | 0         |
| synthetic_regime_garch |                22 |   0.025 |              0.8 | RGARCH-t            | 0.47406 | 0.31698 | 0         |
| synthetic_regime_garch |                22 |   0.05  |              0.8 | RGARCH-t            | 0.47406 | 0.31698 | 0         |
| synthetic_regime_garch |                10 |   0.01  |              0.8 | EGARCH(1,1)-t       | 0.63749 | 0.1308  | 0         |
| synthetic_regime_garch |                10 |   0.025 |              0.8 | EGARCH(1,1)-t       | 0.63749 | 0.1308  | 0.0023419 |
| synthetic_regime_garch |                10 |   0.05  |              0.8 | EGARCH(1,1)-t       | 0.63749 | 0.1308  | 0.04918   |
| synthetic_regime_garch |                10 |   0.01  |              0.8 | EGARCH(2,1)-t       | 0.63815 | 0.13011 | 0         |
| synthetic_regime_garch |                10 |   0.025 |              0.8 | EGARCH(2,1)-t       | 0.63815 | 0.13011 | 0.0023419 |
| synthetic_regime_garch |                10 |   0.05  |              0.8 | EGARCH(2,1)-t       | 0.63815 | 0.13011 | 0.044496  |
| synthetic_regime_garch |                10 |   0.01  |              0.8 | FIGARCH(1,1)-t      | 0.63965 | 0.13047 | 0         |
