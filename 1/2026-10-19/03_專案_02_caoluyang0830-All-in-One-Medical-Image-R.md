# GitHub 專案 02：caoluyang0830/All-in-One-Medical-Image-Restoration

- 日期：2026-10-19
- URL：https://github.com/caoluyang0830/All-in-One-Medical-Image-Restoration
- 描述：
- Stars：21  |  Forks：3  |  Language：Python
- License：NOASSERTION
- Topics：
- 更新時間：2026-11-20T01:25:14+00:00
- 配對論文：https://doi.org/10.1038/s42256-026-01310-z
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
AMIFound 提供一個統一的基礎模型，能夠使用同一組權重完成七種不同醫學影像模態（內視鏡、眼底照相、PET、超音波、X光、CT、MR）的復原與增強任務，包括低光增強、斑點光去除、噪聲減少、聲學伺服 artefact 去除、去模糊、金屬伺服 artefact 減少以及低品質 MR 復原。目標使用者為醫學影像研究者與演算法開發者，解決傳統需要為每種模態任務訓練獨立模型的問題，提供可重現的訓練、評估與降樣生成工具。

## 技術
專案使用 Python 3 與 PyTorch 框架實作，依賴 CUDA 11.8 進行 GPU 加速訓練與推論。核心程式碼位於 src/ 資料夾，包含模型定義（unified foundation model）、資料載入與配對處理（dataset_utils_all.py）、訓練腳本（train_AMIFound.py）以及成對評估腳本（eval_AMIFound.py），同時提供 degradation 生成腳本位於 modality/ 子目錄中，用以合成低品質影像。環境透過 Conda 建立，需求套件見 requirements.txt，支援從外部 Google Drive 下載預訓練權重（last.ckpt）與樣本成對資料。

## 架構
AMIFound 的架構分為四個主要模組：(1) 模型核心，採用單一權重的 Transformer‑based 基礎模型，接受低品質影像輸出復原結果；(2) 資料處理層，透過 dataset_utils_all.py 讀取成對低品質與參考 PNG，依照 70/30 隨機切分（seed 42）產生訓練與驗證批次；(3) 訓練流程，執行 train_AMIFound.py，使用損失函數（L1 + 感知損失）優化模型，定期儲存 checkpoint 至 checkpoints/ 目錄；(4) 評估與降樣生成，eval_AMIFound.py 計算 PSNR、SSIM、LPIPS 並儲存復原影像，modality/ 中的腳本可合成對應任務的退化影像以產生額外測試資料。若需自訂資料路徑，需修改 src/data/dataset_utils_all.py 中的 DATA_ROOT 變數。

## README 摘錄（節選）
```text
# AMIFound: An All-in-One Foundation Model for Multimodal Medical Image Restoration and Enhancement
Official PyTorch implementation accompanying the paper **“An All in One Foundation Model for Multimodal Medical Image Restoration and Enhancement.”**
** Repository:**
AMIFound is a unified medical image restoration model that uses one set of model weights for seven restoration and enhancement tasks across seven imaging modalities. The repository contains the model implementation, training and paired-evaluation code, degradation-generation utilities, pretrained weights hosted externally, and sample paired data.
## Quick Start
Follow Installation (#installation), download the pretrained model and sample data (#pretrained-model-and-sample-data), and complete Data preparation (#data-preparation). You can then run the example in Paired evaluation (#paired-evaluation), or follow Training (#training) to train AMIFound.
## Supported tasks
| Modality | Restoration or enhancement task | Low-quality folder | Reference folder |
| --- | --- | --- | --- |
| Endoscopy | Low-light enhancement | `Endoscopy_dark` | `Endoscopy` |
| Fundus photography | Spot-light artifact removal | `Fundus_spot_light` | `Fundus` |
| PET | Noise reduction | `PET_denoised` | `PET` |
| Ultrasound | Acoustic artifact removal | `Ultrasound_sound_artifacts` | `Ultrasound` |
| X-ray | Deblurring | `X_ray_blur` | `X_ray` |
| CT | Metal artifact reduction | `CT_metal_artifacts` | `CT` |
| MR | Restoration of low-quality MR images | `MR_LQ` | `MR` |
## What is included
[code block omitted]
## Installation
Clone the repository and create an isolated environment:
[code block omitted]
Training and evaluation are designed for an NVIDIA GPU with CUDA. The commands above use CUDA 11.8 as an example.
Alternatively, after creating and activating the Conda environment, install the dependencies with:
[code block omitted]
## Pretrained model and sample data
- Pretrained model (https://drive.google.com/drive/folders/11DfmFFPeKrW1KHtx_MAW3NtyhZOjI262)
- Sample paired data (https://drive.google.com/drive/folders/1f1IPbx_4sMiT2JzZKWsce0UIVt8a7KQa)
Download the pretrained `last.ckpt` checkpoint and place it as follows:
[code block omitted]
The value passed to `--checkpoint_id` is the directory name under `checkpoints/`.
## Data preparation
The standard AMIFound loaders expect paired low-quality and reference PNG images. Within each folder pair, use identical filenames and image dimensions so that sorting produces the correct pairs.
An example layout is:
[code block omitted]
### Path configuration
Before training or evaluation, configure the modality-specific input and reference folder locations in `src/data/dataset_utils_all.py` for your local `DATA_ROOT`.
The repository uses a fixed random split for each paired modality:
- 70% for training
- 30% for evaluation
- random seed 42
## Training
Run the training entry point from the repository root. The following is the configuration represented by the provided example script:
[code block omitted]
Checkpoints are written to:
[code block omitted]
The direct Python command above is recommended. The supplied `run_AMIFound_all_multiexpers2.sh` can also be adapted to the local Conda environment and repository location.
## Paired evaluation
The released evaluation entry point computes PSNR, SSIM, and LPIPS against paired reference images. Run one modality per invocation so that the benchmark and data-loader task are aligned:
[code block omitted]
To evaluate all seven tasks sequentially:
[code block omitted]
Metrics are printed to the terminal. Restored images are saved to:
[code block omitted]
## Usage
This release supports:
- reproduction of the paired-data training protocol;
- quantitative paired evaluation using PSNR, SSIM, and LPIPS;
- saving restored outputs during paired evaluation;
- generation of task-specific degraded images using the scripts in `modiality/`; and
- research on unified restoration across medical imaging modalities.
## Citation
```
