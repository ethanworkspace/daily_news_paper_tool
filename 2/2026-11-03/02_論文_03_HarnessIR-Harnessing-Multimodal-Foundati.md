# 論文 03：HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration

- 日期：2026-11-03
- 來源層級：Tier 3
- 期刊/會議/來源：arXiv (Cornell University)
- Venue：arXiv preprint
- 發布時間：2026-10-07T00:00:00+00:00
- URL：https://arxiv.org/abs/2610.10133
- PDF：https://arxiv.org/pdf/2610.10133
- DOI：10.48550/arxiv.2610.10133
- arXiv：2610.10133
- 影響指標：N/A (repository/preprint)
- 影響指標來源：Repository source has no journal impact factor
- 引用數：1
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2610.10133
- 全文字數：95887（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/PolyU-VCLab/HarnessIR
- 配對 Repo：PolyU-VCLab/HarnessIR

## 摘要
Real-world low-quality images suffer from complex mixed degradations, including but not limited to noise, blur, atmospheric effects, etc. Recent agentic methods usually model real-world image restoration (Real-IR) as a sequential tool calling problem over task-specific single-degradation restoration models. This paradigm, however, is fundamentally limited because complex real-world degradations cannot be cleanly undone degradation by degradation, and the tool used for task-specific models caps the capability of the agent system. In this work, we present HarnessIR, an agentic framework for Real-IR by harnessing a multimodal foundation model (MFM) as the executor. HarnessIR consists of five stages: perception and diagnosis, on-demand tool invocation, prompt composition, execution, and verification-driven refinement. Unlike prior agentic Real-IR methods that rely on tool chains assembled from task-specific models, HarnessIR feeds the restoration requirements, the perceptual diagnosis, and the evidence into an MFM that performs restoration in a single pass, followed by verification stages to determine whether the result warrants further processing. Under our harness, off-the-shelf MFMs handle restoration tasks remarkably well, achieving state-of-the-art results on the widely used MiO100 synthetic benchmark. More importantly, by exploiting the strong generalization ability of MFMs, HarnessIR delivers compelling restoration quality on challenging real-world scenes where previous agentic IR systems often struggle. Codes is available at https://github.com/PolyU-VCLab/HarnessIR.

## 背景與目的
Real-world low-quality images suffer from complex mixed degradations, including but not limited to noise, blur, atmospheric effects, etc. Recent agentic methods usually model real-world image restoration (Real-IR) as a sequential tool calling problem over task-specific single-degradation restoration models. This paradigm, however, is fundamentally limited because complex real-world degradations cannot be cleanly undone degradation by degradation, and the tool used for task-specific models caps t

## 方法
（待補充：需模型或人工分析）

## 結果
（待補充：需模型或人工分析）

## 限制與展望
（待補充：需模型或人工分析）
