# GitHub 專案 05：jakee417/LS-SSDD-v1.0-ShipDetectionComputerVision

- 日期：2026-10-24
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
本專案針對合成孔徑雷達（SAR）影像中的小型船隻進行偵測，利用深度學習模型自動辨識船隻位置與大小，目標使用者為海洋監控、海上搜救、漁業管理及國防相關研究人員與工程師。核心問題在於 SAR 影像雖具全天候、全天候成像能力，但背景雜訊強、船隻尺寸小且形狀多樣，傳統圖像處理方法難以達到高召回率與低誤報率，因此專案透過 Detectron2 框架與自訂資料前處理（海陸遮罩、Otsu 方法產生的 copy‑paste 增強）來提升小型船隻的檢測效果。

## 技術
專案主要使用 Python 3.x，以 Jupyter Notebook 進行互動式開發與實驗。模型基於 Facebook Detectron2（v0.5+）實作，採用 Faster R-CNN 與其變體（如改良的 backbone、特徵金字塔網路）作為偵測骨幹。資料前處理包括使用 Otsu 方法產生海陸遮罩、將 SAR 影像轉換為 Detectron2 所需的 COCO 格式標註，並執行 copy‑paste 資料增強。訓練過程利用 Detectron2 的訓練迴圈與學習率排程，評估則採用 COCO 風格的 mAP 指標。此外，專案參考了多篇 SAR 船隻偵測論文，將其前處理與後處理步驟整合至 notebook 中。

## 架構
專案結構以 Jupyter Notebook 為主要模組，根目錄下依功能分為：train/ 包含基線、實驗與最終模型的訓練 notebook；data/ 負責 SAR 影像前處理、海陸遮罩產生（Otsu 方法）及轉換為 Detectron2 可讀的 COCO 格式；util/ 提供繪圖與 copy‑paste 資料增強輔助函式；eval/ 包含模型評估與最終推論的 notebook（final_evaluation.ipynb）；根目錄的 final_model.ipynb 與 final_evaluation.ipynb 分別負責最佳模型的訓練與推論。資料流程為：原始 SAR 影像 → data/ 前處理 → 產生標註與遮罩 → train/ 訓練模型 → eval/ 評估指標 → final_evaluation.ipynb 進行推論與視覺化。由於模型權重與資料集未納入儲存庫，具體的模型內部結構與超參數設定僅能從 notebook 中推斷，無法給出完整的圖形化架構圖。

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
