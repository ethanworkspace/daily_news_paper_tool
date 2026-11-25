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
- 影響指標：2yr_mean_citedness=12.71, h_index=93, i10_index=459 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Computational Science
- 引用數：35
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2406.17295
- 全文字數：105822（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/lamalab-org/MatText
- 配對 Repo：lamalab-org/MatText

## 摘要
Predicting properties from coordinate–category data—sets of vectors paired with categorical information—is fundamental to computational science, manifesting in materials science as predicting formation energies or elastic moduli from crystal structures. While large language models (LLMs) have increasingly been applied to such tasks, optimal strategies for achieving reliable predictions remain elusive. Here we report fundamental limitations in LLM’s ability to learn from coordinate information in coordinate–category data. Through systematic experiments using synthetic datasets with tunable coordinate and category contributions, and a comprehensive benchmarking framework (MatText), we find that LLMs consistently fail to capture coordinate information while excelling at category patterns. This geometric blindness persists regardless of model size (up to 70 billion parameters), dataset scale (up to 2 × 10 6 structures) or text representation strategy. For material property prediction tasks dominated by structural effects, specialized geometric architectures consistently outperform LLMs, as evidenced by a clear ‘Graph Neural Network Language Model (GNN-LM) wall’ in performance benchmarks. Our analysis provides concrete guidelines for architecture selection in scientific machine learning.

## 背景與目的
本研究針對座標-類別資料（如晶體結構中的原子位置與元素類型）的屬性預測問題，探討大型語言模型（LLM）在此類科學任務中的根本限制。現有研究多將結構資料編碼為文本並應用 LLM，但缺乏系統性理解其對座標資訊的學習能力。作者發現 LLM 在捕捉空間幾何關係上存在「幾何盲點」，無論模型規模（至 70B 參數）、資料集大小（至 200 萬結構）或文本表示策略如何變化，該缺陷均持續存在。對於結構效應主導的材料屬性預測，專門的幾何架構（如圖神經網路）顯著優於 LLM，形成明顯的「GNN-LM 牆」。本文提供架構選擇的具體指導，強調理解模型歸納偏差的重要性。

## 方法
方法包含三大部分：(1) 合成資料集建構：設計可調控座標與類別貢獻的假設勢函數 E = α E_category + (1-α) E_coordinate，α∈[0,1] 連續調節；生成多種座標幾何（如立方體角點）與類別分佈的資料集，並對每個 α 值微調 BERT 模型。定義座標貢獻誤差 L_coord,α 與類別貢獻誤差 L_cat,α，並以 CC-Cliff = L_coord,α − L_cat,α 量化模型對座標學習的系統性劣勢。(2) n-gram 基線比較：將配對距離離散化為多類別分類任務，對比 Transformer 與 n-gram 模型在不同分箱數下的 CC-Cliff，發現兩者行為幾乎一致，顯示 LLM 繼承 n-gram 無法處理位置資訊的特性；注意力分析進一步證實座標資訊未被利用。(3) MatText 基準框架：實作九種文本表示（含 SLICES、Cif Symmetrized 等），支援多種分詞與數值編碼，針對剪切模量、體積模量、鈣鈦礦生成能三項真實材料屬性進行大規模基準測試，系統性評估表示、模型規模、資料量對預測性能的影響。

## 結果
實驗結果顯示：在所有合成資料集上，LLM 的 CC-Cliff 均為正值，即 L_coord,α 遠大於 L_cat,α，證實模型系統性地難以從座標資訊學習；此現象與 n-gram 模型高度吻合，且注意力權重分析顯示座標標記未被有效利用。在 MatText 真實材料基準中，增加座標細節的表示（如 Cif P1）並未提升性能，反而較簡單的組成鍵結表示（SLICES）或局部環境表示表現更好；專門的幾何架構（GNN）在結構主導任務上明顯優於 LLM，形成「GNN-LM 牆」。摘錄未提供可驗證數字，僅呈現定性結論。

## 限制與展望
研究限制包括：合成資料的假設勢函數可能無法完全反映真實材料的複雜能量景觀；基準測試僅涵蓋三種屬性與九種文本表示，未窮盡所有可能的編碼策略；實驗模型以 BERT 類編碼器為主，未涵蓋解碼器專用或指令微調的 LLM；注意力分析僅為質性證據，缺乏量化因果驗證；結論推廣至其他科學領域（如分子動力學、蛋白質結構）仍需進一步驗證。後續研究可探索混合幾何-語言架構、更有效的座標編碼方式，以及擴展縮放定律分析。
