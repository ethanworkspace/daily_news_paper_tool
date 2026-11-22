# GitHub 專案 02：jorlrodriguezg/floro

- 日期：2026-11-02
- URL：https://github.com/jorlrodriguezg/floro
- 描述：
- Stars：14  |  Forks：3  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-02T13:15:31+00:00
- 配對論文：https://doi.org/10.1016/j.isprsjprs.2026.10.008
- 品質分數：8/10 [paper_paired, implementation_signals]

## 在做什麼
主要語言：Python；Stars：14；License：MIT

## 技術
實作語言以 Python 為主。

## 架構
README 未明確提供架構章節，需後續由 LLM 根據程式與文件補充。

## README 摘錄（節選）
```text
## **FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales**
Jorge L. Rodríguez, Victor Angulo-Morales, Areej Alwahas, Mariana Elías-Lara, Fida Mohammad Thoker, Kasper Johansen, Bernard Ghanem, Fernando T. Maestre, and Matthew F. McCabe
Biological and Environmental Science and Engineering Division, King Abdullah University of Science and Technology, Thuwal, Saudi Arabia
Computer, Electrical and Mathematical Science and Engineering Division, King Abdullah University of Science and Technology, Thuwal, Saudi Arabia
--- 
## **Overview**
** FLORO:** is a multimodal geospatial foundation model designed to learn transferable representations from a compact but highly diverse remote sensing corpus.
FLORO is pretrained using masked autoencoding on heterogeneous Earth observation data, including multispectral satellite imagery, synthetic-aperture radar, high-resolution commercial imagery, UAV products, and terrain information. Rather than relying only on very large pretraining corpora, FLORO explores whether diversity across sensors, spatial resolutions, spectral configurations, and ecological settings can produce representations that transfer effectively across remote sensing tasks.
> Under the frozen-encoder evaluation protocol of the PANGAEA benchmark, FLORO demonstrates strong transfer performance across semantic segmentation, scene classification, and regression tasks. Its results suggest that competitive geospatial representations can emerge from carefully curated multimodal pretraining data, even when the number of pretraining samples is much smaller than in several recent large-scale remote sensing foundation models.
--- 
## 🧠 **Architecture**
FLORO uses a Vision Transformer encoder pretrained through masked autoencoding. During pretraining, heterogeneous remote sensing observations are tokenized and partially masked. The encoder learns latent representations from the visible tokens, while lightweight reconstruction decoders predict the masked content for each modality.
> After pretraining, the shallow reconstruction decoders are discarded. The pretrained encoder is then evaluated under frozen-encoder transfer, where task-specific benchmark decoders are trained for downstream tasks such as semantic segmentation, scene classification, and regression.
--- 
## 🌍 **Pretraining Data**
> FLORO is pretrained on a heterogeneous collection of remote sensing observations designed to expose the model to variation in spatial resolution, spectral coverage, sensing geometry, and ecological context.
The pretraining corpus includes:
- **Sentinel-2 multispectral imagery**, providing medium-resolution optical observations across visible, red-edge, near-infrared, and shortwave-infrared bands.
- **Sentinel-1 SAR imagery**, providing radar backscatter information that complements optical observations, particularly under cloud cover or degraded optical conditions.
- **SkySat high-resolution imagery**, introducing fine spatial detail and commercial satellite observation characteristics.
- **Terrain and elevation products**, including global and local digital elevation or terrain-derived data.
- **UAV RGB and multispectral products**, including very high-resolution orthomosaics, digital surface models, and vegetation-structure information.
> The objective is not only to increase the number of pretraining samples, but to increase the diversity of sensing conditions encountered during representation learning.
--- 
## 🔨 **Pretraining regime**
FLORO is pretrained on approximately 80K remote sensing image samples spanning satellite, airborne, UAV, optical, SAR, and terrain-derived data sources. The model supports multispectral optical data, Sentinel-1 SAR backscatter, elevation products, UAV-derived structural information, and high-resolution imagery. FLORO learns by reconstructing masked content from partially observed multimodal inputs, encouraging the encoder to capture both spectral and spatial structure.
```
