# GitHub 專案 04：YipengHu/MPHY0041

- 日期：2026-10-13
- URL：https://github.com/YipengHu/MPHY0041
- 描述：UCL Module: Machine Learning in Medical Imaging
- Stars：21  |  Forks：14  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-10-07T09:12:27+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
本專案為倫敦大學學院（UCL）課程 MPHY0041《醫學影像中的機器學習》的深度學習部分，提供以 Python 為基礎的教學腳本與練習，目標使用者為修讀該課程的學生以及對醫學影像應用深度學習感興趣的學習者，旨在透過實作教學解決影像分類、分割、配準與合成等核心問題。

## 技術
專案主要使用 Python 程式語言，並同時支援 TensorFlow 與 PyTorch 兩種深度學習框架進行模型建構與訓練。教學內容包含基礎的 NumPy、Matplotlib 等資料處理與視覺化庫，以及針對醫學影像常見的 SimpleITK 或 nibabel（依各教程說明）進行影像讀取與前處理。

## 架構
儲存庫結構分為 docs 與 tutorials 兩大部分。docs 內含開發環境說明、Python 與機器學習快速複習、TensorFlow 與 PyTorch 學習指南、形成性評估與閱讀清單。tutorials 依功能分為 classification、segmentation、registration、synthesis 四個子資料夾，每個資料夾內含對應的 Python 腳本與 readme.md，說明所需資料庫、模型架構與執行步驟。資料流程為：讀取樣本醫學影像（2D 超聲、3D MR、CT 切片）→ 前處理 → 建構對應的深度學習模型（依框架選擇）→ 訓練或推論 → 評估結果與視覺化。由於 README 未詳細說明各教程的內部模型細節，以上架構說明僅根據目錄結構與說明推斷而得。

## README 摘錄（節選）
```text
# MPHY0041: Machine Learning in Medical Imaging
UCL Module (https://www.ucl.ac.uk/module-catalogue/modules/machine-learning-in-medical-imaging-MPHY0041) | MPBE (https://www.ucl.ac.uk/medical-physics-biomedical-engineering/) | UCL Moodle Page (https://moodle.ucl.ac.uk)
> Term 1
This repository is for the deep learning part of the module.
## 1. Development environments
This repository contains coding tutorials and exercises based on Python. While assuming basic experience in Python programming, learning materials are summarised in the docs (docs) folder.
- The supported development environment tools are summarised in module development environment (docs/env.md).
- For a refresher, have a look at A Roadmap to Learning Python and Machine Learning by Yourself (docs/python_ml.md).
- Module tutorials are implemented in both TensorFlow (https://www.tensorflow.org/) and PyTorch (https://pytorch.org/).
- Learning TensorFlow for Medical Imaging (docs/tensorflow.md).
- Learning PyTorch for Medical Imaging (docs/pytorch.md).
## 2. Deep learning tutorials
Deep learning tutorials are in Python scripts, in the tutorials (./tutorials) folder.
Individual tutorials may also require other libraries which will be specified in the readme.md in individual tutorial folders (see links below).
- Image classification: Anatomical structure classification on 2D ultrasound images (tutorials/classification/readme.md)
- Image segmentation: Segmentation of organs on 3D MR images (tutorials/segmentation/readme.md)
- Image registration: Unsupervised registration of CT image slices (tutorials/registration/readme.md)
- Image synthesis: Ultrasound image simulation (tutorials/synthesis/readme.md)
## 3. Formative assessment
A list of tasks are detailed in the Formative Assessment (docs/formative.md). Complete them for individual tutorials.
## 4. Reading list
A collection of books and research papers, relevant to deep learning for medical image analysis, is provided in the Reading List (docs/reading.md).
## Contact
> Feel free to create an issue for questions or suggestions.
|Name | Email | Role |
|---------------------|-----------------------------|-------------------------|
|Yipeng Hu | | Lecturer |
|Andre Altmann | | Module Lead |
```
