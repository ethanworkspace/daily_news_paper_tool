# 論文 03：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-11-20
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。現有治療多針對症狀緩解，缺乏能逆轉病理重塑的策略。本研究旨在探討新生兒間充質幹細胞（MSC）及其分泌組分對 HFpEF 小鼠心臟舒張功能的影響，並建立因果機器學習框架以揭示驅動功能改善的免疫路徑，進而確認調節性 T 細胞（Treg）作為潛在治療標靶。

## 方法
研究設計包含兩大部分：體內實驗與因果機器學習分析。體內實驗以 HFpEF 小鼠模型為輸入，分別給予新生兒 MSC 與其無細胞分泌組分（secretome），觀察舒張功能指標、心臟纖維化程度、發炎細胞因子表達以及 Treg 族群擴增情況。因果機器學習框架命名為「變數重要性預測細胞功能」（VIP‑CF），輸入為多維度免疫表型與心臟功能數據，輸出為各免疫變數對心功能改善的因果重要性分數。核心模組採用反事實推論與變數重要性估計，結合干預分布學習，識別出能因果驅動舒張功能恢復的免疫路徑。資料前處理細節、特徵表示方式、損失函數與最佳化策略在摘錄中未說明。推論流程為：先以實驗數據訓練模型，再計算各免疫細胞亞群的因果貢獻，最後將 Treg 標記為關鍵治療靶點。與傳統相關性分析不同，該框架強調因果關係而非單純關聯。

## 結果
作者報告新生兒 MSC 及其分泌組分顯著改善 HFpEF 小鼠的舒張功能，並伴隨 Treg 顯著擴增、發炎反應與纖維化減輕。因果機器學習框架進一步鑑定出驅動功能恢復的免疫路徑，並指出 Treg 為關鍵治療標靶。摘錄未提供可驗證的具體數值（如射出分數變化、Treg 比例變化、p 值等），僅能觀察到上述定性結論。

## 限制與展望
研究僅在小鼠 HFpEF 模型驗證，缺乏人類樣本或臨床數據支持；因果機器學習框架的訓練細節、超參數設定與外部驗證未揭露，難以評估其泛化能力；分泌組分的具體成分未詳細鑑定，機制解釋仍有缺口；後續需在大型動物模型與臨床前試驗中進一步確認療效與安全性。
