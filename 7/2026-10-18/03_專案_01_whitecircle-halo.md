# GitHub 專案 01：whitecircle/halo

- 日期：2026-10-18
- URL：https://github.com/whitecircle/halo
- 描述：Halo is an open-source framework built by White Circle for training large language and multimodal models
- Stars：869  |  Forks：49  |  Language：Python
- License：NOASSERTION
- Topics：agent, async-rl, distributed-training, fine-tuning, grpo, large-language-models, llm, lora, model-parallelism, moe, multimodal, peft, post-training, pytorch, qlora, quantization, reinforcement-learning, rlhf, transformers, vllm
- 更新時間：2026-11-22T08:10:11+00:00
- 配對論文：https://arxiv.org/abs/2606.04036
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Halo 是由 White Circle 開源的訓練框架，專門用於大型語言與多模態模型的預訓練、微調（SFT）、偏好優化以及完全非同步多輪強化學習。它支援單 GPU 到多節點的分散式訓練，整合了專家平行（EP）、內容平行（CP）、張量平行（TP）、專家‑內容平行（ETP）與管線平行（PP），並直接使用 Hugging Face 模型，使檢查點可透過 from_pretrained 載入。目標使用者為希望在不切換後端的情況下，利用現有模型與資料進行大規模 LLM 訓練的研究者與工程師，核心問題在於簡化分散式訓練的設定與維護，提供統一的基礎設施以支援各種訓練方法。

## 技術
Halo 以 Python 為主要語言，建基於 PyTorch、Transformers 與 TRL，並整合 vLLM 或 SGLang 作為推論後端。框架內含 DeepEP V2、FlashAttention‑4、Liger、Grouped GEMM、padding‑free 與 tree packing 優化，支援 BF16、FP8 量化與 AdamWBF16 優化器。透過 FSDP2、DTensor 與 DeviceMesh 實現資料與模型平行，EP 包裝 MoE 塊，CP 包裝注意力，TP/ETP 在原位切分權重，PP 則可與 EP/ETP 組合。此外，Halo 直接訓練 Hugging Face 模型，檢查點採用標準 SafeTensors，LoRA/QLoRA 與模型整合成本低（EP 層僅約 90 行程式碼）。

## 架構
Halo 的程式碼分為 halo/（訓練器、平行性、優化器、核心函式、資料整理器與回呼）、scripts/（訓練入口、推論、資料前處理與檢查點工具）、examples/（依方法與模型分組的可直接運行 YAML 設定）、launcher-configs/（Accelerate、SkyPilot、Nomad 啟動配置）、human-docs/ 與 agent-docs/（使用者與代理人文件）、skills/（代理技能模組）以及 tests/、Dockerfile、Makefile。典型流程：使用者選取 examples/ 中的 YAML 配置，執行 halo launch（或直接呼叫 scripts/training/.py），halo 依參數選擇 python、torchrun 或 accelerate launch 啟動分散式作業。訓練器載入 Hugging Face 模型，依配置加入 EP、CP、TP、ETP 或 PP 包裝層，權重透過 DTensor/DeviceMesh 進行分片，梯度同步使用 NCCL 或 DeepEP 的 all‑to‑all。在 RL 中，多輪環境 rollout 以 Ray Actor 運行於 vLLM/SGLang 伺服器，訓練端透過原生 NCCL 將更新權重推送至推論端完成非同步更新。檢查點採用標準 SafeTensors，可直接由 from_pretrained 載入。

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
