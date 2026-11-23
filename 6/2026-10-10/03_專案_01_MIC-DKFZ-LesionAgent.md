# GitHub 專案 01：MIC-DKFZ/LesionAgent

- 日期：2026-10-10
- URL：https://github.com/MIC-DKFZ/LesionAgent
- 描述：
- Stars：13  |  Forks：0  |  Language：unknown
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-23T16:02:19+00:00
- 配對論文：http://arxiv.org/abs/2611.27876v1
- 品質分數：7/10 [no_language, paper_paired, implementation_signals, stale_seed]

## 在做什麼
LesionAgent 是一個訓練免疫的 LLM 代理，能夠讀取癌症患者的縱向 CT 掃描，從圖像直接產出符合 RECIST 1.1 的腫瘤追蹤與治療反應評估，無需任務特定的微調。它將凍結的 3D 基礎模型當作工具使用，透過座標標註的視角在 3D 空間中操作，維護病灶登記表（lesion registry）來記住每個病灶在各次掃描中的狀態，並依賴決定論的指南引擎計算所有數值與 RECIST 分類，以確保每個數字可追溯。目標使用者為醫療影像研究者、放射科醫師以及需要自動化腫瘤追蹤與療效評估的臨床團隊，核心問題在於現有自動化方法無法像放射科醫師般判斷哪些發現是真病灶、同一病灶在不同時間點是否對應，以及新發現是否代表真實進展，而 LesionAgent 透過 LLM 進行高層次決策、呼叫凍結模型進行低層次感知，並讓決定論引擎負責量測，從而在不需額外訓練的情況下提供可解釋、可驗證的腫瘤追蹤與反應報告。

## 技術
LesionAgent 以 Python 為主要實作語言，採用 LLM 作為決策核心，支援 Claude 與開放權重的大型語言模型（例如 Qwen3.8-27B），可經由 vLLM 本地部署以確保資料留在醫院內。其感知層依賴多個凍結的 3D 基礎模型作為工具：VoxTell 進行自由文字提示的病灶偵測，nnInteractive 進行互動式分割，uniGradICON 與 LongiTrack 聯合進行配準與追蹤，TotalSegmentator 提供器官標註。所有工具透過 18 個型別化的函式介面（偵測、分割、配準、追蹤、遮罩編輯、器官分配、檢視資訊、視圖配對、檢查、登記審查、更新病灶、設定訪視判斷、評分病灶、提出目標、設定目標、RECIST 報告、諮詢臨床師）進行呼叫。決定論的指南引擎則負責從病灶遮罩計算尺寸與套用 RECIST 1.1 準則，確保所有數值可追溯且無需 LLM 進行運算。整個流程可在單張 24 GB GPU 上運行，顯示其對資源的低需求。

## 架構
LesionAgent 的架構分為四個主要模組：感知（Perception）、檢查（Inspection）、登記（Registry）與決策（Decision），外加人機互動（Human）模組。感知模組呼叫凍結的 3D 基礎模型工具，產出病灶候選遮罩、分割結果、配準場與追蹤軌跡；檢查模組提供掃描資訊、單視圖與雙視圖渲染以及對遮罩的視覺檢查，讓 LLM 能觀察模型輸出；登記模組維護病灶×訪視的登記表，負責審查候選病灶、更新已追蹤病灶的遮罩與設定訪視判斷；決策模組則根據登記表與檢查結果呼叫評分、提出目標、設定目標以及 RECIST 報告工具，其中 RECIST 報告由決定論的指南引擎產出，LLM 只負責判斷哪些病灶應成為目標或是否需要進一步檢查。人機互動模組透過 napari 讀書應用讓臨床師即時查看每一步驟、回答 LLM 的問題或更正決策，所有變更會即時反饋回登記表與報告。資料流程為：原始 CT → 感知工具產出遮罩 → 檢查視圖 → LLM 判斷 → 登記更新 → 決策工具產出目標與 RECIST → （選擇性）臨床師回饋 → 循環至下一次訪視。若 README 未明確說明某些內部實作細節，則以上說明僅基於可見的工具分組與流程描述進行合理推斷。

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
