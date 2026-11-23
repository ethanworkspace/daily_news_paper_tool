# GitHub 專案 02：openvinotoolkit/model_server

- 日期：2026-11-21
- URL：https://github.com/openvinotoolkit/model_server
- 描述：A scalable inference server for models optimized with OpenVINO™
- Stars：965  |  Forks：298  |  Language：C++
- License：Apache-2.0
- Topics：ai, cloud, dag, deep-learning, edge, genai, inference, kubernetes, machine-learning, model-serving, openvino, serving
- 更新時間：2026-11-22T16:56:21+00:00
- 配對論文：
- 品質分數：9/10 [implementation_signals]

## 在做什麼
OpenVINO Model Server（OVMS）是一個以 C++ 實作的高性能推理伺服器，專門針對經 OpenVINO 優化的模型提供服務。它同時支援生成式 AI（LLM、VLM、圖像/音訊生成、AI Agent）與傳統深度學習模型（物件偵測、分類、OCR 等），透過 OpenAI‑相容的 REST/gRPC API 與 KServe API 對外暴露模型。OVMS 可在 Docker、裸機、Kubernetes/OpenShift、Windows 等環境運行，並利用 Intel CPU、整合/離散 GPU 及 NPU 進行硬體加速，目標使用者為需要在 Intel 硬體上進行低延遲、可擴充模型服務的 ML 工程師、DevOps 與應用開發者，解決模型部署、版本管理與異質硬體加速的統一難題。

## 技術
OVMS 基於 C++ 與 OpenVINO Toolkit 建構，支援 TensorFlow、ONNX、PaddlePaddle 與 OpenVINO IR 等模型格式，並提供 GGUF、MediaPipe 圖形、Python 執行節點等擴展。伺服器內部實作 OpenAI‑相容的文字生成、嵌入、圖像/音訊生成 API，以及 KServe 的標準 gRPC/REST 推論介面，具備連續批次處理、串流、結構化輸出、推測性解碼等功能。透過模型倉儲功能可從本機儲存、S3、GCS、Azure Blob 或 HuggingFace Hub 拉取模型，支援模型版本控制與熱重載。此外，OVMS 提供 Prometheus 相容的指標、gRPC 串流端點、C API 供原生應用嵌入，並透過 Docker image、Linux/Windows 二進位套件與 Kubernetes/OpenShift 部署文件實現跨平台部署。硬體加速層級透過 OpenVINO 的裝置抽象實現 CPU、Intel GPU 與 NPU 的統一調度。

## 架構
OVMS 的架構可劃分為四個主要層：(1) API 層，提供 OpenAI‑相容 REST/gRPC 端點與 KServe gRPC/REST 端點，負責請求解析與響應組裝；(2) 模型倉儲與配置管理層，負責從本機或雲端儲存庫載入模型、處理版本標籤與熱重載設定；(3) 推論引擎層，基於 OpenVINO 的執行階段，進行裝置抽象（CPU/GPU/NPU）、批次調度、連續批次、串流及推測性解碼等運算；(4) 基礎設施層，包括 Prometheus 指標匯出、gRPC 串流支援、C API 介面以及容器/二進位打包工具。資料流程為：客戶請求經 API 層解析後，呼叫模型倉儲取得對應版本的模型檔案，隨即送至推論引擎執行 OpenVINO 優化的計算，結果經 API 層序列化後回傳給客戶。整個設計模組化且可熱更新，適合在 Docker、裸機或 K8s 環境中水平擴充。若 README 未明確說明內部執行緒調度或細部錯誤處理機制，則該部份為基於上述描述的合理推斷。

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
