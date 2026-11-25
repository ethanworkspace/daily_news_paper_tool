# 論文 05：RadOnc-GPT: An Exploratory Feasibility Study of a Prototype LLM Agent for Radiation Oncology Outcomes Labeling and Registry Auditing.

- 日期：2026-10-18
- 來源層級：Tier 2
- 期刊/會議/來源：Meta-radiology
- Venue：Meta-radiology
- 發布時間：2026-10-15T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43061675/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13784673/
- DOI：10.1016/j.metrad.2026.100245
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2345（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
PURPOSE: Manual outcomes labeling limits the scale and timeliness of radiation oncology research and registry maintenance. We explored the technical feasibility of RadOnc-GPT, a prototype GPT-4o-based agent that retrieves structured and longitudinal clinical evidence from institutional systems and returns schema-constrained outcome labels and supporting rationale. MATERIAL AND METHODS: In this single-institution retrospective feasibility study, we evaluated two tiers of increasing complexity: (i) reproduction of structured demographic and radiotherapy-course data and (ii) outcomes labeling using structured and unstructured data for mandibular osteoradionecrosis in head-and-neck cancer and cancer recurrence in separate prostate and head-and-neck cancer cohorts. Only cases in which the model and baseline registry disagreed underwent review by one unblinded domain-specific oncologist per dataset. Post-review values are therefore described as discrepancy-adjudicated and condition on concordant baseline labels being correct. RESULTS: Across 500 patients, the prototype matched all six demographic/identifier fields (3,000/3,000) and reproduced per-course treatment information in 497/500 patients. In 395 evaluable outcomes-labeling cases, initial accuracy/F1 were 85.0%/63.2% for osteoradionecrosis, 92.5%/92.5% for prostate recurrence, and 92.7%/90.9% for head-and-neck cancer recurrence. Review of 47 discordant cases classified 24 as baseline-label errors, 18 as model errors, and 5 as indeterminate. Discrepancy-adjudicated accuracy/F1 were 95.2%/89.7%, 95.0%/95.1%, and 96.3%/95.5%, respectively. In an assumption-based pooled stress test, treating 1%, 3%, or 5% of the 348 concordant cases as hidden model errors reduced pooled accuracy from 95.4% to 94.4%, 92.6%, and 90.8%, respectively. These scenario analyses do not estimate the true latent-error rate. CONCLUSION: In this single-institution feasibility study, RadOnc-GPT reproduced selected structured radiotherapy data, generated candidate outcome labels from longitudinal clinical records, and flagged model-registry discrepancies for expert review. These results support further evaluation of LLM-assisted outcomes labeling and registry auditing, including blinded multi-reviewer adjudication, multi-institutional validation, and testing in natural-prevalence cohorts.

## 背景與目的
本研究旨在解決放射腫瘤學中人工結果標註規模小、時效性差的問題。現有登錄庫依賴人工抽取結構化與非結構化臨床資料，導致資料更新緩慢且易出錯。作者提出 RadOnc-GPT，一個基於 GPT-4o 的原型代理，能從院內系統自動檢索長期臨床證據，並輸出符合預定結構的結果標籤與理由，以探討 LLM 輔助結果標註與登錄稽核的技術可行性。

## 方法
方法分兩階段。第一階段驗證結構化資料重現：從院內放射治療資訊系統抽取 500 位患者的六項人口統計/識別碼欄位（共 3,000 欄位）與每個治療程序的詳細資訊，讓代理以 GPT-4o 為核心，透過提示工程將查詢轉為結構化查詢語言（或 API 呼叫），取回資料後依預定 JSON Schema 輸出，並與登錄庫逐欄比對。第二階段進行結果標註：針對頭頸癌下顎骨放射性骨壞死、前列腺癌復發、頭頸癌復發三個隊列，代理同時接收結構化治療紀錄（劑量、分次、靶區）與非結構化臨床筆記（出院摘要、影像報告、病理報告），利用長文本上下文窗口進行多輪推理，先抽取關鍵臨床事件，再依疾病特定定義產生二元標籤（有/無）與推理說明，輸出同樣受 Schema 限制。僅當代理標籤與基準登錄不一致時，由對應專科腫瘤醫師（未盲審）進行單一審閱，審閱後的結果稱為「差異裁定」，並假設一致案例的基準標籤正確。訓練目標為零樣本/少樣本提示下的準確標註，無額外微調；損失函數與最佳化不適用。推論流程為：資料檢索 → 提示構建 → GPT-4o 生成 → Schema 驗證 → 與登錄比對 → 差異送審。關鍵差異在於結合結構化與非結構化長期紀錄、採用 Schema‑constrained 輸出與人機協作裁定機制。

## 結果
在 500 例中，六項人口統計欄位全數正確（3,000/3,000），治療程序資訊於 497/500 例重現。395 例可評估結果標註案例中，初始準確率/F1 分別為：骨壞死 85.0%/63.2%、前列腺復發 92.5%/92.5%、頭頸復發 92.7%/90.9%。47 例不一致經審閱後，判定 24 例為登錄錯誤、18 例為模型錯誤、5 例無法判定。差異裁定後準確率/F1 提升至：骨壞死 95.2%/89.7%、前列腺 95.0%/95.1%、頭頸 96.3%/95.5%。壓力測試假設 1%、3%、5% 一致案例為隱性模型錯誤，合併準確率從 95.4% 降至 94.4%、92.6%、90.8%。摘錄未提供可驗證的完整混淆矩陣或置信區間。

## 限制與展望
研究為單一機構回顧性可行性試驗，樣本量有限且僅涵蓋三種結果，無法推廣至其他癌別或機構。審閱僅由單一未盲審醫師進行，缺乏多評審盲法，可能引入偏誤。基準登錄被假設為正確，實際潛在錯誤率未知，壓力測試僅為假設情境。模型未經微調，依賴 GPT-4o 零樣本能力，提示工程細節未公開，難以重現。部署層面需解決資料隱私、系統整合與即時推論延遲等問題。後續需進行多中心盲審驗證、自然流行率隊列測試及錯誤分析。
