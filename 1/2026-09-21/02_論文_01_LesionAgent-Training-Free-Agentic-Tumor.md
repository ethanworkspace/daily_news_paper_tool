# 論文 01：LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- 日期：2026-09-21
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
癌症患者每數月接受 CT 掃描以決定治療是否持續，放射科醫師依 RECIST 1.1 手動判讀，耗時且讀者間差異大。現有 3D 基礎模型雖能零樣本偵測、分割、配準、追蹤病灶，但缺乏端到端的療效評估能力，無法像醫師般綜合判斷病灶身分、跨期追蹤、新發病灶意義與指引規則。本文提出 LesionAgent，一個無需任務專用訓練的 LLM 代理，操作凍結的 3D 模型作為工具，透過座標標註視圖在 3D 空間行動，維護跨就診的病灶登記表，驗證模型輸出，並將所有量測與分類交由確定性指引引擎處理，實現全自動或醫師輔助的縱向 CT 療效評估。

## 方法
LesionAgent 採用 LLM 工具使用迴圈，擁有 18 個型別工具（感知、檢視、登記、決策、人工介入）。感知工具包含：VoxTell 以多提示詞偵測病灶候選；nnInteractive 以單點擊分割遺漏或錯誤追蹤的病灶；uniGradICON 配準基線與追蹤掃描，LongiTrack 利用前期遮罩作為脈絡在追蹤期分割病灶；TotalSegmentator 提供器官分割。病灶登記表以（病灶×就診）矩陣儲存每期遮罩、類型、器官、角色（目標/非目標/新發/拒絕）與狀態（過小、缺失、合併）。代理透過座標標註的 2D 切面（含體素索引與患者方向）在 3D 空間操作，將視圖上讀取的位置轉為 3D 點擊提示。每個病灶以專屬顏色與 ID 標註，便於跨期比對與量測驗證。代理會以第二模型（nnInteractive）重新分割所有遮罩以捕捉失敗。確定性 RECIST 引擎依遮罩計算長短軸、加總目標病灶直徑、判斷反應類別，LLM 不直接計算數值。可選醫師透過 napari 外掛介入選擇目標病灶。全程無任務專用訓練，僅提供技能文件描述讀片流程與 RECIST 規則，支援 Claude Opus 5.5 與開放權重 Qwen3.8-27B。

## 結果
於四個公開縱向 CT 資料集，LesionAgent 全自動追蹤病灶數量與量測準確度優於所有自動基線。同樣 3D 模型以固定規則串接時，56 期追蹤中 33 期誤判進展，LesionAgent 僅 2 期。臨床追蹤 CT 上，與放射科醫師療效判讀一致 23 期中 20 期（含全部 4 次反應變化），平衡準確率 95%。未在 DeepLesion 訓練下，病灶檢索率 89.0% 超過所有在該資料集訓練的追蹤器（87.4%）。消融顯示架構關鍵：相同 LLM 與 3D 模型下，Claude Code 偵測 F1 41% vs LesionAgent 78%；開放權重 LLM 從 6% 升至 73%。另提供 napari 閱讀應用。

## 限制與展望
本文為預印本，實驗規模與統計顯著性未完整揭露。性能依賴凍結 3D 模型的零樣本能力，可能繼承其偏誤。座標標註視圖與登記表設計若不完善，可能影響跨期追蹤正確性。未針對罕見病灶類型、非 RECIST 指引、MRI 等模態驗證。部署需本地 LLM 硬體以保障隱私，LLM 仍有產生幻覺風險，雖有驗證機制緩解。後續需更大規模臨床驗證、支援多指引引擎、改善微小病灶偵測與泛化能力。
