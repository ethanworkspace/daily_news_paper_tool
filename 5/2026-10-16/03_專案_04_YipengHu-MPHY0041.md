# GitHub 專案 04：YipengHu/MPHY0041

- 日期：2026-10-16
- URL：https://github.com/YipengHu/MPHY0041
- 描述：UCL Module: Machine Learning in Medical Imaging
- Stars：21  |  Forks：14  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-10-07T09:12:27+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案為 UCL 課程 MPHY0041《Medical Imaging 中的機器學習》的深度學習部分提供教學資源。它包含以 Python 撰寫的教學腳練習，目標使用者為修讀該課程的學生以及對醫學影像深度學習感興趣的學習者。核心問題在於幫助學習者理解並實作常見的醫學影像任務，如分割、分類、配準與合成，透過 TensorFlow 與 PyTorch 框架進行實作練習。

## 技術
專案主要使用 Python 程式語言，並同時支援兩種主流深度學習框架：TensorFlow 與 PyTorch。教學內容以腳本形式放置在 tutorials 資料夾下，分為影像分類、影像分割、影像配準與影像合成四個主題。每個教學資料夾內含各自的 readme.md，說明所需的額外函式庫。此外，docs 資料夾提供開發環境說明、Python 與機器學習入門指南、TensorFlow 與 PyTorch 的學習資源，以及形成性評估與閱讀清單。

## 架構
專案結構分為 docs 與 tutorials 兩大部分。docs 包含環境設置、程式語言復習、框架學習指南、形成性評估任務與閱讀清單。tutorials 資料夾下又依功能細分為 classification、segmentation、registration 與 synthesis 四個子資料夾，每個子資料夾內含對應的 Python 教學腳本與 readme.md，說明資料載入、模型建構、訓練或推論步驟以及評估方式。使用者通常會先閱讀相應的 readme 了解所需資料與依賴項，然後執行腳本進行實作，資料流程為：載入醫學影像資料集（2D 超聲、3D MR、CT 切片等）→ 預處理 → 建構/載入模型（依框架而定）→ 訓練或推論 → 結果視覺化與評估。由於 README 未詳細說明各腳本內部模組劃分，以上架構說明僅基於目錄結構與文件說明的可觀察資訊。

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
