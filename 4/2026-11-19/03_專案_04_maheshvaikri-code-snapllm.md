# GitHub 專案 04：maheshvaikri-code/snapllm

- 日期：2026-11-19
- URL：https://github.com/maheshvaikri-code/snapllm
- 描述：🔥 Alternative to Ollama — multi-model serving with sub-ms model switching · CPU-only 20B inference for Edge AI · llama.cpp + stablediffusion.cpp
- Stars：44  |  Forks：4  |  Language：C++
- License：NOASSERTION
- Topics：agentic-ai, cpu-inference, edge-ai, llm, llm-inference, llm-serving, llm-tools, local-llm, model-serving, multi-model, multimodal, ollama-alternative
- 更新時間：2026-11-15T09:35:12+00:00
- 配對論文：https://doi.org/10.32388/7mldm5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
SnapLLM 是一個基於 llama.cpp 與 stable-diffusion.cpp 的本地多模型推理引擎，旨在讓使用者在同一台機器上同時載入多種 LLM、視覺語言模型與擴散模型，並能在已載入的模型間以毫秒級切換而不需重新載入權重。它提供 OpenAI 相容的 REST API、命令列介面以及 React/Vite 構建的桌面 UI，適用於需要在邊緣設備或桌面上進行低延遲多模型服務的開發者、研究員與 AI 愛好者。

## 技術
SnapLLM 使用 C++ 實作，核心推理依賴 llama.cpp 與 stable-diffusion.cpp，透過 CMake 建置，支援 GCC 11+/Clang 14+ 或 Visual Studio 2022；桌面應用程式則以 Node.js 18+ 搭配 React 與 Vite 構建。它提供 OpenAI 相容的 HTTP API，內建 GPU/CPU 混合層分配（根據可用 VRAM 自動決策），並採用 vPID（Virtual Processing‑In‑Disk）架構實現模型快取（L1）與 KV 快取（L2），記憶體分層為 HOT（GPU VRAM）、WARM（CPU RAM）與 COLD（SSD）。支援 GGUF 格式的 Llama、Mistral、Mixtral、Qwen、Gemma、Phi、DeepSeek 等文字模型，Gemma 3 Vision、Qwen‑VL、LLaVA 等視覺模型，以及 Stable Diffusion 1.5、SDXL、SD3、FLUX 等擴散模型。

## 架構
SnapLLM 的架構圍繞 vPID 系統展開：L1 層為模型快取，存放模型工作區資料與引擎管理的快取；L2 層為上下文快取，以哈希索引持久化 KV 快取，使得已載入模型間的切換僅需切換指標而不重新載入權重。記憶體分為三層：HOT（GPU VRAM）提供最高存取速度，受限於可用 VRAM；WARM（CPU RAM）為中介層，容量受系統記憶體限制；COLD（SSD）為最慢層，提供儲存空間。當收到載入請求時，模型會被映射到適當的記憶體層並註冊到模型快切；切換模型僅需更新當前活躍模型的指標；生成請求會先查詢 L2 KV 快取，若未命中則進行一般推理。桌面 UI 與 API 透過 localhost 分別在 9780 與 6930 端口通訊，Docker 版本則將 API 綁定到 0.0.0.0:6930 並僅開放給迴路介面，除非額外設定 SNAPLLM_API_KEY 與 CORS 允許來源。

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
