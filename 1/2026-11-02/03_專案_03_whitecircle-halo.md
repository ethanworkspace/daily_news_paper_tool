# GitHub 專案 03：whitecircle/halo

- 日期：2026-11-02
- URL：https://github.com/whitecircle/halo
- 描述：Halo is an open-source framework built by White Circle for training large language and multimodal models
- Stars：869  |  Forks：50  |  Language：Python
- License：NOASSERTION
- Topics：agent, async-rl, distributed-training, fine-tuning, grpo, large-language-models, llm, lora, model-parallelism, moe, multimodal, peft, post-training, pytorch, qlora, quantization, reinforcement-learning, rlhf, transformers, vllm
- 更新時間：2026-11-22T08:10:11+00:00
- 配對論文：https://arxiv.org/abs/2606.04036
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Halo 是一個由 White Circle 開源的訓練框架，專注於大型語言與多模態模型的預訓練、微調（SFT）、偏好優化以及完全非同步多輪強化學習。它直接操作 Hugging Face 模型，支援單卡到多節點的各種平行策略（EP、CP、TP、ETP、PP、FSDP2），旨在降低分散式訓練的實作複雜度，讓研究者與工程師能在不改動模型程式碼的情況下，使用統一的基礎設施進行不同訓練任務。

## 技術
Halo 以 Python 為主要語言，基礎建置於 PyTorch、Transformers、TRL、vLLM 與 SGLang。它整合了 DeepEP V2（專家平行）、FlashAttention‑4、Liger、Grouped GEMM、BF16/FP8 精度、FSDP2、DTensor、DeviceMesh 以及自訂 kernels（GLM‑5 Next 等）。平行ism 以獨立設定的 EP、CP、TP、ETP、PP 軸實作，透過包裝現有模型的 MoE 塊、注意力或權重分片來達成，無需另行實作分散式模型。RL 部分採用 Ray actor 作為 vLLM/SGLang 推論伺服器，訓練端透過 NCCL 同步權重。

## 架構
程式碼結構分為 halo/（訓練器、平行ism、優化器、kernels、collators、callbacks）、scripts/（訓練入口、推論、資料準備、checkpoint 工具）、examples/（依方法與模型分組的可直接運行 YAML 配置）、launcher‑configs/（Accelerate、SkyPilot、Nomad 啟動設定）以及 human‑docs/與 agent‑docs/說明文件。典型執行流程：使用者選取 examples/ 中的配置，執行 `halo launch <config>`（內部依參數選擇 python、torchrun 或 accelerate launch），載入 Hugging Face 模型，根據配置套用 EP/CP/TP/ETP/PP 等平行ism 包裝（EP 透過 DeepEP V2 進行 all‑to‑all，CP/TP/ETP 透過 DeviceMesh 分片，PP 則在各階段內嵌其他平行ism），訓練器負責前向、反向與參數更新；若為 RL 工作流，則透過 Ray actor 啟動 vLLM/SGLang 伺服器進行環境 rollout，訓練端以 NCCL 推送權重更新；checkpoint 以 SafeTensors 格式儲存，可直接由 `from_pretrained` 載入。整個流程在單 GPU 或多節點上皆可運行，無需維護獨立的分散式模型實作。

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
