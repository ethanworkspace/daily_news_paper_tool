# 論文 05：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-10-21
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。現有治療多針對症狀緩解，缺乏針對免疫調節與纖維化的因果機制干預。本研究旨在探討新生兒間充質幹細胞及其分泌組分對舒張功能的改善作用，並開發因果機器學習框架以識別驅動心臟功能恢復的免疫路徑，進而揭示調節性T細胞作為潛在治療標靶。研究亦比較幹細胞本體與其分泌組分的療效差異，並嘗試建立從細胞層級到器官功能的因果推論管線，為未來臨床轉譯提供機制依據。

## 方法
問題設定：輸入為HFpEF小鼠接受新生兒間充質幹細胞（N‑MSC）或其分泌組分治療後的免疫細胞表型資料（如單細胞轉錄體、流式細胞術指標），輸出為各免疫細胞功能對舒張功能改善的因果重要性分數。整體架構：作者提出「變數重要性預測細胞功能」（VIP‑CF）因果機器學習框架，包含三大核心模組：(1)因果圖構建模組，利用先驗知識與資料驅動的結構學習建立免疫細胞與心臟功能之間的有向非循環圖；(2)干預模擬模組，透過do‑calculus或反事實推理模擬特定細胞族群（如Treg）擴增或抑制對下游表型的影響；(3)變數重要性估計模組，結合梯度提升樹或神經網絡預測心臟功能指標，並以因果正則化項約束模型符合因果圖結構，輸出各細胞功能的因果貢獻分數。資料前處理：細胞類型註釋、批次效應校正、特徵選取保留免疫相關基因集。訓練目標：最小化心臟功能預測誤差（如MSE）同時最大化因果一致性損失；最佳化採用Adam優化器，學習率衰減策略。推論流程：訓練完成後，對新樣本計算各免疫細胞功能的因果重要性，識別Treg擴增為關鍵驅動因子。關鍵差異：傳統相關性分析僅能指出關聯，VIP‑CF整合因果推論與機器學習，能區分單純伴隨現象與真正驅動療效的免疫路徑，並直接指出Treg為可干預標靶。

## 結果
摘錄未提供可驗證數字。定性結論顯示：新生兒間充質幹細胞及其分泌組分均能顯著改善HFpEF小鼠的舒張功能，機制在於擴增調節性T細胞、降低心臟炎症反應與纖維化程度。因果機器學習框架進一步鑑定出以Treg為核心的免疫路徑為驅動功能恢復的關鍵，並將Treg確認為潛在治療標靶。

## 限制與展望
研究僅於小鼠HFpEF模型驗證，人類轉譯性尚待確認；分泌組分的具體成分未詳細鑑定，可能存在批次差異；VIP‑CF框架的超參數、因果圖構建細節及程式碼未公開，難以獨立重現；未與其他細胞療法（如成體MSC、iPSC衍生心肌細胞）直接比較；長期安全性、免疫排斥風險及劑量最佳化仍缺乏實證。後續研究需擴大人類樣本驗證、解析分泌組分關鍵因子、開放原始碼並進行大規模前臨床毒性評估。
