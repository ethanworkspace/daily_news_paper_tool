# GitHub 專案 03：thavlik/machine-learning-portfolio

- 日期：2026-11-05
- URL：https://github.com/thavlik/machine-learning-portfolio
- 描述：Assorted machine learning implementations for medical data (legacy)
- Stars：50  |  Forks：5  |  Language：Python
- License：Apache-2.0
- Topics：computed-tomography, computer-vision, deep-learning, eeg, electroencephalography, fmri, functional-mri, gan, hemorrhage-detection, machine-learning, magnetic-resonance-imaging, medical, medicine, mri, neurology, neuroscience, radiology, reinforcement-learning, tumor-segmentation, vae
- 更新時間：2026-10-16T14:31:46+00:00
- 配對論文：https://arxiv.org/abs/1312.6114
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
本專案是 Thomas Havlik 的醫學 AI 投資組合，彙總多項針對醫療影像與生理訊號的機器學習實作，已完成的項目包括腦部 CT 出血類型分類、EEG 細微運動偵測與腹部 CT 腫瘤定位；進行中的研究則涉及 fMRI 特徵推論、MRI 問卷預測與單幀可微 3D 渲染。目標使用者為醫學影像研究者、腦科訊號處理學生與醫工人員，核心在於提供可重現的程式碼與資料集，以驗證及擴展深度學習在醫學領域的應用。

## 技術
該專案以 Python 為主要開發語言，實驗設定透過 YAML 檔案進行，支援 include 指令以組合衍生實驗，入口點為 src/main.py，透過 --config 參數載入設定。實作中使用了 nonechucks 例外抑制庫以提升容錯，並建議使用 Docker 以確保可重現的 GPU 環境，參考 NVIDIA 的 GPU Docker 使用指南。根據 README 中引用的文獻，實作涵蓋變分自編碼器（VAE）、生成對抗網路（GAN）、殘差網路（ResNet）等深度學習模型，適用於影像分類、訊號偵測與分割等任務。資料流程方面，資料集先經過驗證（可透過 exp_params.data.safe 關閉例外抑制），再送入模型進行訓練與驗證，最終輸出預測結果或生成樣本。

## 架構
專案結構以 experiments 目錄為核心，每個子目錄對應一項具體任務（如 rsna-intracranial、grasp_and_lift_eeg、deeplesion 等），內含該任務的 README、實驗設定 YAML 檔案以及所需的腳本或模型定義。所有實驗均透過專案根目錄的 src/main.py 進行啟動，主程式讀取指定的 YAML 配置，透過 include 指令可疊加基礎設定以快速建立衍生實驗。資料載入與前處理依實驗而定，通常在驗證階段會使用 nonechucks 抑制例外以提升容錯，必要時可透過 exp_params.data.safe=false 關閉此行為。訓練流程遵循標準的前向傳播、損失計算與反向傳播，支援 GPU 加速；建議使用 Dockerfile 建立映像，並透過 nvidia-docker 啟用 --gpus all 旗標以獲得完整的 GPU 資源。至於共用的工具（如 transcriber、vpn-operator、t4vd、midas-download-tool）則各自維護獨立的倉庫，主要作為資料蒐集或輔助開發的輔助程式。由於 README 未提供詳細的模型架構圖或具體的類別與函式呼叫關係，以下架構描述主要基於目錄組織與執行方式的推斷。

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
