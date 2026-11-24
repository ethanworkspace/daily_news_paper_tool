# GitHub 專案 02：tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers

- 日期：2026-10-25
- URL：https://github.com/tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers
- 描述：a curated list of high-quality papers on resource-efficient LLMs 🌱
- Stars：168  |  Forks：14  |  Language：unknown
- License：CC0-1.0
- Topics：efficient-deep-learning, generative-ai, large-language-models, machine-learning, machine-learning-systems, resource-efficient, survey
- 更新時間：2026-11-20T11:36:17+00:00
- 配對論文：https://doi.org/10.1145/3845797
- 品質分數：3/10 [collection, collection_name, no_language, paper_paired, stale_seed, collection_paired_override]

## 在做什麼
本專案維護一份高品質論文清單，聚焦於資源效率高的大型語言模型（LLM）研究，提供論文標題、作者、發表會議與 arXiv 鏈接，旨在協助研究人員與工程師快速檢索與了解最新的效率優化技術。

## 技術
該專案採用 Markdown 格式撰寫，以 GitHub 作為托管平台，內容以區段標題與表格呈現，每筆論文條目包含日期、關鍵詞、論文連結與發表會議或期刊資訊，無需編譯或執行環境，僅靠靜態檔案即可瀏覽與搜尋。

## 架構
該倉庫的架構純粹是靜態文件組織：README.md 作為總目錄，底下依照主題（如 LLM 架構設計、預訓練、微調、推理、系統設計等）設定二級標題，每個標題下使用 Markdown 表格列出相關論文的日期、關鍵詞、論文連結與發表場地。資料流程僅為使用者瀏覽或搜尋該 Markdown 檔案，沒有後端服務、模型推論或資料處理管線。若需進一步的互動功能（如關鍵字搜尋），則必須依賴使用者自行實作或使用 GitHub 的搜尋功能。

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
