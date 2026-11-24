# 論文 03：Early evidence for a multi-agent AI simulator for clinical reasoning practice: performance, consistency, and challenges.

- 日期：2026-09-18
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
臨床推理需透過反覆、刻意練習培養，但真實臨床與模擬環境常受限於連續性、回饋與擴展性。大型語言模型（LLM）可生成虛擬病患遭遇，無需真人指導者或標準化病患，惟其效度證據仍稀少。本研究旨在探索 MAESSCR（多代理教學情境模擬器，供臨床推理練習）之表現，該平台讓多個各司其職的 LLM 代理（病患、身體檢查、診斷測試）以文字互動方式與學習者進行臨床情境演練，提供可擴展的練習管道。

## 方法
研究設計為觀察性教學評估。2024 年秋季，175 位二年級醫學生各完成三個 MAESSCR 情境作為課程作業。六位臨床教師共同開發評分工具，從 120 份逐字紀錄（每個案例隨機抽樣 40 份）以二分量表（是/否）評估四大面向：(1) 代理回應的真實感、(2) 對腳本案例細節的遵循度、(3) 平台功能性、(4) 是否干擾學生獨立解讀臨床發現。並輔以質性敘述回顧。MAESSCR 架構採多代理協作：每個代理被指派單一角色（病患、身體檢查、診斷測試），透過文字介面依序回應學生提問與操作，形成完整臨床遭遇流程。系統無額外微調或訓練目標描述，推論過程為學生輸入→對應角色代理生成回應→呈現給學生，循環至遭遇結束。關鍵差異在於將單一 LLM 拆解為多專業角色代理，嘗試模擬真實團隊互動，並強調角色穩定性與情境保真度。

## 結果
評估結果顯示：MAESSCR 於 92%（110/120）逐字紀錄中遵循腳本細節；出現改變診斷關鍵資訊者僅 2.5%（3/120）；病患描繪不真實佔 12%（14/120）；技術問題佔 17%（20/120）。干擾學生獨立推理最常見於代理過早解讀發現：病史/身體檢查代理佔 28%（34/120），診斷/管理代理佔 59%（71/120），惟多數干擾屬輕微，不太可能嚴重破壞整體遭遇。質性回顧進一步指出角色穩定性、情境保真度與學生自主解讀機會為教學價值關鍵。

## 限制與展望
本研究僅在單一醫學院、單一學期、175 位二年級學生進行，樣本與情境多樣性有限。評估工具為二分量表，缺乏連續量化指標與學習成效（如診斷準確度、推理深度）之實證。技術問題（17%）與代理過早解讀（最高 59%）顯示系統穩定性與角色控制仍待改善。未來需擴大機構、引入對照組、採用多維度評估並優化代理協調機制，以驗證教學效益與泛化能力。
