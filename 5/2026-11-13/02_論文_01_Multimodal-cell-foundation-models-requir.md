# 論文 01：Multimodal cell foundation models require synergistic integration beyond alignment

- 日期：2026-11-13
- 來源層級：Tier 1
- 期刊/會議/來源：Nature Machine Intelligence
- Venue：Nature Machine Intelligence
- 發布時間：2026-11-09T00:00:00+00:00
- URL：https://doi.org/10.1038/s42256-026-01328-3
- PDF：https://www.nature.com/articles/s42256-026-01328-3.pdf
- DOI：10.1038/s42256-026-01328-3
- arXiv：
- 影響指標：2yr_mean_citedness=35.95, h_index=187, i10_index=951 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Machine Intelligence
- 引用數：2
- 解析程度：fulltext / pdf+ocr
- 全文來源：https://www.nature.com/articles/s42256-026-01328-3.pdf
- 全文字數：127010（pages=30, ocr_pages=3）
- GitHub/Code：https://github.com/microsoft/cell_synergy
- 配對 Repo：microsoft/cell_synergy

## 摘要
Integrating measurements across modalities and scales into unified quantitative frameworks of cellular function is a central goal in computational biology. Although powerful unimodal foundation models exist, the scarcity of large-scale paired data limits joint multimodal training. This constraint favours compositional foundation models, which fuse frozen unimodal experts through a learned interface. However, it remains unclear when such fusion provides task-relevant information beyond the strongest unimodal representation rather than merely aggregating redundant signal. Here we introduce Synergistic Information Score, a metric grounded in partial information decomposition that quantifies information gain arising only from cross-modal interactions. Extending theory from self-supervised learning, we show that standard alignment-based objectives with frozen encoders collapse to detect linear redundancies, which constrains their ability to capture nonlinear synergistic states. This distinction is especially important for tasks that connect tissue morphology with gene expression. Benchmarking ten fusion methods on spatial transcriptomics datasets, we demonstrate that tasks dominated by linear redundancies are well served by unimodal baselines, whereas complex niche definitions benefit from synergy-aware integration. Finally, we perform a scaling analysis and show that fine-tuning a dominant unimodal expert is the most sample-efficient strategy for standard tasks. Together, these results suggest that progress in multimodal modelling of cellular state requires shifting from alignment-based objectives to synergy-driven integration that exploits complementary cross-modal signal.

## 背景與目的
計算生物學的核心目標是將跨模態、跨尺度的測量整合為統一的細胞功能定量框架。雖然已有強大的單模態基礎模型，但大規模配對資料稀缺，限制了端到端的多模態聯合訓練，導致主流採用組合式基礎模型（CFM），凍結單模態專家並透過學習介面融合。然而，何時融合能提供超越最強單模態表示的任務相關資訊，而非僅疊加冗餘訊號，仍不明確。本文提出基於部分資訊分解的協同資訊分數（SIS），量化僅源自跨模態交互的資訊增益；並從自監督學習的譜理論推導，證明標準對齊目標在凍結編碼器下會崩潰為線性冗餘檢測，無法捕捉非線性協同態。研究在空間轉錄組資料集上基準測試十種融合方法，並進行擴展分析，旨在建立從對齊導向轉向協同驅動整合的原則性指引。

## 方法
研究採用組合式基礎模型架構：從全切片病理影像與空間基因表現（GEX）提取空間匹配的斑塊，分別以最先進的凍結基礎模型編碼器 UNI-25（組織病理）與 Nicheformer（空間轉錄組）轉換為潛在嵌入。僅訓練輕量級融合介面，基準測試十種融合策略，涵蓋簡單聚合（如串接 Concat）、譜方法（CCA、VICReg）與非譜目標（CoMM）。下游評估採用五項生物學任務：利基分類、細胞類型組成回歸、空間鄰域預測、空間一致性與利基一致性，以區分單模態足夠與跨模態依賴的資訊機制。協同資訊分數（SIS）基於部分資訊分解，定義為融合表示在線性探針下相對於最佳單模態基線的相對資訊增益；分類用 F1 Macro，回歸用 R² 估算互資訊。理論上，將自監督學習的譜理論擴展至多模態凍結編碼器設定，說明多樣對齊目標收斂至等效譜解，僅能恢復線性冗餘。實驗使用肺纖維化、人類胸腺發育、乳癌三個空間轉錄組資料集，確保模態間觀察同一物理區域。

## 結果
摘錄未提供可驗證數字。定性結論顯示：由線性冗餘主導的任務（如利基分類、細胞類型組成回歸）單模態基線即表現良好；複雜利基定義等跨模態依賴任務則受益於協同感知整合。協同感知目標（如 CoMM）能在跨模態依賴機制下突破譜上限，而對齊型方法通常飽和於單模態性能附近。擴展分析指出，微調主導單模態專家是在標準任務上最樣本高效的策略。SIS 能有效區分單模態足夠與跨模態依賴任務，作為多模態學習獲益與否的診斷指標。

## 限制與展望
研究受限於高品質配對測量的稀缺，僅涵蓋組織病理與空間轉錄組兩模態，且編碼器凍結可能限制適應性。SIS 以線性探針估算，可能低估非線性協同資訊。基準資料集僅三組，任務類型有限，擴展性與泛化性有待驗證。理論分析假設線性冗餘主導，實際生物系統可能存在更複雜的交互。部署層面，配對資料獲取成本高、模型維護與跨機構標準化仍具挑戰。後續研究可探索更多模態、非線性探針、端到端微調與更大規模配對資料集。
