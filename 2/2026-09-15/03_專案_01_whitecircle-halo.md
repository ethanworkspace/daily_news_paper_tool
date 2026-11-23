# GitHub 專案 01：whitecircle/halo

- 日期：2026-09-15
- URL：https://github.com/whitecircle/halo
- 描述：Halo is an open-source framework built by White Circle for training large language and multimodal models
- Stars：869  |  Forks：50  |  Language：Python
- License：NOASSERTION
- Topics：agent, async-rl, distributed-training, fine-tuning, grpo, large-language-models, llm, lora, model-parallelism, moe, multimodal, peft, post-training, pytorch, qlora, quantization, reinforcement-learning, rlhf, transformers, vllm
- 更新時間：2026-11-22T08:10:11+00:00
- 配對論文：https://arxiv.org/abs/2606.04036
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Halo 是由 White Circle 開源的訓練框架，專門用於大型語言與多模態模型的預訓練、指令微調（SFT）、偏好優化以及完全非同步多輪強化學習（RL）。它直接操作 Hugging Face 模型，支援單卡到多節點的專家平行（EP）、上下文平行（CP）、張量平行（TP）、專家‑張量平行（ETP）與管線平行（PP），並搭配 FSDP2、DTensor、DeviceMesh 與 DeepEP 等底層原始實作，使得相同程式碼可在不同規模的硬體上運行，並保持標準 SafeTensors 檢查點與 from_pretrained 相容。

## 技術
Halo 以 Python 為主要語言，基於 PyTorch 構建分散式訓練堆疊，使用 Transformers 與 TRL 為高階介紹，並直接載入 Hugging Face 模型。其核心技術包括專家平行（EP）透過 DeepEP V2 實作 all‑to‑all 通訊，上下文平行（CP）與張量平行（TP/ETP）利用 FSDP2、DTensor 與 DeviceMesh 進行權重切分，管線平行（PP）則在各階段內嵌 EP/ETP。效能方面整合 FlashAttention‑4、Liger Kernel、Grouped GEMM、樹狀打包與 padding‑free 等優化，並提供 AdamWBF16 優化器與 BF16 完整精度訓練。針對強化學習，採用 Ray 作為環境 Rollout 的 Actor，與 vLLM 或 SGLang 伺服器進行非同步多輪互動，權重同步經由原生 NCCL 完成。此外，框架提供 Docker 镜像（Blackwell/Hopper）與腳本（halo launch、scripts/training/*.py）以免除主機 Python 環境需求。

## 架構
Halo 的程式碼結構如下：halo/ 目錄存放訓練器、平行ism 實作（EP、CP、TP、ETP、PP）、優化器、自訂核心（kernels）、資料整理器與回調；scripts/ 包含訓練入口、推論、資料前處理與檢查點工具；examples/ 提供依訓練方法與模型分組的可直接運行 YAML 配置；launcher‑configs/ 則有 Accelerate、SkyPilot 與 Nomad 的啟動設定；human‑docs/ 與 agent‑docs/ 分別提供面向使用者與代理的文件；skills/ 內建代理技能，用於作業啟動、平行ism 選擇、除錯、模型加入、檢查點管理、資料準備、吞吐優化、RL 設置、測試編寫與文件維護；tests/ 放置 CPU 與分散式 GPU 單元測試；Dockerfile 與 Makefile 負責映像建置、測試與訓練指令。典型執行流程為：先在 examples/ 中選擇對應的 YAML 配置，然後執行 halo launch <config>（或直接運行 scripts/training/.py），在對應的 Blackwell 或 Hopper Docker 映像內啟動 torchrun 或 accelerate launch，訓練器會載入 Hugging Face 模型，依配置套用對應的平行ism 包裝（EP 包裝 MoE 塊，CP 包裝注意力，TP/ETP 切分權重，PP 分割管線階段），進行前向與反向計算；若啟用 RL，則透過 Ray Actor 呼叫 vLLM/SGLang 伺服器取得環境樣本，經過獎勵計算後將更新的權重經 NCCL 同步回訓練端，完成一個訓練步驟。所有檢查點仍以標準 SafeTensors 形式儲存，可透過 from_pretrained 直接載入。

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
