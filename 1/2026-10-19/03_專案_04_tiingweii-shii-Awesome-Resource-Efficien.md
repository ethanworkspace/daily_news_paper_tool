# GitHub 專案 04：tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers

- 日期：2026-10-19
- URL：https://github.com/tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers
- 描述：a curated list of high-quality papers on resource-efficient LLMs 🌱
- Stars：168  |  Forks：14  |  Language：unknown
- License：CC0-1.0
- Topics：efficient-deep-learning, generative-ai, large-language-models, machine-learning, machine-learning-systems, resource-efficient, survey
- 更新時間：2026-11-20T11:36:17+00:00
- 配對論文：https://doi.org/10.1145/3845797
- 品質分數：3/10 [collection, collection_name, no_language, paper_paired, stale_seed, collection_paired_override]

## 在做什麼
這個專案是一個精心維護的論文清單，收錄了與資源效率大型語言模型（LLM）相關的高品質學術論文。它旨在為研究人員、工程師與產業開發者提供一個快速檢索與學習的資源，幫助他們了解在模型架構、訓練、微調、推理與部署等各個階段如何降低計算、記憶體、能源與金錢成本。透過該清單，使用者可以追蹤最新的有效注意力機制、非Transformer架構、分散式訓練、混合精度、參數高效微調、模型壓縮等技術進展，從而在資源受限的環境中設計與部署更實用的LLM系統。

## 技術
該專案本身不包含程式碼或模型實作，而是以 GitHub 的 Markdown 形式呈現論文清單。清單依照主題分類，涵蓋了語言（主要為英文論文）、框架（如 xFormers、FasterTransformer、LightSeq、FairScale、Megatron‑LM、Alpa、GPipe、PipeDream 等）、模型架構（高效 Transformer、非 Transformer 如 RWKV、Hyena、Mamba、MoE 等）、訓練技術（分散式資料/模型並行、混合精度 FP8/FP4、記憶體優化）、推理與系統設計（模型壓縮、量化、剪枝、動態加速、輸入裁剪、部署優化）以及評估指標（計算、記憶體、能源、財務、網路通訊等）。這些內容均來自於該 repo 的 README 與目錄結構，可見的技術重點即是對上述論文的彙整與分類。

## 架構
README 以目錄結構組織論文，頂層為「Table of Contents」，下分為 LLM Architecture Design（含 Efficient Transformer Architecture 與 Non‑transformer Architecture）、LLM Pre‑Training（Memory Efficiency、Distributed Training、Mixed precision training）、LLM Fine‑Tuning、LLM Inference、Model Compression、System Design、Resource‑Efficiency Evaluation Metrics & Benchmarks 等章節。每個章節內以 Markdown 表格列出論文的日期、關鍵字、標題連結與發表會議或期刊。使用者透過瀏覽該 README 可依主題快速定位相關論文；該 repo 沒有執行時的資料流程或模組間互動，僅為靜態的文檔索引。因此架構說明主要是說明其文件組織方式與瀏覽流程，若需了解實際的程式碼或推論管線則該專案未提供，故此處的描述基於可見的目錄與表格資訊。

## README 摘錄（節選）
```text
# Awesome Resource-Efficient LLM Papers (https://awesome.re)
A curated list of high-quality papers on resource-efficient LLMs. (constantly updated)
This is the GitHub repo for our survey paper Beyond Efficiency: A Systematic Survey of Resource-Efficient Large Language Models (https://arxiv.org/pdf/2401.00625). The paper has been published at ACM Computing Survey (CSUR) (https://dl.acm.org/doi/full/10.1145/3845797)
⭐ **If you find our repo helpful, please consider starring ⭐ it—we’d really appreciate your support!** ⭐
## Table of Contents
- Awesome Resource-Efficient LLM Papers (#awesome-resource-efficient-llm-papers-)
- Table of Contents (#table-of-contents)
- LLM Architecture Design (#llm-architecture-design)
- Efficient Transformer Architecture (#efficient-transformer-architecture)
- Non-transformer Architecture (#non-transformer-architecture)
- LLM Pre-Training (#llm-pre-training)
- Memory Efficiency (#memory-efficiency)
- Distributed Training (#distributed-training)
- Mixed precision training (#mixed-precision-training)
- Data Efficiency (#data-efficiency)
- Importance Sampling (#importance-sampling)
- Data Augmentation (#data-augmentation)
- Training Objective (#training-objective)
- LLM Fine-Tuning (#llm-fine-tuning)
- Parameter-Efficient Fine-Tuning (#parameter-efficient-fine-tuning)
- Full-Parameter Fine-Tuning (#full-parameter-fine-tuning)
- LLM Inference (#llm-inference)
- Model Compression (#model-compression)
- Pruning (#pruning)
- Quantization (#quantization)
- Dynamic Acceleration (#dynamic-acceleration)
- Input Pruning (#input-pruning)
- System Design (#system-design)
- Deployment optimization (#deployment-optimization)
- Support Infrastructure (#support-infrastructure)
- Other Systems (#other-systems)
- Resource-Efficiency Evaluation Metrics \& Benchmarks (#resource-efficiency-evaluation-metrics--benchmarks)
- 🧮 Computation Metrics (#-computation-metrics)
- 💾 Memory Metrics (#-memory-metrics)
- ⚡️ Energy Metrics (#️-energy-metrics)
- 💵 Financial Cost Metric (#-financial-cost-metric)
- 📨 Network Communication Metric (#-network-communication-metric)
- 💡 Other Metrics (#-other-metrics)
- Benchmarks (#benchmarks)
- Reference (#reference)
## LLM Architecture Design
### Efficient Transformer Architecture
| Date | Keywords | Paper | Venue |
| :---------: | :------------: | :-----------------------------------------:| :---------: |
| 2025 | Approximate attention | S2-Attention: Hardware-Aware Context Sharding Among Attention Heads (https://arxiv.org/abs/2407.17678) | ArXiv |
| 2025 | Hardware optimization | Explore Activation Sparsity in Recurrent LLMs for Energy-Efficient Neuromorphic Computing (https://arxiv.org/abs/2501.16337) | AICAS |
| 2024 | Approximate attention | Simple linear attention language models balance the recall-throughput tradeoff (https://arxiv.org/abs/2402.18668) | ArXiv |
| 2024 | Hardware optimization | MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases (https://arxiv.org/abs/2402.14905) | ArXiv |
| 2024 | Approximate attention | LoMA: Lossless Compressed Memory Attention (https://arxiv.org/abs/2401.09486) | ArXiv |
| 2024 | Approximate attention | Two Stones Hit One Bird: Bilevel Positional Encoding for Better Length Extrapolation (https://arxiv.org/pdf/2401.16421) | ICML |
| 2024 | Hardware optimization | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning (https://arxiv.org/abs/2307.08691) | ICLR |
| 2023 | Hardware optimization | Flashattention: Fast and memory-efficient exact attention with io-awareness (https://proceedings.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html) | NeurIPS |
| 2023 | Approximate attention | KDEformer: Accelerating Transformers via Kernel Density Estimation (https://arxiv.org/abs/2302.02451) | ICML|
| 2023 | Approximate attention | Mega: Moving Average Equipped Gated Attention (https://openreview.net/forum?id=qNLe3iq2El) | ICLR|
| 2022 | Hardware optimizatio
```
