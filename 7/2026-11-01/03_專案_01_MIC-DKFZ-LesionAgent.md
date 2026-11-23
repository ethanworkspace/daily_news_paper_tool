# GitHub 專案 01：MIC-DKFZ/LesionAgent

- 日期：2026-11-01
- URL：https://github.com/MIC-DKFZ/LesionAgent
- 描述：
- Stars：12  |  Forks：0  |  Language：unknown
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-23T13:44:13+00:00
- 配對論文：http://arxiv.org/abs/2611.27876v1
- 品質分數：7/10 [no_language, paper_paired, implementation_signals, stale_seed]

## 在做什麼
LesionAgent 是一個訓練免疫的 LLM 代理，能讀取癌症患者的縱向 CT 掃描，從影像到每次造訪的 RECIST 1.1 評估，無需任務特定訓練。它將凍結的 3D 基礎模型當作工具使用，透過座標標記的視圖在 3D 空間中操作，維護病灶登記表（lesion registry）來跟蹤每個病灶在各次掃描中的遮罩，並依賴確定性的指南引擎計算所有測量與 RECIST 分類，使每個數字皆可追溯。目標使用者為放射科醫師、腫瘤科醫師及臨床研究人員，核心問題在於提供自動化、可解釋且符合臨床指南的腫瘤反應評估。

## 技術
LesionAgent 以 Python 實作，核心是與任意 LLM（如 Claude 或經 vLLM 服務的開放權重模型，例如 Qwen3.8-27B）結合的代理框架。它將五個已公開的 3D 基礎模型凍結為工具：VoxTell 偵測病灶、nnInteractive / LongiTrack 分割、uniGradICON 配合 LongiTrack 進行配位與追蹤、TotalSegmentator 進行器官標註。這些工具透過 18 個具型別的呼叫組織為感知、檢查、登記、決策與人機互動五組，所有工具在單張 24 GB GPU 上運行。代理透過 LLM 判斷哪些偵測結果為真實病灶、是否為同一病灶以及新發現的真偽，而所有數值由確定性的指南引擎從病灶遮罩計算，確保可追溯。此外，提供 napari 讀取應用程式，使醫師可即時觀察與介入。

## 架構
根據 README，LesionAgent 的架構可劃分為五個主要模組：感知（Perception）負責呼叫 VoxTell、nnInteractive、LongiTrack、uniGradICON、TotalSegmentator 等工具取得病灶偵測、分割、配位與器官標註；檢查（Inspection）提供 study_info、view、view_pair、inspect 等工具讓 LLM 在座標標記的視圖中檢視遮罩；登記（Registry）維護病灶登記表，記錄每個病灶在各訪視的遮罩，並支援審核候選者、更新病灶與設定訪視判斷；決策（Decision）執行評分、提出目標、設定目標以及呼叫確定性指南引擎產生 RECIST 報告；人機（Human）透過 ask_clinician 工具讓臨床醫師介入或回答問題。資料流程始於基線掃描：VoxTell 提供病灶候選，代理透過 LLM 檢查視圖並決定接受或拒絕，接受的病灶進入登記表；在每次隨訪掃描中，先透過配位工具將既有病灶遮罩搬移到新掃描座標，再由 LongiTrack 進行分割，未匹配到既有病灶的發現經過基線位置複檢後才可能被視為新病灶。所有工具的輸出皆由 LLM 再次驗證（例如以第二模型重新分割遮罩），最後由確定性指南引擎從最終遮罩計算體積與最長直徑，應用 RECIST 1.1 規則產出最終報告。由於 README 未提供詳細的類別圖或時序圖，上述架構推斷主要基於工具分組與文字描述的敘述。

## README 摘錄（節選）
```text
# LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT
(https://arxiv.org/abs/2611.27876)&#160;
(https://github.com/MIC-DKFZ/LesionAgent)&#160;
(#roadmap)&#160;
(#napari-app)
This repository contains the official implementation of our paper:
### **LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT**
LesionAgent is an **LLM agent that reads a cancer patient's CT scans end to end**, from the images to the RECIST 1.1 response at every visit, **without any task-specific training**. It operates frozen **3D foundation models as tools**, acts in 3D through **coordinate-labelled views**, remembers every lesion across visits in a **lesion registry**, **verifies every model output** it relies on, and leaves every number to a **deterministic guideline engine**. The harness is **model-agnostic**: it runs with Claude or with an open-weight LLM that can stay inside the hospital.
> **Authors**: Maximilian Rokuss, Jeya Maria Jose Valanarasu, Alejandro Lozano, Benjamin Hamm, Yannick Kirchhoff, Fabian Isensee, Klaus Maier-Hein
> **Paper**: (https://arxiv.org/abs/2611.27876)
--- 
## 📰 News
- **11/2026**: 📄 Preprint released on arXiv (https://arxiv.org/abs/2611.27876)!
--- 
## Overview
Every few months, a cancer patient's CT scans decide whether treatment continues. 3D foundation models can now detect, segment, register and track lesions, yet none of them reads the scans as a radiologist does. A radiologist decides **which findings are lesions**, **which are the same lesion months later** and **whether a new spot means progression**, and checks each decision against the rules of a clinical guideline.
LesionAgent splits this read by the kind of decision:
- **3D foundation models perceive** the lesions: VoxTell (https://github.com/MIC-DKFZ/VoxTell) detects, nnInteractive (https://github.com/MIC-DKFZ/nnInteractive) segments, uniGradICON (https://github.com/uncbiag/uniGradICON) registers, LongiTrack (https://huggingface.co/ykirchhoff/LongiTrack) tracks and TotalSegmentator (https://github.com/wasserth/TotalSegmentator) assigns organs.
- **The LLM judges** what the models cannot: is a finding a lesion, is it the same lesion at the next visit, is a new finding real, and which lesions should be followed? It checks every mask in rendered views, and a second model re-segments each mask to catch failures.
- **A deterministic guideline engine measures** the lesions on their masks and applies RECIST 1.1, so the LLM never computes a number or a response category.
At baseline, VoxTell proposes lesion candidates and the agent accepts or rejects each one. Every accepted lesion enters the registry (lesions × visits), which holds its mask at every visit. At each follow-up, registration carries every lesion into the new scan, where LongiTrack segments it. A finding that matches no tracked lesion becomes a new lesion only after the agent has checked the same position at baseline. The agent acts only through **18 typed tools**:
| Group | Tools (model) |
|---|---|
| Perception | `detect` (VoxTell), `segment` (nnInteractive / LongiTrack), `track_all` (uniGradICON + LongiTrack), `refine_lesion` (nnInteractive), `edit_mask`, `totalsegmentator` (TotalSegmentator) |
| Inspection | `study_info`, `view`, `view_pair`, `inspect` |
| Registry | `review_candidates`, `update_lesion`, `set_visit_judgement` |
| Decision | `score_lesions`, `propose_targets`, `set_targets`, `recist_report` (engine) |
| Human | `ask_clinician` |
--- 
## ✨ Highlights
- 🤖 **Runs with any LLM**: one harness with the same tools and skill for every model. Use Claude, or an open-weight LLM (e.g. Qwen3.8-27B) served with vLLM (https://github.com/vllm-project/vllm), so the whole read can stay inside the hospital.
- 🧊 **Training-free**: frozen 3D foundation models as tools, no task-specific training. All tools run on a single 24 GB GPU.
- 🧾 **Every number traceable**: a deterministic guideline engine computes every measurement an
```
