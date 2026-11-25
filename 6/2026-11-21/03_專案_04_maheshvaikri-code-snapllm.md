# GitHub 專案 04：maheshvaikri-code/snapllm

- 日期：2026-11-21
- URL：https://github.com/maheshvaikri-code/snapllm
- 描述：🔥 Alternative to Ollama — multi-model serving with sub-ms model switching · CPU-only 20B inference for Edge AI · llama.cpp + stablediffusion.cpp
- Stars：44  |  Forks：4  |  Language：C++
- License：NOASSERTION
- Topics：agentic-ai, cpu-inference, edge-ai, llm, llm-inference, llm-serving, llm-tools, local-llm, model-serving, multi-model, multimodal, ollama-alternative
- 更新時間：2026-11-15T09:35:12+00:00
- 配對論文：https://doi.org/10.32388/7mldm5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
SnapLLM 是一個基於 llama.cpp 與 stable-diffusion.cpp 的本地多模型推理引擎，旨在提供 Ollama 的替代方案，支援同時載入多個 LLM、視覺語言模型與擴散模型，透過常駐模型選擇機制實現毫秒級模型切換，並提供 OpenAI 相容的 REST API、React/Vite 桌面 UI 與 CLI，適用於需要在邊緣設備或工作站上進行低延遲、多域 AI 服務的開發者與研究者。

## 技術
SnapLLM 使用 C++ 實作核心推理引擎，依賴 llama.cpp 處理 GGUF 格式的文字模型與 stable-diffusion.cpp 處理 Stable Diffusion 系列模型；桌面應用採用 React 與 Vite 建構，Node.js 18+ 作為開發環境；透過 CMake 編譯，支援 GPU/CPU 混合層分配（需 CUDA 12.x），提供 OpenAI 相容的 API endpoints，實作 vPID（Virtual Processing‑In‑Disk）架構分為 L1 模型快取與 L2 KV 快取，並採用記憶體分層（HOT GPU VRAM、WARM CPU RAM、COLD SSD）管理模型與上下文，同時提供 Docker 镜像與健康檢查。

## 架構
SnapLLM 的架構分為三層：伺服器核心（C++）負責模型載入、切換與推理；vPID 系統提供 L1 模型快取（模型工作區與引擎管理資料）與 L2 KV 快取（雜湊索引的上下文持久化），依據可用資源將模型層放置於 HOT（GPU VRAM）、WARM（CPU RAM）或 COLD（SSD）層；API 層 expose REST endpoints（/v1/chat/completions、/api/v1/models/* 等），內部流程為：客戶請求 → API 金鑰驗證 → 路由至對應 handler → 若需載入模型則透過 /api/v1/models/load 將模型檔案映射至工作區並放入適當記憶體層；切換已載入模型僅更新 vPID 指標，避免重新載入權重；文字生成走向 llama.cpp 推理管道，視覺或圖像生成則呼叫 stable-diffusion.cpp；桌面 UI 透過 Vite 在 localhost:9780 提供 React 應用，與 API 透過 WebSocket 或 fetch 交互；Docker 容器將服務綁定至 127.0.0.1:6930，僅開放 loopback 並可透過 SNAPLLM_API_KEY 與 CORS 設定控制對外存取。README 未提供詳細序列圖，以上說明基於文中描述的模組與流程推斷。

## README 摘錄（節選）
```text
Local Multi-Model LLM Inference with Desktop UI, CLI & API
Preprint Paper Link (https://doi.org/10.32388/7MLDM5)
🤩 Star this repository - It helps others discover SnapLLM 🤩
Features |
Installation |
Quick Start |
API Reference |
Architecture |
Demo Videos |
Contributing |
Sponsors
Developed by Mahesh Vaikri
--- 
## What is SnapLLM?
SnapLLM is a local inference engine built on llama.cpp and
stable-diffusion.cpp. It can keep multiple models loaded and select an
already-resident model without reloading its weights. Actual load, switch, and
generation latency depends on model size, hardware, memory pressure, and build
configuration; benchmark your own workload before setting latency targets.
### The Problem
One common single-resident-model workflow:
[code block omitted]
### The SnapLLM Solution
[code block omitted]
--- 
## Features
### Core Capabilities
| Feature | Description |
|---------|-------------|
| **Resident Model Selection** | Select between loaded models without reloading their weights |
| **Reload After Eviction** | Memory mapping can benefit from the operating-system page cache |
| **Multi-Model Management** | Load and manage multiple models simultaneously |
| **GPU/CPU Hybrid** | Automatic layer distribution based on available VRAM |
| **OpenAI-Compatible API** | Drop-in replacement for OpenAI API |
| **Multi-Modal Support** | LLM, Vision (VLM), and Stable Diffusion models |
| **KV Cache Persistence** | Persist context state and use indexed cache lookup; generation work still depends on query and context size |
| **Web UI** | React dashboard served by Vite at `localhost:9780`; the API listens on `localhost:6930` |
| **Desktop Application** | Beautiful React-based UI for model management |
### Supported Model Types
- **Text LLMs**: Llama 1/2/3, Mistral, Mixtral, Qwen, Gemma, Phi, DeepSeek, and all GGUF models
- **Vision Models**: Gemma 3 Vision, Qwen-VL, LLaVA (with mmproj files)
- **Diffusion Models**: Stable Diffusion 1.5, SDXL, SD3, FLUX (via stable-diffusion.cpp)
### Performance
SnapLLM reports operation timing at runtime where available. Published
end-to-end latency guarantees require a reproducible benchmark that records the
model, quantization, prompt, build flags, hardware, cache state, and sampling
configuration. No such guarantee is made by this README.
--- 
## Installation
### Prerequisites
- **Windows**: Visual Studio 2022 with C++ workload
- **Linux**: GCC 11+ or Clang 14+
- **CUDA**: 12.x (for GPU acceleration)
- **CMake**: 3.18+
- **Node.js**: 18+ (for desktop app)
### Build from Source
#### Windows (GPU)
[code block omitted]
#### Windows (CPU only)
[code block omitted]
#### Linux (GPU)
[code block omitted]
### Verify Installation
[code block omitted]
--- 
## How to Start the Server
### Windows (recommended)
[code block omitted]
This launcher auto-detects the newest build and starts the server on `127.0.0.1:6930`.
If the desktop app is built, it will launch the UI; otherwise it opens the browser.
### Windows (manual)
[code block omitted]
### Start with a model preloaded
[code block omitted]
### Linux/macOS
[code block omitted]
### Docker
The Compose service binds inside its container on `0.0.0.0`, publishes only to
host loopback, and requires a runtime API key:
[code block omitted]
### Docker Hub image
Tagged releases publish a CPU image to Docker Hub as
` /snapllm: ` and `latest` through the protected
`docker-publish` GitHub environment. Configure repository secrets
`DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`, then create a release tag. The
published image listens on `0.0.0.0:6930` inside the container and includes a
health check for `/health`. The `-cuda` image uses the NVIDIA CUDA 12.6 runtime
and requires NVIDIA Container Toolkit plus `--gpus all`; the unqualified image
is CPU-only.
The container runs as an unprivileged user with a read-only root filesystem,
dropped Linux capabilities, a read-only model mount, and a writable workspace
mount. Changing the host port mapping to a public interface is a d
```
