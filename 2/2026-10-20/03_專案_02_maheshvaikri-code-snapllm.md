# GitHub 專案 02：maheshvaikri-code/snapllm

- 日期：2026-10-20
- URL：https://github.com/maheshvaikri-code/snapllm
- 描述：🔥 Alternative to Ollama — multi-model serving with sub-ms model switching · CPU-only 20B inference for Edge AI · llama.cpp + stablediffusion.cpp
- Stars：44  |  Forks：4  |  Language：C++
- License：NOASSERTION
- Topics：agentic-ai, cpu-inference, edge-ai, llm, llm-inference, llm-serving, llm-tools, local-llm, model-serving, multi-model, multimodal, ollama-alternative
- 更新時間：2026-11-15T09:35:12+00:00
- 配對論文：https://doi.org/10.32388/7mldm5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
SnapLLM 是一個基於 llama.cpp 與 stable-diffusion.cpp 的本地推理引擎，支援同時載入多個模型並且在已載入的模型間進行毫秒級切換，無需重新載入權重。它提供 OpenAI 相容的 REST API、命令列介面以及以 React/Vite 構建的桌面應用，適用於需要在邊緣設備或桌面上執行大型語言模型、視覺語言模型以及擴散模型的開發者與研究者。核心目標是解決單一常駐模型工作流程中模型切換成本高的問題，實現多模型管理與低延遲推理。

## 技術
SnapLLM 使用 C++ 實作，核心推理引擎依賴 llama.cpp（支援 Llama、Mistral、Qwen、Gemma、Phi、DeepSeek 等 GGUF 格式）與 stable-diffusion.cpp（支援 SD 1.5、SDXL、SD3、FLUX 等擴散模型）。它提供 OpenAI 相容的 API、React/Vite 桌面 UI（Node.js 18+）、CMake 建置系統，並支援 GPU/CPU 混合層分配（依據可用 VRAM 自動決策）、記憶體分層（HOT GPU VRAM、WARM CPU RAM、COLD SSD）、KV Cache 持久化與雜湊索引查詢（vPID L2），以及 Docker 镜像（CPU 與 CUDA 版本）。

## 架構
SnapLLM 的架構分為伺服器核心、模型管理與上下文快取三層。伺服器基於 HTTP API（預設監聽 127.0.0.1:6930），提供模型載入（/api/v1/models/load）、切換（/api/v1/models/switch）、卸載以及文字、視覺與圖像生成端點。模型管理採用 vPID（Virtual Processing‑In‑Disk）架構：L1 層為模型快取，儲存工作區中繼資料與引擎管理的快取；L2 層為上下文快取，持久化 KV cache 並以雜湊索引實現快速查詢。記憶體分層依序為 HOT（GPU VRAM）、WARM（CPU RAM）、COLD（SSD），模型的權重可依可用資源放置於不同層。每個模型擁有獨立的工作區目錄，內含模型檔案與相關 mmproj（多模投影）檔案。桌面應用以 React + Vite 構建，透過 API 與伺服器互通，提供儀表板、聊天、圖像生成、視覺分析、模型比較等功能。Docker 部署則將服務綁定在容器內部的 0.0.0.0:6930，僅公開至迴路環境，並需透過 SNAPLLM_API_KEY 進行驗證。README 中已提供上述架構圖與資料流說明，未見其他未說明的元件。

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
