# 論文 01：Multimodal cell foundation models require synergistic integration beyond alignment

- 日期：2026-11-11
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
整合多模態與多尺度測量為統一細胞功能定量框架是計算生物學核心目標。雖存在強大單模態基礎模型，但大規模配對資料稀缺限制聯合多模態訓練，導致採用組合式基礎模型（CFM）凍結單模態專家並透過學習介面融合。然而，何時融合能提供超越最強單模態表示的任務相關資訊，而非僅聚合冗餘訊號，仍不清楚。本文提出基於部分資訊分解的協同資訊分數（SIS），量化僅源自跨模態交互的資訊增益；理論證明標準對齊目標在凍結編碼器下會崩潰為檢測線性冗餘，限制捕捉非線性協同狀態；在空間轉錄組資料集上基準測試十種融合方法，發現線性冗餘主導任務適合單模態基線，複雜微環境定義受益於協同感知整合；擴展分析顯示微調主導單模態專家為標準任務最樣本高效策略。研究建議多模態細胞狀態建模需從對齊目標轉向協同驅動整合。

## 方法
研究引入協同資訊分數（SIS）作為診斷指標，基於部分資訊分解（PID）定義：SIS = (I(Y;Z3) - max(I(Y;Z1), I(Y;Z2))) / max(I(Y;Z1), I(Y;Z2))，其中 Z1、Z2 為凍結單模態表示，Z3 = [g1(Z1); g2(Z2)] 為融合表示。互資訊以線性探針估計（分類用 F1 Macro，迴歸用 R2），SIS 衡量融合介面是否使協同資訊線性可及。實驗架構：從全切片組織病理與空間 GEX 提取空間匹配斑塊，使用 UNI-25（組織病理）與 Nicheformer（空間轉錄組）凍結編碼器產生潛在嵌入。基準測試十種融合介面：聚合（串接）、光譜（CCA、VICReg）、非光譜（CoMM）。下游任務涵蓋微環境分類、細胞類型組成迴歸、空間鄰域預測、空間一致性與微環境一致性。資料集包含肺纖維化、人類胸腺發育、乳癌三組空間轉錄組資料。理論部分將自監督學習光譜理論擴展至多模態凍結編碼器設定，證明多樣對齊目標收斂至等效光譜解，僅能恢復冗餘、難以獲取非線性協同資訊。另進行微調擴展分析，比較不同樣本量下多模態整合價值。

## 結果
摘錄未提供可驗證數字。定性結論：線性冗餘主導任務（如細胞類型組成迴歸）單模態基線表現已足；複雜微環境定義等跨模態依賴任務，協同感知整合（如 CoMM）能突破光譜天花板，對齊方法則飽和於單模態性能附近。SIS 能區分單模態充分與跨模態依賴機制。擴展分析顯示微調主導單模態專家為標準任務最樣本高效策略。多模態融合在單模態充分任務僅提供有限增益，跨模態依賴任務則能揭露單模態無法獲取的互補訊號。

## 限制與展望
研究受限於配對資料稀缺，融合介面需在低配對監督下訓練；SIS 在強模態不平衡下保守，融合必須超越主導單模態基線才為正；評估僅限線性探針，未探討非線性下游模型；理論分析假設編碼器凍結，未涵蓋端到端聯合訓練；基準僅含三組空間轉錄組資料，泛化性待驗證；對齊融合可能抑制模態特異訊號，風險難從下游指標單獨檢測。後續研究應發展協同驅動整合目標、獲取更多高品質配對資料、擴展至非線性探針與端到端訓練場景。
