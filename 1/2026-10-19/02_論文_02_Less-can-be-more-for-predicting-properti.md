# 論文 02：Less can be more for predicting properties with large language models

- 日期：2026-10-19
- 來源層級：Tier 1
- 期刊/會議/來源：Nature Computational Science
- Venue：Nature Computational Science
- 發布時間：2026-10-12T00:00:00+00:00
- URL：https://doi.org/10.1038/s43588-026-01045-2
- PDF：https://www.nature.com/articles/s43588-026-01045-2.pdf
- DOI：10.1038/s43588-026-01045-2
- arXiv：2406.17295
- 影響指標：2yr_mean_citedness=12.77, h_index=93, i10_index=460 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Computational Science
- 引用數：34
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2406.17295
- 全文字數：105822（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/lamalab-org/MatText
- 配對 Repo：lamalab-org/MatText

## 摘要
Predicting properties from coordinate–category data—sets of vectors paired with categorical information—is fundamental to computational science, manifesting in materials science as predicting formation energies or elastic moduli from crystal structures. While large language models (LLMs) have increasingly been applied to such tasks, optimal strategies for achieving reliable predictions remain elusive. Here we report fundamental limitations in LLM’s ability to learn from coordinate information in coordinate–category data. Through systematic experiments using synthetic datasets with tunable coordinate and category contributions, and a comprehensive benchmarking framework (MatText), we find that LLMs consistently fail to capture coordinate information while excelling at category patterns. This geometric blindness persists regardless of model size (up to 70 billion parameters), dataset scale (up to 2 × 10 6 structures) or text representation strategy. For material property prediction tasks dominated by structural effects, specialized geometric architectures consistently outperform LLMs, as evidenced by a clear ‘Graph Neural Network Language Model (GNN-LM) wall’ in performance benchmarks. Our analysis provides concrete guidelines for architecture selection in scientific machine learning.

## 背景與目的
本研究探討大型語言模型（LLM）在座標-類別資料（如晶體結構的原子位置與元素類型）上預測材料性質的能力。現有研究多將結構編碼為文本並微調 LLM，但缺乏系統性理解其對座標資訊的學習極限。作者指出 LLM 在處理幾何關係時存在根本性盲區，這對材料設計與發現至關重要。研究使用可調參數 α 的合成資料集與 MatText 基準平台，系統性比較 LLM、n-gram 與圖神經網路在座標與類別貢獻下的表現，揭示幾何盲區並提供實務選型建議。本文目標為量化 LLM 對座標與類別資訊的學習差距，並提出架構選擇指引。

## 方法
問題設定為從包含三維座標向量與離散類別標籤的座標-類別資料預測標量性質。作者構建合成資料集，採用物理啟發的假設位能函數 E = α·E_category + (1-α)·E_coordinate，α∈(0,1) 連續調控類別與座標對目標的貢獻；生成多種座標幾何與類別分佈的資料集，並對每個 α 產生對應標籤。模型端以 BERT 為代表的 Transformer（含因果與遮罩語言模型）對文本化後的結構進行微調預測。輸入表示採用 MatText 框架提供的九種文本表徵（如 SLICES、CIF Symmetrized 等），涵蓋組成、鍵結、週期性、對稱性與完整原子座標等不同歸納偏向；並支援原子級與表徵專用的分詞策略及數值分詞變體。訓練目標為最小化回歸損失（MSE），優化採用標準 AdamW。評估指標定義座標貢獻誤差 L_coord,α = Σ_{α∈{0,0.2,0.4}} loss(α) - 3·loss(0.5) 及類別貢獻誤差 L_cat,α = Σ_{α∈{0.6,0.8,1.0}} loss(α) - 3·loss(0.5)；兩者差值為 Coordinate-Category Cliff (CC-Cliff)。為探究失效機制，另以 n-gram 模型重複實驗，並將座標貢獻的成對距離離散化為多類別分類任務（bin 數從粗到細），觀察 CC-Cliff 隨 bin 數變化。此外，利用注意力權重分析驗證座標 token 是否被模型利用。推論流程為：文本化結構 → 分詞 → 模型前向 → 回歸頭輸出性質。關鍵差異在於：LLM 僅以序列方式處理座標，缺乏幾何等變性；GNN 等專用幾何架構則顯式建模空間關係。

## 結果
實驗顯示所有合成資料集的 CC-Cliff 均為正值，即 L_coord,α 顯著大於 L_cat,α，表示 LLM 學習座標資訊的樣本效率遠低於類別資訊。n-gram 模型呈現幾乎相同的 CC-Cliff 趨勢，說明 LLM 對座標的處理行為可由 n-gram 近似，缺乏組合泛化能力。在 MatText 基準上，增加座標細節的表徵（如 CIF P1）並未提升預測效能，甚至較簡單的組成表徵（SLICES）表現更好；Local-Env 等局部環境表徵在體積模量與剪力模量預測上與完整座標表徵相當。專用幾何架構（GNN）在結構主導的性質上明顯優於 LLM，形成所謂「GNN-LM wall」。摘錄未提供可驗證數字，僅能觀察到定性結論：LLM 擅長類別模式，對幾何關係存在系統性盲區。

## 限制與展望
研究主要基於合成資料與單一 BERT 族模型（最大 70B 參數），真實材料資料集的多樣性、噪聲與規模可能改變結論；文本表徵雖涵蓋九種但仍非窮盡，分詞與數值編碼策略的影響僅部分探討；評估僅針對三項性質（剪力模量、體積模量、鈣鈦礦形成能），其他性質（如電子結構、光學性質）的泛化性未知；注意力分析為間接證據，未直接證明座標資訊完全不可恢復。後續工作可擴展至更大規模真實數據、更多模型家族（如 LLaMA、Mistral）、多模態融合與幾何感知的提示工程，以驗證並緩解幾何盲區。
