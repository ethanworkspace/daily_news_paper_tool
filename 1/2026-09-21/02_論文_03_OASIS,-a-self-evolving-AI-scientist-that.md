# 論文 03：OASIS, a self-evolving AI scientist that integrates omics data and literature knowledge for plant stress research.

- 日期：2026-09-21
- 來源層級：Tier 4（一般期刊）
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
- 全文字數：1505（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Abiotic stress constrains plant growth and crop productivity, yet converting rapidly expanding stress-related literature and heterogeneous biological data into testable hypotheses remains difficult. Here, we present omics-guided AI scientist for integrative stress research (OASIS), a self-evolving omics-guided AI scientist that links literature-derived mechanistic evidence with omics and other structured data in a traceable workflow for plant stress research. OASIS coordinates six specialized agents for planning, hybrid retrieval, evidence distillation, data interrogation, review, and synthesis. Its knowledge base spans six plant species and four major stress categories and automatically incorporates newly published studies. At the same time, the self-evolving experience learning module distills historical trajectories into reusable procedural rules for experience-based self-evolution. On PlantStressQA, a 200-question expert-curated benchmark, OASIS achieved 84.0/100, exceeding baseline large language models by 33.9-50.2 points, and showed its largest gains on tasks requiring multi-step integration of literature and data-level evidence. In a case study on rice salt tolerance, OASIS combined Arabidopsis regulatory evidence, orthology, and genetic loci to prioritize five candidates. Genetic analysis revealed that loss of OsPP2a function causes salt stress-responsive phenotypes accompanied by altered Na+/K+ homeostasis in rice. OASIS is publicly accessible at https://www.oasis.ac.cn.

## 背景與目的
非生物胁迫限制植物生長與作物產能，但快速增長的胁迫相關文獻與異質生物數據難以轉化為可驗證假設。本研究提出 OASIS，一個自我演化的組學引導 AI 科學家，旨在將文獻衍生的機制證據與組學等結構化數據在可追蹤的工作流中連結，支援六種植物物種與四大胁迫類別，並自動納入新發表研究，解決跨模態知識整合與假設生成的缺口。

## 方法
OASIS 採用多代理協作架構，包含六個專用代理：規劃、混合檢索、證據蒸餾、數據詮釋、審查與綜合。輸入為研究問題，輸出為可測試的假設或候選基因清單。知識庫涵蓋六植物物種、四大胁迫類別，並能自動更新新文獻。混合檢索結合文獻語義搜尋與結構化組學數據查詢；證據蒸餾從文本抽取機制證據；數據詮釋對組學數據進行統計與網絡分析；審查代理評估證據一致性；綜合代理整合多源證據生成最終建議。自我演化經驗學習模組將歷史執行軌跡提煉為可重用程序規則，實現基於經驗的自我演化。整體流程為可追蹤的管線，但摘錄未提供具體模型架構、訓練目標、損失函數或優化策略等技術細節。

## 結果
在專家策劃的 PlantStressQA 200 題基準測試中，OASIS 獲得 84.0/100 分，較基線大型語言模型高出 33.9–50.2 分，尤其在需多步整合文獻與數據層級證據的任務上提升最大。水稻鹽耐受案例研究中，OASIS 結合拟南芥調控證據、同源基因與遺傳座位優先出五個候選；遺傳分析證實 OsPP2a 功能缺失導致鹽胁迫表型並伴隨 Na+/K+ 平衡改變。摘錄未提供其他可驗證數字。

## 限制與展望
僅涵蓋六物種與四類胁迫，泛化能力未知；基準測試僅 200 題且基線模型未具體命名，比較公平性有待進一步驗證；自我演化模組的效能評估缺乏消融實驗；計算資源需求、推理延遲與部署擴展性未描述；知識庫自動更新機制的錯誤傳播風險未討論；後續研究需擴大物種與胁迫範圍、引入更多基線、量化經驗學習貢獻並進行獨立實驗驗證。
