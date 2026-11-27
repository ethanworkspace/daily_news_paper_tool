# GitHub 專案 05：jakee417/LS-SSDD-v1.0-ShipDetectionComputerVision

- 日期：2026-10-10
- URL：https://github.com/jakee417/LS-SSDD-v1.0-ShipDetectionComputerVision
- 描述：Small Vessel Detection from Synthetic Aperture Radar (SAR) Imagery using Deep Learning
- Stars：28  |  Forks：3  |  Language：Jupyter Notebook
- License：
- Topics：deep-learning, imagery, ls-ssdd, sar, vessel-detection
- 更新時間：2025-06-24T12:10:36+00:00
- 論文層級：未對應論文（海事）
- 配對論文：
- 品質分數：6/10 [implementation_signals, stale_backfill]

## 在做什麼
此專案提供用於合成孔徑雷達（SAR）影像中小型船舶偵測的深度學習程式碼，包含資料前處理、模型訓練與推論的互動式 Jupyter Notebook，面向遠端遙測與電腦視覺研究者、學生以及海事監控單位，旨在提供可重現的基線與實驗平台，解決 SAR 低分辨率與斑點噪聲導致的小型船舶辨識困難，促進後續模型改進與應用。

## 技術
該專案主要使用 Python 與 Jupyter Notebook 進行開發，核心偵測模型建構於 Facebook Research 的 Detectron2 框架（基於 PyTorch），資料前處理透過 Notebook 將 SAR 影像轉換為 Detectron2 可接受的 COCO‑like 格式，利用 Otsu 方法產生海陸遮罩以進行 copy‑paste 資料增強，訓練階段提供多個基線與實驗 Notebook，最終模型於 final_model.ipynb 中訓練，推論與評估則分別於 final_evaluation.ipynb 與 eval/ 目錄中的 Notebook 完成。

## 架構
專案結構採模組化 Notebook 組織：data/ 目錄負責 SAR 影像前處理與轉換為 Detectron2 格式；train/ 目錄包含各種基線、實驗以及最終模型的訓練腳本（final_model.ipynb）；util/ 提供繪圖與海陸遮罩產生（Otsu 方法）以支援 copy‑paste 資料增強；eval/ 目錄負責模型效能評估；最終模型的訓練在 final_model.ipynb 中完成，推論則在 final_evaluation.ipynb 中載入外部權重進行偵測並產生結果，評估則透過 eval/ 目錄的 Notebook 計算指標。資料流程為：原始 SAR 影像 → 前處理 (data/) → Detectron2 資料集 → 模型訓練 (train/、final_model.ipynb) → 得到權重 → 推論 (final_evaluation.ipynb) → 評估 (eval/)。由於權重與資料集未納入此 repo，實際執行需自行下載。

## README 摘錄（節選）
```text
# LS-SSDD-v1.0-ShipDetectionComputerVision
This is the code repository for the paper _Small Vessel Detection from Synthetic Aperture Radar (SAR) Imagery using Deep Learning_ .
This project was done as part of Stanford's CS 230, Deep Learning course.
Please see this link: https://cs230.stanford.edu/past-projects/#outstanding-projects for our posting.
Given the numerous models under consideration and the modular data downloading process, we present our code through interactive Jupyter notebooks.
Note that model weights, model output, and the dataset are *not* in this repo.
The original dataset can be found at: https://github.com/TianwenZhang0825/LS-SSDD-v1.0-OPEN
We make heavy use of Detectron2 which can be found at: https://github.com/facebookresearch/detectron2
## Overview
The root directory features two notebooks training our best model and also performing inference.
`final_model.ipynb` is where we train the Improved model
`final_evaluation.ipynb` is where we perform inference on the Improved model
### class documents
Contains our papers as part of the CS230 Deep Learning.
### papers
Collection of papers that we used in the course of this project
### train
All of our training notebooks (which include baselines, experiments, and our final models presented in our paper)
### data
Notebooks for preprocessing data and converting into `Detectron2` format
### util
Notebooks for generating plots for the writeup and developing the sea-land mask for copy-paste augmentation using Otsu's method
### eval
Notebooks for evaluating our models
```
