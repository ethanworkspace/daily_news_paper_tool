# GitHub 專案 04：YipengHu/MPHY0041

- 日期：2026-10-21
- URL：https://github.com/YipengHu/MPHY0041
- 描述：UCL Module: Machine Learning in Medical Imaging
- Stars：21  |  Forks：14  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-10-07T09:12:27+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
本專案為倫敦大學學院（UCL）MPHY0041《醫學影像機器學習》課程的深度學習部分，提供一系列以 Python 為基礎的教學腳本與文件，目標使用者為修讀該課程的研究生與對醫學影像分析感興趣的學習者，旨在透過實作教學幫助學習者理解並應用影像分類、器官分割、影像配對與影像合成等核心深度學習技術於醫學影像資料上。

## 技術
該專案主要使用 Python 程式語言，並同時支援 TensorFlow 與 PyTorch 兩種深度學習框架進行模型實作。教學材料以 Python 腳本形式放置於 tutorials 資料夾下，每個子資料夾（classification、segmentation、registration、synthesis）含有對應的 readme 與範例程式。環境設定說明位於 docs/env.md，提供依賴套件與開發工具的安裝指引；此外，docs 目錄尚包含 Python 與機器學習入門指南、閱讀清單與形成性評估任務說明。

## 架構
專案結構以 docs 與 tutorials 為主要目錄。docs 包含開發環境指南（env.md）、Python 與機器學習復習資料（python_ml.md）、各框架學習文件（tensorflow.md、pytorch.md）、形成性評估任務（formative.md）與閱讀清單（reading.md）。tutorials 下分為四個主題：classification（2D 超聲影像的解剖結構分類）、segmentation（3D MR 影像的器官分割）、registration（CT 影像切片的無監督配對）與 synthesis（超聲影像模擬）。每個教學腳本會讀取對應的樣本醫學影像資料，透過 TensorFlow 或 PyTorch 建立、訓練或推論模型，並將中間結果或最終輸出（如分類標籤、分割遮罩、變形場或合成影像）寫出或視覺化，以示範完整的資料流程與模型應用。若需更細部的模組內部實作，則需參考各 tutorial 資料夾中的具體程式碼。

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
