# 論文 02：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-10-16
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。本研究旨在探討新生兒間充質幹細胞及其分泌組分對舒張功能的改善機制，並發現其能擴增調節性 T 細胞、降低發炎與纖維化。作者提出一種新的因果機器學習框架——變數重要性預測細胞功能（VIP），以識別驅動心臟功能改善的免疫路徑，並將調節性 T 細胞確立為治療標的。這項工作對於開發針對 HFpEF 的免疫調節策略具備重要意義。

## 方法
方法部分僅在摘要中提及核心概念，缺乏具體實驗設計、模型架構、訓練細節與推論流程的描述。根據摘錄可推斷：問題設定為給定 HFpEF 小鼠接受新生兒間充質幹細胞或其分泌組分治療後的免疫細胞表型與心臟功能指標，輸出為舒張功能改善的因果免疫路徑及關鍵細胞靶點。模型為一因果機器學習框架，命名為「變數重要性預測細胞功能」（VIP），旨在從高維免疫組學資料中推斷變數對細胞功能的因果重要性。核心模組可能包含：資料前處理（單細胞/流式細胞術資料標準化、批次效應校正）、特徵表示（基因表達、表面標記、細胞因子分泌）、因果發現演算法（如基於干預的變數重要性排序）、以及下游通路富集分析。訓練目標推測為最大化對舒張功能改善的解釋力，損失函數可能結合預測誤差與因果正則化項；最佳化策略未說明。推論階段將訓練好的 VIP 模型應用於治療組與對照組資料，輸出關鍵免疫通路與調節性 T 細胞的因果權重。與既有方法的關鍵差異在於引入因果推斷而非單純相關分析，並專注於細胞層級功能預測。然而，摘錄未提供具體架構圖、超參數、資料集規模、基線模型名稱或消融實驗細節，因此無法進一步驗證技術細節。

## 結果
摘錄未提供可驗證數字。定性結論顯示：新生兒間充質幹細胞及其分泌組分能顯著改善 HFpEF 小鼠的舒張功能，機制為擴增調節性 T 細胞、降低心臟發炎與纖維化；VIP 框架識別出驅動功能改善的因果免疫路徑，並將調節性 T 細胞確認為關鍵治療標的。

## 限制與展望
本文僅提供摘要層級資訊，缺乏實驗組數、樣本量、統計顯著性、基線療法比較、長期安全性、人類轉譯驗證等關鍵評估指標。VIP 框架的可重現性、超參數敏感度、因果推斷假設（如無未測量混雜因子）未經驗證。此外，僅在小鼠模型展示，臨床轉譯風險尚不明確。後續研究需補充完整方法細節、獨立隊列驗證、機制實驗（如 Treg 去除實驗）以及多中心臨床前試驗。
