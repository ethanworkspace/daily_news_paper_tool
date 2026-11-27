# 論文 02：Reference values for PSA, PSA density, and MRI prostate volume in healthy German men.

- 日期：2026-09-26
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
- 配對 Repo：

## 摘要
OBJECTIVES: To establish stratified normative reference values for MRI-derived prostate volume (PV), prostate-specific antigen (PSA), and PSA density (PSAD) in German men with no known prostate pathologies, accounting for age, body-mass index, and height. MATERIALS AND METHODS: This study included men from the prospective population-based Study of Health in Pomerania, Germany, with 10 years of follow-up. Men with diagnosed prostate cancer, benign prostatic hyperplasia, or lower urinary tract symptoms were excluded to derive reference values unaffected by disease or interventions. PV and PSAD were obtained from pelvic MRI using deep-learning segmentation. In a test set, segmentation-derived volumes were compared with manual PVs. PV, PSA, and PSAD were modeled using generalized additive models for location, scale, and shape (GAMLSS). RESULTS: Out of 1696 men, 1037 were analyzed (median age 46.00 years [IQR 38.00-56.00]). Median PV was 31.29 mL (5th-95th: 20.74-51.39), PSA 0.81 ng/mL (0.32-2.79), and PSAD 0.025 ng/mL² (0.011-0.071). PV and PSA increased progressively with age, whereas PSAD showed greater age-stability, peaking at 71 years, plateauing until 75, and then declining. Age-adjusted PSAD never exceeded 0.11 ng/mL², unlike PSA, which rose continuously. Body-mass index correlated positively with PV but inversely with PSAD; PSA showed a negative association with height. CONCLUSION: This study provides reference values and percentile curves for PV, PSA, and PSAD in men without prostate disease, along with an open-access calculator. PSAD showed age-stability, contrasting with continuously rising PSA. These reference values may help distinguish normal from pathological prostatic variation across age strata and inform PSAD thresholds in screening programs. KEY POINTS: Question Population-based reference values with long-term follow-up for PV, PSA, and PSAD are lacking, limiting the distinction between normal variation and disease-related changes. Findings Among 1037 men without prostate disease, 95th percentiles were: PV 51.39 mL, PSA 2.79 ng/mL, and PSAD 0.071 ng/mL². PSAD remained below 0.11 ng/mL² across all age ranges. Clinical relevance MRI-based percentiles for PV and PSAD may help identify normal variation, reducing unnecessary evaluations while supporting early detection of abnormalities. An open-access calculator enables personalized assessment for clinical and research purposes.

## 背景與目的
本研究旨在建立無前列腺疾病德國男性的 MRI 衍生前列腺體積（PV）、前列腺特異抗原（PSA）與 PSA 密度（PSAD）的分層常模參考值，並考量年齡、體重指數（BMI）與身高的影響。現有文獻缺乏長期追蹤的族群基準值，導致難以區分正常生理變異與疾病相關變化，進而影響篩檢閾值的制定。研究利用前瞻性族群隊列「Study of Health in Pomerania」，排除已診斷前列腺癌、良性前列腺增生或下尿路症狀者，以深度學習分割獲取 PV 與 PSAD，並以 GAMLSS 建立百分位曲線，提供開放存取計算器供臨床與研究使用。

## 方法
問題設定與輸入輸出：輸入為盆腔 MRI 影像與對應的 PSA 數值、年齡、BMI、身高；輸出為個體化的 PV、PSA、PSAD 參考百分位。 整體架構：1) 從 1696 名參與者中依排除標準篩選 1037 名無疾病男性；2) 以深度學習模型對 MRI 進行前列腺分割，獲得體積；3) 於測試集將分割體積與人工標註體積比較驗證；4) 將 PV、PSA、PSAD 分別以廣義加性模型（GAMLSS）建模，納入年齡、BMI、身高為平滑項，估計位置、尺度與形狀參數，產生各年齡層的百分位曲線；5) 開發開放存取計算器供查詢。 核心模組：深度學習分割（架構、損失函數、訓練細節未於摘錄說明），GAMLSS 統計建模（採用適當分布族，如 Box‑Cox t 或 Box‑Cox power exponential，具體分布未提及）。 資料前處理：MRI 影像標準化、前列腺區域裁切；PSA 數值對數轉換（若有）未明確提及。 訓練目標與最佳化：分割模型以 Dice 係數或類似指標優化；GAMLSS 以最大似然估計參數。 推論流程：新受試者輸入 MRI 影像與臨床變量 → 分割模型產生 PV → 計算 PSAD = PSA / PV → 代入 GAMLSS 模型獲得對應百分位。 與既有方法差異：首次結合族群基礎 MRI 深度學習分割與 GAMLSS 多變量參考建模，並提供年齡、BMI、身高同時調整的開放計算器。

## 結果
分析 1037 名男性（中位年齡 46 歲，IQR 38–56）。中位 PV 31.29 mL（5–95 百分位 20.74–51.39），中位 PSA 0.81 ng/mL（0.32–2.79），中位 PSAD 0.025 ng/mL²（0.011–0.071）。PV 與 PSA 隨年齡持續上升；PSAD 隨年齡相對穩定，於 71 歲達峰值，維持至 75 歲後下降，年齡調整後 PSAD 從未超過 0.11 ng/mL²。BMI 與 PV 呈正相關、與 PSAD 呈負相關；PSA 與身高呈負相關。95 百分位值分別為 PV 51.39 mL、PSA 2.79 ng/mL、PSAD 0.071 ng/mL²。摘錄未提供可驗證的分割模型 Dice 分數、GAMLSS 擬合優度指標或外部驗證數字。

## 限制與展望
研究對象限於德國波美拉尼亞地區男性，種族與地理代表性有限；排除標準可能導致選擇偏誤，無法推廣至有症狀或高風險族群。深度學習分割僅於內部測試集與人工標註比較，缺乏外部獨立驗證與多中心影像異質性測試。GAMLSS 模型假設分布族與平滑項形式未詳細揭露，可能影響極端百分位估計準確性。未評估參考值對臨床決策（如活檢率、過度診斷）的實際影響。後續研究需進行多族群外部驗證、整合縱向追蹤結果、探討不同 MRI 序列與分割架構對參考值穩健性的影響。
