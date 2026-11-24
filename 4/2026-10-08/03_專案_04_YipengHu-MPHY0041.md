# GitHub 專案 04：YipengHu/MPHY0041

- 日期：2026-10-08
- URL：https://github.com/YipengHu/MPHY0041
- 描述：UCL Module: Machine Learning in Medical Imaging
- Stars：21  |  Forks：14  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-10-07T09:12:27+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
本專案為倫敦大學學院（UCL）MPHY0041《醫學影像機器學習》課程的深度學習部分，提供以 Python 為基礎的教學腳本與練習，涵蓋 2D 超聲波影像分類、3D MR 影像器官分割、CT 切片無監督配對以及超聲波影像合成四個主題，目標使用者為修讀該課程的學生及對醫學影像深度學習感興趣的學習者，旨在透過實作教學幫助學習者理解並應用 TensorFlow 與 PyTorch 在醫學影像分析上的常見任務。

## 技術
專案主要使用 Python 3，深度學習框架採用 TensorFlow 2.x 與 PyTorch 1.x，教學內容以獨立的 Python 腳本形式放置於 tutorials 資料夾，每個教學可能依賴額外套件（如 NumPy、SimpleITK、 nibabel 等）並在各自的 readme.md 中說明。開發環境說明於 docs/env.md，提供安裝與依賴管理的指引，同時提供 Python 與機器學習入門文件（docs/python_ml.md）作為預備知識。資料流程方面，教學腳本讀取樣本影像資料，進行前處理、模型建構、訓練與評估，全部以可執行的 script 呈現。

## 架構
根據 README，專案結構大致分為四個主要部分：docs（開發環境、Python 基礎、TensorFlow/PyTorch 指南、形成性評估與閱讀清單）、tutorials（依功能分為 classification、segmentation、registration、synthesis 四個子資料夾，每子資料夾內含對應的 Python 教學腳本與 readme.md）、formative assessment（docs/formative.md）以及聯絡資訊。在每個教學腳本中，典型的執行流程為：讀取對應的醫學影像資料集 → 進行必要的前處理（如歸一化、裁切、資料增強） → 建構 TensorFlow 或 PyTorch 模型 → 進行模型訓練與驗證 → 輸出分割、分類、配對或合成結果並進行可視化或評估。由於 README 未提供具體的模型架構、資料來源或訓練超參數細節，以上流程僅基於文件中所述的教學目錄與說明進行合理推斷。

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
