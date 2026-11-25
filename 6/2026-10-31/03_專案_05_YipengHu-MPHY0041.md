# GitHub 專案 05：YipengHu/MPHY0041

- 日期：2026-10-31
- URL：https://github.com/YipengHu/MPHY0041
- 描述：UCL Module: Machine Learning in Medical Imaging
- Stars：21  |  Forks：14  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-10-07T09:12:27+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案為 UCL MPHY0041 課程的深度學習部分，提供以 Python 撰寫的教學腳本與練習，涵蓋醫學影像的分類、分割、配準與合成四個主題，幫助學生理解並實作常見的深度學習方法於臨床影像分析。

## 技術
專案主要使用 Python 程式語言，並同時提供 TensorFlow 與 PyTorch 兩種深度學習框架的實作範例。教學材料以純文字腳本形式放置於 tutorials 資料夾，並搭配 docs 資料夾中的環境設定、Python 溫習與閱讀清單。

## 架構
資料夾結構包括 docs（環境、Python 溫習、TensorFlow、PyTorch、形成性評估、閱讀清單）與 tutorials（classification、segmentation、registration、synthesis）。每個 tutorial 獨立執行：載入對應的醫學影像（2D 超聲、3D MR、CT 切片），進行前處理後喂入 CNN 模型，輸出標籤、分割映射、變形場或合成影像。由於 README 未詳細說明模型內部或資料流程，以上架構推斷僅基於目錄結構與所述任務。

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
