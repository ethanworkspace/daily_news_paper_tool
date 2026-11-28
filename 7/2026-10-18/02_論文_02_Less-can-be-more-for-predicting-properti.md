# 論文 02：Less can be more for predicting properties with large language models

- 日期：2026-10-18
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
預測座標-類別資料（向量與離散類別標籤配對）的性質是計算科學核心任務，材料科學中表現為從晶體結構（原子位置向量與元素類別）預測形成能、彈性模數等性質。近年大型語言模型（LLM）被嘗試用於此類任務，將結構資料編碼為文本，但最佳策略仍不明確。本文發現 LLM 存在根本性限制：無論模型規模（高達 70B 參數）、資料集大小（高達 200 萬結構）或文本表示策略如何，LLM 皆持續無法捕捉座標資訊，卻擅長學習類別模式，稱之為「幾何盲點」。對於結構效應主導的材料性質預測，專門幾何架構（如圖神經網路 GNN）顯著優於 LLM，形成明顯的「GNN-LM 牆」。研究提供科學機器學習中架構選擇的具體指導，強調理解模型歸納偏見的重要性。

## 方法
研究設計合成資料集系統探針 LLM 對座標與類別資訊的學習能力。每個資料點包含 3D 座標（類比原子位置）與類別標籤（類比原子類型），目標標量值由物理啟發的假設勢函數計算：E = α E_category + (1-α) E_coordinate，α∈(0,1) 可連續調節類別與座標貢獻比重。生成多種座標幾何（如立方體角點）與類別分佈的資料集，對每個資料集變化 α（0, 0.2, …, 1）構建從純座標依賴到純類別依賴的能量景觀。微調 BERT 模型預測標籤，定義兩個聚合誤差指標：座標貢獻 L_coord,α = Σ_{α∈α_g} loss(α) - 3×loss(0.5)（α_g={0,0.2,0.4}）與類別貢獻 L_cat,α = Σ_{α∈α_c} loss(α) - 3×loss(0.5)（α_c={0.6,0.8,1.0}）。若 L_coord,α ≫ L_cat,α 則稱為座標-類別懸崖（CC-Cliff），量化模型對座標資訊學習的系統性劣勢。 為釐清失敗來源，引入 n-gram 模型作為基線，並將座標貢獻中的成對距離離散化為多類別分類任務（bin 數從少到多），觀察 CC-Cliff 隨任務複雜度變化。同時建立開源框架 MatText，實作九種晶體結構文本表示（如 SLICES、Cif Symmetrized、Cif P1、Local-Env 等），涵蓋成分、鍵結、週期性、對稱性、原子位置等不同歸納偏見；支援原子級與表示專用 tokenization、數值 tokenization 策略；支援因果與遮罩語言模型的預訓練與微調、模型與資料擴展；提供注意力機制分析、基於注意力分數的 token 貢獻評估、CC-Cliff 分析模組。在真實材料任務（剪力模量 μ、體積模量 K、鈣鈦礦形成能 E_f）上，系統比較不同表示下的預測性能，並驗證 tokenizer 與數值編碼對結果的影響。

## 結果
在所有合成資料集上，LLM 均呈現顯著正向 CC-Cliff（L_coord,α 遠大於 L_cat,α），表明模型在座標主導任務上表現嚴重劣於類別主導任務。此現象與 n-gram 模型行為幾乎完全一致，暗示 LLM 繼承了 n-gram 對位置資訊的無效建模特性；注意力分析進一步證實座標資訊在預測中未被利用。MatText 基準測試顯示，增加座標資訊的表示（如 Cif P1）並未提升性能，反而較簡單的表示（SLICES、Local-Env）在體積模量與剪力模量預測上表現更優或相当，支持座標資訊無法被 LLM 有效利用的結論。此發現跨 tokenization 策略與數值編碼方式均穩健。在結構效應主導的材料性質預測中，專門幾何架構（GNN）持續以顯著優勢超越 LLM，形成明確的「GNN-LM 牆」。摘錄未提供可驗證的具體數值指標（如 MAE、RMSE、準確率等），僅呈現定性比較結論。

## 限制與展望
合成資料集雖可精確控制座標與類別貢獻，但假設勢函數為簡化物理模型，可能無法完全捕捉真實材料系統的複雜相互作用。實驗主要針對 BERT 風格的遮罩語言模型（最高 70B 參數），對解碼器專用或其他 LLM 架構的泛化性尚待驗證。MatText 基準涵蓋的性質（剪力模量、體積模量、鈣鈦礦形成能）與九種文本表示雖具代表性，但未涵蓋所有材料類別與預測任務，結論推廣至其他科學領域需謹慎。注意力分析僅提供間接證據，未從理論上證明 LLM 無法學習座標關係的根本機制。架構選擇指南基於經驗觀察，缺乏對混合架構（如幾何感知語言模型）的系統評估。後續研究可探索：改進座標編碼策略、結合幾何先驗的混合模型、更大規模與多樣化資料集上的驗證、以及對其他科學領域（如分子動力學、量子化學）的延伸。
