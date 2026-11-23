# 論文 01：LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- 日期：2026-11-03
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
癌症患者每數月接受一次 CT 掃描以決定治療是否持續，放射科醫師依據 RECIST 1.1 指引手動判讀病灶、追蹤跨期病灶並評估治療反應，但此過程耗時、讀者間差異大（同標靶病灶一致率僅 41%，肺結節偵測敏感度 51–83%），且單一 3D 基礎模型僅能零樣本完成偵測、分割、配準或追蹤等單一步驟，無法端到端完成完整反應評估。現有代理雖能調用專用模型，但多針對單一影像研究，無法處理多期 3D 影像與時間維度的病灶追蹤。因此，本研究旨在開發免訓練的 LLM 代理 LesionAgent，整合凍結的 3D 基礎模型作為工具，透過座標標註視圖在 3D 空間操作、跨期病灶登記簿記憶、自我驗證模型輸出，並將所有數值計算與分類交由確定性指引引擎執行，實現端到端的縱向 CT 腫瘤監測。

## 方法
LesionAgent 採用 LLM 工具使用迴圈，僅透過 18 個型別化工具（表 1）在共享工作空間操作：感知工具包含 detect（VoxTell 多提示偵測候選病灶）、segment（nnInteractive 點擊分割補漏或修正追蹤遮罩）、track_all（uniGradICON 配準傳播病灶點並以 LongiTrack 分割）、refine_lesion、edit_mask、totalsegmentator；檢查工具含 study_info、view、view_pair、inspect；登記簿工具含 review_candidates、update_lesion、set_visit_judgement；決策工具含 score_lesions、propose_targets、set_targets、recist_report（確定性引擎）；人機互動工具 ask_clinician。病灶登記簿以病灶×就診矩陣儲存每期遮罩、類型、器官、角色（標靶/非標靶/新發/拒絕）及狀態（過小、缺失、合併），確保無病灶靜默遺失。代理透過座標標註的 2D 切面（標示體素索引與患者方向）在 3D 體積中定位，將視覺位置轉為 3D 點擊提示，並以第二模型重新分割驗證遮罩。確定性 RECIST 引擎依遮罩測量長短軸、加總標靶病灶直徑、套用 30% 縮小/20% 增大+5mm/新發病灶規則產出反應類別，LLM 僅負責判斷「是否為病灶」、「哪些為標靶」、「新發發現是否明確」等語義決策。系統可全自動或經由 napari 外掛讓臨床醫師介入，支援 Claude Opus 5.5 與開源 Qwen3.8-27B 等 LLM 不變更技能文件即可運行。

## 結果
在四個公開縱向 CT 資料集上，LesionAgent 完全自動模式下追蹤病灶數量與測量準確度均優於所有自動基線；同樣 3D 模型以固定規則串接時，56 次追蹤中有 33 次誤判為進展，LesionAgent 僅 2 次。臨床追蹤 CT 中，與放射科醫師反應判讀一致 20/23 次，包含全部 4 次反應變化（平衡準確率 95%）。未在 DeepLesion 訓練情況下，病灶檢索率 89.0% 高於在該資料集訓練的追蹤器 87.4%。消融顯示代理架構而非 LLM 本身為關鍵：相同 LLM 與 3D 模型下，Claude Code 偵測 F1 41% 對 LesionAgent 78%；開源 LLM 從 6% 提升至 73%。結節測量落於讀者間變異範圍內。

## 限制與展望
評估僅涵蓋四個公開資料集與 23 例臨床追蹤，癌症類型、掃描協定多樣性有限；依賴凍結 3D 基礎模型（VoxTell、nnInteractive、uniGradICON、LongiTrack、TotalSegmentator）的零樣本表現，其偵測與分割錯誤會傳遞至下游；座標標註視圖僅提供切面檢查，可能遺漏 3D 結構資訊；病灶合併、消失、過小等狀態處理依賴啟發式規則；確定性引擎僅實作 RECIST 1.1，其他指引需重寫引擎；LLM 判斷仍可能出現幻覺或邏輯錯誤；系統需較大計算資源運行多個 3D 模型；napari 外掛為研究原型，臨床部署需進一步驗證與合規；論文為預印本，尚未經同儕審查。
