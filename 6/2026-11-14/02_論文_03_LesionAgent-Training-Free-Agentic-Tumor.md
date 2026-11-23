# 論文 03：LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- 日期：2026-11-14
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
癌症患者每數月接受 CT 掃描以依 RECIST 1.1 判斷治療反應，現有 3D 基礎模型雖能單獨完成偵測、分割、配準與追蹤，但缺乏像放射科醫師般整合多步驟、跨時序判讀並套用臨床指引的能力。現有追蹤器需人工指定目標病灶、無法自動判斷新發病灶與進展，且端到端訓練受限於縱向標註資料稀缺。本文提出 LesionAgent，一個無需任務特定訓練的 LLM 代理，透過凍結的 3D 基礎模型作為工具、座標標註視圖、病灶登記表與確定性指引引擎，實現從多期 CT 到 RECIST 反應的完整自動判讀，填補自動化縱向腫瘤監測的關鍵缺口。

## 方法
問題設定：輸入為患者多期 CT 影像序列 s1…sT，輸出為每次追蹤的 RECIST 反應類別。整體架構為 LLM 代理在工具使用迴圈中操作 18 個型別工具（偵測、分割、追蹤、修正、器官分割、資訊查詢、視圖渲染、配對視圖、檢查、候選審查、病灶更新、訪視判斷、評分、目標提議、目標設定、RECIST 報告、詢問醫師），共享工作空間包含影像、病灶登記表、凍結 3D 模型與指引引擎。核心模組：(1) 病灶登記表以病灶×訪視矩陣儲存類型、器官、角色及各訪視的遮罩或狀態（過小、缺失、合併），確保無病灶遺失。(2) 座標標註 2D 視圖：每張渲染切片標示絕對體素索引與患者方向，使 LLM 可將視覺位置轉為 3D 點擊提示。(3) 自我驗證：偵測以 VoxTell 多提示產生候選，LLM 於渲染視圖逐一接受/拒絕；追蹤階段以 uniGradICON 配準後由 LongiTrack 分割，若無結果則檢查配準位置並標記缺失；新發候選需回溯基線位置確認。(4) 確定性指引引擎：依遮罩計算長短軸、加總目標病灶直徑、套用 RECIST 1.1 規則產出反應類別，LLM 不直接計算數值。(5) 目標病灶選擇：代理自行評分並提議最多五組合法目標組合，或讓醫師從中選擇。推理流程：基線偵測→登記→目標選擇→各追蹤期配準追蹤→新發候選驗證→二次分割修正→指引引擎計算報告。關鍵差異在於：以 Harness 讓 LLM 在 3D 空間透過座標視圖操作、跨訪視記憶與驗證、將數值判斷外包給確定性引擎，且完全無任務特定訓練。

## 結果
於四個公開縱向 CT 資料集，LesionAgent 完全自動模式下追蹤病灶數量與測量準確度均優於所有自動基線；固定規則串接相同 3D 模型在 56 次追蹤中誤判進展 33 次，LesionAgent 僅 2 次。臨床追蹤 CT 上與放射科醫師反應一致 23 中 20 例（含全部 4 次反應變化），平衡準確率 95%。未在 DeepLesion 訓練情況下，病灶檢索率 89.0% 超過所有在 DeepLesion 訓練的追蹤器（87.4%）。Harness 效應顯著：同樣 LLM 與 3D 模型下，Claude Code 偵測 F1 41% 對 LesionAgent 78%；開放權重 LLM 從 6% 提升至 73%。摘錄未提供可驗證數字之其他細項指標（如具體 Dice、Hausdorff 距離），但定性顯示 LesionAgent 在病灶偵測、跨期追蹤與反應判讀上均達臨床可用水準。

## 限制與展望
評估僅限四個公開資料集與部分臨床追蹤 CT，外部泛化性尚待驗證；依賴凍結的 3D 基礎模型（VoxTell、nnInteractive、LongiTrack、uniGradICON、TotalSegmentator）性能上限受限於這些模型本身；座標標註視圖僅提供 2D 切片，可能遺漏 3D 空間資訊；確定性指引引擎僅實作 RECIST 1.1，其他指引需重寫引擎；LLM 品質對代理行為影響大，開放權重模型在醫院本地部署時需考慮算力與隱私；未量化醫師介入時的點擊次數與時間成本；長期追蹤中病灶合併、分裂等複雜拓撲變化處理細節未詳述。後續研究可擴展至多指引、多模態影像、更大規模臨床驗證與自適應模型微調。
