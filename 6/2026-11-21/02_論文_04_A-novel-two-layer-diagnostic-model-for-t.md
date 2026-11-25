# 論文 04：A novel two-layer diagnostic model for the differential diagnosis of acute febrile illnesses: Applying analytic hierarchy process and Bayesian-inspired evidence updating to real-world data.

- 日期：2026-11-21
- 來源層級：Tier 2
- 期刊/會議/來源：PLOS digital health
- Venue：PLOS digital health
- 發布時間：2026-11-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43077467/
- PDF：
- DOI：10.1371/journal.pdig.0001846
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1871（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Acute febrile illnesses (AFIs) remain one of the most pressing diagnostic challenges worldwide, particularly in low- and middle-income countries where overlapping symptoms and limited diagnostic capacity, together with high disease burden contribute to substantial morbidity and mortality. Conventional approaches often rely on empiric treatment or rapid diagnostic tests with suboptimal sensitivity and specificity, while modern machine learning solutions face issues of data scarcity and limited interpretability and generalizability. To address this gap, we propose a transparent and scalable two-layer diagnostic model to aid healthcare professionals in the differential diagnosis of AFIs. Data on symptom prevalence and biomarker ranges for ten AFIs were derived from the literature to build a knowledge base comprising ~2100 symptom and ~1500 biomarker data points. In the first layer of the model, symptom weights, derived by applying the Analytic Hierarchy Process (AHP) to pooled symptom prevalence, are used to generate initial disease scores, providing a preliminary ranking of AFIs. In the second layer, these rankings are refined via a Bayesian updating framework that employs pooled biomarker prevalence estimates derived using a Random Effects Model (REM). The model was validated across four publicly available real-world datasets encompassing diverse AFIs. The datasets originate from four different countries with populations totalling 2724 patients aged 0-74 years. Results demonstrated good performance, with mean top-3 diagnostic accuracy ranging from 70-91% when both symptom and biomarker layers were used. In this study, we demonstrate a promising approach that leverages pooled real-world data, thus offering a scalable, interpretable, and evidence-based tool for supporting differential diagnosis of AFIs in resource-limited healthcare settings.

## 背景與目的
急性發熱性疾病（AFI）在低中所得國家因症狀重疊、診斷資源有限與疾病負擔高，導致嚴重發病率與死亡率。傳統經驗性治療或快速檢測敏感度特異度不足，現有機器學習模型則面臨資料稀少、可解釋性差與泛化能力不足的問題。本研究旨在建立一個透明、可擴展的兩層診斷模型，結合文獻蒐集的症狀與生物標記流行率，輔助醫療人員進行 AFI 鑑別診斷，提供可解釋且具證據基礎的決策支援工具。

## 方法
方法包含兩層架構。第一層：從文獻彙整十種 AFI 的症狀流行率，建立約 2100 筆症狀資料點；採用層次分析法（AHP）對症狀流行率進行成對比較與權重計算，得到各症狀對各疾病的權重，進而依患者呈現症狀計算初始疾病分數，產生疾病初步排名。第二層：同樣從文獻蒐集生物標記範圍與流行率，約 1500 筆資料點；使用隨機效應模型（REM）對多研究的生物標記流行率進行合併估計，獲得合併後的條件機率；接著以貝氏更新機制，將第一層的初步排名作為先驗，結合患者實際生物標記檢測結果，計算後驗疾病機率並重新排序。模型輸入為患者症狀集合與可用生物標記數值，輸出為十種 AFI 的機率排名。訓練階段僅涉及文獻資料的統計合併與 AHP 權重推導，無傳統監督式學習；推論時依序執行症狀評分、AHP 加權、REM 合併機率、貝氏更新。關鍵差異在於結合 AHP 產生可解釋症狀權重，並以 REM 合併異質研究的生物標記證據，實現兩階段證據整合。

## 結果
模型於四個公開真實世界資料集（來自四國，共 2724 例，年齡 0–74 歲）驗證。當同時使用症狀與生物標記兩層時，平均 Top‑3 診斷準確率介於 70%–91% 之間。摘錄未提供各資料集單獨準確率、Top‑1 準確率、敏感度/特異度、消融實驗數值或統計顯著性檢定結果。定性上顯示兩層結合優於單層，且模型具可解釋性與可擴展性。

## 限制與展望
限制包括：(1) 知識庫僅基於文獻彙整，未納入本地流行病學實際分布，可能導致先驗偏誤；(2) AHP 權重依賴專家判斷與文獻報告品質，主觀性較高；(3) REM 合併假設研究間異質性為隨機效應，若研究數極少或異質性極大，合併估計不穩定；(4) 驗證資料集雖跨國但總樣本 2724 例，子群樣本較小，外部效度有待更大規模前瞻性研究確認；(5) 模型未處理缺失生物標記或症狀不完整的情況，實際部署需補充插補策略。後續研究可探索結合本地電子病歷資料微調權重、引入不確定性量化、以及在臨床工作流中進行前瞻性效益評估。
