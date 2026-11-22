# GitHub 專案 01：earth-insights/SegEarth-R1

- 日期：2026-11-20
- URL：https://github.com/earth-insights/SegEarth-R1
- 描述：SegEarth-R1: Geospatial Pixel Reasoning via Large Language Model
- Stars：159  |  Forks：11  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-09-23T08:08:53+00:00
- 配對論文：https://www.semanticscholar.org/paper/eab0e7a7082dd467eee45b66d15df841da8ccec2
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
SegEarth-R1 提供一種基於大型語言模型的地理空間像素推理方法，使使用者能以自然語言提出隱含的空間查詢（例如『顯示最近洪水影響的農田』），系統則解析指令、融合多尺度視覺特徵並直接輸出目標區域的分割遮罩。該專案面向遙感研究人員、GIS 分析師以及環境與災害管理從業者，旨在克服傳統分割/偵測方法對複雜、依賴領域知識與使用者意圖的隱含查詢處理能力不足的問題，透過構建 EarthReason 基準資料集與提出簡單有效的語言導向分割基線，提升遙感圖像的推理與參考分割性能。

## 技術
SegEarth-R1 以 Python 實作，採用階層式視覺編碼器處理超高解析度遙感影像並進行激進的視覺標記壓縮；大型語言模型負責解析使用者的自然語言指令；描述投影模組將語言嵌入與多尺度視覺特徵融合；最後的遮罩生成器直接查詢描述嵌入以產生目標區域的分割遮罩。訓練過程使用 DeepSpeed 進行分散式優化，參考開源專案 PSALM 與 Mask2Former 的結構與權重，透過 conda 環境安裝相依套件，支援資料準備、模型訓練與評估的腳本。

## 架構
根據 README，SegEarth-R1 的架構可劃分為四個主要模組：(1) 階層式視覺編碼器，負責讀取並壓縮超高解析度遙感影像的視覺標記；(2) 大型語言模型，負責將使用者的自然語言指令轉換為語言嵌入；(3) 描述投影模組，將語言嵌入與編碼器的多尺度視覺特徵進行融合，產生描述特徵；(4) 遮罩生成器，直接根據描述特徵查詢並預測目標區域的分割遮罩。訓練階段透過 DeepSpeed 優化，資料流程為載入 EarthReason 影像與對應的問答對，經過編碼、投影與遮罩預測後計算損失並反向傳播。評估時則使用相同的前向流程產生遮罩並與標準答案比較。由於 README 未提供詳細的網路結構圖或具體的層數、維度等資訊，以上說明僅基於文件中描述的模組與資料流程進行推斷。

## README 摘錄（節選）
```text
# SegEarth-R1: Geospatial Pixel Reasoning via Large Language Model
[🤗 Project (https://earth-insights.github.io/SegEarth-R1)] [🤗 Paper (https://arxiv.org/abs/2504.09644)] [🤗 Dataset (https://huggingface.co/datasets/earth-insights/EarthReason)] [🤗 Checkpoint (https://huggingface.co/earth-insights)]
🎉 TL;DR We introduce the geospatial pixel reasoning task, construct the first benchmark dataset (EarthReason), and propose a simple yet effective baseline (SegEarth-R1).
Remote sensing has become critical for understanding environmental dynamics, urban planning, and disaster management. However, traditional remote sensing workflows often rely on explicit segmentation or detection methods, which struggle to handle complex, implicit queries that require reasoning over spatial context, domain knowledge, and implicit user intent. Motivated by this, we introduce a new task, i.e., geospatial pixel reasoning, which allows implicit querying and reasoning and generates the mask of the target region. To advance this task, we construct and release the first large-scale benchmark dataset called EarthReason, which comprises 5,434 manually annotated image masks with over 30,000 implicit question-answer pairs. Moreover, we propose SegEarth-R1, a simple yet effective language-guided segmentation baseline that integrates a hierarchical visual encoder, a large language model (LLM) for instruction parsing, and a tailored mask generator for spatial correlation. The design of SegEarth-R1 incorporates domain-specific adaptations, including aggressive visual token compression to handle ultra-high-resolution remote sensing images, a description projection module to fuse language and multi-scale features, and a streamlined mask prediction pipeline that directly queries description embeddings. Extensive experiments demonstrate that SegEarth-R1 achieves state-of-the-art performance on both reasoning and referring segmentation tasks, significantly outperforming traditional and LLM-based segmentation methods.
## 🗞️ Update
- **`2025-05-04`**: The code, dataset and checkpoints are released.
- **`2025-04-15`**: 🔥🔥🔥 We release the paper of SegEarth-R1 on arXiv (https://arxiv.org/abs/2504.09644).
## 🔧 Usage：
Follow the guidelines below to set up, train and evaluate:
* Preparation ⚙️ (docs/Preparation.md): Instructions for organizing datasets and pretrained weights for proper model training and inference.
* Installation 💻 (docs/Installation.md): Set up the `segearthr1` conda environment, install dependencies, and clone the repo.
* Training 🏋️‍♂️ (docs/Training.md): Run `scripts/train.sh` with DeepSpeed, modifying parameters like data and model paths for training.
* Evaluation 🎯 (docs/Evaluation.md): Run `scripts/eval.sh` to evaluate the model, updating paths as needed.
## ⭐️ Citation
If you find this project useful, welcome to cite us.
[code block omitted]
## 🙏 Acknowledgement
We appreciate PSALM (https://github.com/zamling/PSALM) and Mask2Former (https://github.com/facebookresearch/Mask2Former) for making their models and code available as open-source contributions.
```
