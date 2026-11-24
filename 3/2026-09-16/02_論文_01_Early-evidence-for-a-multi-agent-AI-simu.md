# 論文 01：Early evidence for a multi-agent AI simulator for clinical reasoning practice: performance, consistency, and challenges.

- 日期：2026-09-16
- 來源層級：Tier 2
- 期刊/會議/來源：Diagnosis (Berlin, Germany)
- Venue：Diagnosis (Berlin, Germany)
- 發布時間：2026-09-16T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42740524/
- PDF：
- DOI：10.1515/dx-2026-0069
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2197（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
OBJECTIVES: Clinical reasoning develops through repeated, deliberate practice, yet clinical and simulation environments are often limited by continuity, feedback, and scalability constraints. Large language models (LLMs) may address this by generating virtual clinical encounters accessible without live instructors or standardized patients but validity evidence remains limited. This study explored the performance of MAESSCR (Multi-Agent Educational Scenario Simulator for Clinical Reasoning), a platform where multiple LLM-based agents, each assigned a distinct role (i.e. patient, physical exam, diagnostic testing) interact with learners through a text-based encounter. METHODS: In Fall of 2024, 175 second-year medical students completed three MAESSCR clinical encounters as coursework. Six clinician-educators developed a rating tool to evaluate 120 transcripts (40 randomly sampled per case) using a dichotomous (yes/no) scale across four domains: (1) realism of agent responses, (2) adherence to scripted case details, (3) platform functionality, and (4) interference with students' independent reasoning through clinical findings. Qualitative narrative review supplemented binary ratings. RESULTS: MAESSCR followed scripted details in 92 % (110/120) of transcripts. Diagnosis-changing information occurred in 2.5 % (3/120). Unrealistic patient portrayal appeared in 12 % (14/120) of encounters, and technical issues in 17 % (20/120). AI agents most often interfered with student's clinical reasoning by interpreting findings before the students had the opportunity. This occurred in 28 % (34/120) of encounters due to history/physical exam agents and 59 % (71/120) because of diagnostics/management agents. Most disruptions were minor and unlikely to compromise the overall encounter. CONCLUSIONS: Multi-agent, LLM-based simulations offer a scalable approach to deliberate practice of clinical reasoning. Educational value depends on role stability, contextual fidelity, and learners' opportunity to interpret clinical information independently. Specific design considerations are essential to ensure AI-generated simulations support, rather than disrupt, the clinical reasoning process.

## 背景與目的
臨床推理需透過反覆、刻意練習發展，但真實臨床與模擬環境常受限於連續性、回饋與擴展性。大型語言模型（LLM）可生成虛擬臨床情境，提供無需真人指導者或標準化病人的練習機會，惟其效度證據仍稀少。本研究旨在探索 MAESSCR（多代理人教育情境模擬器，供臨床推理練習）之表現，評估多角色 LLM 代理人透過文字互動支援學生推理的可行性與品質。

## 方法
研究設定為多代理人 LLM 模擬平台，輸入為學生以文字進行的病史詢問、身體檢查請求與診斷檢查指令；輸出為各代理人依角色（病人、身體檢查、診斷檢查/管理）回應的文字。系統架構包含三個獨立 LLM 代理人，各自依預設腳本與案例細節扮演特定角色，透過共享對話歷史維持情境一致性。核心機制為角色提示工程與腳本約束，確保代理人遵循預設臨床資料並避免過早解釋發現。資料前處理將 175 位二年級醫學生於 2024 秋季完成的三次模擬記錄整理為逐字稿，隨機抽樣每案 40 份共 120 份供評估。六位臨床教育者共同開發二分量表評分工具，針對四大領域（代理人回應真實感、腳本細節遵循度、平台功能性、對學生獨立推理的干擾）進行是/否判斷，並輔以質性敘述審查。訓練目標並非模型微調，而是驗證提示設計與多代理人協作對教學品質的影響；推論流程為學生發起動作 → 相應代理人依角色生成回應 → 記錄對話 → 事後專家評分。與既有單一代理人或靜態案例模擬不同，本系統強調角色分工、動態互動與腳本忠實度的結合。

## 結果
專家評分顯示 MAESSCR 於 92%（110/120）逐字稿遵循腳本細節，僅 2.5%（3/120）出現改變診斷的資訊。病人角色真實感缺失佔 12%（14/120），技術問題佔 17%（20/120）。干擾學生獨立推理最常見於代理人過早解釋發現：病史/身檢代理人 28%（34/120），診斷/管理代理人 59%（71/120），但多數干擾屬輕微，未嚴重損害整體情境。質性審查進一步指出角色穩定性與情境保真度為關鍵。

## 限制與展望
研究僅在單一醫學院、三個案例與 175 位二年級學生進行，樣本與情境多樣性有限；評分工具為二分量表，缺乏細緻度量，且無學生學習成效或長期保留的實證；技術故障與代理人過早解釋仍存，可能影響推理訓練品質；未與其他模擬平台或真人標準化病人比較，泛化性待進一步驗證。後續研究需擴大樣本、引入多樣案例、開發更精細評估指標並探討教學成效。
