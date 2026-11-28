# GitHub 專案 03：maheshvaikri-code/snapllm

- 日期：2026-11-17
- URL：https://github.com/maheshvaikri-code/snapllm
- 描述：🔥 Alternative to Ollama — multi-model serving with sub-ms model switching · CPU-only 20B inference for Edge AI · llama.cpp + stablediffusion.cpp
- Stars：44  |  Forks：4  |  Language：C++
- License：NOASSERTION
- Topics：agentic-ai, cpu-inference, edge-ai, llm, llm-inference, llm-serving, llm-tools, local-llm, model-serving, multi-model, multimodal, ollama-alternative
- 更新時間：2026-11-15T09:35:12+00:00
- 論文層級：未對應論文
- 配對論文：https://doi.org/10.32388/7mldm5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
SnapLLM 是一個基於 llama.cpp 與 stable-diffusion.cpp 的本地推理引擎，提供多模型同時載入與毫秒級切換的服務，作為 Ollama 的替代方案。它面向需要在邊緣設備或桌面上運行大型語言模型、視覺語言模型與擴散模型的開發者與研究者，解決單一模型常駐時頻繁重載權重導致延遲高的問題，透過常駐模型選擇與 KV cache 持續化實現低延遲推理。

## 技術
SnapLLM 使用 C++ 核心，整合 llama.cpp 進行 LLM 推理與 stable-diffusion.cpp 進行圖像生成，支援 GGUF 量化模型、Gemma 3 Vision、Qwen‑VL、LLaVA 等視覺模型以及 Stable Diffusion 1.5/SDXL/SD3/FLUX 等擴散模型。桌面端採用 React + Vite 構建 UI，Node.js 為開發依賴，透過 CMake 編譯，提供 OpenAI 相容 REST API，並實作 GPU/CPU 混合層分配、vPID 模型快取與 KV cache 持續化。

## 架構
架構分為後端服務與桌面應用兩大部分。後端以 C++ 實作的 SnapLLM Server 負責模型載入、切換與推理，採用 vPID（Virtual Processing‑In‑Disk）架構：L1 模型快取保存模型工作區與引擎管理資料，L2 內容快取持久化 KV cache 並以哈希索引進行快速查詢。記憶分層包括 HOT（GPU VRAM）、WARM（CPU RAM）與 COLD（SSD），模型依可用資源自動分派。桌面端由 React/Vite 構建的 UI 透過 WebSocket 或 REST 與後端溝通，提供模型管理、對話、圖像生成與視覺分析等功能。資料流程為：使用者透過 API 或 UI 載入模型 → 模型放入對應記憶層 → 透過 /switch 端點選擇已載入模型（無需重載權重） → 進行文字、視覺或圖像生成，同時可透過 context API 進行 KV cache 預計算與索引查詢。

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
