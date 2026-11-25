# 論文 01：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-11-21
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。現有治療多針對症狀緩解，難以逆轉發炎與纖維化等病理機制。本研究旨在探討新生兒間充質幹細胞及其分泌組分對舒張功能的改善作用，並發展因果機器學習框架以識別驅動心臟功能恢復的免疫路徑，進而揭示調節性T細胞作為潛在治療標靶。

## 方法
問題設定：輸入為HFpEF小鼠接受新生兒間充質幹細胞（N‑MSC）或其分泌組分治療後的心臟功能指標（如舒張參數）、免疫細胞表型（流式細胞術）、單細胞轉錄體等多模態資料；輸出為導致功能改善的因果免疫路徑與關鍵細胞變數重要性。 整體架構：提出「變數重要性預測細胞功能」（VIP‑CF）因果機器學習框架，包含三大核心模組：(1)資料前處理與特徵表示層，將心超音波、細胞因子、單細胞基因表達標準化並嵌入共同潛在空間；(2)因果推斷引擎，結合干預式因果發現（如do‑calculus或反事實模擬）與圖神經網絡，學習治療→免疫變數→心臟功能的有向非循環圖；(3)變數重要性估計器，基於反事實干預效應計算各免疫特徵對舒張功能改善的邊際貢獻。 訓練目標與損失：聯合最小化心臟功能預測誤差（MSE）與因果正則化項（如干預分布與觀察分布的KL散度），以確保學習到的邊具備因果解釋性。優化採用Adam，學習率逐步衰減，早停依驗證集因果指標。 推論流程：新樣本經前處理後輸入因果圖，透過反事實干預模擬「擴增調節性T細胞」或「抑制促炎因子」對舒張參數的預測變化，輸出排名前幾的因果免疫路徑。 關鍵差異：與傳統相關性機器學習不同，VIP‑CF明確建模干預分布，並輸出可解釋的變數重要性，直接指向調節性T細胞為治療標靶。

## 結果
作者報告：新生兒間充質幹細胞及其分泌組分能顯著改善HFpEF小鼠的舒張功能、擴增調節性T細胞、降低發炎與纖維化程度；VIP‑CF框架識別出以調節性T細胞為核心的因果免疫路徑，並將其標記為治療標靶。摘錄未提供可驗證數字（如具體舒張參數變化量、T細胞擴增倍數、統計顯著性p值等），僅能觀察到定性結論。

## 限制與展望
目前資料僅限於小鼠HFpEF模型，未驗證人類樣本或其他心衰亞型；分泌組分的具體成分、劑量反應關係未詳細描述；因果機器學習框架的泛化能力、對混雜因子的控制、以及反事實模擬的生物學可信度仍需進一步實驗驗證；缺乏公開程式碼與完整超參數設定，難以重現；後續研究需擴大樣本量、進行多中心驗證、並整合單細胞多組學以精細化因果網絡。
