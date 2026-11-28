# GitHub 專案 05：jakee417/LS-SSDD-v1.0-ShipDetectionComputerVision

- 日期：2026-10-15
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
本專案提供一個基於深度學習的小型船舶偵測 pipeline，針對合成孔徑雷達（SAR）影像進行目標辨識與定位。主要使用 Detectron2 框架實作改良的物件偵測模型，透過 Jupyter Notebook 進行資料前處理、模型訓練與推論評估。目標使用者為從事遙感圖像分析、海上監控或學術研究的研究生與工程師，他們需要在缺乏標註資料的 SAR 圖像上快速驗證深度學習模型的表現。核心問題在於 SAR 影像具有強烈的斑點噪聲與複雜背景，傳統方法難以偵測小型船舶；本專案透過模組化的資料下載、預處理（包括海陸遮罩產生與 Otsu 方法的 copy‑paste 資料增強）以及可互動的 notebook，讓使用者能夠重現論文中的實驗流程，並自行替換資料集或模型結構進行實驗。

## 技術
專案主要以 Python 為開發語言，使用 Jupyter Notebook 作為互動式開發環境。核心偵測模型建基於 Facebook AI Research 的 Detectron2 框架，採用 Faster R-CNN 或其變體作為 backbone，並透過自訂資料集載入器將 SAR 影像轉換為 Detectron2 所需的 COCO 格式。資料流程包括：從原始 LS-SSDD 資料集下載影像與標註、利用 Otsu 方法產生海陸遮罩以進行 copy‑paste 資料增強、將增強後的樣本轉為 Detectron2 可訓練的字典列表。訓練過程使用 notebook `final_model.ipynb`，其中設定學習率、批次大小、訓練週期以及模型檢查點儲存。推論則在 `final_evaluation.ipynb` 中載入已訓練好的權重，對測試影像執行偵測，並透過視覺化 notebook 產生預測框與評估指標（如 mAP、召回率）。此外，專案還提供論文閱讀與相關參考文獻的 notebook，方便使用者快速查閱理論基礎。

## 架構
根據 README 與目錄結構，專案採用模組化的 notebook 組織方式，主要分為六個功能區塊：`train` 放置各種訓練實驗 notebook（包括基線、消融實驗與最終改良模型）；`data` 負責原始 SAR 影像的前處理、格式轉換以及產生 Detectron2 所需的標註檔；`util` 提供繪圖與海陸遮罩生成（Otsu 方法）的輔助腳本，支援 copy‑paste 資料增強；`eval` 包含模型評估與結果視覺化的 notebook；`class documents` 與 `papers` 則存放課程報告與參考文獻。資料流程自 `data` notebook 讀取原始影像，經過遮罩產生與資料增強後轉為 Detectron2 字典，送入 `train` notebook 進行模型訓練；訓練完成後，權重被載入至 `eval` notebook 中進行推論與效能評估。由於 README 未提供詳細的類別圖或模組間依賴圖，以上架構描述僅基於目錄結構與 notebook 名稱的推斷，若需更精細的元件互動細節則必須參考原始 notebook 內容。

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
