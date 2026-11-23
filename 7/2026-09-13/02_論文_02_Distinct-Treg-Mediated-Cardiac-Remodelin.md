# 論文 02：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-09-13
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法。新生兒間充質幹細胞（MSC）及其分泌組（secretome）在臨床前模型中展現改善舒張功能的潛力，但其精確的免疫調節機制與關鍵效應細胞類型尚未釐清。本研究旨在探討新生兒 MSC 及其分泌組對 HFpEF 小鼠心臟重塑的影響，並開發一套因果機器學習框架，以系統性鑑別驅動心臟功能改善的免疫路徑，進而鎖定調節性 T 細胞（Treg）作為治療標靶，填補現有療法與機制理解之間的鴻溝。

## 方法
問題設定與輸入輸出：以 HFpEF 小鼠模型為研究對象，輸入為新生兒 MSC 移植與其分泌組給藥兩種干預方式，輸出為心臟舒張功能指標、纖維化程度、發炎反應及免疫細胞群體變化（特別是 Treg 擴增）。 模型與系統整體架構：研究結合體內實驗干預與計算因果推論。實驗端執行 MSC/分泌組治療、心臟超音波評估、組織學染色與免疫表型分析；計算端建構「變數重要性預測細胞功能」（variable importance prediction for cellular function，VIP-CF）因果機器學習框架，整合多維度免疫數據以推斷因果路徑。 核心模組與演算法機制：VIP-CF 框架採用因果發現與變數重要性排序策略，從高維免疫特徵中識別對心臟功能改善具因果貢獻的關鍵免疫通路與細胞類型。具體演算法細節（如圖結構學習、反事實推理、正則化策略）於摘錄中未揭露。 資料前處理與表示：推測包含單細胞或流式細胞術免疫表型數據、心功能連續變量與組織學半定量評分，經標準化、批次效應校正後輸入模型，但具體特徵工程步驟未於摘錄說明。 訓練目標與最佳化：目標為最大化預測心臟功能改善的因果解釋力，損失函數可能結合預測誤差與因果圖稀疏性約束；優化器、學習率、早停條件等超參數未提供。 推論與執行流程：訓練完成後，將模型應用於實驗數據，輸出變數重要性排名，揭示 Treg 擴增為核心因果中介，並追溯上游分泌組成分與下游抗纖維化/抗發炎路徑。 與既有方法關鍵差異：傳統相關性分析無法區分因果與旁觀效應；VIP-CF 引入因果機器學習，直接從觀察數據推論干預免疫通路對表型的因果影響，提供可驗證的治療標靶假設。

## 結果
新生兒 MSC 及其分泌組顯著改善 HFpEF 小鼠舒張功能，並伴隨 Treg 顯著擴增、心肌發炎浸潤減少與纖維化面積縮小。VIP-CF 框架鑑定出 Treg 為介導心臟功能改善的關鍵因果細胞類型，並解析出相關免疫調節路徑。摘錄未提供可驗證數字（如 p 值、效應量、樣本數、統計顯著性），僅能觀察到定性結論：兩種療法均有效，且 Treg 為共同核心效應器。

## 限制與展望
依目前可取得資料，無法確認實驗樣本數、統計功效、長期療效追蹤、分泌組成分鑑定深度、VIP-CF 框架在獨立隊列或人類樣本上的外部驗證情況。潛在限制包括：僅限小鼠模型，轉譯至人類 HFpEF 異質性尚待證實；分泌組有效成分未解構，機制不夠精確；因果推論假設（如無未測混雜）可能違反；單一時間點終點評估，動態重塑過程未捕捉。後續研究需擴大人類樣本驗證、解析分泌組關鍵因子、進行長期安全性評估並改進因果模型泛化能力。
