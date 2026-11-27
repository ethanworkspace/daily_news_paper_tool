# 論文 02：Early evidence for a multi-agent AI simulator for clinical reasoning practice: performance, consistency, and challenges.

- 日期：2026-09-16
- 來源層級：Tier 4（一般期刊）
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
臨床推理能力需透過反覆、刻意練習培養，但真實臨床與模擬環境常受限於連續性、回饋品質與規模擴展。大型語言模型（LLM）可生成虛擬病患遭遇，提供無需真人指導者或標準化病患的練習機會，惟其效度證據仍稀少。本研究旨在探索 MAESSCR（多代理教學情境模擬器，供臨床推理練習）之表現，該平台讓多個各司其職的 LLM 代理（病患、體格檢查、診斷測試）以文字互動方式與學習者進行臨床情境演練。

## 方法
研究設計為觀察性教學評估。2024 年秋季，175 位二年級醫學生各完成三個 MAESSCR 臨床遭遇作為課程作業。系統架構採多代理協作：每個案例預先編寫腳本，包含病患敘述、體檢發現與檢驗結果；三個 LLM 代理分別扮演病患（提供病史回應）、體檢代理（依學生請求回傳體檢徵象）、診斷/管理代理（依學生下單回傳檢驗影像與初步判讀）。學生以文字輸入詢問、要求檢查、下達醫囑，代理即時回應，形成完整遭遇記錄。評估階段由六位臨床教師共同開發二分量表（是/否），對隨機抽取的 120 份逐字稿（每案 40 份）進行四維度評分：(1) 代理回應真實感、(2) 是否遵循腳本細節、(3) 平台功能運作、(4) 是否干擾學生自主推理（如提前解讀發現）。並輔以質性敘述回顧補充二元評分。資料前處理僅涉及逐字稿匿名化與分段；無額外微調或訓練目標，推論流程為即時多輪對話。與既有單一代理或靜態案例教材不同，本系統強調角色分工與動態互動，並嘗試量化代理干擾學生推理的頻率。

## 結果
結果顯示：92%（110/120）逐字稿符合腳本細節；僅 2.5%（3/120）出現改變診斷的關鍵資訊錯誤。病患代理呈現不真實表現佔 12%（14/120），技術故障佔 17%（20/120）。干擾學生自主推理最常見於代理提前解讀發現：病史/體檢代理佔 28%（34/120），診斷/管理代理佔 59%（71/120）。大多數干擾屬輕微，未嚴重損害整體遭遇品質。質性回顧進一步指出角色穩定性與情境保真度為教學價值關鍵。

## 限制與展望
研究限制包括：單一醫學院、單一學期、僅三個案例，樣本與情境多樣性有限；評估僅採二分量表與專家主觀判斷，缺乏學習成效量化指標（如診斷準確度、推理深度）；未報告 LLM 版本、提示詞設計與超參數，難以重現；代理提前解讀發現的干擾機制未深入分析；未來需擴大樣本、引入對照組、建立標準化效度框架並探討長期教學影響。
