# GitHub 專案 04：thavlik/machine-learning-portfolio

- 日期：2026-11-02
- URL：https://github.com/thavlik/machine-learning-portfolio
- 描述：Assorted machine learning implementations for medical data (legacy)
- Stars：50  |  Forks：5  |  Language：Python
- License：Apache-2.0
- Topics：computed-tomography, computer-vision, deep-learning, eeg, electroencephalography, fmri, functional-mri, gan, hemorrhage-detection, machine-learning, magnetic-resonance-imaging, medical, medicine, mri, neurology, neuroscience, radiology, reinforcement-learning, tumor-segmentation, vae
- 更新時間：2026-10-16T14:31:46+00:00
- 配對論文：https://arxiv.org/abs/1312.6114
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
此專案是 Thomas Havlik 的醫學機器學習作品集，收錄了多項完成的實驗與進行中的研究，目標使用者為對醫學影像與訊號（CT、EEG、fMRI）感興趣的研究者與學生，核心在提供可重現的程式碼與資料處理流程，示範如何應用深度學習模型進行腦出血分類、運動偵測、腫瘤定位等醫學任務。

## 技術
專案主要以 Python 實作，使用 PyTorch 框架進行深度學習模型的建置與訓練，涵蓋變分自編碼器（VAE）、生成對抗網路（GAN）、漸進式 GAN、beta‑VAE、StyleGAN、Instance Normalization 以及殘差網路（ResNet）等架構；實驗設定透過 YAML 檔案與 include 指令組合，主入口為 src/main.py，支援 Docker 容器化運行，並利用 nonechucks 庫提升資料載入容錯性。

## 架構
每個實驗皆放在 experiments/ 目錄下，擁有獨立的 README 與資料準備腳本；使用者透過指定 YAML 配置檔（可透過 include 指令疊加基礎設定），執行 src/main.py 時會讀取 exp_params，建立對應的資料集載入器、模型實例化與訓練/評估迴圈；資料流程為：原始醫學影像或訊號 → 預處理（標準化、切片、增強） → 模型前向傳播 → 損失計算與反向傳播 → 模型更新；工具方面，t4vd 用於從 YouTube 建立標註資料集，midas-download-tool 批次下載公開 MRI，vpn-operator 則為以 Rust 寫成的 Kubernetes VPN sidecar 控制器，提供網路隔離與安全傳輸。

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
