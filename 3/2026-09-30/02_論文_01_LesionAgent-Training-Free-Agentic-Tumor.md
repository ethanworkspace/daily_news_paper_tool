# 論文 01：LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- 日期：2026-09-30
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
癌症患者需定期接受 CT 掃描以判斷治療反應，放射科醫師依 RECIST 1.1 手動讀片，但讀片耗時且讀者間差異大（目標病灶一致率僅 41%）。現有 3D 基礎模型能零樣本完成偵測、分割、配準與追蹤，但缺乏端到端的反應評估能力，且缺乏大規模縱向標註資料訓練整合模型。本文提出 LesionAgent，一個無需任務特定訓練的 LLM 代理，透過凍結的 3D 模型作為工具、病灶登記表、座標標註視圖與確定性指引引擎，實現從影像到 RECIST 反應的完整自動化讀片。

## 方法
問題設定：輸入患者多時間點 CT 影像序列 s1…sT，輸出每次追蹤的 RECIST 1.1 反應類別。整體架構為 LLM 代理在工具使用迴圈中運作，擁有 18 個型別工具（表 1），僅能透過共享工作空間（影像、病灶登記表、3D 模型、指引引擎）行動，無殼層、檔案存取或程式執行權限。核心模組：(1) 病灶登記表，以病灶×就診矩陣儲存每個病灶的類型、器官、角色（目標/非目標/新發/拒絕）及各就診的遮罩或狀態（太小、缺失、合併），確保無病灶被靜默遺失。(2) 座標標註 2D 視圖：將體素絕對索引與患者方向標註於每一切片，使 LLM 能從 2D 視圖讀取位置並轉為 3D 提示（如點擊未被偵測的病灶）。(3) 自我驗證：對每個依賴的模型輸出進行二次分割（refine_lesion）以捕捉失敗。(4) 確定性指引引擎：根據遮罩計算長短軸、加總目標病灶直徑、套用 RECIST 規則，LLM 不計算任何數值。工具鏈：基線期以 VoxTell 多提示偵測候選，LLM 於視圖中接受/拒絕；nnInteractive 點擊補漏或修正錯誤遮罩。追蹤期以 uniGradICON 配準影像，傳播病灶中心點並以 LongiTrack 分割；偵測器僅回傳未被追蹤病灶覆蓋的發現作為新病灶候選。目標病灶由代理自行評分並提出合法組合，或讓臨床醫師從中選擇。推論流程：基線偵測→候選審查→登記→目標選擇→每次追蹤配準與追蹤→新病灶偵測與驗證→指引引擎產出報告。關鍵差異：讓 LLM 在 3D 空間透過座標視圖行動、跨就診記憶病灶、驗證模型輸出、將數值判斷交給確定性引擎，而非固定管線或單一模型。

## 結果
在四個公開縱向 CT 資料集上，LesionAgent 完全自動化下追蹤的病灶數量與測量準確度均優於所有自動基線。相同 3D 模型以固定規則串接時，56 次追蹤中有 33 次誤判為進展，LesionAgent 僅 2 次。臨床追蹤 CT 中，與放射科醫師反應一致率 20/23（平衡準確率 95%），包含所有 4 次反應變化。未在 DeepLesion 訓練下，病灶檢索率 89.0% 超過所有在該資料集訓練的追蹤器（87.4%）。同樣 LLM 與 3D 模型下，Claude Code 偵測 F1 41%，LesionAgent 78%；開放權重 LLM 從 6% 提升至 73%。摘錄提供上述可驗證數字。

## 限制與展望
為預印本，未經同行審查；評估資料集雖含四個公開集與臨床追蹤案例，但樣本量有限，缺乏前瞻性臨床試驗驗證。代理依賴凍結的 3D 基礎模型，其偵測與分割錯誤會傳播至登記表，雖有二次驗證機制但無法完全消除。座標標註視圖僅提供 2D 切片，可能遺漏 3D 空間資訊。LLM 推理可能產生幻覺，影響病灶接受/拒絕判斷。確定性引擎僅支援 RECIST 1.1，其他準則需重寫引擎。開放權重 LLM 在醫院內部部署時效能仍落後專有模型。部署需 GPU 資源與 napari 外掛整合，臨床工作流整合尚待驗證。
