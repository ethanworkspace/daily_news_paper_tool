# 論文 03：LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- 日期：2026-11-12
- 來源層級：Tier 3
- 期刊/會議/來源：arXiv
- Venue：arXiv preprint
- 發布時間：2026-11-20T17:21:36+00:00
- URL：http://arxiv.org/abs/2611.27876v1
- PDF：https://arxiv.org/pdf/2611.27876v1.pdf
- DOI：
- arXiv：2611.27876
- 影響指標：N/A (preprint)
- 影響指標來源：arXiv preprint (not peer-reviewed journal/conference)
- 引用數：0
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2611.27876
- 全文字數：103572（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/MIC-DKFZ/LesionAgent
- 配對 Repo：MIC-DKFZ/LesionAgent

## 摘要
Every few months, a cancer patient's CT scans decide whether treatment continues. 3D foundation models can now detect, segment, register and track lesions, yet none of them reads the scans as a radiologist does. A radiologist decides which findings are lesions, which are the same lesion months later and whether a new spot means progression, and checks each decision against the extensive rules of a clinical guideline. We introduce LesionAgent, an LLM agent that performs this read end to end without task-specific training. It operates frozen 3D models as tools, acts in 3D through coordinate-labelled views, remembers every lesion across visits in a registry, verifies every model output it relies on, and leaves every number to a deterministic guideline engine. On four public longitudinal CT datasets, LesionAgent tracks more lesions and measures them more accurately than every automatic baseline, and where the same 3D models chained by fixed rules call progression falsely at 33 of 56 follow-ups, it does so twice. On clinical follow-up CTs, it agrees with the radiologists' response at 20 of 23 follow-ups, including every change in response, and without training on DeepLesion, it retrieves more of its lesions than every tracker trained on it (89.0% vs. 87.4%). Its harness, not its LLM, makes the difference: given the same LLM and 3D models but not the harness, Claude Code reaches a detection F1 of 41% and LesionAgent 78%, and an open-weight LLM that can run inside the hospital rises from 6% to 73%. LesionAgent and a napari reading app for any LLM are available at https://github.com/MIC-DKFZ/LesionAgent.

## 背景與目的
癌症患者定期接受 CT 掃描以評估治療反應，現有 3D 基礎模型雖能單獨完成偵測、分割、配準與追蹤，但缺乏如放射科醫師般整合臨床指南（RECIST 1.1）進行端到端評估的能力。人工讀片耗時且讀者間一致性低（目標病灶選擇一致率僅 41%），且缺乏大規模縱向標註資料訓練端到端模型。本文提出 LesionAgent，一個無需任務特定訓練的 LLM 代理，透過凍結的 3D 基礎模型作為工具、病灶註冊表、座標標註視圖與確定性指南引擎，實現全自動或醫師輔助的縱向 CT 病灶追蹤與反應評估。

## 方法
LesionAgent 以 LLM 為核心代理，在工具使用迴路中操作 18 個型別化工具（偵測、分割、追蹤、修正、檢視、註冊表管理、決策、RECIST 引擎、醫師互動）。輸入為患者多時間點 CT 影像序列，輸出為各隨訪的 RECIST 反應類別與報告。核心架構包含：(1) 病灶註冊表：跨時間點儲存每個病灶的類型、器官、角色（目標/非目標/新發/拒絕）及各時間點的遮罩或狀態（過小、缺失、合併），確保無病灶遺失。(2) 座標標註 2D 視圖：將體素索引與患者方向標註於切片上，使 LLM 能從 2D 視圖讀取位置轉為 3D 點擊提示，實現「在 3D 中行動、透過 2D 觀察」。(3) 自我驗證機制：對每個模型輸出（偵測候選、追蹤遮罩）進行二次檢視，必要時以 nnInteractive 點擊重新分割。(4) 確定性指南引擎：根據遮罩計算長短軸、加總目標病灶直徑、套用 RECIST 1.1 規則，LLM 僅負責判斷「是否為病灶」、「是否為新發病灶」等語義決策，不計算數值。(5) 目標病灶選擇：代理自行評分並提出合法目標集合，或讓醫師從中選擇。推理流程：基線期以 VoxTell 多提示偵測候選，經 LLM 逐一切片驗收後存入註冊表；隨訪期先以 uniGradICON 配準、LongiTrack 傳播並分割既有病灶，再以 VoxTell 偵測未被追蹤的新發候選，LLM 回溯基線位置確認新發性；所有遮罩經 nnInteractive 二次修正，最終由引擎產出反應。關鍵差異在於：無訓練、工具凍結、註冊表記憶、座標視圖實現 3D 操作、指南引擎分離數值計算，且提供 napari 外掛供臨床互動。

## 結果
於四個公開縱向 CT 資料集，LesionAgent 完全自動模式下追蹤病灶數量與測量準確度均優於所有自動基線。固定規則串接相同 3D 模型在 56 個隨訪中誤判疾病進展 33 次，LesionAgent 僅 2 次。臨床隨訪 CT 上與放射科醫師反應一致率 20/23（平衡準確率 95%），包含所有 4 次反應變化。未在 DeepLesion 訓練下，病灶檢索率 89.0% 優於在該資料集訓練的追蹤器 87.4%。消融顯示：相同 LLM 與 3D 模型下，Claude Code 偵測 F1 41% → LesionAgent 78%；開放權重 LLM 從 6% 提升至 73%。

## 限制與展望
評估僅涵蓋四個公開資料集與一組臨床隨訪 CT，樣本量與癌症類型多樣性有限；代理依賴特定凍結模型（VoxTell、nnInteractive、uniGradICON、LongiTrack、TotalSegmentator），其泛化能力受限於這些模型的零樣本表現；RECIST 引擎為確定性規則，無法處理指南模糊地帶；臨床部署需解決計算資源、隱私（雖可本地運行）與醫師介入介面整合問題；未來需驗證於更多癌種、不同掃描協定、真實臨床工作流程，並探索代理對罕見病灶、偽影的魯棒性。
