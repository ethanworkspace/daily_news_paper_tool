# GitHub 專案 05：jakee417/LS-SSDD-v1.0-ShipDetectionComputerVision

- 日期：2026-10-23
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
本專案利用深度學習模型，針對合成孔徑雷達（SAR）影像進行小型船舶偵測，旨在提升海上監視系統對微小目標的識別能力。主要使用 Detectron2 框架，透過 Jupyter Notebook 進行模型訓練與推論，提供完整的資料前處理、訓練、評估與視覺化流程。目標使用者包括海洋遙測研究者、船舶監控工程師以及對 SAR 目標檢測感興趣的深度學習實踐者。核心問題在於 SAR 影像具有斑點噪聲、低對比度與小目標特徵不明顯，傳統方法難以達到理想偵測率，因此需藉由端到端的深度學習管線學習特徵表示與區域提議，以實現高精度的小型船舶偵測。

## 技術
本專案以 Python 為主要程式語言，採用 Jupyter Notebook 作為互動式開發環境。核心偵測框架為 Detectron2（基於 PyTorch 的物件偵測庫），提供了 Faster R-CNN、Mask R-CNN 等可擴充的模型結構。資料流程包括：利用 Otsu 方法產生海陸遮罩，進行 copy‑paste 資料增強；將原始 SAR 影像轉換為 Detectron2 所需的 COCO 風格標註格式；在 train 目錄中的 Notebook 進行基線與改進模型的訓練；利用 eval 目錄中的 Notebook 進行模型推論與效能評估；util 目錄中的 Notebook 負責繪製實驗圖表與產生視覺化結果。此外，專案引用了多篇論文作為方法參考，但未在倉庫中包含模型權重或資料集，需自行從原始來源下載。

## 架構
根據 README 目錄結構，可將專案分為六個主要模組：class documents 與 papers 存放課程報告與參考文獻；train 包含各種訓練 Notebook，涵蓋基線實驗、消融研究以及最終改進模型的訓練流程；data 負責資料前處理，包括 SAR 影像的讀取、海陸遮罩產生（Otsu 方法）、copy‑paste 資料增強以及轉換為 Detectron2 所需的標註格式；util 提供繪圖函式與實驗圖表生成，支援寫報與結果分析；eval 包含推論 Notebook，載入訓練好的模型對測試集進行偵測，計算精準率、召回率等指標並輸出視覺化結果；最終的 final_model.ipynb 與 final_evaluation.ipynb 分別位於根目錄，用於訓練最佳模型與進行對應的推論。資料流程大致為：原始 SAR 影像 → data 模組前處理與增強 → 產生 Detectron2 格式資料集 → train 模組訓練模型 → eval 模組進行推論與評估 → util 模組產生圖表與報告。由於倉庫中未提供模型權重與資料集，上述流程需搭配外部下載的 LS-SSDD 資料集才能完整執行。

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
