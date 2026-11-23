# GitHub 專案 01：MIC-DKFZ/LesionAgent

- 日期：2026-09-13
- URL：https://github.com/MIC-DKFZ/LesionAgent
- 描述：
- Stars：13  |  Forks：0  |  Language：unknown
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-23T16:02:19+00:00
- 配對論文：http://arxiv.org/abs/2611.27876v1
- 品質分數：7/10 [no_language, paper_paired, implementation_signals, stale_seed]

## 在做什麼
LesionAgent 是一個訓練免疫的 LLM 代理，能端到端讀取癌症患者的縱向 CT 掃描，從影像直接產出每次造訪的 RECIST 1.1 評估，而無需任何任務特定的訓練。它將凍結的 3D 基礎模型當作工具使用，透過座標標註的視圖在三維空間中操作，並維護一個病灶登記表（lesion registry）來記錄每個病灶在所有時間點的遮罩。每一步的模型輸出都會被驗證，最終的尺寸與 RECIST 分類由確定性的指南引擎從病灶遮罩計算得出，LLM 只負責判斷哪些發現是病灶、哪些是同一病灶以及新發現的真偽。目標使用者為放射科醫師、腫瘤科醫師及醫學影像研究者，核心問題在於如何在缺乏標註資料的情況下自動、可追蹤地完成縱向腫瘤追蹤與治療反應評估。

## 技術
LesionAgent 的技術堆疊包括：可與任何 LLM 搭配的模型無關 harness，支援 Claude 或開放權重的 LLM（例如 Qwen3.8-27B）透過 vLLM 本地部署，確保資料留在醫院內；凍結的 3D 基礎模型作為工具，具體為 VoxTell（病灶偵測）、nnInteractive（病灶分割）、uniGradICON（配註）、LongiTrack（追蹤）與 TotalSegmentator（器官分配）；系統提供 18 個型別化的工具，分為感知、檢查、登記、決策與人機互動五組；所有工具的輸出皆由 LLM 調用，且每個遮罩會被第二個模型重新分割以偵測失敗；最後由確定性的指南引擎根據病灶遮罩計算測量值與 RECIST 1.1 類別，確保每個數字皆可追溯；整個流程可在單張 24 GB GPU 上運行。

## 架構
LesionAgent 包含五個模組：感知（呼叫 VoxTell、nnInteractive、uniGradICON、LongiTrack、TotalSegmentator 完成偵測、分割、配註、追蹤與器官標註）；檢查（提供 study_info、view、view_pair、inspect 讓 LLM 透過座標標註視圖檢視遮罩）；登記（維護 lesion registry，記錄每個病灶在所有訪視的遮罩，提供 review_candidates、update_lesion、set_visit_judgement）；決策（呼叫 score_lesions、propose_targets、set_targets 與 recist_report 計算尺寸並套用 RECIST 1.1）；人機（透過 ask_clinician 在 napari App 中讓醫師介入、回答問題或更正決策）。資料流程：基線掃描由 VoxTell 提出候選病灶，LLM 驗證後登記；隨訪掃描先經 uniGradICON 配註將舊病灶遮罩搬移，LongiTrack 細分割，未匹配者經 LLM 再次核對基線後才成為新病灶；所有病灶遮罩送入確定性指南引擎計算體積與最長直徑，套用 RECIST 1.1 產出報告；每一步的工具呼叫、LLM 判斷與引擎計算皆被記錄，可在 napari 中即時檢視。以上架構推斷自 README，具體實作細節仍需參考程式碼。

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
