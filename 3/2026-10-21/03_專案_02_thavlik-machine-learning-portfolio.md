# GitHub 專案 02：thavlik/machine-learning-portfolio

- 日期：2026-10-21
- URL：https://github.com/thavlik/machine-learning-portfolio
- 描述：Assorted machine learning implementations for medical data (legacy)
- Stars：50  |  Forks：5  |  Language：Python
- License：Apache-2.0
- Topics：computed-tomography, computer-vision, deep-learning, eeg, electroencephalography, fmri, functional-mri, gan, hemorrhage-detection, machine-learning, magnetic-resonance-imaging, medical, medicine, mri, neurology, neuroscience, radiology, reinforcement-learning, tumor-segmentation, vae
- 更新時間：2026-10-16T14:31:46+00:00
- 配對論文：https://arxiv.org/abs/1312.6114
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
本專案是一個醫學影像與訊號的機器學習實作集合，包含腦內出血類型分類、EEG 細微運動偵測、腹部 CT 腫瘤定位等已完成任務，以及 fMRI 特徵推斷、MRI 問卷預測、可微分 3D 渲染等進行中的研究。目標使用者為醫學 AI 研究者、醫學生與對醫學影像處理感興趣的開發者，核心在於利用深度學習方法解決醫學資料的標註稀疏、模態複雜及小樣本挑戰。

## 技術
專案主要使用 Python 實作，透過 YAML 檔案定義實驗參數，由 src/main.py 讀取配置啟動訓練或推論流程。建議使用 Docker 建立可重現的 GPU 環境，並透過 nonechucks 套件提升資料載入容錯性。根據所引用文獻，實作涵蓋變分自編碼器 (VAE)、生成對抗網路 (GAN)、卷積神經網路 (CNN)、循環神經網路 (RNN) 與強化學習等模型，並支援批次大小調整以適應 11 GiB 顯卡。

## 架構
專案結構以 experiments 為主要模組，每個子目錄對應一個具體任務（如 rsna-intracranial、grasp_and_lift_eeg、deeplesion 等），內含該任務的資料準備、模型定義與訓練腳本。所有實驗透過統一的入口 src/main.py 讀取放置於專案根目錄的 YAML 配置檔，配置中可經由 include 指令組合衍生實驗，以減少重複樣板碼。資料流程為：載入資料集 → 前處理（依需求進行正規化、切片等） → 模型前向傳播 → 損失計算 → 反向傳播與參數更新 → 驗證與指標記錄。Dockerfile 用於建立含 CUDA 與相依套件的映像，確保在不同主機上可重現結果。由於 README 未提供詳細的類別圖或服務間通訊方式，以上架構描述僅基於可見的目錄結構與執行說明。

## README 摘錄（節選）
```text
# Thomas Havlik's Medical AI Portfolio
(https://github.com/thavlik/machine-learning-portfolio)
(https://www.python.org/)
(./LICENSE-Apache)
(./LICENSE-MIT)
I am a deep learning researcher that is applying for the 2024 medical school admission cycle. It seems beneficial to offer concrete examples of how I work with medical data. These projects are enumerated here, and each has its own page that details the challenges faced and the results achieved. A few other miscellaneous projects also made the cut.
In accordance with non-disclosure, none of my professional medical AI work is featured here.
## Experiments
These experiments make use of ground truth provided with the data. Ground truth for medical data typically constitutes either empirical measurement or the judgment of attending physicians.
### Completed projects
This is a list of tasks that I have "solved", meaning that I've trained a model capable of performing the task with respectable accuracy.
- RSNA Intracranial Hemorrhage Prediction (experiments/rsna-intracranial/README.md): classification of brain CT scans by hemorrhage type
- Grasp-and-Lift EEG Detection (experiments/grasp_and_lift_eeg/README.md): fine-grain detection of motor activity using EEG
- DeepLesion (experiments/deeplesion/README.md): localization of tumors on abdominal CT scans
### Works in progress
These are tasks that I haven't solved yet, mostly because training on fMRI scans is nontrivial and requires way more video memory than I have at my disposal. As the potential for machine interpretation of fMRI data is enormous, I am determined to deliver on a project with this modality.
- StudyForrest (experiments/forrestgump/README.md) (WIP): infer features of an audio-only film with fMRI
- LA5c Study (experiments/la5c/README.md) (WIP): predict participants' questionnaire answers from their MRI scans
- Neural Rendering (experiments/graphics/README.md) (WIP): single-shot, differentiable 3D rendering
## Datasets
These are datasets that I have compiled. My interest in the modeling of visual manifolds was first inspired by recurrent dreams of mine that assume the form of video games (https://en.wikipedia.org/wiki/Tetris_effect), particularly those from my childhood. I have always found such media of dreaming to be both visually intuitive and semantically potent - attributes critical for unsupervised learning.
- Neurosurgery Video Dataset (https://github.com/thavlik/neurosurgery-video-dataset) (WIP): brain & spine surgery videos curated with the intent of enhancing neurosurgical e-Shadowing
- Doom Gameplay Dataset (https://github.com/thavlik/doom-gameplay-dataset): 170+ hours of unlabeled Doom 1/2 (https://en.wikipedia.org/wiki/Doom_(1993_video_game)) gameplay
- Quake Gameplay Dataset (https://github.com/thavlik/quake-gameplay-dataset): 200+ hours of unlabeled Quake 1 (https://en.wikipedia.org/wiki/Quake_(video_game)) gameplay
## Tools
These are various pieces of software I have written that pertain to either medical education or machine learning research. I think the potential for software to enhance medical education is substantial, especially given the promises of machine learning.
- e-Shadowing Transcriber (https://github.com/thavlik/transcriber): an application for enhancing the medical e-Shadowing experience
- vpn-operator (https://github.com/thavlik/vpn-operator): a Kubernetes controller for VPN sidecars written in pure Rust
- t4vd (Tool for Video Data) (https://github.com/thavlik/t4vd): a collaborative, open source platform for easily creating labeled datasets from YouTube videos
- Midas Download Tool (https://github.com/thavlik/midas-download-tool): a collection of scripts that bulk downloads MRIs made public by Kitware (https://www.kitware.com/) on their now-retired MIDAS platform. The repository now serves as an archive for the difficult-to-find CASILab Brain MRI dataset comprised of healthy volunteers.
## Running Code
Configurations are defined in `.yaml` files, which can be composed via the `include:` d
```
