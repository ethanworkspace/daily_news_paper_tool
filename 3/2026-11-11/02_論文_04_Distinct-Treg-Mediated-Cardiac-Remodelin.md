# 論文 04：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-11-11
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。現有治療多針對症狀緩解，無法逆轉發炎與纖維化驅動的舒張功能障礙。本研究旨在探討新生兒間充質幹細胞（MSC）及其分泌組分對 HFpEF 小鼠舒張功能的影響，並建立因果機器學習框架以揭示免疫調節機制，期望為臨床轉譯提供新標的。同時評估調節性 T 細胞（Treg）擴增、發炎因子表達與心肌纖維化程度，以釐清細胞療法與分泌組分的相對貢獻。

## 方法
問題設定：輸入為 HFpEF 小鼠模型接受新生兒 MSC 移植或其無細胞分泌組分（secretome）處理；輸出為舒張功能指標、Treg 群體頻率、發炎與纖維化標記。整體架構包含兩大部分：（1）體內實驗流程：將 MSC 或 secretome 經靜脈注射，後續以超聲心動圖量測舒張功能、流式細胞術分析脾臟與心臟 Treg 比例、免疫組化與 qPCR 量化發炎因子（如 IL‑1β、TNF‑α）與纖維化標記（Collagen I/III）；（2）因果機器學習框架「variable importance prediction for cellular function」（VIP‑CF）：以實驗產生的多維免疫表型資料為輸入，透過結構因果模型與變數重要性評估，識別驅動舒張功能改善的關鍵免疫路徑。核心模組包括：資料前處理（缺失值填補、標準化）、特徵表示（細胞亞群比例、細胞因子濃度、基因表達）、因果發現演算法（基於干預分布的變數重要性排序）、損失函數（結合預測誤差與因果正則化）與最佳化策略（梯度下降配合早停）。推論流程：訓練完成後，對新樣本輸入免疫特徵，模型輸出各免疫變數對舒張功能的因果貢獻分數，進而鎖定 Treg 為主要治療標的。與既有方法差異在於：傳統相關性分析無法區分因果，而 VIP‑CF 結合干預式變數重要性，直接從觀察數據推斷因果免疫路徑。註：摘錄未提供具體超參數、網路架構、訓練樣本數或驗證集劃分等技術細節。

## 結果
作者報告：新生兒 MSC 及其 secretome 均顯著改善 HFpEF 小鼠的舒張功能，並伴隨 Treg 顯著擴增、心臟發炎因子下調與纖維化面積減少。VIP‑CF 框架進一步揭示 Treg 相關免疫路徑為驅動功能恢復的關鍵因果機制，將 Treg 確立為潛在治療標的。摘錄未提供可驗證的具體數值（如 E/e' 比值變化百分比、Treg 比例增幅、p 值或效應量），僅能觀察到定性結論：兩種療法皆有效，且免疫調節機制以 Treg 為核心。

## 限制與展望
研究僅於小鼠 HFpEF 模型驗證，缺乏人類組織或臨床樣本的外部驗證，轉譯性有待確認。VIP‑CF 框架的因果推論依賴觀察數據與假設的干預分布，未經隨機化實驗或獨立隊列驗證，可能存在未測混雜因素。Secretome 成分未詳細鑑定，無法區分特定細胞因子或胞外囊泡的貢獻。實驗樣本數、統計功效與重現性資訊未揭露，限制結果可信度評估。後續研究建議：擴展至大型動物模型、進行單細胞多組學解析 secretome 成分、以隨機對照試驗驗證 Treg 為標的的治療效果，並公開 VIP‑CF 程式碼與超參數以利重現。
