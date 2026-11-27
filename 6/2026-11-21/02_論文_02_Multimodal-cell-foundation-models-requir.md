# 論文 02：Multimodal cell foundation models require synergistic integration beyond alignment

- 日期：2026-11-21
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature Machine Intelligence
- Venue：Nature Machine Intelligence
- 發布時間：2026-11-09T00:00:00+00:00
- URL：https://doi.org/10.1038/s42256-026-01328-3
- PDF：https://www.nature.com/articles/s42256-026-01328-3.pdf
- DOI：10.1038/s42256-026-01328-3
- arXiv：
- 影響指標：2yr_mean_citedness=36.09, h_index=186, i10_index=954 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Machine Intelligence
- 引用數：3
- 解析程度：fulltext / pdf+ocr
- 全文來源：https://www.nature.com/articles/s42256-026-01328-3.pdf
- 全文字數：127763（pages=30, ocr_pages=3）
- GitHub/Code：https://github.com/microsoft/cell_synergy
- 配對 Repo：microsoft/cell_synergy

## 摘要
Integrating measurements across modalities and scales into unified quantitative frameworks of cellular function is a central goal in computational biology. Although powerful unimodal foundation models exist, the scarcity of large-scale paired data limits joint multimodal training. This constraint favours compositional foundation models, which fuse frozen unimodal experts through a learned interface. However, it remains unclear when such fusion provides task-relevant information beyond the strongest unimodal representation rather than merely aggregating redundant signal. Here we introduce Synergistic Information Score, a metric grounded in partial information decomposition that quantifies information gain arising only from cross-modal interactions. Extending theory from self-supervised learning, we show that standard alignment-based objectives with frozen encoders collapse to detect linear redundancies, which constrains their ability to capture nonlinear synergistic states. This distinction is especially important for tasks that connect tissue morphology with gene expression. Benchmarking ten fusion methods on spatial transcriptomics datasets, we demonstrate that tasks dominated by linear redundancies are well served by unimodal baselines, whereas complex niche definitions benefit from synergy-aware integration. Finally, we perform a scaling analysis and show that fine-tuning a dominant unimodal expert is the most sample-efficient strategy for standard tasks. Together, these results suggest that progress in multimodal modelling of cellular state requires shifting from alignment-based objectives to synergy-driven integration that exploits complementary cross-modal signal.

## 背景與目的
本研究針對計算生物學中整合多模態數據（組織病理影像與基因表達）的核心挑戰：大規模配對數據稀缺，導致聯合訓練困難，主流做法採用組合式基礎模型（CFM），凍結單模態編碼器並透過學習介面融合。然而，現有基於對齊的融合目標往往僅捕捉線性冗餘，無法獲取跨模態非線性協同資訊，特別是在連結組織形態與基因表達的任務中。本文提出協同資訊分數（SIS），基於部分資訊分解量化僅來自跨模態交互的資訊增益，並從理論與實驗證明對齊目標會陷入譜上限，限制協同狀態捕捉。目標在於建立診斷指標區分單模態足夠與跨模態依賴任務，推動從對齊導向轉向協同驅動的整合。

## 方法
研究採用凍結的單模態基礎模型編碼器：組織病理使用 UNI-25，空間轉錄組使用 Nicheformer。從全切片病理影像與空間 GEX 數據中提取空間匹配的切片，確保兩模態觀察同一物理區域。將切片轉換為潛在嵌入後，僅訓練融合介面，隔離融合機制對下游表現的影響。基準測試十種融合介面，涵蓋聚合（串接）、光譜類（CCA、VICReg）與非光譜類（CoMM）。下游評估五項生物學任務：生態位分類、細胞類型組成回歸、空間鄰域預測、空間一致性與生態位一致性，涵蓋局部表型、空間組織與表徵一致性。引入 SIS，基於最小互信息假設，定義為融合表徵對下游變數 Y 的互信息增益相對於最強單模態基線的比率；實務上以線性探針（分類用 F1 Macro，回歸用 R2）估計互信息，僅測量融合介面使協同資訊線性可及的程度。並擴展自監督學習的譜理論至多模態凍結編碼器設定，解釋多樣對齊目標收斂至等效譜解，僅能恢復冗餘而難以獲取非線性協同資訊。另進行微調縮放分析，比較單模態微調與多模態整合在不同數據規模下的樣本效率。

## 結果
實驗顯示，基於對齊的融合方法在跨模態依賴任務中表現飽和於單模態基線附近（譜上限），而協同感知目標（如 CoMM）能突破譜上限。由線性冗餘主導的任務（如細胞類型組成回歸）單模態基線已足夠；複雜生態位定義等任務則受益於協同整合。縮放分析表明，對標準任務而言，微調優勢單模態專家為最樣本高效策略。SIS 成功區分單模態足夠與跨模態依賴機制。摘錄未提供可驗證的具體數值（如 F1、R2 具體分數），僅呈現定性結論。

## 限制與展望
研究受限於配對數據稀缺、凍結編碼器無法適應下游任務、SIS 僅以線性探針估計協同資訊（可能低估非線性協同）、強模態不平衡下 SIS 傾向保守、基準數據集僅涵蓋三類組織（肺纖維化、胸腺發育、乳癌），泛化性有待驗證。對齊融合可能抑制模態特有訊號，風險在於誤判冗餘為協同。後續研究可探索非線性探針、更豐富配對數據、協同驅動目標設計及端到端微調策略。
