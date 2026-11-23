# GitHub 專案 02：MIC-DKFZ/LesionAgent

- 日期：2026-11-12
- URL：https://github.com/MIC-DKFZ/LesionAgent
- 描述：
- Stars：7  |  Forks：0  |  Language：unknown
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-23T06:39:42+00:00
- 配對論文：http://arxiv.org/abs/2611.27876v1
- 品質分數：7/10 [no_language, paper_paired, implementation_signals, stale_seed]

## 在做什麼
LesionAgent 是一個訓練‑free 的 LLM 代理，能夠端到端讀取癌症患者的縱向 CT 掃描，從原始影像直接產出符合 RECIST 1.1 的腫瘤反應評估，無需任何任務特定的微調。它將凍結的 3D 基礎模型當作工具使用（如 VoxTell 偵測、nnInteractive 分割、uniGradICON 配準、LongiTrack 追蹤、TotalSegmentator 器官標註），透過 18 個型別化的工具執行感知、檢查、病灶登記與決策。病灶資訊存於病灶登記表（lesion × visits），每次隨訪都會經過配準搬移至新掃描，新發現的病灶必須經過基線位置驗證後才被納入。最終的尺寸與 RECIST 類別由確定性的指南引擎從病灶遮罩計算得出，LLM 只負責判斷與驗證，整個流程可在單張 24 GB GPU 上運行，並支援任何 LLM（如 Claude 或開放權重的 Qwen），可選擇完全自動或透過 napari 讀書應用讓臨床醫師參與。

## 技術
LesionAgent 的技術核心包括：(1) 大型語言模型（LLM）作為決策與判斷的中樞，支援 Claude 或開放權重模型（例如 Qwen3.8‑27B）並可經由 vLLM 在本地部署；(2) 凍結的 3D 基礎模型作為工具，涵蓋 VoxTell（文字提示可通用的 3D 分割）、nnInteractive（點、框、塗鴉、套索等交互式分割）、uniGradICON（配準）、LongiTrack（縱向追蹤）與 TotalSegmentator（器官標註）；(3) 18 個型別化工具分為感知、檢查、登記、決策與人機五組，透過統一的介面呼叫；(4) 所有模型均在單張 24 GB GPU 上運行，無需任務特定訓練；(5) 透過 napari 讀書應用提供即時視覺化與臨床醫師互動；(6) 決策過程中，LLM 只負責判斷與驗證，所有數值（病灶尺寸、RECIST 類別）由確定性的指南引擎從病灶遮罩計算，確保可追溯與可重現。

## 架構
LesionAgent 的架構分為五個模組：感知模組呼叫 VoxTell、nnInteractive、LongiTrack 等 3D 基礎模型執行病灶偵測、分割、配準與追蹤；檢查模組提供 study_info、view、view_pair、inspect 等工具讓 LLM 在渲染視圖中檢查遮罩並請求第二模型重新分割以驗證；登記模組維護病灶登記表（lesion × visits），負責審閱候選病灶、更新病灶遮罩與設定訪視判斷；決策模組執行病灶評分、提出目標病灶、設定目標集合以及呼叫確定性指南引擎產出 RECIST 報告；人機模組透過 ask_clinician 讓臨床醫師介入或更正決策。資料流程以基線掃描為起點：VoxTell 提出病灶候選，LLM 接受或拒絕，接受的病灶進入登記表；每次隨訪掃描經過 uniGradICON+LongiTrack 配準將既有病灶搬移至新影像，LongiTrack 進行分割，未匹配到既有病灶的發現經過基線位置驗證後才被視為新病灶；LLM 透過 inspection 工具檢視遮罩並請求 nnInteractive 重新分割以捕獲失敗；最終所有病灶遮罩送入指南引擎，依 RECIST 1.1 計算尺寸與變化，生成報告。整個流程僅依賴凍結模型與 LLM 的工具調用，無需額外訓練。

## README 摘錄（節選）
```text
# LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT
(https://github.com/MIC-DKFZ/LesionAgent)&#160;
(#roadmap)&#160;
(#napari-app)
This repository contains the official implementation of our paper:
### **LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT**
LesionAgent is an **LLM agent that reads a cancer patient's CT scans end to end**, from the images to the RECIST 1.1 response at every visit, **without any task-specific training**. It operates frozen **3D foundation models as tools**, acts in 3D through **coordinate-labelled views**, remembers every lesion across visits in a **lesion registry**, **verifies every model output** it relies on, and leaves every number to a **deterministic guideline engine**. The harness is **model-agnostic**: it runs with Claude or with an open-weight LLM that can stay inside the hospital.
> **Authors**: Maximilian Rokuss, Jeya Maria Jose Valanarasu, Alejandro Lozano, Benjamin Hamm, Yannick Kirchhoff, Fabian Isensee, Klaus Maier-Hein
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
- 🧾 **Every number traceable**: a deterministic guideline engine computes every measurement and RECIST 1.1 category from the lesion masks, and every lesion, tool call and decision behind the response stays visible.
- 🩺 **Clinician in the loop**: read fully automatically, or tog
```
