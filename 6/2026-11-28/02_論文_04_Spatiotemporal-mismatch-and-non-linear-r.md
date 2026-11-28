# 論文 04：Spatiotemporal mismatch and non-linear relationships between ecological quality and carbon storage in the Yellow River Delta coastal wetlands (1985-2020).

- 日期：2026-11-28
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：Environmental research
- Venue：Environmental research
- 發布時間：2026-11-24T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43078175/
- PDF：
- DOI：10.1016/j.envres.2026.126271
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2001（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Understanding the coupling relationship between ecological quality and ecosystem carbon storage (CS) is crucial for effective coastal wetland management. Across eight discrete observation years from 1985 to 2020 in the Yellow River Delta (YRD), we evaluated InVEST-modeled CS alongside a modified Remote Sensing Ecological Index (RSEI). A coupling coordination degree (CCD) model was employed to quantify their joint status, while a four-quadrant classification scheme identified the bidirectional spatial mismatches between them. Among pixels with continuous temporal records, CS trends were predominantly negative, whereas RSEI trends were predominantly positive. Both high-RSEI/low-CS and low-RSEI/high-CS patterns emerged, revealing marked spatial divergence between superior surface ecological conditions and high modeled carbon stocks. Deterministically, the "Good" coordination class comprised the largest spatial extent across all eight observations, whereas approximately 10% of valid pixels remained in the lowest coordination class at both temporal endpoints. An explainable machine learning framework combining XGBoost with Shapley additive explanations (SHAP) uncovered distinct non-linear associations governing predicted CCD. In the full model, the normalized difference vegetation index (NDVI)-an essential RSEI component-exhibited the highest mean absolute contribution, with sensitivity further validated against a reduced model excluding four RSEI-related covariates. Specifically, the marginal SHAP contribution of NDVI crossed zero near 0.22, while that of land surface temperature transitioned across zero around 30 °C. Furthermore, the contribution of distance-to-water peaked locally near 1.4 km, and that of population density declined steeply across low-density ranges. Ultimately, these spatial mappings delineate priority target locations for paired field validation of surface conditions and carbon stocks, providing actionable empirical support for coastal zone planning.

## 背景與目的
本研究旨在探討黃河三角洲沿海濕地中生態品質與生態系統碳儲存之耦合關係。現有研究多單獨評估碳儲存或生態指數，缺乏時空耦合與非線性驅動機制的量化分析，導致管理決策難以兼顧表層生態狀況與地下碳庫。本文利用 1985‑2020 年八個觀測年份的遙感資料，結合 InVEST 模型估算碳儲存與修正後的遠感生態指數（RSEI），透過耦合協調度（CCD）模型與四象限分類揭示雙向空間錯配，並引入 XGBoost‑SHAP 可解釋機器學習框架，量化關鍵驅動因子的非線性邊際貢獻，為濕地規劃提供實證依據。

## 方法
問題設定：輸入為多時相遙感影像衍生的 NDVI、地表溫度（LST）、水體距離、人口密度等共變量，以及 InVEST 模型輸出的像素級碳儲存（CS）與修正後 RSEI；輸出為耦合協調度（CCD）數值與四象限錯配類別。整體架構分三階段：(1) 碳儲存估算——以土地利用、土壤有機碳密度等參數驅動 InVEST 模型，產生連續 CS 圖層；(2) 生態品質指數——計算 NDVI、LST、濕度、建設用地比例四項指標，經標準化加權合成為修正 RSEI；(3) 耦合協調度與錯配識別——依 CCD 公式計算 CS 與 RSEI 的協調度，再以四象限法將像素歸類為高 RSEI/低 CS、低 RSEI/高 CS 等類別。核心模組為可解釋機器學習：以 XGBoost 回歸預測 CCD，特徵為上述四項 RSEI 相關變量與社經變量；損失函數採用預設平方誤差，透過梯度提升迭代優化。推論流程為：依序輸入特徵 → XGBoost 預測 CCD → SHAP 計算各特徵邊際貢獻 → 繪製空間熱力圖。關鍵差異在於將物理模型（InVEST）與遙感指數（RSEI）耦合，並以 SHAP 揭示非線性閾值（如 NDVI 0.22、LST 30 °C、水體距離 1.4 km），超越傳統線性相關或單一指標評估。

## 結果
主要結果顯示：在具備完整時間序列的像素中，CS 呈負趨勢為主，RSEI 則以正趨勢為主，兩者出現顯著空間分歧，同時存在高 RSEI/低 CS 與低 RSEI/高 CS 兩類錯配。八個觀測期皆以「良好」協調等級佔據最大面積，而約 10 % 有效像素在首尾年份均維持最低協調等級。XGBoost‑SHAP 分析指出 NDVI 為全模型平均絕對貢獻最高的特徵，其邊際 SHAP 值在 NDVI≈0.22 附近穿越零點；LST 在約 30 °C 穿越零點；水體距離在 1.4 km 處呈局部峰值；人口密度在低密度區間貢獻急劇下降。摘錄未提供模型預測精度（如 RMSE、R²）等可驗證數字。

## 限制與展望
研究限制包括：(1) 僅八個離散年份，無法捕捉年際變異與極端事件；(2) CS 為 InVEST 模擬值，缺乏實地碳庫驗證，可能存在系統性偏差；(3) RSEI 為修正版本，權重設定與指標選擇具主觀性；(4) CCD 模型假設雙向耦合線性加權，未考慮滯後效應；(5) XGBoost‑SHAP 僅提供相關性解釋，因果推論仍待實驗證實；(6) 空間解析度受限於遙感影像，細尺度異質性可能被平滑。未來需結合長期實地量測、動態耦合模型與因果推斷方法，擴展至其他三角洲驗證泛化能力。
