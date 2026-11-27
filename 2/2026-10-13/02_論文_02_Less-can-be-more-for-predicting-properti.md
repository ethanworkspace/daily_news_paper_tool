# 論文 02：Less can be more for predicting properties with large language models

- 日期：2026-10-13
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
本研究針對座標-類別資料（如晶體結構中的原子位置與元素類型）的屬性預測任務，探討大型語言模型（LLM）能否有效學習座標資訊。現有研究多將結構資料編碼為文本並套用 LLM，但缺乏系統性分析其對連續向量與離散類別的學習差異。作者指出 LLM 在處理幾何關係時存在根本性盲點，這對材料科學等依賴精確結構預測的領域影響深遠。本文目標在於量化 LLM 對座標與類別資訊的學習效率差距，建立基準框架 MatText，並提供架構選擇的實務指導。

## 方法
研究設計包含三大部分：(1) 合成資料集建構：依物理啟發的假設位能函數 E = α·E_category + (1-α)·E_coordinate，透過連續調整 α∈[0,1] 產生純座標、純類別與混合任務，涵蓋多種幾何排列與類別分佈。(2) 模型與評估指標：微調 BERT（含因果與遮罩語言模型）並計算座標貢獻誤差 L_coord,α 與類別貢獻誤差 L_cat,α，定義座標-類別懸崖（CC-Cliff）為兩者差值，量化幾何盲點。(3) 基準框架 MatText：實作九種文本表示（如 SLICES、CIF Symmetrized、Local-Env 等），支援多種分詞策略、數值編碼、預訓練與微調流程，並整合注意力分析模組。另引入 n-gram 模型作為基線，驗證 LLM 行為是否可由 n-gram 近似。實驗跨越模型規模（至 70B 參數）、資料規模（至 2×10^6 結構）與表示策略，系統性探討歸納偏誤對座標學習的影響。

## 結果
摘錄未提供可驗證數字。定性結論顯示：(1) 所有合成資料集均出現顯著正向 CC-Cliff，即 LLM 在座標主導任務誤差遠大於類別主導任務，證實幾何盲點普遍存在。(2) n-gram 模型行為與 LLM 高度一致，說明 LLM 未有效利用位置資訊。(3) MatText 基準測試中，僅含組成與鍵結資訊的 SLICES 表現優於含完整座標的 CIF P1，Local-Env 在體積模量與剪力模量預測具可比性，進一步佐證座標資訊未被有效編碼。(4) 專門幾何架構（GNN）在結構主導任務上明顯超越 LLM，形成「GNN-LM 牆」。

## 限制與展望
研究限制包括：合成資料雖可控但可能無法完整反映真實材料系統的複雜性；實驗模型上限為 70B 參數，更大規模 LLM 表現未知；文本表示集合雖廣但非窮盡，未涵蓋所有可能編碼策略；評估僅針對靜態屬性預測，動態或多尺度任務未探討；注意力分析僅為質性證據，缺乏量化機制解釋。後續研究可朝混合幾何-語言架構、改進座標編碼、擴展至其他科學領域及更大規模模型驗證方向發展。
