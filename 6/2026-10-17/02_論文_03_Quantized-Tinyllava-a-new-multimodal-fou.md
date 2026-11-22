# 論文 03：Quantized-Tinyllava: a new multimodal foundation model enables efficient split learning

- 日期：2026-10-17
- 來源層級：Tier 3
- 期刊/會議/來源：ArXiv
- Venue：ArXiv
- 發布時間：2025-11-28T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/4f5e2ad858550bbf00e905658115717e459499ea
- PDF：
- DOI：10.48550/arxiv.2511.23402
- arXiv：2511.23402
- 影響指標：N/A (preprint)
- 影響指標來源：preprint (not peer-reviewed journal/conference)
- 引用數：11
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2511.23402
- 全文字數：54671（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/anonymous-1742/Quantized-TinyLLaVA
- 配對 Repo：anonymous-1742/Quantized-TinyLLaVA

## 摘要
Multimodal foundation models are increasingly trained on sensitive data across domains such as finance, biomedicine, and personal identifiers. However, this distributed setup raises serious privacy concerns due to the need for cross-partition data sharing. Split learning addresses these concerns by enabling collaborative model training without raw data exchange between partitions, yet it introduces a significant challenge: transmitting high-dimensional intermediate feature representations between partitions leads to substantial communication costs. To address this challenge, we propose Quantized-TinyLLaVA, a multimodal foundation model with an integrated communication-efficient split learning framework. Our approach adopts a compression module that quantizes intermediate feature into discrete representations before transmission, substantially reducing communication overhead. Besides, we derive a principled quantization strategy grounded in entropy coding theory to determine the optimal number of discrete representation levels. We deploy our framework in a two-partition setting, with one partition operating as the client and the other as the server, to realistically simulate distributed training. Under this setup, Quantized-TinyLLaVA achieves an approximate \textbf{87.5\%} reduction in communication overhead with 2-bit quantization, while maintaining performance of the original 16-bit model across five benchmark datasets. Furthermore, our compressed representations exhibit enhanced resilience against feature inversion attacks, validating the privacy of transmission. The code is available at https://github.com/anonymous-1742/Quantized-TinyLLaVA.

## 背景與目的
Multimodal foundation models are increasingly trained on sensitive data across domains such as finance, biomedicine, and personal identifiers. However, this distributed setup raises serious privacy concerns due to the need for cross-partition data sharing. Split learning addresses these concerns by enabling collaborative model training without raw data exchange between partitions, yet it introduces a significant challenge: transmitting high-dimensional intermediate feature representations betwee

## 方法
（待補充：需模型或人工分析）

## 結果
（待補充：需模型或人工分析）

## 限制與展望
（待補充：需模型或人工分析）
