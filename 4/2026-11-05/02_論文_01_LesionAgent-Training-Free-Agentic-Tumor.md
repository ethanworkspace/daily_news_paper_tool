# 論文 01：LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- 日期：2026-11-05
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
癌症患者定期接受 CT 掃描以決定治療持續與否，放射科醫師依 RECIST 1.1 指引人工判讀，但過程耗時、讀者間差異大且易漏測微小病灶。現有 3D 基礎模型能零樣本偵測、分割、配準與追蹤病灶，但缺乏端到端的療效評估能力；現有代理系統亦未能跨多期 CT 執行完整判讀。本文提出 LesionAgent，一個無需任務特定訓練的 LLM 代理，透過凍結的 3D 基礎模型作為工具、座標標註的 2D 視圖在 3D 空間操作、病灶登記表跨就診記憶、自我驗證機制與確定性指引引擎，實現從影像到 RECIST 回應的全自動或醫師輔助判讀，填補臨床工作流程的自動化缺口。

## 方法
LesionAgent 採用工具調用迴圈架構，核心為一 LLM（支援 Claude Opus 5.5 與開源 Qwen3.8-27B）在共享工作空間中透過 18 個型別化工具操作凍結的 3D 基礎模型。輸入為患者多期 CT 影像序列，輸出為各追蹤期的 RECIST 回應報告。關鍵模組：(1) 病灶登記表：以病灶×就診矩陣儲存每期遮罩與狀態（目標、非目標、新發、拒絕、太小、缺失、合併），確保無病灶靜默遺失。(2) 座標標註 2D 視圖：將體素索引與患者方向標註於切片上，使 LLM 讀取的 2D 位置可直接轉為 3D 點擊提示，實現跨維度操作。(3) 感知工具鏈：基線期用 VoxTell 多提示詞偵測候選，LLM 於視圖中逐一接受/拒絕；漏測時以 nnInteractive 點擊補充。追蹤期先以 uniGradICON 配準影像，再以 LongiTrack 傳播並分割既有病灶；未偵測到者標記為缺失。新發候選經基線期同位置檢查後始確認為新病灶。所有遮罩再經 nnInteractive 二次精修以捕捉失敗。(4) 目標選擇：LLM 依 RECIST 規則自行評分並提議最多五個目標病灶，或讓臨床醫師從合法集合中選擇。(5) 確定性指引引擎：根據遮罩計算長短軸、加總目標病灶直徑、套用 RECIST 1.1 規則產生回應類別與報告，LLM 不直接計算數值。整個流程無需任務特定訓練，可全自動或透過 napari 外掛引入醫師互動。

## 結果
於四個公開縱向 CT 資料集，LesionAgent 完全自動模式下追蹤病灶數量與測量準確度均優於所有自動基線。固定規則串接相同 3D 模型在 56 追蹤期中誤判進展達 33 例，LesionAgent 僅 2 例。臨床追蹤 CT 上與放射科醫師回應一致率 20/23（含全部 4 次回應變化），平衡準確率 95%。未在 DeepLesion 訓練情況下，病灶檢索率 89.0% 優於在該資料集訓練的追蹤器 87.4%。消融顯示 harness 關鍵：相同 LLM 與 3D 模型下，Claude Code 偵測 F1 從 41% 提升至 78%，開源 LLM 從 6% 提升至 73%。結節測量落於讀者間變異範圍內。

## 限制與展望
本文為預印本，尚未經同儕審查。實驗僅涵蓋四個公開資料集與部分臨床追蹤 CT，對其他癌別、掃描協定、造劑差異的泛化性尚待驗證。代理性能受限於凍結 3D 模型的上限，且依賴特定工具實作（VoxTell、uniGradICON、LongiTrack、nnInteractive 等），移植至不同模型需重新適配。確定性引擎目前僅實作 RECIST 1.1，其他指引需修改引擎。開源 LLM 於院內硬體運行的延遲、記憶體需求與穩定性未詳細報告。LLM 判斷病灶接受/拒絕可能引入主觀誤差，缺乏大規模前瞻性臨床試驗驗證安全性與法規合規。後續研究需擴展至多中心、多指引、前瞻性驗證。
