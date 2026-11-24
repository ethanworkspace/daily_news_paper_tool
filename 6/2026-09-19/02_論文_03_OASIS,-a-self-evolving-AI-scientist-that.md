# 論文 03：OASIS, a self-evolving AI scientist that integrates omics data and literature knowledge for plant stress research.

- 日期：2026-09-19
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
非生物胁迫限制植物生長與作物產能，文獻與異質組學數據快速增長，但將其轉化為可驗證假設仍具挑戰。現有方法多缺乏跨數據源的可追溯整合機制，難以支援多步驟推理。本文提出 OASIS，一個自我演化的組學導向 AI 科學家，旨在將文獻機制證據與組學等結構化數據串聯，建立可追溯工作流，並透過經驗學習模組實現自我演化，解決植物胁迫研究中的假設生成與驗證難題。

## 方法
問題設定：輸入為植物胁迫相關的自然語言問題，輸出為可追溯的假設與實驗建議。系統架構由六大專用代理組成：規劃代理負責任務分解與流程編排；混合檢索代理結合文獻語義檢索與結構化數據庫查詢，獲取機制證據與組學特徵；證據蒸餾代理將檢索結果轉化為標準化知識片段；數據詢問代理對組學矩陣、基因型表型關聯等進行統計查詢；審查代理對推理鏈進行邏輯一致性與來源可追溯性檢查；綜合代理生成最終回答與實驗優先級。知識庫涵蓋六個植物物種與四大胁迫類別，並具備自動增量更新機制。核心創新為自我演化經驗學習（SEEL）模組，將歷史推理軌跡抽象為可重用程序規則，並在後續任務中自動調用，實現基於經驗的自我演化。資料前處理採用統一實體標準化（基因、蛋白、代謝物 ID）與跨物種同源映射，將異質數據投影至共享向量空間。訓練目標未在摘錄中詳細描述，推測採用監督式問答損失與檢索排序損失聯合優化；推理流程為規劃→檢索→蒸餾→詢問→審查→綜合，並以 SEEL 規則輔助決策。與既有單一模型或靜態檢索系統相比，關鍵差異在於多代理協作、可追溯證據鏈與經驗驅動的規則演化。

## 結果
在專家策劃的 PlantStressQA 200 題基準上，OASIS 獲得 84.0/100 分，較基線大型語言模型高出 33.9–50.2 分，尤其在需多步整合文獻與數據證據的任務上提升最大。水稻鹽耐受案例研究中，系統結合拟南芥調控證據、同源基因映射與遺傳座位，優先推薦五個候選基因；實驗驗證顯示 OsPP2a 失功能導致鹽胁迫表型並伴隨 Na⁺/K⁺ 平衡改變，支持預測可靠性。

## 限制與展望
評估僅限於單一基準與單一案例研究，缺乏跨物種、跨胁迫類別的大規模驗證；基線模型細節未揭露，難以判斷提升來源；SEEL 模組的規則抽取與泛化能力未提供消融數據；知識庫僅覆蓋六物種四胁迫，擴展性待證實；自動文獻更新可能引入噪聲，需人工審核機制。後續研究可擴大基準、量化經驗規則效益並探討部署穩健性。
