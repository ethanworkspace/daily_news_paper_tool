# GitHub 專案 01：earth-insights/SegEarth-R1

- 日期：2026-10-13
- URL：https://github.com/earth-insights/SegEarth-R1
- 描述：SegEarth-R1: Geospatial Pixel Reasoning via Large Language Model
- Stars：159  |  Forks：11  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-09-23T08:08:53+00:00
- 配對論文：https://www.semanticscholar.org/paper/eab0e7a7082dd467eee45b66d15df841da8ccec2
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
SegEarth-R1 是一個以大型語言模型驅動的地理空間像素推理框架，旨在解決遙感影像中隱含查詢的問題。專案首先提出「地理空間像素推理」任務，使用自然語言描述作為指令，直接輸出對應區域的分割遮罩。為支援此任務，團隊發布了首個大規模基準資料集 EarthReason，包含 5,434 張手動標註的遙感影像與超過 30,000 個隱含問答對。目標使用者包括遙感研究者、GIS 分析師、環境與災害管理專業人員，他們需要能夠依賴語言指令進行複雜空間推理而不依賴傳統的明確分割或偵測流程。核心問題在於傳統方法難以處理需要空間上下文、領域知識與使用者意圖的隱含查詢；SegEarth-R1 透過語言導向的分割 pipeline 將自然語言轉換為遮罩預測，提供一種端到端的解決方案。

## 技術
專案主要使用 Python 實作，結合了多種可見的技術組件：(1) 階層式視覺編碼器（Hierarchical Visual Encoder）負責從超高解析度遙感影像中提取多尺度特徵，並採用激進的視覺 token 壓縮以縮減計算開銷；(2) 大型語言模型（LLM）用於解析使用者的自然語言指令，產生描述嵌入（description embedding）；(3) 描述投影模組（Description Projection Module）負責將語言嵌入與多尺度視覺特徵進行融合；(4) 定制的遮罩生成器（Tailored Mask Generator）直接查詢融合後的描述嵌入以預測目標區域的遮罩；(5) 訓練過程採用 DeepSpeed 進行分散式優化，支援大規模模型與資料集；(6) 資料與模型透過 HuggingFace 平台發布，使用 datasets 與 checkpoints 儲存庫；(7) 環境設置透過 conda（segearthr1）與提供的 Installation.md 完成依賴安裝。所有上述技術均可從 README 中直接觀察到。

## 架構
SegEarth-R1 的架構可視為四個主要模組的串聯流程：首先，階層式視覺編碼器處理輸入遙感影像，產生多尺度特徵圖並透過激進的 token 壓縮降低序列長度；其次，LLM 接收使用者的語言指令，生成對應的描述嵌入；第三，描述投影模組將該語言嵌入與視覺編碼器的多尺度特徵進行對齊與融合，產生兼具語意與空間資訊的聯合表示；最後，定制的遮罩生成器根據聯合表示直接查詢描述嵌入，逐像素預測目標區域的二元遮罩，得到最終分割結果。訓練階段透過 scripts/train.sh 呼叫 DeepSpeed 優化器，根據 docs/Training.md 中的參數設定進行梯度更新；評估階段則執行 scripts/eval.sh，載入檢查點與測試資料計算指標。資料流程方面，EarthReason 資料集經過預處理後送入視覺編碼器，語言指令經過 tokenizer 傳入 LLM，兩者的輸出在描述投影模組相遇，最終經遮罩生成器產出遮罩。若需更詳細的內部層次（例如具體的編碼器 backbone 或 LLM 版本），README 未提供進一步細節，因此上述架構說明僅基於可見的模組描述與訓練/評估腳本的推斷。

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
