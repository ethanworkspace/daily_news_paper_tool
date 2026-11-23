# GitHub 專案 02：maheshvaikri-code/snapllm

- 日期：2026-09-16
- URL：https://github.com/maheshvaikri-code/snapllm
- 描述：🔥 Alternative to Ollama — multi-model serving with sub-ms model switching · CPU-only 20B inference for Edge AI · llama.cpp + stablediffusion.cpp
- Stars：44  |  Forks：4  |  Language：C++
- License：NOASSERTION
- Topics：agentic-ai, cpu-inference, edge-ai, llm, llm-inference, llm-serving, llm-tools, local-llm, model-serving, multi-model, multimodal, ollama-alternative
- 更新時間：2026-11-15T09:35:12+00:00
- 配對論文：https://doi.org/10.32388/7mldm5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
SnapLLM 是一個基於 llama.cpp 與 stable-diffusion.cpp 的本地推理引擎，支援同時載入多個模型並在已載入模型之間進行毫秒級切換，無需重新載入權重。它提供 OpenAI 相容的 REST API、命令列介面以及以 React/Vite 構建的桌面 UI，適用於需要在邊緣設備或工作站上運行大型語言模型、視覺語言模型與擴散模型的開發者與研究者。

## 技術
SnapLLM 使用 C++ 實作核心推理引擎，依賴 llama.cpp 進行 LLM 推論、stable-diffusion.cpp 進行圖像生成，並透過 CMake 建置。桌面應用採用 Node.js 18+ 與 React/Vite，提供 Web UI。支援 GPU/CPU 混合層分配、記憶體階層（HOT GPU VRAM、WARM CPU RAM、COLD SSD）、vPID 處理記憶體系統（L1 模型快取、L2 KV 快取），以及 GGUF、mmproj 等模型格式。API 提供 OpenAI 相容端點與自訂的模型管理、視覺、擴散與上下文快取介面。

## 架構
架構分為三層：底層推理引擎（C++）負責模型載入、權重管理與推論；中間 vPID 系統維護 L1 模型快取（模型工作區與引擎管理資料）與 L2 KV 快取（經雜湊索引的上下文狀態），並依據記憶體階層將模型放置於 GPU VRAM、CPU RAM 或 SSD；最上層為服務介面，包括 OpenAI 相容的 REST API（預設監聽 127.0.0.1:6930）、命令列工具與以 React/Vite 建置的桌面 UI（預設於 localhost:9780）。模型透過 POST /api/v1/models/load 載入，POST /api/v1/models/switch 在已載入模型間切換，生成則透過 /v1/chat/completions、/api/v1/generate 等端點進行，上下文可透過 /api/v1/contexts/ingest 預先計算 KV 快取並經 /api/v1/contexts/{id}/query 查詢。

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
