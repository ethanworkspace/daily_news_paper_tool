# 論文 01：LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- 日期：2026-10-10
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
癌症患者定期接受 CT 掃描以決定治療是否持續，現有 3D 基礎模型能單獨完成偵測、分割、配準與追蹤，但缺乏如放射科醫師般整合臨床指南（RECIST 1.1）進行端到端讀片。人工讀片耗時且讀者間差異大（目標病灶選擇一致率僅 41%），且小病灶易被遺漏。本文提出 LesionAgent，一個無需任務特定訓練的 LLM 代理，透過凍結的 3D 模型作為工具、病灶註冊表、座標標註視圖與確定性指南引擎，實現全自動或醫師輔助的縱向 CT 病灶追蹤與療效評估，填補現有方法無法整合多步驟決策的缺口。

## 方法
輸入為患者多次就診的 3D CT 序列（基線與追蹤掃描），輸出為每次追蹤的 RECIST 1.1 療效類別。LesionAgent 採用 LLM 工具調用迴圈，擁有 18 個型別工具（表 1），操作凍結的 3D 基礎模型：VoxTell 以多提示詞偵測病灶候選，nnInteractive/LongiTrack 進行點擊式分割與縱向分割，uniGradICON 執行跨時相配準，TotalSegmentator 提供器官分割。核心模組包含：(1) 病灶註冊表，記錄每個病灶在各時相的遮罩、類型、器官、角色（目標/非目標/新發/拒絕）與狀態（過小、缺失、合併），確保無病灶靜默遺失；(2) 座標標註 2D 視圖，將體素索引與患者方向標記於切片上，使 LLM 能將視覺位置轉為 3D 點擊提示；(3) 自我驗證機制，以第二模型重新分割每個遮罩並逐切片檢查，捕捉單一模型失誤；(4) 目標病灶選擇，LLM 依評分提出候選組合，可選讓臨床醫師從中挑選；(5) 確定性指南引擎，依遮罩計算長短軸、加總目標病灶直徑並套用 RECIST 規則，LLM 不直接計算數值。推理流程：基線偵測→註冊表建立→每次追蹤配準與追蹤分割→新發候選偵測→驗證與狀態更新→指南引擎產出報告。關鍵差異在於無訓練的代理架構、跨時相註冊表、座標視圖實現 3D 操作、模型輸出驗證與規則引擎分離，使同樣模型在固定規則鏈下誤判進展 33/56 例，LesionAgent 僅 2 例。

## 結果
在四個公開縱向 CT 資料集上，LesionAgent 完全自動模式下追蹤病灶數量與測量準確度均優於所有自動基線。相同 3D 模型以固定規則串接時，56 例追蹤中誤判疾病進展達 33 例，LesionAgent 僅 2 例。臨床追蹤 CT（23 例）中，與放射科醫師療效判讀一致 20 例，包含全部 4 次療效變化（平衡準確率 95%）。未在 DeepLesion 訓練情況下，病灶檢索率 89.0% 超過所有在該資料集訓練的追蹤器（87.4%）。代理架構效果顯著：相同 LLM 與 3D 模型下，Claude Code 偵測 F1 41%，LesionAgent 78%；開放權重 LLM 從 6% 提升至 73%。摘錄未提供更詳細的消融實驗數字，但定性顯示代理能減少誤判並提升檢出率。

## 限制與展望
資料限制：僅在四個公開資料集與 23 例臨床追蹤 CT 驗證，癌症類型與樣本量有限；方法依賴凍結 3D 模型的零樣本表現，若基礎模型偵測失敗則代理難以修正；座標標註視圖僅提供切片級資訊，可能遺漏 3D 結構細節；評估僅針對 RECIST 1.1，未涵蓋其他指南；部署需 GPU 執行 3D 模型與 LLM 推理，開放權重 LLM 效能仍落後專有模型。潛在風險包含自動判讀錯誤導致治療決策偏差。後續研究可擴展至多模態、其他療效準則、更大規模臨床驗證與更輕量化部署。
