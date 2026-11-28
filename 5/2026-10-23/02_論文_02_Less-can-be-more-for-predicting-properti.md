# 論文 02：Less can be more for predicting properties with large language models

- 日期：2026-10-23
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature Computational Science
- Venue：Nature Computational Science
- 發布時間：2026-10-12T00:00:00+00:00
- URL：https://doi.org/10.1038/s43588-026-01045-2
- PDF：https://www.nature.com/articles/s43588-026-01045-2.pdf
- DOI：10.1038/s43588-026-01045-2
- arXiv：2406.17295
- 影響指標：2yr_mean_citedness=12.70, h_index=92, i10_index=460 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Computational Science
- 引用數：34
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2406.17295
- 全文字數：105822（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/lamalab-org/MatText
- 配對 Repo：lamalab-org/MatText

## 摘要
Predicting properties from coordinate-category data-sets of vectors paired with categorical information-is fundamental to computational science, manifesting in materials science as predicting formation energies or elastic moduli from crystal structures. While large language models (LLMs) have increasingly been applied to such tasks, optimal strategies for achieving reliable predictions remain elusive. Here we report fundamental limitations in LLM's ability to learn from coordinate information in coordinate-category data. Through systematic experiments using synthetic datasets with tunable coordinate and category contributions, and a comprehensive benchmarking framework (MatText), we find that LLMs consistently fail to capture coordinate information while excelling at category patterns. This geometric blindness persists regardless of model size (up to 70 billion parameters), dataset scale (up to 2 × 106 structures) or text representation strategy. For material property prediction tasks dominated by structural effects, specialized geometric architectures consistently outperform LLMs, as evidenced by a clear 'Graph Neural Network Language Model (GNN-LM) wall' in performance benchmarks. Our analysis provides concrete guidelines for architecture selection in scientific machine learning.

## 背景與目的
本研究針對「座標-類別資料」的屬性預測問題，即從連續向量（如原子座標）與離散類別（如元素類型）混合的資料中預測材料屬性（生成能、彈性模數等）。現有研究嘗試將結構資料編碼為文本並套用大型語言模型（LLM），但缺乏系統性理解 LLM 對座標資訊的學習能力。作者發現 LLM 在處理座標關係時存在根本性缺陷，無論模型規模（至 70B 參數）、資料集大小（至 200 萬結構）或文本表示策略如何變化，均表現出「幾何盲點」。此缺口對材料設計與發現具有深遠影響，亟需明確架構選擇指南。

## 方法
研究設計包含三大階段： 1. 合成資料集與可調控位能函數：構建含 3D 座標與類別標籤的資料點，透過位能函數 E = α·E_category + (1-α)·E_coordinate（α∈[0,1]）連續調節座標與類別對目標值的貢獻，生成多組 α 掃描資料集，涵蓋不同座標幾何與類別分佈。 2. 模型訓練與誤差度量：對每個 α 版本微調 BERT（雙向編碼器），計算兩項聚合誤差：座標貢獻 L_coord,α = Σ_{α∈{0,0.2,0.4}} loss(α) − 3·loss(0.5) 與類別貢獻 L_cat,α = Σ_{α∈{0.6,0.8,1.0}} loss(α) − 3·loss(0.5)。定義座標-類別懸崖（CC-Cliff）為 L_coord,α − L_cat,α，正值代表模型在座標主導任務上系統性劣於類別主導任務。 3. n-gram 基線與離散化實驗：將配對距離貢獻離散化為多數分類（bin 數從粗到細），比較 Transformer 與對應 n-gram 模型的 CC-Cliff 變化，驗證 LLM 行為是否可由 n-gram 近似。 4. MatText 基準框架：實作九種文本表示（如 SLICES、CIF Symmetrized、Local-Env 等），支援原子級與表示專用分詞、數值分詞策略，整合因果與遮罩語言模型的預訓練/微調流程，並提供注意力分析與 CC-Cliff 計算模組。 5. 實驗控制：跨表示、分詞器、模型規模（至 70B）、資料集規模（至 2M）進行消融，確保結論不受單一表示或超參數干擾。

## 結果
主要發現： 1. 所有合成資料集均呈現顯著正向 CC-Cliff（L_coord,α ≫ L_cat,α），證實 LLM 系統性無法有效學習座標資訊，且隨模型放大、資料增多或表示改變均不改善。 2. n-gram 模型與 Transformer 在 CC-Cliff 隨 bin 數變化趨勢幾乎重疊，顯示 LLM 對座標資訊的處理僅相當於 n-gram 統計關聯，缺乏幾何推理能力；注意力分析進一步顯示座標 token 在預測時未被有效利用。 3. MatText 實驗中，增加座標資訊的表示（如 CIF P1）未提升預測效能，反而僅含組成與鍵結資訊的 SLICES 在剪切模量、體積模量與鈣鈦礦生成能三項任務上表現最佳；Local-Env 在體積與剪切模量上表現接近。 4. 結論不隨分詞器或數值分詞策略改變。 摘錄未提供可驗證數字（如具體 MAE/RMSE、統計顯著性），僅能觀察到定性結論：LLM 在結構主導任務上明顯劣於幾何專用架構（GNN），形成「GNN-LM 牆」。

## 限制與展望
1. 合成資料集雖可精確控制座標/類別貢獻，但其物理真實性與真實材料系統（如異質介面、缺陷、熱力學平衡）仍有落差，推廣性需進一步驗證。 2. 實驗僅涵蓋 BERT 類編碼器與 n-gram 基線，未測試更大規模或不同架構的 LLM（如 GPT 系列、LLaMA、指令微調模型），結論對所有 LLM 的普適性存疑。 3. MatText 基準僅評估三種屬性與九種表示，未涵蓋電子結構、光學、磁性等多樣屬性，亦未比較最新幾何深度學習模型（如 SE(3)-Transformer、GemNet）。 4. 未系統探討預訓練語料、領域適應策略或提示工程對座標學習的影響。 5. 注意力分析僅為質性證據，缺乏量化幾何資訊流動的指標。 後續研究建議：擴展至更多真實材料任務、引入幾何感知注意力機制、探討混合 GNN-LM 架構、建立更全面的座標-類別基準集。
