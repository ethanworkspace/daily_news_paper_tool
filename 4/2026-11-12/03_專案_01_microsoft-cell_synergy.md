# GitHub 專案 01：microsoft/cell_synergy

- 日期：2026-11-12
- URL：https://github.com/microsoft/cell_synergy
- 描述：The repository has code to study synergistic information in multimodal cell foundation models
- Stars：5  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-19T16:13:48+00:00
- 配對論文：https://doi.org/10.1038/s42256-026-01328-3
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
本專案研究多模態細胞基礎模型中的協同資訊，提出 Synergistic Information Score (SIS) 來量化跨模態非線性互動超越簡單冗餘的貢獻。透過凍結的 UNI2（圖像）與 Nicheformer（基因表達）編碼器，僅訓練對齊介面，評估十種對齊方法在三個空間轉錄組資料集（肺、乳腺、胸腺）上的表現，旨在闡明何時多模態融合能提供任務相關的協同資訊，何時僅疊加冗餘訊號。目標使用者為計算生物學與多模態自監督學習研究者，幫助他們設計及評估能捕捉跨模態協同效應的細胞基礎模型。

## 技術
專案以 Python 3.10 為主要語言，依賴 CUDA 支援的 GPU 進行加速運算，並使用 SLURM 管理批次作業。環境透過 conda 建置。核心技術包括：凍結的 UNI2 組織病理圖像編碼器（HuggingFace MahmoodLab/UNI2-h）與 Nicheformer 基因表達編碼器（theislab/nicheformer）；實作十種對齊方法：光譜類 CCA、DCCA；非光譜類 CoMM、SimCLR、BYOL、SimSiam、Barlow Twins、VICReg、DIM 與 Concat 基線。協同資訊透過 SIS 計算模組（sis.py）以互信息近似值（以下游任務的 F1 Macro 與 R² 為代理）量化。資料流程涉及 scripts/data_processing/ 的預處理、src/cell_synergy/models/ 的對齊模型、examples/ 的教學腳本以及 configs/data/ 的資料集設定。

## 架構
架構分為四層：資料處理層（scripts/data_processing/）負責將三個空間轉錄組資料集（肺、乳腺、胸腺）轉換為適合模型的格式；表示層使用凍結的 UNI2 與 Nicheformer 編碼器分別產生圖像與基因表達的單模態嵌入 Z₁、Z₂；對齊層位於 src/cell_synergy/models/，依據所選方法（光譜或非光譜）學習介面以產生多模態表示 Z₃；評估層透過 sis.py 計算 SIS（以互信息近似值），並呼叫 example_evaluate_f1_r2.py、example_spatial_*.py 等腳本進行下游任務（細胞類別分類、鄰域預測）以取得 F1 與 R² 作為互信息代理。訓練流程由 scripts/train_*.py 啟動，可透過 SLURM 提交批次作業；推論則載入訓練好的對齊模型，對新資料產生 Z₃ 並計算 SIS。若 README 未明確說明某些內部細節（例如具體的超參數設定或詳細的 SLURM 腳本），則該部分屬於推斷，已在說明中註明。

## README 摘錄（節選）
```text
# Cell Synergy: Multimodal Self-Supervised Learning for Biological Data
(LICENSE)
(https://www.python.org/downloads/)
(https://www.biorxiv.org/content/10.64898/2026.02.23.707420v3)
(https://doi.org/10.5281/zenodo.22731602)
This repository contains the code and data processing pipelines for **"Beyond alignment: synergistic integration is required for multimodal cell foundation models"**.
## Overview
This work investigates how multimodal self-supervised learning (SSL) methods align gene expression (GEX) and histopathology image (IMG) representations in spatial transcriptomics data. We use frozen pretrained encoders (UNI2 for images, Nicheformer for gene expression) and train only the alignment interface. We introduce the **Synergistic Information Score (SIS)** to quantify how well alignment methods capture nonlinear interactions between modalities, beyond simple redundancy.
### Key Contributions
1. **Theoretical Framework**: Extends spectral theory to cross-covariance matrices, revealing a "spectral ceiling" that limits linear alignment methods
2. **SIS Metric**: Novel metric to measure synergistic information capture, distinguishing methods that extract nonlinear interactions from those that only capture redundancy
3. **Comprehensive Benchmarking**: Evaluation of 10 alignment methods (spectral: CCA, DCCA; non-spectral: CoMM, SimCLR, BYOL, SimSiam, Barlow Twins, VICReg, DIM, Concat) across three datasets (lung, breast, thymus)
4. **Data Scaling Analysis**: Systematic study of how data scale affects multimodal alignment performance
5. **Spatial Evaluation**: Task-specific evaluation ranging from local redundancy (cell type classification) to long-range spatial organization (neighborhood prediction)
## Paper Abstract
> The vision of a "virtual cell"---a computational model that simulates biological function across modalities and scales---has become a defining goal in computational biology. While powerful unimodal foundation models exist, the lack of large-scale paired data prohibits the joint training of multimodal approaches. This scarcity favors compositional foundation models (CFMs): architectures that fuse frozen unimodal experts via a learned interface. However, it remains unclear when this multimodal fusion adds task-relevant information beyond the strongest unimodal representation and when it merely aggregates redundant signal. Here, we introduce the Synergistic Information Score (SIS), a metric grounded in partial information decomposition (PID), that quantifies the information gain achievable only through cross-modal interactions. Extending theoretical results from self-supervised learning, we show that standard alignment-based fusion objectives on frozen encoders inherently collapse to detecting linear redundancies, limiting their ability to capture nonlinear synergistic states. This distinction is directly relevant for tasks aiming to link tissue morphology and gene expression. Benchmarking ten fusion methods on spatial transcriptomics datasets, we use SIS to demonstrate that tasks dominated by linear redundancies are sufficiently served by unimodal baselines, whereas complex niche definitions benefit from synergy-aware integration objectives that enable cross-modal interactions beyond linear alignment. Finally, we perform a scaling analysis which highlights that fine-tuning a dominant unimodal expert is the most sample-efficient path for standard tasks, suggesting that the benefits of multimodal frameworks only emerge when tasks depend on information distributed across modalities. Together, these results establish that building towards a virtual cell will require a fundamental shift from alignment objectives that emphasize shared structure to synergy-maximizing integration that preserves and exploits complementary cross-modal signal.
## Repository Structure
[code block omitted]
## Installation
### Prerequisites
- Python 3.10
- CUDA-capable GPU (recommended)
- SLURM workload manager (for running batch jobs)
### Setup
[c
```
