# GitHub 專案 03：thavlik/machine-learning-portfolio

- 日期：2026-10-31
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
此專案是 Thomas Havlik 的醫學機器學習作品集，包含已完成的 CT 出血分類、EEG 運動偵測與腫瘤定位，以及進行中的 fMRI 特徵推論、MRI 問卷預測與可微分 3D 渲染。目標使用者為醫學影像研究者與學生，核心問題在於將多模態醫學資料與深度學習模型結合，以實現疾病偵測、病灶分割及功能影像解釋。

## 技術
專案主要以 Python 實作，透過 YAML 檔案定義實驗參數，並由 src/main.py 讀取設定啟動訓練或推論。為確保環境可重現，建議使用 Docker，並參考 NVIDIA 指南啟用 GPU。README 中提到的模型包括變分自編碼器（VAE）、生成對抗網路（GAN）、殘差網路（ResNet）以及強化學習方法，這些通常依賴於 PyTorch 或 TensorFlow 等深度學習框架。資料流程方面，實驗會先載入對應的醫學資料集（CT、EEG、fMRI、MRI），經過前處理後送入模型進行分類、分割或特徵推論，結果則寫入日誌或輸出檔案。此外，專案使用 nonechucks 套件來抑制資料載入例外，以提升容錯能力。

## 架構
專案採用模組化結構：頂層目錄包含 experiments/（各任務子目錄）、src/（共用腳本與 main.py）以及工具資料夾（如 transcriber、vpn‑operator、t4vd、midas‑download-tool）。每個實驗在 experiments/<task>/ 中提供獨立的資料集下載、前處理、模型定義與訓練循環，透過 YAML 檔案指定超參數與資料路徑。執行時，使用者呼叫 `python src/main.py --config experiments/<task>/config.yaml`，main.py 讀取設定、初始化資料載器、建構模型（依任務選用 VAE、GAN、ResNet 等）、進行訓練或推論，並將指標與樣本輸出至 runs/ 目錄。Dockerfile 用於封裝相依套件與 CUDA 執行環境。由於 README 未提供詳細的類別圖或序列圖，上述架構推斷基於目錄組織與說明的執行方式。

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
