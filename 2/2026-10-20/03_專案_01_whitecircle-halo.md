# GitHub 專案 01：whitecircle/halo

- 日期：2026-10-20
- URL：https://github.com/whitecircle/halo
- 描述：Halo is an open-source framework built by White Circle for training large language and multimodal models
- Stars：869  |  Forks：49  |  Language：Python
- License：NOASSERTION
- Topics：agent, async-rl, distributed-training, fine-tuning, grpo, large-language-models, llm, lora, model-parallelism, moe, multimodal, peft, post-training, pytorch, qlora, quantization, reinforcement-learning, rlhf, transformers, vllm
- 更新時間：2026-11-22T08:10:11+00:00
- 配對論文：https://arxiv.org/abs/2606.04036
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Halo 是由 White Circle 開發的開源訓練框架，專門用於大型語言與多模態模型的預訓練、監督微調（SFT）、偏好優化以及完全非同步多輪強化學習（RL）。它支援單 GPU 到多節點的擴展，並直接訓練 Hugging Face 模型，保持標準 SafeTensors 检查點與 from_pretrained 相容。目標使用者為研究與工程團隊，他們需要一個統一的基礎設施來進行各種訓練方法，而無需為每種方法重新實作分散式程式碼。

## 技術
Halo 以 Python 為主要語言，基於 PyTorch、Transformers 與 TRL 建構。訓練過程可使用 FSDP2、DTensor、DeviceMesh 進行資料與模型並行，並支援 Expert Parallelism (EP)、Context Parallelism (CP)、Tensor Parallelism (TP)、Expert‑Tensor Parallelism (ETP) 與 Pipeline Parallelism (PP)。效能優化整合了 DeepEP V2、FlashAttention 4、Liger、Grouped GEMM、BF16 AdamW 優化器以及針對 GLM‑5 Next 的自訂核心。為非同步多輪 RL，框架透過 Ray Actor 與 vLLM 或 SGLang 伺服器進行環境 rollout，權重同步則利用原生 NCCL。此外，Halo 提供 Docker 镜像（Blackwell/Hopper）以及 LoRA/QLora、PEFT 支援，使得模型整合成本低且可直接使用 Hugging Face 的 from_pretrained 載入检查點。

## 架構
Halo 的程式碼結構如下：halo/ 包含訓練器、並行性封裝（EP、CP、TP、ETP、PP）、優化器、核心函式、資料整理器與回調；scripts/ 提供訓練入口、推理、資料預處理與检查點工具；examples/ 存放依訓練方法與模型分組的可直接運行 YAML 配置；launcher-configs/ 包含 Accelerate、SkyPilot 與 Nomad 的啟動設定；human-docs/ 與 agent-docs/ 分別提供面向使用者與代理的文件；skills/ 包含供 Claude Code、Codex 等代理使用的啟動、除錯、模型加入等腳本。典型執行流程為：使用者選取 examples/ 中的 YAML 配置，執行 `halo launch <config>`（或直接呼叫 scripts/training/*.py），halo 會依參數選擇 python、torchrun 或 accelerate launch 啟動訓練。訓練器會將模型套用對應的並行性封裝（例如 EP 包裝 MoE 塊，CP 包裝注意力，TP/ETP 進行權重切分），訓練循環中利用 PyTorch 的分散式原始進行前向與反向傳播。在 RL 場景中，訓練端透過 NCCL 將更新後的權重推送至運行 vLLM 或 SGLang 的 Ray Actor 伺服器，伺服器產生多輪環境 rollout 並將經驗返回訓練端進行梯度更新。检查點採用標準 SafeTensors 格式，可直接由 `from_pretrained` 載入。若 README 未提供足夠細節，則上述架構說明僅基於可見的模組與資料流程描述。

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
