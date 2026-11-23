# 論文 02：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-11-05
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
心臟衰竭合併保留射出分數（HFpEF）缺乏有效的疾病修飾療法，臨床上亟需新治療策略。本研究旨在探討新生兒間充質幹細胞（neonatal MSCs）及其分泌組（secretome）對HFpEF小鼠心臟重塑的影響，並開發因果機器學習框架以解析免疫調節機制。現有療法多針對症狀緩解，鮮能逆轉病理重塑；本文透過實驗證實新生兒MSCs及其分泌組可擴增調節性T細胞（Tregs）、抑制發炎與纖維化，改善舒張功能，並提出「細胞功能變數重要性預測」（variable importance prediction for cellular function, VIP）因果機器學習框架，鑑別驅動心臟功能改善的因果免疫路徑，確立Tregs為治療標靶，填補HFpEF免疫調節機制與計算預測的雙重空白。

## 方法
本研究包含實驗生物學與計算因果推論兩大面向。實驗面：建立HFpEF小鼠模型，施予新生兒MSCs或其分泌組，量測舒張功能指標、Tregs擴增程度、發炎因子與纖維化標記；但摘錄未提供模型構建細節、給藥劑量、時間點、流式細胞術面板、組織學定量方法等關鍵實驗參數。計算面：提出新穎因果機器學習框架「細胞功能變數重要性預測」（VIP for cellular function），旨在從高維度免疫細胞數據中識別因果致病路徑。問題設定為：輸入為單細胞或群體層級的免疫細胞表型/功能變數，輸出為對心臟功能改善具因果影響力的關鍵免疫路徑與細胞亞型。核心機制為變數重要性預測結合因果推論，區別於傳統相關性分析，能推斷Tregs擴增對舒張功能改善的因果貢獻。然而，摘錄未揭露模型架構（如圖神經網絡、結構方程模型或反事實推論細節）、特徵表示方式（基因表達、表面標記、細胞因子分泌谱）、訓練目標與損失函數（如因果效應估計誤差、正則化項）、最佳化策略、推論流程（干預分布估計、敏感性分析），亦未說明與既有因果發現方法（如DoWhy、CausalML、GRN推論）的具體差異。依目前可取得資料，無法確認上述技術細節。

## 結果
作者報告新生兒MSCs及其分泌組均能顯著改善HFpEF小鼠舒張功能，機制在於擴增Tregs、降低發炎反應與減輕心肌纖維化。因果機器學習框架VIP成功鑑別出驅動心臟功能改善的因果免疫路徑，並將Tregs鎖定為關鍵治療標靶。摘錄未提供可驗證數字（如E/e'比值變化百分比、Tregs比例增幅、膠原蛋白體積分數、P值、效應量、樣本數），亦未列出基線療法比較組（如成體MSCs、載體對照、藥物治療）的量化結果。可觀察到的定性結論為：新生兒MSCs與分泌組療效相近，提示無細胞療法潛力；Tregs擴增為核心機制；因果ML框架可從複雜免疫數據中解析關鍵調節節點。

## 限制與展望
依目前可取得資料，主要限制包括：1) 僅在小鼠模型驗證，人類轉譯性未知；2) 實驗設計細節（模型誘導方式、給藥方案、對照組設置）未揭露，難以評估內部效度；3) 因果ML框架VIP的技術細節（架構、訓練數據規模、超參數、基線比較方法）缺失，無法判斷其泛化能力與穩健性；4) 未報告長期療效、安全性（如致瘤風險、免疫排斥）及劑量反應關係；5) 分泌組成分未鑑定，活性成分不明；6) 單一HFpEF模型（可能為代謝/高血壓雙重打擊模型）無法代表異質性臨床表型。後續研究需於大型動物與人類樣本驗證，完善VIP框架技術文檔並開源，並探討Tregs特異性調節策略（如低劑量IL-2、Tregs過繼移植）與分泌組成分解析。
