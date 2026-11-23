# GitHub 專案 05：G14nTDo4/PathAgent

- 日期：2026-09-18
- URL：https://github.com/G14nTDo4/PathAgent
- 描述：[ECCV 2026] Official code implementation for paper "PathAgent: Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning"
- Stars：58  |  Forks：7  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-23T11:09:49+00:00
- 配對論文：https://arxiv.org/abs/2511.17052
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
PathAgent 是一個免訓練的互動式代理人，專門針對全切片病理圖像（WSI）進行可解釋的分析。它透過協調現成的病理模型（如 CLAM、Quilt‑LLaVA、PLIP）以及大型語言模型驅動的代理推理，實現多步驟推理、自適應放大與強化證據檢索，從而提供可追蹤的決策過程與競爭力的準確率，服務於需要病理圖像解讀的研究人員、臨床病理學家與醫學影像科技開發者。

## 技術
技術上，PathAgent 以 Python 為主要實作語言，結合 CLAM 進行切片切割與 patch 生成、Quilt‑LLaVA 生成病理描述、PLIP 產生 patch 特徵向量，並呼叫大型語言模型執行代理式多步驟推理。資料流程包含 patch 生成、描述產生、特徵嵌入與 LLM 驅動的 Navigator‑Executor 互動，全部透過腳本與命令列介面進行。

## 架構
架構上，PathAgent 包含三個核心模組：Executor 負責多步驟推理，依據當前分析狀態產生動態邏輯與指引；Navigator 負責證據檢索，透過自適應放大機制選擇合適的圖像尺度並簡化查詢策略以提升證據捕捉準確度；第三為資料準備與特徵提取管線，依序執行 CLAM patch 生成、Quilt‑LLaVA 描述產生、PLIP 特徵嵌入，產生的 patch 特徵與文字描述作為 Navigator 與 Executor 的輸入。推理時，Executor 與 Navigator 迭代交互，直至得到可追蹤的決策輸出。

## README 摘錄（節選）
```text
# [ECCV 2026] PathAgent: Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning
(https://github.com/G14nTDo4/PathAgent)
(https://arxiv.org/abs/2511.17052)
(https://arxiv.org/pdf/2511.17052.pdf)
Official code implementation for paper "PathAgent: Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning"
> Jingyun Chen, Linghan Cai, Zhikang Wang, Yi Huang, Songhan Jiang, Shenjin Huang, Hongpeng Wang, Yongbing Zhang
★ Quick start pathology agent: https://github.com/G14nTDo4/Awesome-Pathology-Agents (https://github.com/G14nTDo4/Awesome-Pathology-Agents)
## Overview
PathAgent is the first training-free interactive agent specifically designed for whole-slide pathology image (WSI) analysis. By coordinating off-the-shelf pathology models through an agent, it yields traceable decisions and competitive accuracy, suggesting a pragmatic route of computational pathology.
The contributions of PathAgent can be summarized in three aspects:
1. Dynamic analytic Logic: We replace single-step reasoning with Multi-Step Reasoning in the Executor. This mechanism can construct analytic logic and dynamically provide guidelines to retrieve task-relevant information.
2. Adaptive Magnification: PathAgent can adaptively select an appropriate scale based on the analytic state, generating more refined visual evidence.
3. Enhanced Evidence Retrieval: We improve the accuracy of evidence capture by simplifying the query strategy of the Navigator.
Figure. Illustration of PathAgent's inference procedure.
## 1. Installation
[code block omitted]
## 2. Data Preparation
The following steps take the WSI-VQA dataset as an example.
### 2.1 Patch Generation
Copy data_preparation_script/coordinate_generation.py to the CLAM (https://github.com/mahmoodlab/CLAM) project directory, and use the following code to generate the patches.
[code block omitted]
The DATA_DIRECTORY is the storage directory for svs files.
[code block omitted]
The above command will segment every slide in DATA_DIRECTORY and generate the following folder structure at the specified RESULTS_DIRECTORY:
[code block omitted]
Using the h5 file in RESULTS_DIRECTORY, we can extract the patch from WSI.
[code block omitted]
The above command will generate the following folder structure at the specified RESULTS_DIRECTORY/patches_output:
[code block omitted]
### 2.2 Description Generation
Before generating the description, we first need to modify the Quilt-LLaVA system prompt, replacing quilt-llava/llava/conversation.py with data_preparation_script/conversation_pathology_v0.py. Please note that the final file name is still conversation.py. The different name is only to distinguish the file from the file in the Quilt-LLaVA (https://github.com/aldraus/quilt-llava) project.
Multiple processes can be executed simultaneously to speed up the description generation process, which is also very user-friendly for users with limited VRAM. Only the description files for each block need to be concatenated at the end. Here, we divide all WSIs in the test set into four equal parts. Readers can adjust the number of parts as needed.
[code block omitted]
The above command will generate the following folder structure at the specified RESULTS_DIRECTORY/split_name:
[code block omitted]
Copy data_preparation_script/description_generation.py and data_preparation_script/multi_description_generation.sh to the Quilt-LLaVA project directory, and use the following code to generate the description.
[code block omitted]
The above command will generate the following folder structure at the specified RESULTS_DIRECTORY/desc:
[code block omitted]
The following command is used to merge all JSON files in the desc folder into a single JSON file.
[code block omitted]
### 2.3 Patch Embeddings Generation
Copy data_preparation_script/img_emb_generation.py and data_preparation_script/multi_emb_generation.sh to the PLIP (https://github.com/PathologyFo
```
