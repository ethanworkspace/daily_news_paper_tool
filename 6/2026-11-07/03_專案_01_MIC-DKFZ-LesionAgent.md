# GitHub 專案 01：MIC-DKFZ/LesionAgent

- 日期：2026-11-07
- URL：https://github.com/MIC-DKFZ/LesionAgent
- 描述：
- Stars：12  |  Forks：0  |  Language：unknown
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-23T13:44:13+00:00
- 配對論文：http://arxiv.org/abs/2611.27876v1
- 品質分數：7/10 [no_language, paper_paired, implementation_signals, stale_seed]

## 在做什麼
LesionAgent 是一個訓練‑free 的 LLM 代理，能讀取癌症患者的縱向 CT 掃描，從影像到每次訪視的 RECIST 1.1 評估，全程不需任務特定訓練。它將凍結的 3D 基礎模型作為工具，透過座標標記的視圖進行感知，使用病灶登記表跟蹤每個病灶在各訪視中的狀態，並依賴確定性的指南引擎計算所有測量與 RECIST 分類，使每個數字皆可追蹤。目標使用者為放射科醫師、腫瘤科醫師及醫學影像研究者，核心在解決縱向 CT 病灶追蹤與治療反應評估的自動化、可解釋與臨床可用需求。

## 技術
技術上，LesionAgent 以 Python 實作，採用模型‑agnostic 的 LLM 調度層，可搭配 Claude 或透過 vLLM 部署的開放權重模型（如 Qwen3.8‑27B）運行。其核心工具是凍結的 3D 基礎模型：VoxTell 偵測病灶候選，nnInteractive 進行交互式分割，uniGradICON 執行配準，LongiTrack 負責縱向追蹤，TotalSegmentator 提供器官標註。此外，系統內建 18 種型別的工具（感知、檢查、登記、決策與人機互動），並透過 napari 提供即時閱讀介面。所有工具在單張 24 GB GPU 上即可執行，無需任務特定訓練，且每次模型輸出皆由第二模型重新分割以驗證正確性。

## 架構
架構方面，LesionAgent 分為五個主要模組：感知模組調用 VoxTell、nnInteractive、uniGradICON、LongiTrack、TotalSegmentator 等凍結 3D 基礎模型，產生病灶遮罩與器官標註；檢查模組透過座標標記的視圖讓 LLM 檢視並驗證模型輸出，必要時呼叫第二模型重新分割；登記模組維護病灶登記表（lesion × visits），記錄每次訪視的遮罩與判斷；決策模組呼叫 LLM 進行病灶同一性判斷、新發現真偽評估及目標病灶選擇，然後交給確定性的指南引擎計算所有幾何測量與 RECIST 1.1 分類；人機模組透過 napari 讓臨床醫師即時觀察、回答問題或更正決策。資料流程從基線掃描開始，VoxTell 提出病灶候選，經代理過濾後登記；隨訪掃描經 uniGradICON 配準將既有病灶遮罩搬移至新圖像，LongiTrack 進行細分割，未匹配到既有病灶的發現必須經基線位置複查後才被視為新病灶；所有遮罩最終送入指南引擎產生 RECIST 報告。若 README 未明確說明某些細節（例如具體工具參數或內部調度細節），則以上說明基於可見的工具分組與流程描述進行合理推斷。

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
