# 論文 02：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-11-07
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。現有治療多針對症狀緩解，缺乏針對免疫調節與纖維化的機制性介入。本研究旨在探討新生兒間充質幹細胞（MSC）及其分泌組分對 HFpEF 小鼠舒張功能的影響，並建立因果機器學習框架以揭示驅動心臟功能改善的免疫路徑，進而確立調節性 T 細胞（Treg）作為潛在治療標靶。

## 方法
研究採用 HFpEF 小鼠模型，分別施予新生兒 MSC 及其無細胞分泌組分（secretome）進行治療。輸入為細胞療法與分泌組分劑量，輸出為心臟舒張功能指標（如 E/e' 比值）、組織學纖維化程度、發炎細胞子群變化與 Treg 數量。實驗流程包含：(1) 建立 HFpEF 模型並隨機分組；(2) 靜脈注射 MSC 或給予 secretome；(3) 於預設時間點進行超音波心臟檢查、流式細胞術分析免疫細胞組成、免疫組化與 Masson 染色評估纖維化；(4) 建立名為「變數重要性預測細胞功能」（variable importance prediction for cellular function，VIP‑CF）的因果機器學習框架，輸入多維免疫表型與功能讀數，輸出對舒張功能改善具因果貢獻的免疫路徑與關鍵細胞類型。核心模組包含特徵選取、反事實推論與變數重要性排序，損失函數結合預測誤差與因果正則化項。推論階段對新樣本輸入免疫特徵，輸出預測的功能改善機率與關鍵驅動因子。與既有方法的關鍵差異在於引入因果推斷而非單純相關分析，並聚焦於細胞層級的功能變數重要性。摘錄未提供具體模型架構、超參數、訓練資料規模或優化策略細節。

## 結果
作者報告 MSC 及其 secretome 均能顯著改善 HFpEF 小鼠的舒張功能，並伴隨 Treg 顯著擴增、發炎細胞浸潤減少與心肌纖維化減輕。VIP‑CF 框架識別出以 Treg 為核心的因果免疫路徑，進一步支持 Treg 為治療標靶。摘錄未提供可驗證的具體數值（如 p 值、效應量、樣本數），僅能觀察到定性結論：治療組舒張功能改善、免疫微環境重塑且機器學習揭示 Treg 關鍵角色。

## 限制與展望
研究僅在單一 HFpEF 小鼠模型驗證，缺乏多模型、大型動物或人類樣本的外部驗證。MSC 與 secretome 的劑量、給藥時程、長期安全性未詳細說明。因果機器學習框架的架構、訓練資料組成、超參數設定與泛化能力未公開，難以評估其可重現性與臨床轉譯潛力。此外，未探討 Treg 擴增的具體分子機制、可能的副作用或免疫抑制風險。後續研究需擴大樣本、進行機制解析、公開模型細節並評估臨床可行性。
