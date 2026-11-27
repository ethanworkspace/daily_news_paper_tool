# GitHub 專案 05：jakee417/LS-SSDD-v1.0-ShipDetectionComputerVision

- 日期：2026-10-03
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
此專案提供用於合成孔徑雷達（SAR）影像中小型船舶偵測的深度學習實作，包含資料前處理、模型訓練與推論的 Jupyter Notebook，以 Detectron2 為基礎，目標使用者為遠測與電腦視覺研究者及學生。該專案不包含模型權重與資料集，使用者需自行從提供的連結下載 LS-SSDD 資料集，並可參考隨附的論文與實驗筆記本了解基線與改進模型的實作細節。

## 技術
主要使用 Python 與 Jupyter Notebook 進行開發，核心偵測框架採用 Facebook 的 Detectron2（建置於 PyTorch 上），資料前處理筆記本將原始 SAR 影像轉換為 Detectron2 所需的 COCO 格式，利用 Otsu 方法產生海陸遮罩以進行 copy‑paste 資料增強，訓練過程透過偵測器的訓練迴圈進行優化，評估則利用標準的 COCO 指標（AP、AR）衡量模型在小型船舶上的表現。

## 架構
專案結構採用模組化筆記本方式：data 目錄中的 Notebook 負責下載與前處理資料，將 SAR 影像標註轉換為 Detectron2 可讀取的 dataset；train 目錄保存各種基線實驗與最終改進模型的訓練腳本（final_model.ipynb）；利用訓練好的權重，final_evaluation.ipynb 進行影像推論並產生偵測結果；eval 目錄提供評估腳本計算精準度與召回率；util 目錄則含用於繪圖的 Notebook 與根據 Otsu 方法產生海陸遮罩的程式，支援 copy‑paste 資料增強。若 README 未明確說明特定模型架構，則推斷為基於 Detectron2 的 Faster R-CNN 或 RetinaNet 系列，但此部份僅為根據常見用法的推論。

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
