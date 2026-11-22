# 論文 01：FLORO: A multimodal geospatial foundation model for ecological remote sensing across sensors and scales

- 日期：2026-11-02
- 來源層級：Tier 2
- 期刊/會議/來源：ISPRS Journal of Photogrammetry and Remote Sensing
- Venue：ISPRS Journal of Photogrammetry and Remote Sensing
- 發布時間：2026-10-28T00:00:00+00:00
- URL：https://doi.org/10.1016/j.isprsjprs.2026.10.008
- PDF：https://www.sciencedirect.com/science/article/pii/S0924271626005058/pdf
- DOI：10.1016/j.isprsjprs.2026.10.008
- arXiv：2605.28174
- 影響指標：2yr_mean_citedness=14.99, h_index=256, i10_index=3577 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: ISPRS Journal of Photogrammetry and Remote Sensing
- 引用數：0
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2605.28174
- 全文字數：183001（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/jorlrodriguezg/floro
- 配對 Repo：jorlrodriguezg/floro

## 摘要
The proliferation of remote sensing platforms has generated an unprecedented diversity of Earth observation data, creating both the opportunity and the challenge of extracting transferable knowledge across sensors, scales, and environments. Foundation models have emerged as a promising framework for this challenge, leveraging large datasets to learn representations that generalize across tasks and sensing conditions in real-world Earth observation. However, many current approaches rely on very large pretraining datasets and remain constrained by fixed sensor configurations, limited observation-type flexibility, or narrow evaluation settings. These limitations are particularly relevant for ecological and environmental applications, where data are often heterogeneous across platforms, resolutions, and data sources. We introduce FLORO, a multimodal geospatial foundation model designed to learn transferable representations from a comparatively small, heterogeneous remote-sensing pretraining dataset. FLORO is pretrained using masked autoencoding on a heterogeneous combination of Sentinel-1, Sentinel-2, SkySAT imagery, terrain data, and UAV-derived products. To accommodate real-world sensor variability, FLORO incorporates availability-aware inputs that indicate which spectral bands and auxiliary observations are present in each sample, enabling a unified input space across heterogeneous sensor configurations. We evaluated FLORO on the PANGAEA benchmark under a frozen-encoder protocol across scene classification, segmentation, and regression tasks. Despite being pretrained on a smaller dataset than competing foundation models, FLORO achieved strong and stable transfer across optical, optical-SAR, and optical-elevation benchmarks spanning medium-resolution satellite, airborne, and ultra-high-resolution UAV imagery. FLORO obtained the second-best average segmentation performance across six PANGAEA benchmarks, the third-best average rank across three scene-classification benchmarks, and excelled in regression tasks, while qualitative results showed improved preservation of spatial structure in flood, urban, biomass, and canopy-height prediction settings. Overall, these results position FLORO as a practical framework for ecological and environmental monitoring under heterogeneous sensing conditions. To support benchmarking and reproducibility, the source code and PANGAEA evaluation integration, including access to the benchmark datasets, are available at https://github.com/jorlrodriguezg/floro , with pretrained model checkpoints at https://huggingface.co/jorlrodriguezg/floro .

## 背景與目的
The proliferation of remote sensing platforms has generated an unprecedented diversity of Earth observation data, creating both the opportunity and the challenge of extracting transferable knowledge across sensors, scales, and environments. Foundation models have emerged as a promising framework for this challenge, leveraging large datasets to learn representations that generalize across tasks and sensing conditions in real-world Earth observation. However, many current approaches rely on very l

## 方法
（待補充：需模型或人工分析）

## 結果
（待補充：需模型或人工分析）

## 限制與展望
（待補充：需模型或人工分析）
