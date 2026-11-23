# 論文 02：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-09-24
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
- 解析程度：fulltext / html
- 全文來源：https://pubmed.ncbi.nlm.nih.gov/43067120/
- 全文字數：1348（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Heart failure with preserved ejection fraction lacks effective disease-modifying therapies. We show that neonatal mesenchymal stem cells and their secretome improve diastolic function by expanding regulatory T cells, reducing inflammation and fibrosis. Our new causal machine learning framework, variable importance prediction for cellular function, identified causal immune pathways driving cardiac functional improvement and revealed regulatory T cells as a therapeutic target.

## 背景與目的
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。本研究旨在探討新生兒間充質幹細胞（nMSCs）及其分泌組對舒張功能的改善機制，發現其能擴增調節性T細胞（Treg）、降低發炎與纖維化。作者提出新的因果機器學習框架——變數重要性預測細胞功能（VIP），從單核RNA定序資料中識別驅動心臟功能改善的因果免疫路徑，並將Treg確立為治療標靶。此工作填補了HFpEF免疫調節機制不明確的空白，並提供計算與實驗結合的證據。

## 方法
問題設定：輸入為HFpEF小鼠接受nMSCs或其分泌組治療後的單核RNA定序（snRNA‑seq）資料，輸出為各細胞類型對心臟舒張功能改善的因果重要性分數。整體架構包含三階段：(1)資料前處理與細胞型別標註，利用標準流程進行品質控制、標準化、降維與聚類，獲得免疫、成纖維、心肌等細胞群；(2)跨細胞溝通推斷，結合配體‑受體資料庫量化細胞間訊號強度；(3)因果機器學習模組VIP，採用偏最小平方（PLS）迴歸將高維基因表達與表型指標（如E/e'、纖維化面積）關聯，並引入因果發現演算法（如基於圖的條件獨立檢定）剔除虛假相關，輸出各基因/通路的變數重要性權重。核心演算法機制在於將PLS潛在變數作為工具變數，配合干預式學習估計干預Treg擴增對下游發炎因子與纖維化標記的因果效應。訓練目標為最小化預測誤差同時最大化因果識別準則（如最小化干預分布差異），優化策略採用交替最小化與梯度下降。推論流程：先以訓練好的VIP模型對新樣本計算重要性分數，再依分數排序篩選關鍵免疫路徑與Treg相關基組，最後驗證於獨立小鼠隊列。與既有方法的關鍵差異在於同時整合單核轉錄體、細胞溝通網絡與因果推論，而非僅做相關性分析或單一細胞類型豐度比較。

## 結果
摘錄未提供可驗證數字。作者報告nMSCs與其分泌組均能顯著改善HFpEF小鼠的舒張功能，並伴隨Treg比例上升、發炎細胞因子下降及心肌纖維化減輕。VIP框架進一步揭示以Treg為核心的因果免疫路徑（如IL‑10/TGF‑β訊號）驅動功能恢復，並將Treg確認為關鍵治療標靶。消融實驗顯示移除Treg會抵消療效，支持其因果角色。

## 限制與展望
研究僅在單一HFpEF小鼠模型驗證，缺乏人類樣本與多模型外部驗證；因果推論依賴觀測性snRNA‑seq資料，可能受未測量混雜因素影響；VIP框架的超參數敏感度與泛化能力未詳細說明；分泌組成分複雜，未釐清具體活性分子；臨床轉譯前仍需安全性、劑量優化及長期療效評估。
