# GitHub 專案 05：DEEPX-AI/dx-all-suite

- 日期：2026-11-19
- URL：https://github.com/DEEPX-AI/dx-all-suite
- 描述：DEEPX NPU SDK (DXNN) for edge AI: compile, quantize and deploy ONNX models on DEEPX NPUs
- Stars：80  |  Forks：23  |  Language：Python
- License：NOASSERTION
- Topics：ai-accelerator, computer-vision, deep-learning, deepx, dx-m1, dxnn, edge-ai, gstreamer, inference, npu, on-device-ai, onnx, quantization, yolo
- 更新時間：2026-11-19T11:01:31+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
DEEPX DX-AllSuite (DXNN) 是一套端到端的邊緣 AI 平台，負責將訓練好的 ONNX 模型編譯、量化並產出 DEEPX NPU 專用的 .dxnn 執行檔，同時提供運行時環境、GStreamer 外掛、Python/C++ API 與 ModelZoo，讓開發者能在支援 DEEPX NPU 的設備上進行即時視覺推論與實體 AI 應用。目標使用者為嵌入式系統工程師、邊緣 AI 開發者與研究人員，核心問題在於簡化模型從訓練到 NPU 部署的全流程，降低開發複雜度與效能損失。

## 技術
技術重點包括：以 Python 3.8~3.14 與 C++ 為主要開發語言，使用 DEEPX 自研的 DX-COM 編譯器將 ONNX 模型進行 INT8 智慧量化，產出 .dxnn 二進位檔；透過 DX-STREAM（基於 GStreamer 的自訂外掛）實現前處理、推論與後處理的一條視訊管線；提供完整的 Python/C++ API 與 300+ 個 ModelZoo 預訓練模型；支援 Docker 镜像（GHCR）與 Helm chart（dx-npu）進行 Kubernetes 部署；此外尚有 Agent‑Driven Development（Beta）、DX AI Studio、DX‑Benchmark 與 DX‑Edge 等輔助工具。

## 架構
架構分為兩大環境：編譯環境（Host PC）負責模型轉換、量化與 .dxnn 生成，使用 DX-Compiler（dx-com）工具鏈；運行環境（Target Device）載入 NPU 驅動與 DX-Runtime，透過 dx_engine 執行 .dxnn 模型，搭配 DX-STREAM GStreamer 外掛進行即時資料流處理；核心元件包括 DX-COM 編譯器、DX-RT 執行階段、NPU 驅動、韌體更新模組、ModelZoo、容器映像與 Kubernetes 設備插件（dx-m1），資料流從影像擷取 → 前處理 → NPU 推論 → 後處理 → 輸出/顯示。若需更細部的模組互連圖，請參考官方文件的架構概覽。

## README 摘錄（節選）
```text
# DXNN - DEEPX NPU SDK (DX-AllSuite: DEEPX All Suite)
** DX-AllSuite** is an all-in-one software platform designed to streamline the entire process of compiling, optimizing, simulating, and deploying AI inference applications on **DEEPX NPUs**. It ensures optimal compatibility and powerful hardware performance through a complete toolchain that covers everything from model creation to real-world "Physical AI" deployment.
Figure. DXNN SDK Full Architecture Overview.
** Key Features**
- **High Efficiency**: Equipped with the proprietary **DX-COM** compiler that extracts 100% of NPU performance. It utilizes advanced quantization (Intelligent Quantization with INT8) to minimize accuracy loss while maximizing inference speed.
- **Seamless Integration**: Build intelligent video analytics pipelines that bridge the entire pre-processing, inference, and post-processing workflow. Using **DX-STREAM** (GStreamer-based custom plugins), you can deploy complex vision tasks without extensive code modifications.
- **Flexible Ecosystem**: Fully supports **Python and C++ APIs** and offers a **ModelZoo** with 300+ optimized models. As a leader in the Open-Source Physical AI Alliance, we provide seamless workflows for popular frameworks.
Figure. DXNN SDK Simple Architecture Overview.
## Documentation Navigation
If you are a first-time user, we recommend following the documentation in this order.
- **Introduction (./docs/source/index.md)**: DX-AS overview and component descriptions
- **Step 1. DX-AllSuite Architecture Overview (./docs/source/01_DX-AllSuite_Architecture_Overview.md)**: SDK overview, module descriptions, and ModelZoo usage
- **Step 2. Setting Up Environment (./docs/source/02_Setting_Up_Environment.md)**: Detailed Local/Docker installation and troubleshooting
- **Step 3. Running Your First NPU Model (./docs/source/03_Running_Your_First_NPU_Model.md)**: Step-by-step hands-on script execution
- **Step 4. Checking Version Compatibility (./docs/source/04_Version_Compatibility.md)**: SDK, Driver, and Firmware dependency matrix
- **Step 5. FAQ Troubleshooting Guide (./docs/source/05_FAQ_Troubleshooting_Guide.md)**: Solutions for environment conflicts and GUI session (X11) errors
** Optional** — Kubernetes deployment:
- **Kubernetes Quickstart (./docs/source/06_Kubernetes_Quickstart.md)**: Schedule DX-M1 NPUs as a Kubernetes resource with the `dx-npu` Helm chart
- **Kubernetes Beginner Guide (./docs/source/07_Kubernetes_Beginner_Guide.md)**: Kubernetes explained from scratch, with hands-on NPU examples
** Tools and solutions** — pick what fits your project:
- **★ Agent-Driven Development (Beta) (./docs/source/00_Agent_Driven_Development.md)**: Build DEEPX apps with natural-language prompts using AI coding agents (Claude Code, Cursor, GitHub Copilot, OpenCode, Codex CLI)
- **DX AI Studio (Beta) (./dx-ai-studio/README.md)**: All-in-one browser workspace for AI development on DEEPX NPUs — Install & launch (./dx-ai-studio/docs/source/01_Installation_and_Launch.md)
- **DX-Benchmark (Beta) (./dx-benchmark/README.md)**: Reproducible YOLO26 NPU benchmarks (Model-Level + E2E Pipeline) with an interactive performance dashboard
- **DX-Edge (./dx-edge/README.md)**: Deploying DEEPX NPUs through AWS Marketplace — Greengrass Solution (ZTP runtime deployment), Compiler Solution (ONNX → `.dxnn` on AWS), and Getting Started Guides for the DX-AIPlayer N97 and the DX-M1 Raspberry Pi 5 Dev Kit
## Getting Started
** DX-AllSuite** provides two environments depending on your intended use. Choose the environment that fits your needs to get started.
### AI Model Compile Environment (Host PC)
This environment is used for converting and optimizing trained AI models into DEEPX NPU-specific binaries.
- **Arch**: x86_64
- **OS**: Ubuntu 26.04 / 24.04 / 22.04 / 20.04 (LTS), Fedora 42-45, Red Hat Enterprise Linux 9-10, and CentOS Stream 9-10
- **Hardware**: x86_64 Host PC
- **Software**: Python 3.8~3.14, CUDA (Optional for simulation)
- **Key Tasks**: AI model (`.onnx`) comp
```
