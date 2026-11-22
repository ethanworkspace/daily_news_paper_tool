# 論文 01：Multimodal cell foundation models require synergistic integration beyond alignment

- 日期：2026-11-09
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
Integrating measurements across modalities and scales into unified quantitative frameworks of cellular function is a central goal in computational biology. Although powerful unimodal foundation models exist, the scarcity of large-scale paired data limits joint multimodal training. This constraint favours compositional foundation models, which fuse frozen unimodal experts through a learned interface. However, it remains unclear when such fusion provides task-relevant information beyond the strong

## 方法
（待補充：需模型或人工分析）

## 結果
（待補充：需模型或人工分析）

## 限制與展望
（待補充：需模型或人工分析）
