# GitHub 專案 05：jakee417/LS-SSDD-v1.0-ShipDetectionComputerVision

- 日期：2026-10-17
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
此專案針對合成孔徑雷達（SAR）影像中的小型船隻進行偵測，採用深度學習方法。目標使用者為海上監控、遙感研究與船舶安全領域的研究者與工作者，他們需要自動化地從 SAR 圖像中辨識小型船隻，以減少人工解讀的負擔並提升偵測效率。核心問題在於 SAR 影像雜訊大、船隻尺寸小且背景複雜，傳統方法難以達到理想的準確率，因此專案透過 Detectron2 框架訓練改進的物件偵測模型來解決此問題。

## 技術
專案主要使用 Python 實作，以 Jupyter Notebook 為互動開發環境。偵測模型基於 Facebook 的 Detectron2（建置在 PyTorch 上），採用改進的 Faster R-CNN 或類似的兩階段偵測架構。資料處理流程包括利用 Otsu 方法產生海陸遮罩以進行 copy‑paste 資料增強，以及將 SAR 影像轉換為 Detectron2 所需的 COCO 格式。此外，專案引用了多篇論文作為方法參考，並提供用於繪圖與實驗紀錄的工具筆記本。

## 架構
根據 README，專案目錄結構分為數個功能區塊：`train` 放置各種訓練筆記本（基線、實驗與最終模型）；`data` 包含前處理與格式轉換筆記本，將原始 SAR 影像轉為 Detectron2 可讀取的資料集；`util` 提供繪圖與產生海陸遮罩（Otsu 方法）的工具；`eval` 負責模型評估與指標計算；`final_model.ipynb` 與 `final_evaluation.ipynb` 分別負責改進模型的訓練與推論。資料流程大致為：原始 SAR 影像 → 前處理（雜訊減弱、海陸遮罩產生） → 轉換為 Detectron2 格式 → 在 `train` 中進行模型訓練 → 得到權重後在 `final_evaluation.ipynb` 進行推論 → 在 `eval` 中計算精準率、召回率等指標。由於模型權重、輸出與資料集未納入此倉庫，實際執行需自行從連結的原始資料庫下載資料。

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
