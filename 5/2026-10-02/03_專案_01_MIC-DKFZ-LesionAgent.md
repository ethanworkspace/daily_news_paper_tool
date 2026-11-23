# GitHub 專案 01：MIC-DKFZ/LesionAgent

- 日期：2026-10-02
- URL：https://github.com/MIC-DKFZ/LesionAgent
- 描述：
- Stars：13  |  Forks：0  |  Language：unknown
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-23T16:02:19+00:00
- 配對論文：http://arxiv.org/abs/2611.27876v1
- 品質分數：7/10 [no_language, paper_paired, implementation_signals, stale_seed]

## 在做什麼
LesionAgent 是一個訓練‑free 的 LLM 代理，能直接讀取癌症患者的縱向 CT 影像，從偵測病灶、分割、配位、追蹤到依照 RECIST 1.1 評估治療反應，全部使用凍結的 3D 基礎模型作為工具，不需要任務特定訓練。目標使用者為醫學影像研究者與臨床醫師，解決現有自動化方法無法像放射科醫師般判斷哪些發現是真病灶、同一病灶的隨訪對應以及新發現是否代表進展的問題。

## 技術
專案以 Python 實作，核心是可換裝的 LLM（如 Claude 或開放權重的 Qwen3.8‑27B，可經 vLLM 本地部署）。它將凍結的 3D 基礎模型作為工具：VoxTell 偵測病灶、nnInteractive/LongiTrack 分割與追蹤、uniGradICON 配位、TotalSegmentator 器官標註。透過 18 個型別化的工具（感知、檢查、登記、決策、人機互動）與確認機制（第二次分割驗證），以及一個決定論的 RECIST 指引引擎來計算所有數值。

## 架構
LesionAgent 的架構分為五個模組：感知模組呼叫 VoxTell、nnInteractive、LongiTrack、uniGradICON、TotalSegmentator 等工具取得病灶遮罩；檢查模組提供影像資訊、視圖與配對視圖供 LLM 判斷；登記模組維護病灶×訪次登記表，儲存每次訪次的遮罩；決策模組呼叫評分工具、提出目標病灶、設定目標並透過決定論引擎產出 RECIST 報告；人機模組透過 napari 讀書應用讓臨床醫師即時檢視、回答問題或更正決策。資料流程：基線掃描經 VoxTell 提出病灶候選 → LLM 接受/拒絕 → 接受的病灶進入登記表；隨訪掃描經 uniGradICON 配位、LongiTrack 傳遞既有病灶遮罩 → LLM 檢查新發現是否為真病灶或同一病灶 → 登記表更新 → 決策引擎根據遮罩計算尺寸與 RECIST 1.1 分類 → 報告輸出。全部工具在單張 24 GB GPU 上運行，LLM 可為本地或遠端服務。

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
