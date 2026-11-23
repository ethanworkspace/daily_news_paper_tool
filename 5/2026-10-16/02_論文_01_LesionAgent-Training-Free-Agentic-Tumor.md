# 論文 01：LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- 日期：2026-10-16
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
癌症病患需定期接受 CT 掃描以決定治療持續與否，現有 3D 基礎模型雖能零樣本偵測、分割、配準與追蹤病灶，但缺乏如放射科醫師般整合臨床指南（RECIST 1.1）進行端到端讀片的能力。人工讀片耗時且變異大（兩醫師選同標靶病灶僅 41%），且小病灶易被遺漏。LesionAgent 提出一個無需任務特定訓練的 LLM 代理，操作凍結的 3D 基礎模型作為工具，透過座標標註的 2D 視圖在 3D 空間行動，維護跨就診的病灶登記表，驗證模型輸出，並將所有量測與分類交由確定性指南引擎處理，實現完全自動或醫師輔助的縱向 CT 讀片。

## 方法
問題設定：輸入為病患多次就診的 CT 影像序列 s1…sT（基線 s1），輸出為每次追蹤的 RECIST 1.1 回應類別。整體架構為 LLM 代理在工具使用迴圈中運作，擁有 18 個型別工具（表 1），作用於共享工作空間（掃描、病灶登記表、3D 模型、指南引擎），無殼層、檔案存取或程式執行權限，支援開源 LLM 本地部署。核心模組： 1. 感知工具：detect 使用 VoxTell 多提示詞提出病灶候選；segment 以 nnInteractive 點擊補漏或重分割；track_all 以 uniGradICON 配準掃描、傳播病灶點並用 LongiTrack 分割追蹤；refine_lesion、edit_mask、totalsegmentator 提供二次修正。 2. 病灶登記表：狀態儲存在 LLM 外部，記錄每個病灶在每次就診的類型、器官、角色（標靶/非標靶/新發/拒絕）與遮罩或狀態（太小、缺失、合併），確保無病灶靜默遺失。 3. 3D 行動透過 2D 座標視圖：所有視圖軸標註絕對體素索引與病患方向，代理在 2D 切片讀取位置即可轉為 3D 提示（如點擊遺漏病灶），並以顏色與 ID 標示各病灶跨就診對應。 4. 自我驗證：第二模型重分割每個遮罩以捕捉失誤，代理在視圖中檢查工具輸出。 5. 標靶選擇：代理自行評分並提議標靶組合，或讓臨床醫師從有效集合中選擇。 6. 確定性指南引擎：根據遮罩計算長短軸、加總標靶直徑、判斷新發病灶，套用 RECIST 規則產出回應類別與報告，LLM 不直接計算數值。 推論流程：基線階段 detect 提出候選 → 代理逐一接受/拒絕 → 登記表建立 → 選定標靶；追蹤階段 track_all 配準並分割 → detect 回傳未被追蹤候選作為新發病灶 → 代理檢查基線同位置確認新發 → 指南引擎計算回應。關鍵差異在於「線束」設計：座標視圖、跨時間登記表、模型輸出驗證、規則引擎分離，使相同 LLM 與 3D 模型在無線束時偵測 F1 僅 41%（Claude Code）或 6%（開源模型），加入線束後分別達 78% 與 73%。

## 結果
在四個公開縱向 CT 資料集上，LesionAgent 完全自動模式下追蹤病灶數量與量測準確度優於所有自動基線。相同 3D 模型以固定規則串接時，56 次追蹤中有 33 次誤判進展，LesionAgent 僅 2 次。臨床追蹤 CT 中，與放射科醫師回應一致率 20/23（含全部 4 次回應變化），平衡準確率 95%。未在 DeepLesion 訓練下，病灶檢索率 89.0% 優於在該資料集訓練的追蹤器 87.4%。結節量測落於讀者間變異範圍內。消融顯示線束而非 LLM 為關鍵：相同模型下 Claude Code 偵測 F1 從 41% 提升至 78%，開源模型從 6% 提升至 73%。

## 限制與展望
本文為預印本，尚未經同儕審查。評估雖涵蓋四公開資料集與臨床追蹤 CT，但對不同癌別、掃描儀廠牌、造影協定、切片厚度等變異的泛化性仍待驗證。代理性能強依賴凍結 3D 基礎模型的零樣本能力，罕見病灶或極端影像品質可能導致感知失敗。開源 LLM（Qwen3.8-27B）雖在線束下大幅提升，仍落後專有模型。無任務特定訓練意味著難以適應機構特定指南（超出 RECIST）。病灶偵測假陰性/假陽性會直接影響下游回應判斷，臨床部署需整合現有 PACS 與讀片工作流，napari 外掛僅為原型。後續研究方向：擴展至其他回應準則（如 iRECIST、PERCIST）、融合多模態資料、提升開源 LLM 在醫療代理任務表現、進行前瞻性臨床驗證。
