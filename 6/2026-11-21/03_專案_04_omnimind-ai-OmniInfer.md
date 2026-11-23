# GitHub 專案 04：omnimind-ai/OmniInfer

- 日期：2026-11-21
- URL：https://github.com/omnimind-ai/OmniInfer
- 描述：Unified, efficient, and easy-to-use inference infrastructure for edge AI || 面向端侧 AI 的統一、高效、易用的推理基础設施
- Stars：1338  |  Forks：12  |  Language：Rust
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-22T06:06:30+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
OmniInfer 是一個統一、高效且易於使用的端侧 AI 推理基礎設施，專為在本地運行大型語言模型（LLM）與視覺語言模型（VLM）而設計。它隱藏模型編譯、硬件適配與部署複雜性，提供跨平台的 CLI、終端使用者介面以及 OpenAI/Anthropic 相容的本地 HTTP API，支援多種後端引擎，使開發者、研究者與邊緣設備使用者能以最小設定獲得快速、低記憶體足跡的推理服務。

## 技術
OmniInfer 以 Rust 實作核心框架，提供統一的後端抽象層，可動態切換 llama.cpp、stable-diffusion.cpp、ik_llama.cpp、MNN、MLX、TurboQuant、LiteRT-LM、ExecuTorch QNN、OmniInfer Native、vLLM 與 vla.cpp 等引擎。它支援 GGUF 分割模型直接載入，緊追 llama.cpp 基線（如 b10665），並即時提供 Qwen3.8‑Flash‑Next 與 Qwen3.8‑27B 視覺語言模型的 Day‑0 支援。透過跨平台編譯與模組化設計，同一程式碼基礎可產出 Linux/macOS/Windows CLI、Android Gradle 模組與 iOS Swift Package，實現從桌面到邊緣設備的一致推理體驗。

## 架構
OmniInfer 的架構圍繞統一的後端抽象層展開：頂層提供 CLI（omniinfer）與終端使用者介面（TUI），負責後端發現、模型探索與啟動；下層是後端插件系統，封裝 llama.cpp、stable-diffusion.cpp、MNN、MLX 等具體推理引擎，統一處理模型載入（GGUF、分割目錄）、參數配置（上下文長度、GPU 卸載、KV cache）與 token 生成。服務模式下，omniinfer serve 暴露 OpenAI/Anthropic 相容的 HTTP API，將請求路由至相同的後端抽象層進行推理。移動端則透過 Android Gradle 模組與 iOS Swift Package 將同一核心庫嵌入應用，實現模型發現與後端選擇的跨平台一致性。README 未提供詳細圖表，以上結構依據功能說明與模組文件推斷。

## README 摘錄（節選）
```text
# OmniInfer
English | 简體中文
Easy, fast, and private LLM &amp; VLM inference for every device.
Quick Start ·
Documentation ·
Releases
## Quick Start
### Install OmniInfer
Linux x64
macOS arm64
Windows x64 PowerShell
curl -fsSL https://raw.githubusercontent.com/omnimind-ai/OmniInfer/main/scripts/install.sh | bash
curl -fsSL https://raw.githubusercontent.com/omnimind-ai/OmniInfer/main/scripts/install.sh | bash
irm https://raw.githubusercontent.com/omnimind-ai/OmniInfer/main/scripts/install.ps1 | iex
The installers download the latest CLI-only GitHub Release, verify its SHA-256 checksum, and install it for the current user. For fixed versions, custom paths, manual installation, source setup, and removal, see Installation (docs/installation.md).
### Start in three steps
1. Run `omniinfer` in a terminal.
2. Choose a compatible backend. The TUI can install an available prebuilt runtime for you.
3. Select a local model and start chatting.
To run the local OpenAI- and Anthropic-compatible service, start `omniinfer serve` and follow the CLI Guide (docs/CLI.md) or API Reference (docs/API.md). Source builds and mobile embedding are documented separately.
## News
- **2026-08-28** — **Qwen3.8-Flash-Next support.** OmniInfer now tracks llama.cpp `b10665` and can load split GGUF model directories directly. Use a source-built llama.cpp backend until the matching prebuilt runtime is published in OmniInfer.
- **2026-08-14** — 🚀 **Day-0 support for Qwen3.8-27B.** OmniInfer is ready for Qwen's latest 27B vision-language model from day one.
## Demo
Short, focused recordings of the main entry points. Each demo covers one capability.
### Terminal UI — choose a backend, load a model, chat locally
Running `omniinfer` opens a terminal UI that recommends a compatible backend, loads a local model, and starts a fully local chat session.
Static preview: terminal UI screenshot
### Browser VLA demo — SmolVLA on LIBERO
The optional vla-libero example (examples/vla-libero/README.md) runs a SmolVLA policy through a managed vla.cpp runtime in the LIBERO simulator, showing live camera views, the predicted action, and latency in a browser dashboard.
Static preview: SmolVLA LIBERO dashboard screenshot
## About
OmniInfer is a high-performance, cross-platform inference engine for running Large Language Models (LLM) and Vision-Language Models (VLM) locally. It abstracts away model compilation, hardware adaptation, and deployment complexity, enabling efficient local inference with minimal configuration.
> OmniInfer powers the inference layer of Omni Studio (https://omnimind.com.cn/omnistudio), a unified model orchestration platform.
OmniInfer is fast with:
- Optimized token generation speed and minimal memory footprint
- Multiple backend engines, including llama.cpp, stable-diffusion.cpp, ik_llama.cpp, MNN, MLX, TurboQuant, LiteRT-LM, ExecuTorch QNN, and OmniInfer Native where supported
- Hardware-aware adaptation and optimization
OmniInfer is flexible and easy to use with:
- Seamless multi-backend switching for the best available engine on each device
- OpenAI-compatible and Anthropic-compatible local API endpoints
- Support for text and vision-language workloads
- Fine-grained parameter control for context length, GPU offloading, KV cache, and backend-native launch options
OmniInfer runs everywhere:
- Linux, macOS, Windows — desktop and server
- Android and iOS — mobile and edge devices
- One codebase across CLI, HTTP gateway, and mobile modules
## Platform Support
| Platform | Distribution | Representative runtimes |
|---|---|---|
| Linux x64 | Release CLI and source checkout | llama.cpp, stable-diffusion.cpp, ik_llama.cpp, vLLM, vla.cpp |
| macOS arm64 | Release CLI and source checkout | llama.cpp, MLX, TurboQuant |
| Windows x64 | Release CLI and source checkout | llama.cpp, stable-diffusion.cpp, vLLM through WSL2 |
| Android | Gradle module | llama.cpp, MNN, LiteRT-LM, ExecuTorch QNN |
| iOS | Swift package | Embedded native inference service |
Runtime availability
```
