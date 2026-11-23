# 論文 02：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-09-29
- 來源層級：Tier 1
- 期刊/會議/來源：JACC. Basic to translational science
- Venue：JACC. Basic to translational science
- 發布時間：2026-11-21T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43067120/
- PDF：
- DOI：10.1016/j.jacbts.2026.101751
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：479（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Heart failure with preserved ejection fraction lacks effective disease-modifying therapies. We show that neonatal mesenchymal stem cells and their secretome improve diastolic function by expanding regulatory T cells, reducing inflammation and fibrosis. Our new causal machine learning framework, variable importance prediction for cellular function, identified causal immune pathways driving cardiac functional improvement and revealed regulatory T cells as a therapeutic target.

## 背景與目的
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法，現有治療多針對症狀而非免疫發炎機制。本研究旨在探討新生兒間充質幹細胞（MSC）及其分泌組對舒張功能的改善效果，並開發因果機器學習框架「細胞功能變數重要性預測」（VIP for cellular function），以鑑別驅動心臟功能改善的因果免疫路徑，進而揭示調節性T細胞（Treg）作為治療標靶。貢獻在於同時提供實驗證據與計算方法，證實MSC與分泌組透過擴增Treg、減少發炎與纖維化來改善舒張功能，並建立可解釋的因果推論工具。

## 方法
問題設定：輸入為HFpEF小鼠接受新生兒MSC或其分泌組治療後的心臟免疫細胞表型（如流式細胞術）、基因表達（如單細胞RNA-seq）及心臟功能指標（如超聲心動圖舒張參數）；輸出為各免疫細胞亞群對心臟功能改善的變數重要性分數與因果路徑。模型整體架構：作者提出一套因果機器學習框架，名為「細胞功能變數重要性預測」，核心在於從觀察性資料中推斷干預分布，而非單純相關分析。核心模組推測包含：資料整合層（多模態免疫與功能資料對齊）、因果圖推論層（利用條件獨立性檢定或干預演算法學習因果結構）、變數重要性估計層（結合反事實推理計算各細胞功能對預後的因果貢獻）。資料前處理：摘錄未詳細說明，但可推測包含單細胞資料品質控制、批次效應校正、細胞亞群註解、功能指標標準化。訓練目標與損失函數：摘錄未提供具體損失函數、最佳化策略或超參數設定。推論流程：訓練完成後，將模型應用於治療組與對照組資料，輸出關鍵免疫路徑與Treg的重要性排序，進而指導實驗驗證。與既有方法差異：傳統相關分析無法區分因果與混雜，本框架聲稱能識別因果免疫路徑，但架構細節、理論保證（如可識別性條件）及基線比較方法（如隨機森林、因果森林、DoWhy等）均未在摘錄中揭露。依目前可取得資料，無法確認模型具體數學形式、訓練算法與計算複雜度。

## 結果
作者報告新生兒MSC及其分泌組在HFpEF小鼠模型中顯著改善舒張功能，機制為擴增調節性T細胞、降低發炎反應與纖維化程度。因果機器學習框架進一步鑑別出驅動心臟功能改善的因果免疫路徑，並指認Treg為關鍵治療標靶。摘錄未提供可驗證數字（如射出分數變化量、纖維化面積百分比、Treg擴增倍數、統計顯著性p值等），僅能觀察到定性結論：MSC與分泌組均具療效，且計算方法能揭示因果免疫機制。

## 限制與展望
研究僅於小鼠HFpEF模型驗證，人類轉譯性未知；因果機器學習框架的架構細節、超參數、訓練資料規模、基線比較方法均未揭露，難以評估其泛化能力與因果推論可靠性；實驗缺乏與現有藥物療法（如SGLT2抑制劑）的直接比較；未探討MSC移植的長期安全性、免疫排斥或腫瘤風險；分泌組成分未完全鑑定，機制細節仍待釐清。後續研究需於大型動物與臨床樣本驗證，並公開模型碼與資料以利重現。
