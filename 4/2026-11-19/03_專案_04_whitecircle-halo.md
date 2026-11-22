# GitHub 專案 04：whitecircle/halo

- 日期：2026-11-19
- URL：https://github.com/whitecircle/halo
- 描述：Halo is an open-source framework built by White Circle for training large language and multimodal models
- Stars：869  |  Forks：50  |  Language：Python
- License：NOASSERTION
- Topics：agent, async-rl, distributed-training, fine-tuning, grpo, large-language-models, llm, lora, model-parallelism, moe, multimodal, peft, post-training, pytorch, qlora, quantization, reinforcement-learning, rlhf, transformers, vllm
- 更新時間：2026-11-22T08:10:11+00:00
- 配對論文：https://arxiv.org/abs/2606.04036
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Halo 是由 White Circle 開放原始碼的訓練框架，專門用於大型語言與多模態模型的預訓練、監督微調（SFT）、偏好優化以及完全非同步多輪強化學習。它直接操作 Hugging Face 模型，支援單卡至多節點的專家平行（EP）、內容平行（CP）、張量平行（TP）、專家‑內容平行（ETP）與管線平行（PP），並提供 BF16 訓練、融合核心、DeepEP V2、FlashAttention‑4、Liger、Grouped GEMM 等效能優化，使研究者與工程師能在同一程式碼基礎上進行從預訓練到強化學習的完整流程。

## 技術
Halo 以 Python 為主要實作語言，基於 PyTorch、Hugging Face Transformers 與 TRL 構建訓練循環，並整合 vLLM 或 SGLang 作為 RL 推論後端。框架內建 FSDP2、DTensor 與 DeviceMesh 為分散式基礎，使用 DeepEP V2 處理 Expert Parallelism 的 all‑to‑all 通訊，並支援 FlashAttention‑4、Liger、Grouped GEMM、樹狀打包、AdamWBF16 優化器以及針對 GLM‑5 Next、Blackwell、Hopper 等架構的回退核心。此外，Halo 提供 LoRA/QLoRA、量化（FP8、BF16）與多種平行策略（EP、CP、TP、ETP、PP）的可組合配置，使得預訓練、微調、偏好優化、蒸餾與強化學習共用同一分散式基礎設施。

## 架構
Halo 的程式碼結構分為數個主要目錄：halo/ 包含訓練器、平行ism（EP/CP/TP/ETP/PP）、優化器、核心函式、資料整理器與回調；scripts/ 提供訓練入口、推論、資料預處理與檢查點工具；examples/ 存放依訓練方法與模型分組的可直接運行 YAML 配置；launcher‑configs/ 包含 Accelerate、SkyPilot 與 Nomad 的啟動設定；human‑docs/ 與 agent‑docs/ 分別提供面向使用者的任務導向指南與完整技術參考；skills/ 包含供 Claude Code、Codex 等 AI 代理使用的職能腳本，用於啟動作業、選擇平行設定、除錯分散式運行、新增模型、管理檢查點、準備資料、優化吞吐量、設定 RL、撰寫測試與維護文件；tests/ 包含 CPU 與分散式 GPU 單元測試；Dockerfile 與 Makefile 負責 Blackwell 與 Hopper 架構的容器映像建置與測試。典型執行流程為：先在 examples/ 中選擇適當的 YAML 配置，然後執行 `halo launch <config>`（或直接運行對應的 Python 腳本），在容器內部 halo 會依據配置選擇 `python`、`torchrun` 或 `accelerate launch` 來啟動訓練，分散式訓練透過 PyTorch 的 FSDP2、DTensor 與 DeviceMesh 進行資料與模型切分，EP 使用 DeepEP V2 進行 all‑to‑all 專家通訊，RL 階段則以 Ray Actor 執行環境輪出，對接 vLLM 或 SGLang 推論伺服器，權重同步透過原生 NCCL 進行，檢查點以標準 SafeTensors 格式儲存，可直接由 `from_pretrained` 載入。

## README 摘錄（節選）
```text
Halo
Frontier-Lab Training for Everyone
Blog post ·
Docs ·
Examples ·
Benchmarks
## What is Halo
Halo is an open-source framework built by White Circle (https://whitecircle.com) for training large language and multimodal models. It supports pre-training, SFT, preference optimization, fully asynchronous multi-turn RL, and much more.
The same codebase runs on one GPU or across multiple nodes, with EP, CP, TP, ETP, PP, FSDP2, fused kernels, BF16 training, and distributed rollouts.
Halo trains Hugging Face models directly. Checkpoints still load with `from_pretrained`, and the EP layer a MoE family adds is under 90 lines for every family but GPT-OSS, at 168 (Model Integration Cost (human-docs/model-integration-cost.md)).
On 8× B300, Halo 1.2.0 trains Qwen3.6-35B-A3B on packed 64k and 128k rows at 1.10–1.12× Megatron Bridge, 1.47× TRL 1.17.1 and 1.9–2.0× NeMo AutoModel 0.7.0, and Qwen3.5-122B-A10B at 1.50× TRL and 1.7–1.9× NeMo; it trails a tuned Megatron by 11.5% on dense Qwen3.5-9B at 64k (Benchmarks (#benchmarks)). It runs 1.11–2.07× as fast as Halo 1.1.0 on the twelve shapes benchmarked against it.
`Pre- & Post-Training` · `EP / CP / TP / ETP / PP` ·
`Multi-Node` · `Verifiable & Multi-Turn RL` · `FA4 + Liger + Grouped GEMM` · `Full BF16`
## Why Halo
- **Halo trains Hugging Face models directly.** Trainers subclass Hugging Face or TRL trainers, checkpoints remain standard SafeTensors, and `from_pretrained` continues to work.
- **Parallelism is added to the existing model.** EP wraps MoE blocks, CP wraps attention, and TP/ETP shard weights in place. There is no separate distributed implementation of the model.
- **The distributed stack is built on PyTorch.** FSDP2, DTensor, and DeviceMesh provide the primitives, and DeepEP handles the all-to-all communication for Expert Parallelism.
- **Each parallelism axis has its own setting.** EP, CP, TP, ETP, and PP are configured separately. EP combines with CP, TP, or ETP, PP combines with EP or ETP, and other pairings are rejected at config time.
- **Training methods share the same infrastructure.** Pre-training, SFT, preference optimization, distillation, and RL use the same parallelism and checkpointing code, so a new method doesn't need its own distributed implementation.
- **SFT can train a release's MTP head.** The multi-token-prediction head that ships for speculative decoding trains beside a fine-tune or over a frozen trunk (MTP heads (agent-docs/optimization/mtp-heads.md)).
- **Performance optimizations are integrated.** Halo includes DeepEP V2, FlashAttention 4, Liger, Grouped GEMM, padding-free and tree packing, AdamWBF16, and kernels for GLM-5 Next, with fallbacks for Blackwell, Hopper, and older GPUs.
- **RL is asynchronous, with a clean Transformers ↔ vLLM/SGLang split.** Multi-turn environment rollouts run as Ray actors against vLLM or SGLang servers, and the trainer pushes updated weights to them over native NCCL. The training side stays plain Transformers, with no Megatron backend or veRL dependency. See Async GRPO with Environments (human-docs/training-methods/async-grpo-environments.md).
## Latest updates
- **2026-11-07 — Halo 1.3.0rc1.** A release candidate for faster RL at scale. On synchronous GRPO with
Qwen3.5-35B-A3B on two 8× B300 nodes, a step takes 0.137 s per 1k response tokens against Miles v0.1.3's 0.176
(GRPO against Miles (agent-docs/optimization/throughput-benchmarks.md#grpo-against-miles)).
- **Faster GRPO:** rows pack into token-budget micro-batches, importance weights can come from the loss forward,
and weight sync can run one group across servers.
- **New in RL:** score centering on SGLang, FP8-weight rollouts for Qwen3.5/3.6 MoE, adapter-only sync to
SGLang, and GLM-5.3-Flash under GRPO.
- **Scale:** gathered EP saves striped over several writers, adapter merges with no model load, and startup
checks for setups that used to fail hours into a run.
- **2026-11-04 — Halo 1.2.0.** Training steps are faster than in 1.1.0 on all twelve shapes benchmarked
aga
```
