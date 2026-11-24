# 論文 02：OASIS, a self-evolving AI scientist that integrates omics data and literature knowledge for plant stress research.

- 日期：2026-09-21
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
非生物胁迫嚴重限制植物生長與作物產能，但文獻快速增長與異質組學資料難以轉化為可驗證假設。現有方法缺乏將文獻機制證據與組學結構化資料整合、且具可追溯工作流與自我演化能力的 AI 系統。本文提出 OASIS，一個自我演化的組學導向 AI 科學家，協調規劃、混合檢索、證據蒸餾、資料詢證、審查與綜合六大專用代理，建立涵蓋六物種四大胁迫類別的知識庫並自動更新，並引入 SEEL 模組將歷史軌跡提煉為可重用程序規則，實現基於經驗的自我演化，旨在為植物胁迫研究提供可追溯、可演進的假設生成平台。

## 方法
問題設定：輸入為植物胁迫相關的研究問題（如基因優先排序），輸出為可追溯的假設與候選基因清單。整體架構採多代理協作：① 規劃代理將問題分解為子任務；② 混合檢索代理並行檢索文獻（語意搜尋）與結構化組學資料庫（基因表達、變異體、正交同源等）；③ 證據蒸餾代理從文獻中抽取機制性證據並標註來源；④ 資料詢證代理對組學資料執行查詢與統計分析；⑤ 審查代理交叉驗證文獻與資料層面的證據一致性；⑥ 綜合代理整合所有證據生成最終回答。知識庫涵蓋六種植物、四大胁迫類別，並具備自動文獻增量更新機制。核心創新為 SEEL（自我演化經驗學習）模組：將歷史推理軌跡（規劃、檢索、蒸餾、詢證、審查步驟）自動提煉為可重用的程序規則庫，後續任務可直接調用，實現經驗驅動的自我演化。推理流程為：使用者提問 → 規劃 → 混合檢索 → 證據蒸餾與資料詢證並行 → 審查 → 綜合輸出。與既有單一 LLM 或檢索增強方法不同，OASIS 強調多代理分工、文獻與組學雙軌證據整合、可追溯性與經驗規則的持續累積。

## 結果
在專家策劃的 PlantStressQA 基準（200 題）上，OASIS 獲得 84.0/100 分，較基線大型語言模型高出 33.9–50.2 分，且在需多步整合文獻與資料層證據的任務上提升最明顯。水稻鹽耐受案例研究中，OASIS 結合拟南芥調控證據、正交同源與遺傳座位，優先推薦五個候選基因；實驗驗證顯示 OsPP2a 功能缺失導致鹽胁迫表型並伴隨 Na⁺/K⁺ 平衡改變，證明系統能產生可實證的假設。摘錄未提供其他定量指標（如召回率、執行時間）或更多消融實驗數字。

## 限制與展望
目前知識庫僅涵蓋六物種四類胁迫，泛化至其他作物或胁迫類型仍待驗證；PlantStressQA 僅 200 題，基準規模有限，可能無法全面反映真實研究複雜度；案例研究僅針對單一基因 OsPP2a 進行實驗驗證，其餘四候選基因未實證；SEEL 依賴歷史軌跡，若早期推理含錯誤可能傳遞偏誤；系統計算資源消耗、延遲與部署細節未揭露；文獻自動更新可能引入噪聲或偏向高引用文獻。後續研究可擴展物種與胁迫覆蓋、引入更多組學模態、改進經驗規則品質控制、並進行大規模濕實驗驗證。
