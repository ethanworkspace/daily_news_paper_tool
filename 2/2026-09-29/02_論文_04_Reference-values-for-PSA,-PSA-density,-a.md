# 論文 04：Reference values for PSA, PSA density, and MRI prostate volume in healthy German men.

- 日期：2026-09-29
- 來源層級：Tier 4（一般期刊）
- 期刊/會議/來源：European radiology
- Venue：European radiology
- 發布時間：2026-09-25T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42789055/
- PDF：
- DOI：10.1007/s00330-026-12937-2
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2431（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：ProstateAssistant/ProstateAssistant.github.io

## 摘要
OBJECTIVES: To establish stratified normative reference values for MRI-derived prostate volume (PV), prostate-specific antigen (PSA), and PSA density (PSAD) in German men with no known prostate pathologies, accounting for age, body-mass index, and height. MATERIALS AND METHODS: This study included men from the prospective population-based Study of Health in Pomerania, Germany, with 10 years of follow-up. Men with diagnosed prostate cancer, benign prostatic hyperplasia, or lower urinary tract symptoms were excluded to derive reference values unaffected by disease or interventions. PV and PSAD were obtained from pelvic MRI using deep-learning segmentation. In a test set, segmentation-derived volumes were compared with manual PVs. PV, PSA, and PSAD were modeled using generalized additive models for location, scale, and shape (GAMLSS). RESULTS: Out of 1696 men, 1037 were analyzed (median age 46.00 years [IQR 38.00-56.00]). Median PV was 31.29 mL (5th-95th: 20.74-51.39), PSA 0.81 ng/mL (0.32-2.79), and PSAD 0.025 ng/mL² (0.011-0.071). PV and PSA increased progressively with age, whereas PSAD showed greater age-stability, peaking at 71 years, plateauing until 75, and then declining. Age-adjusted PSAD never exceeded 0.11 ng/mL², unlike PSA, which rose continuously. Body-mass index correlated positively with PV but inversely with PSAD; PSA showed a negative association with height. CONCLUSION: This study provides reference values and percentile curves for PV, PSA, and PSAD in men without prostate disease, along with an open-access calculator. PSAD showed age-stability, contrasting with continuously rising PSA. These reference values may help distinguish normal from pathological prostatic variation across age strata and inform PSAD thresholds in screening programs. KEY POINTS: Question Population-based reference values with long-term follow-up for PV, PSA, and PSAD are lacking, limiting the distinction between normal variation and disease-related changes. Findings Among 1037 men without prostate disease, 95th percentiles were: PV 51.39 mL, PSA 2.79 ng/mL, and PSAD 0.071 ng/mL². PSAD remained below 0.11 ng/mL² across all age ranges. Clinical relevance MRI-based percentiles for PV and PSAD may help identify normal variation, reducing unnecessary evaluations while supporting early detection of abnormalities. An open-access calculator enables personalized assessment for clinical and research purposes.

## 背景與目的
族群為基礎的 MRI 前列腺體積（PV）、前列腺特異抗原（PSA）與 PSA 密度（PSAD）長期追蹤參考值缺乏，導致難以區分正常生理變異與疾病相關變化。本研究旨在建立無前列腺病變的德國男性分層常模參考值，並納入年齡、體重指數（BMI）與身高等共變量，提供百分位曲線與開放存取計算器，以協助臨床篩檢與研究判讀。

## 方法
研究設計為前瞻性族群基礎隊列（Study of Health in Pomerania，德國），追蹤 10 年，初始 1696 名男性，排除已診斷前列腺癌、良性前列腺增生或下尿路症狀者，最終納入 1037 名（中位年齡 46 歲，IQR 38–56）。影像採骨盆 MRI，利用深度學習分割模型自動量測前列腺體積，並在測試集與人工分割體積比對驗證。PSAD 定義為 PSA 除以 MRI 體積。統計建模採用廣義加性模型（GAMLSS）同時擬合位置、尺度與形狀參數，將 PV、PSA、PSAD 分別以平滑函數建模為年齡、BMI、身高的函數，產出各年齡層的百分位曲線，並發布開放存取計算器供個別化評估。

## 結果
1037 名受試者中，PV 中位數 31.29 mL（5–95 百分位 20.74–51.39），PSA 中位數 0.81 ng/mL（0.32–2.79），PSAD 中位數 0.025 ng/mL²（0.011–0.071）。PV 與 PSA 隨年齡持續上升；PSAD 隨年齡相對穩定，於 71 歲達峰值，75 歲前維持平台期後下降，年齡調整後 PSAD 從未超過 0.11 ng/mL²。BMI 與 PV 呈正相關、與 PSAD 呈負相關；PSA 與身高呈負相關。95 百分位分別為 PV 51.39 mL、PSA 2.79 ng/mL、PSAD 0.071 ng/mL²。定性結論顯示 PSAD 年齡穩定性優於 PSA，參考值有助區分正常與病理變異。

## 限制與展望
研究對象僅為德國波美拉尼亞地區男性，種族與地理代表性有限，外推性需謹慎。排除標準可能導致較健康的子群體，影響參考值的普適性。深度學習分割僅在內部測試集與人工分割比較，缺乏外部驗證與多中心測試。GAMLSS 模型假設平滑關係，若真實關係呈現非平滑變化可能產生偏差。縱向隊列僅作橫斷面建模，未充分利用重複測量資訊。計算器基於當前模型，臨床應用前需在不同族群與篩檢方案中進行前瞻性驗證。
