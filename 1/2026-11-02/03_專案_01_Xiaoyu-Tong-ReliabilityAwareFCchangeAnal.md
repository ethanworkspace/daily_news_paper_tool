# GitHub 專案 01：Xiaoyu-Tong/ReliabilityAwareFCchangeAnalysis

- 日期：2026-11-02
- URL：https://github.com/Xiaoyu-Tong/ReliabilityAwareFCchangeAnalysis
- 描述：
- Stars：1  |  Forks：2  |  Language：MATLAB
- License：
- Topics：
- 更新時間：2026-10-21T07:33:22+00:00
- 配對論文：https://doi.org/10.1038/s44220-026-00729-y
- 品質分數：6/10 [paper_paired]

## 在做什麼
本專案提供一個可靠性感知的框架，用於分析抗抑鬱藥物或安慰劑導致的腦功能連接（FC）變化。透過將任務預測效能與測試‑再測試可靠性（信號雜訊比）結合，框架能在監督學習（分類、回歸）與非監督學習（CVQ）中同時尋找具有顯著組間差異且個體內變異小的FC維度，幫助研究者區分真實的治療效應與隨機波動或測量噪聲。目標使用者為神經科學、精神醫學及生物統計領域的研究人員，他們需要可解釋且可重複的FC變化分析工具。

## 技術
該專案以 MATLAB 實作，核心為可靠性感知學習目標，將信號雜訊比（SNR）作為可靠性約束，與預測任務（分類使用交叉熵，回歸使用均方誤差）及 L0 稀疏正則化共同組成總損失函數。在監督學習中，分類與回歸各自經歷初始化、連續稀疏化與微調三階段優化（optimizeClassification_* / optimizeRegression_*），其中 updateG_Classification.m 在稀疏化步驟中被呼叫。非監督學習則透過 CVQ.m 實現，示範腳本 demoMain_CVQ.m 展示如何尋找僅在活性藥物組顯著變化而安慰劑組與測試‑再測試變異小的FC維度。程式碼結構遵循明確的模組化流程，便於擴展與參數調整。

## 架構
資料流程始於受試者的前後治療功能連接矩陣（FC），先計算組間時間點差異作為訊號（signal）與同一時間點的測試‑再測試差異作為噪聲（noise）。在監督學習路徑中，優化管線首先透過 optimize*_Initialization.m 初始化FC維度載入與預測權重，接著在 optimize*_ContinuousSparsification.m 中反覆更新載入（G）與權重（W），以最小化包含 SNR 損失、任務損失與 L0 正則化的總損失；updateG_Classification.m 負責在此步驟中更新載入矩陣。最後，optimize*_FineTuning.m 進行微調以提升泛化與可解釋性。非監督學習則由 CVQ.m 直接最佳化僅在活性藥物組顯著變化且測試‑再測試變異小的FC維度，demoMain_CVQ.m 提供使用範例。整個框架以模組化函式形式呈現，便於插入不同的特徵或替換損失項目。

## README 摘錄（節選）
```text
# A Reliability-Aware Framework for Treatment-Induced Functional Connectivity (FC) Change Analysis
Code Repo for the accompanying paper Early Brain Functional Connectivity Changes Induced by Antidepressants and Placebo (https://doi.org/10.1038/s44220-026-00729-y), which demonstrates its applications in antidepressant treatment.
> Tong, X., Fonzo, G.A., Carlisle, N.B. et al. Early brain functional connectivity changes induced by antidepressants and placebo. Nature Mental Health (2026). https://doi.org/10.1038/s44220-026-00729-y
## Workflow
The most straightforward way to characterize treatment-induced FC changes may be to simply calculate the pre-to-post-treatment change in FC features; however, this procedure may mix treatment effects with random fluctuations and measurement noise , especially when FC changes are assessed at the individual level. In this study, we address this challenge by introducing an explicit learning objective that maximizes the test-retest reliability of identified FC change patterns (**Fig. 1b**), as well as separating the overall FC changes into distinct interpretable dimensions (**Fig. 1a,c**).
## Formulation
Reliability-aware FC change analysis is a versatile framework that can be applied to either classification, regression, or unsupervised learning tasks. Essentially, it represents a family of learning objectives integrating task performance with reliability assessment. In this study, reliability of FC changes is encouraged by maximizing signal-to-noise ratio (SNR), where signal is defined as between-timepoint FC differences, and noise as within-timepoint test-retest FC differences. Namely, we sought FC change dimensions with significant, clinically meaningful between-timepoint differences and minimal test-retest variability.
### Supervised learning
In this study, reliability-aware predictive learning combines three learning objectives in the overall loss function -- SNR constraint, prediction task, and regularization:
[code block omitted]
Since the loss function is to be minimized, the SNR loss is defined as the ratio between noise power and signal power:
[code block omitted]
For classification, the task loss is:
[code block omitted]
For regression, the task loss is:
[code block omitted]
L0-regularization is implemented on both FC dimension loadings and predictive weights to enhance generalizability and interpretability.
### Unsupervised learning
In this study, we used reliability-aware unsupervised learning to identify active-drug-specific FC changes -- this analysis involves no prediction tasks.
Essentially, we seek FC dimensions showing significant changes in the active drug arm and minimal changes in the placebo arm and test-retest differences. This learning objective can be formularized as:
[code block omitted]
> See corresponding Methods sections and Appendix A of the accompanying paper for math details.
## Project Structure
[code block omitted]
## Optimization Pipelines
### Classification
optimizeClassification_Initialization.m --> optimizeClassification_ContinuousSparsification.m --> optimizeClassification_FineTuning.m
updateG_Classification.m is called inside optimizeClassification_ContinuousSparsification.m
### Regression
optimizeRegression_Initialization.m --> optimizeRegression_ContinuousSparsification.m --> optimizeRegression_FineTuning.m
### Unsupervised learning (CVQ analysis)
Optimization is achieved by CVQ.m
demoMain_CVQ.m demonstrates the context of CVQ implementation.
## Contact
tongxy@stanford.edu
```
