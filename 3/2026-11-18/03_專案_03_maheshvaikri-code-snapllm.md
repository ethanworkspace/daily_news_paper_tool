# GitHub 專案 03：maheshvaikri-code/snapllm

- 日期：2026-11-18
- URL：https://github.com/maheshvaikri-code/snapllm
- 描述：🔥 Alternative to Ollama — multi-model serving with sub-ms model switching · CPU-only 20B inference for Edge AI · llama.cpp + stablediffusion.cpp
- Stars：44  |  Forks：4  |  Language：C++
- License：NOASSERTION
- Topics：agentic-ai, cpu-inference, edge-ai, llm, llm-inference, llm-serving, llm-tools, local-llm, model-serving, multi-model, multimodal, ollama-alternative
- 更新時間：2026-11-15T09:35:12+00:00
- 配對論文：https://doi.org/10.32388/7mldm5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
SnapLLM 是一個基於 llama.cpp 與 stable-diffusion.cpp 的本地多模型推理引擎，目標使用者為需要在同一設備上運行多種語言、視覺與擴散模型的開發者、研究者與邊緣 AI 實踐者。其核心問題在於傳統單一模型常駐方式導致模型切換時必須重新載入權重，造成顯著延遲與記憶體浪費。SnapLLM 透過常駐多模型與即時選取機制，讓已載入的模型可在不重新載入權重的情況下切換，降低切換成本，提升資源利用率，並提供 OpenAI 相容 API、桌面 UI 與 CLI，方便本地部署與實驗。

## 技術
SnapLLM 使用 C++ 實作，核心推理引擎整合 llama.cpp（支援 GGUF 量化的 LLM）與 stable-diffusion.cpp（支援 SD 1.5、SDXL、SD3、FLUX 等擴散模型），並透過 CMake 建置系統支援 Windows（Visual Studio 2022）、Linux（GCC 11+/Clang 14+）與 CUDA 12.x 加速。提供 OpenAI 相容的 RESTful API（預設監聽 127.0.0.1:6930），以及基於 React 與 Vite 的桌面應用程式（UI 在 localhost:9780），同時保留 CLI 工具。模型管理採用 vPID（Virtual Processing‑In‑Disk）架構，分為 L1 模型快取與 L2 KV 快取，記憶體分層包括 HOT（GPU VRAM）、WARM（CPU RAM）與 COLD（SSD），可依可用資源自動分配層級。支援的模型類型涵蓋 Llama 1/2/3、Mistral、Mixtral、Qwen、Gemma、Phi、DeepSeek 等 GGUF LLM，視覺模型如 Gemma 3 Vision、Qwen‑VL、LLaVA（需 mmproj），以及擴散模型。所有請求均經過 API 金鑰與 CORS 來源檢查，並提供健康檢查端點 /health。

## 架構
SnapLLM 的架構圍繞 vPID（Virtual Processing‑In‑Disk）系統展開：L1 層負責模型工作區的中繼資料與引擎管理的快取資料；L2 層則負責 KV cache 的持久化與以雜湊索引進行快速查詢。記憶體分為三個階層——HOT（GPU VRAM，最高存取速度），WARM（CPU RAM，中等速度），COLD（SSD，最低速度）——模型與其工作區可依據目前可用資源自動放置於適當階層。當使用者透過 /api/v1/models/switch 端點選擇已載入的模型時，系統僅在 L1/L2 層更新指標，避免重新讀取模型權重，因而實現所謂的亞毫秒級模型切換（實際延遲仍受模型大小、硬體、記憶體壓力與編譯旗標影響）。啟動流程包括：伺服器監聽於設定的 host:port，載入模型時會將模型檔案映射至對應記憶體階層並建立工作區；生成請則依據目前活躍模型執行推理，若啟用 KV cache 持久化則會在 L2 層進行索引查詢以重用先前計算的上下文。桌面應用則以 React/Vite 構建，透過同一組 API 與伺服器互通，提供儀表板、聊天、圖像生成、視覺分析、模型管理、A/B 比較、上下文管理等功能。由於 README 未提供詳細的類別圖或序列圖，以上架構說明僅基於文中所述的 vPID、記憶體層級、模型工作區與 API 端點推斷。

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
