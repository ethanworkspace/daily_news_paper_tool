# GitHub 專案 02：sgl-project/sglang

- 日期：2026-11-21
- URL：https://github.com/sgl-project/sglang
- 描述：SGLang is a high-performance serving framework for large language models and multimodal models.
- Stars：38921  |  Forks：10702  |  Language：Python
- License：Apache-2.0
- Topics：attention, blackwell, cuda, deepseek, diffusion, glm, gpt-oss, inference, llama, llm, minimax, moe, qwen, qwen-image, reinforcement-learning, transformer, vlm, wan
- 更新時間：2026-11-22T06:16:32+00:00
- 配對論文：
- 品質分數：10/10 [implementation_signals]

## 在做什麼
SGLang is a high-performance serving framework for large language models and multimodal models.
SGLang is a high-performance serving framework for large language models and multimodal models.

主要語言：Python；Topics：attention, blackwell, cuda, deepseek, diffusion, glm, gpt-oss, inference；Stars：38921；License：Apache-2.0

## 技術
實作語言以 Python 為主。
從 topics 可見技術方向：attention, blackwell, cuda, deepseek, diffusion, glm, gpt-oss, inference。
專案描述：SGLang is a high-performance serving framework for large language models and multimodal models.

## 架構
README 未明確提供架構章節；依描述推斷此專案聚焦於：SGLang is a high-performance serving framework for large language models and multimodal models.

## README 摘錄（節選）
```text
# SGLang: Fast inference for LLMs and multimodal models
Docs |
Cookbook |
Website |
Blog |
Slack
SGLang is an open-source inference framework for large language, vision-language, and diffusion models, optimized for agentic workloads, large-scale serving, and RL rollouts. SGLang Diffusion (https://docs.sglang.io/docs/sglang-diffusion) is its built-in engine for image, video, audio, and action generation, included in this repository and the `sglang` Python package.
👋 Get started below, or meet the community at SGLang Events (https://www.sglang.io/events), including meetups, developer meetings, workshops, and office hours.
> **SGLang Summit 2026: Meet the builders of open AI (https://www.sglang.io/summit)**
> **Our flagship annual gathering · November 12–13 · San Francisco**
> 
> Go deep on inference, training, and AI hardware through technical talks, live demos, and hands-on workshops. Bring your deployment challenges and meet the engineers and researchers building the stack.
## Get Started
Pull the Docker image, which includes SGLang and its dependencies:
[code block omitted]
Alternatively, install SGLang in an activated Python environment with uv:
[code block omitted]
Next, launch your model:
- Quickstart (https://docs.sglang.io/docs/get-started/quickstart): Run your first model and send a request.
- Cookbook (https://cookbook.sglang.io/): Choose your model and hardware to get a ready-to-run launch command.
## Supported Hardware
SGLang supports a wide range of GPUs, TPUs, NPUs, CPUs, and Apple Silicon platforms.
| Platform | Representative hardware |
| --- | --- |
| NVIDIA (https://docs.sglang.io/docs/hardware-platforms/nvidia-gpus) | B200/B300/GB200/GB300; H100/H200/H800/H20; A100; RTX 30/40/50 series, RTX 6000 Ada / PRO 6000; DGX Spark, Jetson Orin |
| AMD (https://docs.sglang.io/docs/hardware-platforms/amd_gpu) | Instinct MI300X, MI325X, MI350X, MI355X |
| Google TPU (https://docs.sglang.io/docs/hardware-platforms/tpu) | v6e, v7; SGLang-TorchTPU (https://github.com/sgl-project/sglang-torchtpu) / SGL-JAX (https://github.com/sgl-project/sglang-jax) |
| Intel (GPU (https://docs.sglang.io/docs/hardware-platforms/xpu) / CPU (https://docs.sglang.io/docs/hardware-platforms/cpu_server)) | Arc / Arc Pro B-Series GPUs, Xeon CPUs |
| Apple Silicon (https://docs.sglang.io/docs/hardware-platforms/apple_metal) | Macs via Metal / MLX |
| Huawei Ascend (https://docs.sglang.io/docs/hardware-platforms/ascend-npus/getting-started/installation) | A2, A3, 950PR/DT NPUs |
| Moore Threads (https://docs.sglang.io/docs/hardware-platforms/mthreads_gpu) | MTT S5000 GPUs |
Integrations in progress: AWS Trainium, Alibaba T-Head PPU (https://github.com/sgl-project/sglang/issues/37519), Cambricon MLU (https://github.com/sgl-project/sglang/pull/26898), Qualcomm QAIC, MetaX, Hygon HCU/DCU, Iluvatar CoreX, and more.
SGLang-TorchTPU brings the SGLang serving engine to Google TPUs through PyTorch, torch_tpu, and Pallas kernels. It supports LLM and vision-language serving on TPU7x (Ironwood), including tensor and expert parallelism across hosts. SGL-JAX provides the JAX-based TPU serving path.
See the Cookbook (https://cookbook.sglang.io/) and platform guides for model compatibility and setup.
## SGL Ecosystem
| Area | Projects | Purpose |
| --- | --- | --- |
| Diffusion | SGLang Diffusion (https://docs.sglang.io/docs/sglang-diffusion/installation) | Built into SGLang for image, video, audio, and action generation. |
| Audio | SGLang Omni (https://github.com/sgl-project/sglang-omni) | Audio model serving for text-to-speech (TTS) and automatic speech recognition (ASR). |
| Speculative Decoding | SpecForge (https://github.com/sgl-project/SpecForge) | Train draft models for speculative decoding and deploy them with SGLang. |
| RL and Post-Training | Miles (https://github.com/radixark/miles), slime (https://github.com/THUDM/slime), AReaL (https://github.com/inclusionAI/AReaL), Tunix (https://github.com/google/tunix), verl (https://github.com/volcengine/verl) | Tra
```
