# 論文 02：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-10-27
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法，現有治療多針對症狀而非病理機制，導致預後不佳。本研究旨在探討新生兒間充質幹細胞（MSC）及其分泌組分對舒張功能的改善機制，並發展一套因果機器學習框架——變數重要性預測細胞功能（VIP‑CF），以從高維免疫數據中識別驅動心臟功能恢復的關鍵免疫路徑，進而揭示調節性T細胞（Treg）作為潛在治療標靶。此工作填補了HFpEF免疫調節機制與治療靶點之間的知識鴻溝。

## 方法
問題設定：輸入為HFpEF小鼠接受新生兒MSC或其分泌組分治療後的多組學免疫數據（如單細胞RNA-seq、流式細胞術指標），輸出為舒張功能指標（E/e'、左心室剛度）與免疫細胞群體變化。整體架構包含三層：(1)資料前處理與特徵工程，將細胞亞型比例、細胞因子濃度、基因表達模組化為數值向量；(2)因果機器學習核心——變數重要性預測細胞功能（VIP‑CF），結合干預式因果推論（do‑calculus）與集成樹模型，估算每個免疫特徵對心臟功能改善的平均處理效應（ATE）；(3)結果解釋模組，輸出變數重要性排名與因果路徑圖。核心演算法機制：先以隨機森林擬合觀察數據，再利用傾向分數匹配或雙重稳健估計器修正混淆，計算各特徵在干預下的反事實預測差異，並以排列重要性衡量貢獻。訓練目標為最小化預測誤差（MSE）同時最大化因果效應估計的穩定性，採用交叉驗證選擇超參數。推論流程：新樣本經相同前處理後輸入VIP‑CF，獲得關鍵免疫驅動因子與其定量因果效應，指導後續實驗驗證。與既有相關性分析或單純預測模型不同，VIP‑CF明確區分相關與因果，並能處理高維共線性免疫特徵。

## 結果
作者報告：新生兒MSC及其分泌組分顯著改善HFpEF小鼠的舒張功能，並擴增調節性T細胞（Treg），降低心肌炎症與纖維化程度。VIP‑CF框架識別出以Treg擴增為核心的因果免疫路徑，並將Treg列為關鍵治療標靶。摘錄未提供可驗證數字（如具體E/e'變化、Treg比例增幅、p值），僅能觀察到定性結論：MSC與分泌組分均具療效，且免疫調節機制經因果模型驗證。

## 限制與展望
研究限制：(1)僅在單一HFpEF小鼠模型驗證，缺乏多模型與人類樣本外部驗證；(2)VIP‑CF因果假設依賴無未測混淆，實際免疫微環境可能存在隱性變數；(3)摘錄未揭露樣本數、測序深度、超參數設定，難以評估統計功效與模型穩健性；(4)MSC分泌組分成分未完全鑑定，轉譯臨床前需進一步純化與安全性評估。後續建議擴大隊列、整合多組學、進行前瞻性干預實驗。
