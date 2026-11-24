# 論文 04：OASIS, a self-evolving AI scientist that integrates omics data and literature knowledge for plant stress research.

- 日期：2026-09-26
- 來源層級：Tier 2
- 期刊/會議/來源：Molecular plant
- Venue：Molecular plant
- 發布時間：2026-09-18T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42760786/
- PDF：
- DOI：10.1016/j.molp.2026.09.005
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1359（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Abiotic stresses constrain plant growth and crop productivity, yet converting rapidly expanding literature and heterogeneous biological data into testable hypotheses remains difficult. Here we present OASIS, a self-evolving omics-guided AI scientist that links literature-derived mechanistic evidence with omics and other structured data in a traceable workflow for plant stress research. OASIS coordinates six specialized agents for planning, hybrid retrieval, evidence distillation, data interrogation, review, and synthesis. Its knowledge base spans six plant species and four major stress categories and automatically incorporates newly published studies, while the Self-Evolving Experience Learning (SEEL) module distills historical trajectories into reusable procedural rules for experience-based self-evolution. On PlantStressQA, a 200-question expert-curated benchmark, OASIS achieved 84.0/100, exceeding baseline LLMs by 33.9-50.2 points, and showed its largest gains on tasks requiring multi-step integration of literature and data-level evidence. In a rice salt-tolerance case study, OASIS combined Arabidopsis regulatory evidence, orthology, and genetic loci to prioritize five candidates. Loss of OsPP2a function produced salt-response phenotypes accompanied by altered Na+/K+ homeostasis. OASIS is publicly accessible at https://www.oasis.ac.cn.

## 背景與目的
非生物胁迫限制植物生長與作物產能，文獻與異質組學數據快速增長卻難轉化為可驗證假設。現有方法多為單一模型或靜態知識庫，缺乏跨物種、跨胁迫類別的機制整合與自我演進能力。本文提出 OASIS，一個自我演進的組學導向 AI 科學家，旨在將文獻機制證據與組學等結構化數據以可追溯工作流串聯，支援六大植物物種與四類主要胁迫，並能自動納入新發表研究，透過自我演進經驗學習（SEEL）模組將歷史軌跡提煉為可重用程序規則，實現基於經驗的自我演進，解決多步驟文獻與數據層面證據整合的難題。

## 方法
問題設定：輸入為植物胁迫研究的自然語言問題或假設生成需求，輸出為可追溯的機制假設、候選基因清單及實驗建議。整體架構採用多智能體協作框架，包含六大專用代理：規劃代理負責任務分解與流程編排；混合檢索代理結合文獻語義檢索與結構化組學數據庫查詢；證據蒸餾代理從文獻與數據中提取機制級證據並標註來源；數據審問代理執行正交同源映射、表達量差異分析、基因座位關聯等組學層面驗證；審查代理對整合證據進行一致性與邏輯檢核；綜合代理生成最終假設報告與可視化證據鏈。知識庫涵蓋六種植物（如拟南芥、水稻等）與四大胁迫類別（鹽、乾旱、低溫、高溫），並具備自動增量更新機制，能即時納入新發表論文。核心創新為自我演進經驗學習（SEEL）模組：將歷史推理軌跡（規劃、檢索、蒸餾、審問、審查、綜合的完整鏈路）轉化為可重用的程序規則庫，後續任務可直接調用並持續優化，實現基於經驗的自我演進。資料前處理包含文獻全文切分、實體識別、關係抽取，組學數據標準化、正交同源對齊與基因座位標註。摘錄未提供具體訓練目標、損失函數或最佳化策略細節。推理流程依序經過規劃→混合檢索→證據蒸餾→數據審問→審查→綜合，每步均保留來源追溯。與既有單一大語言模型或靜態知識圖譜方法相比，關鍵差異在於多代理協作、文獻與組學異構數據的即時融合、可追溯證據鏈以及 SEEL 驅動的持續自我改進。

## 結果
在專家策劃的 PlantStressQA 基準（200 題）上，OASIS 獲得 84.0/100 分，較基線大語言模型高出 33.9–50.2 分，且在需多步驟整合文獻與數據層面證據的任務上提升最明顯。水稻鹽耐受案例研究中，OASIS 結合拟南芥調控證據、正交同源與遺傳座位，優先推薦五個候選基因；實驗驗證顯示 OsPP2a 功能缺失導致鹽胁迫表型並伴隨 Na⁺/K⁺ 離子平衡改變。摘錄未提供其他消融實驗或統計顯著性數字。

## 限制與展望
目前知識庫僅覆蓋六物種四胁迫，擴展性未經大規模驗證；PlantStressQA 僅 200 題，可能無法全面反映真實研究多樣性；案例研究僅針對水稻鹽胁迫單一情境，缺乏跨物種、跨胁迫的獨立實驗驗證；SEEL 依賴歷史軌跡品質，錯誤傳播風險尚未量化；計算資源、推理延遲與部署細節未揭露。後續研究可擴充物種與胁迫類別、引入不確定性估計、建立更大規模基準並進行前瞻性實驗驗證。
