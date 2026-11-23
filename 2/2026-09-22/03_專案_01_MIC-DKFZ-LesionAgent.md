# GitHub 專案 01：MIC-DKFZ/LesionAgent

- 日期：2026-09-22
- URL：https://github.com/MIC-DKFZ/LesionAgent
- 描述：
- Stars：13  |  Forks：0  |  Language：unknown
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-23T16:02:19+00:00
- 配對論文：http://arxiv.org/abs/2611.27876v1
- 品質分數：7/10 [no_language, paper_paired, implementation_signals, stale_seed]

## 在做什麼
LesionAgent 是一個訓練‑free 的 LLM 代理，專門針對縱向 CT 影像進行腫瘤追蹤與治療反應評估。它將凍結的 3D 基礎模型當作工具使用，透過病灶登記表（lesion registry）紀錄每個病灶在各次掃描中的遮罩，並由確定性的指南引擎根據遮罩計算 RECIST 1.1 指標，使得整個讀影過程可追溯、可解釋且無需任務特定訓練。目標使用者為放射科醫師、腫瘤科醫師及臨床研究人員，核心問題在於如何自動化且符合臨床指南的腫瘤測量與進展判斷，同時保留醫師在迴圈中的最終決策權。

## 技術
LesionAgent 的技術堆疊包括：可互換的大型語言模型（支援 Claude 或開放權重模型如 Qwen3.8‑27B，可透過 vLLM 本地部署）；凍結的 3D 基礎模型作為工具，具體為 VoxTell（病灶偵測）、nnInteractive（病灶分割）、uniGradICON（配準）、LongiTrack（追蹤）與 TotalSegmentator（器官標註）；共計 18 個型別化工具，分為感知、檢查、登記、決策與人機互動五組；整個 harness 與模型無關，可在單張 24 GB GPU 上運行；此外提供 napari 讀影應用程式，讓醫師可即時觀察與介入。

## 架構
LesionAgent 的架構分為五個模組：感知模組呼叫 VoxTell、nnInteractive、uniGradICON、LongiTrack 與 TotalSegmentator 等工具取得病灶候選、分割、配準與追蹤結果；檢查模組提供 study_info、view、view_pair 與 inspect 等工具讓 LLM 在標註視圖上驗證模型輸出；登記模組維護 lesion × visits 的病灶登記表，透過 review_candidates、update_lesion 與 set_visit_judgement 等工具增刪與標記病灶；決策模組呼叫 score_lesions、propose_targets、set_targets 與 recist_report（決定性指南引擎）計算 RECIST 1.1 指標；人機模組透過 ask_clinician 讓醫師介入或回答問題。資料流程為：基線掃描由 VoxTell 提出病灶候選，經 LLM 判斷後登記；隨訪掃描先透過配準工具將既有病灶搬移至新影像，再由 LongiTrack 分割，未匹配到既有病灶的區域經 LLM 再次檢查是否為新病灶；所有遮罩最終送入決定性指南引擎得到尺寸與 RECIST 分類，整個過程在 napari app 中可視化，醫師可於任何步驟修正決策。

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
