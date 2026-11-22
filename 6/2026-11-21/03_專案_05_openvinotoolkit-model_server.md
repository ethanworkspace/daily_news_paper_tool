# GitHub 專案 05：openvinotoolkit/model_server

- 日期：2026-11-21
- URL：https://github.com/openvinotoolkit/model_server
- 描述：A scalable inference server for models optimized with OpenVINO™
- Stars：963  |  Forks：297  |  Language：C++
- License：Apache-2.0
- Topics：ai, cloud, dag, deep-learning, edge, genai, inference, kubernetes, machine-learning, model-serving, openvino, serving
- 更新時間：2026-11-22T00:26:56+00:00
- 配對論文：
- 品質分數：9/10 [implementation_signals]

## 在做什麼
A scalable inference server for models optimized with OpenVINO™
A scalable inference server for models optimized with OpenVINO™

主要語言：C++；Topics：ai, cloud, dag, deep-learning, edge, genai, inference, kubernetes；Stars：963；License：Apache-2.0

## 技術
實作語言以 C++ 為主。
從 topics 可見技術方向：ai, cloud, dag, deep-learning, edge, genai, inference, kubernetes。
專案描述：A scalable inference server for models optimized with OpenVINO™

## 架構
README 未明確提供架構章節；依描述推斷此專案聚焦於：A scalable inference server for models optimized with OpenVINO™

## README 摘錄（節選）
```text
# OpenVINO&trade; Model Server
** High-performance model serving for Generative AI and classic deep learning — powered by OpenVINO (https://github.com/openvinotoolkit/openvino) and optimized for Intel hardware.**
(https://github.com/openvinotoolkit/model_server/blob/main/LICENSE)
(https://hub.docker.com/r/openvino/model_server)
(https://github.com/openvinotoolkit/model_server/releases)
(https://docs.openvino.ai/2026/model-server/ovms_docs_deploying_server.html)
--- 
## What is OVMS?
OpenVINO Model Server (OVMS) is a production-grade, C++ inference server that exposes ML models over standard network APIs. It serves both **Generative AI**, **Agentic** workloads (LLMs, VLMs, image generation, audio) and **classic deep learning** models (object detection, classification, OCR, and more).
- **OpenAI-compatible API** for text generation, embeddings, image generation, and audio
- **KServe** APIs for classic model inference
- **Runs anywhere** — Docker, bare metal, Kubernetes/OpenShift, Windows
- **Intel-optimized** — CPU, GPU, NPU acceleration via OpenVINO
--- 
## Quick Start
### Serve an LLM with OpenAI-compatible API
** On Linux (Docker):**
[code block omitted]
> For GPU acceleration, use the `latest-gpu` image tag and pass `--device /dev/dri --group-add $(stat -c '%g' /dev/dri/render* | head -n1)` to expose the Intel GPU device.
** On Windows (binary package):**
[code block omitted]
** Query the model:**
[code block omitted]
[code block omitted]
> LLM QuickStart (https://docs.openvino.ai/2026/model-server/ovms_docs_llm_quickstart.html)
### Serve a Classic Model with KServe API
** Download the model:**
[code block omitted]
** On Linux (Docker):**
[code block omitted]
> For GPU acceleration, use the `latest-gpu` image tag and pass `--device /dev/dri --group-add $(stat -c '%g' /dev/dri/render* | head -n1)` to expose the Intel GPU device.
** Windows (binary package):**
[code block omitted]
Run inference with a sample client
[code block omitted]
[code block omitted]
> Vision model QuickStart (https://docs.openvino.ai/2026/model-server/ovms_docs_quick_start_guide.html)
--- 
## Features
### Generative AI
- LLM text generation (https://docs.openvino.ai/2026/model-server/ovms_demos_continuous_batching.html) — continuous batching, streaming, structured output, speculative decoding
- VLM (Vision Language Models) (https://docs.openvino.ai/2026/model-server/ovms_demos_continuous_batching_vlm.html)
- AI Agents with MCP servers (https://docs.openvino.ai/2026/model-server/ovms_demos_continuous_batching_agent.html)
- Text embeddings (https://docs.openvino.ai/2026/model-server/ovms_demos_embeddings.html) — OpenAI-compatible `/v1/embeddings`
- Reranking (https://docs.openvino.ai/2026/model-server/ovms_demos_rerank.html) — Cohere-compatible API
- Image generation (https://docs.openvino.ai/2026/model-server/ovms_demos_image_generation.html) — OpenAI-compatible `/v1/images/generations`
- Speech recognition and TTS (https://docs.openvino.ai/2026/model-server/ovms_demos_audio.html) — OpenAI-compatible audio API
- GGUF model support (https://docs.openvino.ai/2026/model-server/ovms_demos_gguf.html)
### Classic Models & Pipelines
- TensorFlow, ONNX, PaddlePaddle, OpenVINO IR model formats
- MediaPipe graphs (https://docs.openvino.ai/2026/model-server/ovms_docs_mediapipe.html)
- Python execution nodes (https://docs.openvino.ai/2026/model-server/ovms_docs_python_support_reference.html)
- Dynamic input shapes (https://docs.openvino.ai/2026/model-server/ovms_docs_dynamic_input.html)
### Deployment & Integration
- Docker (docs/deploying_server_docker.md), bare metal (Linux & Windows) (docs/deploying_server_baremetal.md), Kubernetes / OpenShift (docs/deploying_server_kubernetes.md)
- Model repository (https://docs.openvino.ai/2026/model-server/ovms_docs_models_repository.html): local storage, S3, GCS, Azure Blob, HuggingFace Hub
- Model versioning (https://docs.openvino.ai/2026/model-server/ovms_docs_model_version_policy.html) and hot-reload (https://docs.openvino
```
