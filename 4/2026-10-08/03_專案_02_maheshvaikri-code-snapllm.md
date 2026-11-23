# GitHub 專案 02：maheshvaikri-code/snapllm

- 日期：2026-10-08
- URL：https://github.com/maheshvaikri-code/snapllm
- 描述：🔥 Alternative to Ollama — multi-model serving with sub-ms model switching · CPU-only 20B inference for Edge AI · llama.cpp + stablediffusion.cpp
- Stars：44  |  Forks：4  |  Language：C++
- License：NOASSERTION
- Topics：agentic-ai, cpu-inference, edge-ai, llm, llm-inference, llm-serving, llm-tools, local-llm, model-serving, multi-model, multimodal, ollama-alternative
- 更新時間：2026-11-15T09:35:12+00:00
- 配對論文：https://doi.org/10.32388/7mldm5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
SnapLLM 是一個基於 llama.cpp 與 stable-diffusion.cpp 的本地多模型推理引擎，目標使用者為需要在邊緣或桌面環境同時運行多種 LLM、視覺與擴散模型的開發者與 AI 愛好者。它解決單一模型頻繁載入與卸載導致的延遲與資源浪費問題，透過已駐留模型的即時切換、OpenAI 相容 API、React/Vite 桌面 UI 與 CLI，提供統一的模型管理與推理服務。

## 技術
SnapLLM 使用 C++ 作為核心推理引擎，整合 llama.cpp 進行 LLM 推理與 stable-diffusion.cpp 進行圖像生成，支援 GGUF 量化模型、視覺模型（Gemma 3 Vision、Qwen‑VL、LLaVA）與擴散模型（SD 1.5、SDXL、SD3、FLUX）。桌面端採用 React 與 Vite 構建 UI，Node.js 18+ 提供開發與打包環境，透過 CMake 3.18+ 與 Visual Studio 2022 / GCC 11+ / Clang 14+ 編譯。提供 OpenAI 相容的 REST API，內建 KV Cache 持久化（vPID L2）與模型快取（vPID L1），支援 GPU/CPU 混合層分配，並可透過環境變數控制 API 金鑰、CORS 與工作空間路徑。

## 架構
SnapLLM 架構分為三層：底層推理引擎（C++）負責模型載入、權重管理與推理執行；中層 vPID 系統實作 L1 模型快取與 L2 KV Cache 持久化，提供已載入模型的即時切換與上下文索引查詢；頂層服務與介面層包含 OpenAI 相容的 HTTP API（預設 127.0.0.1:6930）、React/Vite 桌面 UI（預設 localhost:9780）與 CLI。資料流程為：使用者透過 API 或 UI 載入模型至模型工作區，模型被放置於 HOT（GPU VRAM）、WARM（CPU RAM）或 COLD（SSD）記憶體層級；切換時僅更新 vPID L1 指標，無需重新載入權重；生成請求會調用對應引擎，必要時讀取 L2 KV Cache 進行上下文查詢，最後返回結果給 API 或 UI。

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
