# GitHub 專案 04：YipengHu/MPHY0041

- 日期：2026-10-25
- URL：https://github.com/YipengHu/MPHY0041
- 描述：UCL Module: Machine Learning in Medical Imaging
- Stars：21  |  Forks：14  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-10-07T09:12:27+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案為倫敦大學學院（UCL）MPHY0041《醫學影像機器學習》課程的深度學習部分提供程式教學與練習，主要面向修讀該課程的學生以及對醫學影像深度學習感興趣的學習者。透過提供圖像分類、分割、配準與合成四個方向的 Jupyter/Python 教學腳本，協助學習者了解並實作常見醫學影像分析任務，解決缺乏實作教材與框架對比學習的問題。

## 技術
專案以 Python 為主要程式語言，同時支援 TensorFlow 與 PyTorch 兩種深度學習框架。教學內容以 Python 腳本形式放置於 tutorials 資料夾下，各教學單獨的 readme.md 會列出所需的額外函式庫。環境設定說明位於 docs/env.md，並提供 Python 與機器學習入門文件（docs/python_ml.md）、TensorFlow 與 PyTorch 專屬學習指引（docs/tensorflow.md、docs/pytorch.md）。此外，docs 資料夾還包含形成性評估任務清單與閱讀清單，供學習者參考與自我評估。

## 架構
專案結構主要分為 tutorials 與 docs 兩大部分。tutorials 下又依功能分為 classification、segmentation、registration、synthesis 四個子資料夾，每個子資料夾內含對應的 Python 教學腳本與該腳本的 readme.md，說明資料來源、所需套件與執行步驟。docs 資料夾則提供開發環境設置（env.md）、Python 與機器學習基礎複習（python_ml.md）、TensorFlow 與 PyTorch 的學習指引、形成性評估任務（formative.md）與閱讀清單（reading.md）。由於 README 未詳細說明具體的資料載入流程、模型訓練或推論的執行細節，因此架構敘述僅基於目錄結構與說明文件的可見資訊，推斷依據不足。

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
