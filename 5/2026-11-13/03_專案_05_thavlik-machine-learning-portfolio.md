# GitHub 專案 05：thavlik/machine-learning-portfolio

- 日期：2026-11-13
- URL：https://github.com/thavlik/machine-learning-portfolio
- 描述：Assorted machine learning implementations for medical data (legacy)
- Stars：50  |  Forks：5  |  Language：Python
- License：Apache-2.0
- Topics：computed-tomography, computer-vision, deep-learning, eeg, electroencephalography, fmri, functional-mri, gan, hemorrhage-detection, machine-learning, magnetic-resonance-imaging, medical, medicine, mri, neurology, neuroscience, radiology, reinforcement-learning, tumor-segmentation, vae
- 更新時間：2026-10-16T14:31:46+00:00
- 配對論文：https://arxiv.org/abs/1312.6114
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
此專案是 Thomas Havlik 的醫學 AI 投資組合，收錄了多項針對醫療影像與生理訊號的機器學習實驗，包括腦內出血分類、EEG 運動活動偵測與腹部 CT 腫瘤定位，並提供相關資料集與工具（如影片標記平台、MRI 下載腳本、K8s VPN 控制器），目標使用者為希望重現或擴展醫學深度學習研究的研究者、學生與醫療 AI 從業者。

## 技術
核心實作以 Python 為主語言，實驗透過 src/main.py 讀取 YAML 設定檔啟動，使用 Docker 確保環境可重現，並引用 nonechucks 來提升資料載入容錯性。專案中還包含以 Rust 編寫的 Kubernetes 控制器 vpn-operator（用於 VPN sidecar），以及以 Python/JavaScript 開發的 t4vd 影片標記平台與 Midas 下載工具。深度學習模型方面，實驗涉及卷積神經網路與變分自編碼器等常見架構（具體框架未在 README 中明確說明）。

## 架構
專案結構以 experiments 目錄分類不同任務（如 rsna-intracranial、grasp_and_lift_eeg、deeplesion），每個任務內含專屬的 Python 腳本與資料處理模組。統一入口為 src/main.py，透過 --config 指向實驗專用的 YAML 檔案，YAML 中可透過 include: 指令組合基礎配置，以減少樣板碼。資料流程為：載入對應的 Dataset 類別 → 前處理 → 模型前向傳播 → 損失計算與反向傳播（視任務而定） → 評估指標輸出。Dockerfile 描述建置鏡像的步驟，支援 GPU 運行；若需除錯可關閉 nonechucks 的安全模式。工具與資料集則以獨立倉庫形式提供，透過網路克隆或下載取得。若 README 未詳細說明某些內部實作（例如具體的網路結構或優化器選擇），則屬於推斷範圍。

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
