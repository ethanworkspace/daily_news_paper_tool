# 論文 02：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-10-14
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。現有治療多針對症狀緩解，缺乏針對免疫調節與纖維化的因果機制介入。本研究旨在探討新生兒間充質幹細胞（neonatal MSC）及其分泌組分對 HFpEF 小鼠舒張功能的改善效果，並開發因果機器學習框架「變數重要性預測細胞功能」（VIP‑CF），以識別驅動心臟功能恢復的免疫路徑，進而揭示調節性 T 細胞（Treg）作為潛在治療標靶。

## 方法
問題設定：輸入為 HFpEF 小鼠接受新生兒 MSC 或其分泌組分治療後的多維免疫表型資料（如流式細胞術、細胞因子濃度、組織學纖維化指標等），輸出為舒張功能指標（E/e'、左心室充盈壓）的改善程度。模型整體架構：作者提出因果機器學習框架 VIP‑CF，採用變數重要性評估結合反事實推論，以識別對心臟功能改善具因果影響的免疫特徵。核心模組包含（1）特徵工程：將免疫細胞比例、分泌因子濃度、纖維化面積等標準化為數值向量；（2）因果發現層：利用基於圖的因果發現演算法（如 PC 或 GES）構建免疫網絡圖；（3）變數重要性預測層：結合集成學習（隨機森林或梯度提升）與干預效應估計，計算每個免疫變數對預測目標的平均處理效應。資料前處理：缺失值插補、批次效應校正、主成分降維以緩解高維共線性。訓練目標：最小化預測誤差（均方誤差）同時最大化因果效應估計的穩定性，採用交叉驗證選擇超參數。推論流程：輸入新樣本免疫特徵，經因果圖過濾後輸入重要性模型，輸出關鍵驅動因子排序與預測的功能改善幅度。與既有方法的關鍵差異：傳統相關性分析僅能揭示關聯，VIP‑CF 引入因果推論並量化干預效應，直接指向 Treg 擴增為機制核心。註：摘錄未提供具體演算法細節、損失函數形式、超參數設定或程式碼實作，以上描述僅依摘要推斷。

## 結果
主要實驗結果顯示，新生兒 MSC 及其分泌組分均能顯著改善 HFpEF 小鼠的舒張功能，並伴隨 Treg 細胞比例顯著上升、發炎細胞因子下降與心肌纖維化面積減少。VIP‑CF 分析進一步確認 Treg 擴增為驅動功能恢復的關鍵因果路徑。摘錄未提供可驗證的具體數值（如 E/e' 變化百分比、Treg 比例增幅、p 值或效應量），故無法呈現定量比較。定性結論為：MSC 與分泌組分效果相近，免疫調節機制以 Treg 為核心。

## 限制與展望
研究限制包括：僅在單一 HFpEF 小鼠模型驗證，缺乏多模型、大樣本及人類樣本的外部驗證；因果機器學習框架的具體演算法、超參數與程式碼未公開，難以重現與擴展；免疫表型測量僅涵蓋有限面板，可能遺漏其他關鍵細胞亞群；治療劑量、給藥時程與長期安全性未詳細報告。潛在風險為過度解讀因果推論結果，若混雜因子未充分控制可能產生假陽性標靶。後續研究建議：在多中心、多物種隊列中驗證 VIP‑CF；公開完整模型與資料以利獨立重現；結合單細胞轉錄體擴展免疫特徵空間；評估 MSC 分泌組分的成分組成與劑量反應關係。
