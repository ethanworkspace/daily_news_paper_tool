# GitHub 專案 02：thavlik/machine-learning-portfolio

- 日期：2026-10-20
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
此專案是 Thomas Havlik 的醫學機器學習作品集，收錄多項針對醫療影像與生理訊號的深度學習實驗，包括 RSNA 顱內出血分類、EEG 細微運動偵測、腹部 CT 腫瘤定位以及正在進行的 fMRI 特徵推論、MRI 問卷預測與可微分 3D 渲染等任務，目標使用者為醫學研究者、影像科技師以及對醫學 AI 感興趣的開發者，核心在於展示如何利用現有標註資料訓練模型解決臨床相關的分割、偵測與預測問題。

## 技術
專案以 Python 為主要開發語言，實驗設定透過 YAML 檔案進行參數化，可透過 include 指令組合衍生實驗；執行入口為 src/main.py，透過 --config 指向對應的 YAML 檔案；為確保環境可重現，提供 Dockerfile 與建議使用 NVIDIA GPU 的 Docker 運行方式；程式中使用了 nonechucks 來提升資料載入容錯性；根據引用的論文（VAE、GAN、殘差網路等），可見實際運用了深度學習框架（如 PyTorch 或 TensorFlow）進行模型構建與訓練。

## 架構
專案結構以 experiments 為主要模組，每個子目錄對應一項具體任務（如 rsna-intracranial、grasp_and_lift_eeg、deeplesion 等），內含該任務的 README、資料準備腳本、模型定義與訓練腳本；所有實驗共用 src/main.py 作為統一啟動腳本，透過讀取實驗專屬的 YAML 配置來決定資料路徑、模型超參數與訓練策略；資料流程為：載入醫療影像或生理訊號 → 預處理（歸一化、切片、增強） → 送入對應的深度學習模型（VAE、GAN、CNN 等） → 進行前向計算與損失評估 → 反向傳播更新權重 → 驗證階段產出分割 mask、分類機率或特徵向量；若使用 Docker，則在容器內掛載資料卷並執行相同的指令。

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
