# GitHub 專案 02：thavlik/machine-learning-portfolio

- 日期：2026-10-17
- URL：https://github.com/thavlik/machine-learning-portfolio
- 描述：Assorted machine learning implementations for medical data (legacy)
- Stars：50  |  Forks：5  |  Language：Python
- License：Apache-2.0
- Topics：computed-tomography, computer-vision, deep-learning, eeg, electroencephalography, fmri, functional-mri, gan, hemorrhage-detection, machine-learning, magnetic-resonance-imaging, medical, medicine, mri, neurology, neuroscience, radiology, reinforcement-learning, tumor-segmentation, vae
- 更新時間：2026-10-16T14:31:46+00:00
- 論文層級：未對應論文
- 配對論文：https://arxiv.org/abs/1312.6114
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
本專案是 Thomas Havlik 的醫學機器學習作品集，收錄了多項基於醫療影像與生理訊號的深度學習實作，包括腦部 CT 出血類型分類、EEG 細微運動偵測、腹部 CT 腫瘤定位以及 fMRI 特徵推論等任務。目標使用者為醫學研究者、醫學生與對醫療 AI 感興趣的開發者，旨在提供可重現的範例，說明如何處理醫療資料、設計實驗與評估結果，同時展示資料集蒐集與工具開發經驗。

## 技術
專案以 Python 為主要開發語言，實驗透過 YAML 組態檔案進行參數配置，支援 include 指令以減少樣板碼，並由 src/main.py 作為統一入口點。為確保環境可重現，提供 Dockerfile 與建議使用 NVIDIA GPU 的 Docker 運行方式。資料處理流程中使用 nonechucks 庫來抑制資料集例外，提升容錯性。此外，專案還包含自行開發的工具，如用於從 YouTube 建立標註資料集的 t4vd、用於批量下載公開 MRI 的 MIDAS 下載工具，以及用於醫學 e‑Shadowing 的轉錄器與 Kubernetes VPN sidecar 控制器。整體採用深度學習方法進行模型訓練與評估，但未在 README 中具體說明使用的框架版本。

## 架構
專案結構主要分為 experiments、tools 與根目錄三部分。每個實驗（如 rsna-intracranial、grasp_and_lift_eeg、deeplesion 等）均具備獨立的 README 與 YAML 組態檔，實驗執行時透過 main.py 讀取組態，進行資料載入（依賴各自的 Dataset 類別）、模型定義、訓練迴圈與驗證評估，最終輸出指標與模型檔案。tools 目錄則提供資料集蒐集、視訊標註、VPN 管理與轉錄等輔助功能，各自有各自的 README 與使用說明。根目錄含 LICENSE、requirements.txt（版本未約束）與 Dockerfile。由於 README 未詳細說明模型內部架構或訓練細節，架構描述僅基於可見的檔案組織與執行流程進行推論。

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
