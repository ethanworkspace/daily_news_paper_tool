# GitHub 專案 05：DEEPX-AI/dx-all-suite

- 日期：2026-11-18
- URL：https://github.com/DEEPX-AI/dx-all-suite
- 描述：DEEPX NPU SDK (DXNN) for edge AI: compile, quantize and deploy ONNX models on DEEPX NPUs
- Stars：80  |  Forks：23  |  Language：Python
- License：NOASSERTION
- Topics：ai-accelerator, computer-vision, deep-learning, deepx, dx-m1, dxnn, edge-ai, gstreamer, inference, npu, on-device-ai, onnx, quantization, yolo
- 更新時間：2026-11-19T11:01:31+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
DEEPX NPU SDK (DXNN) for edge AI: compile, quantize and deploy ONNX models on DEEPX NPUs
DEEPX NPU SDK (DXNN) for edge AI: compile, quantize and deploy ONNX models on DEEPX NPUs

主要語言：Python；Topics：ai-accelerator, computer-vision, deep-learning, deepx, dx-m1, dxnn, edge-ai, gstreamer；Stars：80；License：NOASSERTION

## 技術
實作語言以 Python 為主。
從 topics 可見技術方向：ai-accelerator, computer-vision, deep-learning, deepx, dx-m1, dxnn, edge-ai, gstreamer。
專案描述：DEEPX NPU SDK (DXNN) for edge AI: compile, quantize and deploy ONNX models on DEEPX NPUs

## 架構
README 未明確提供架構章節；依描述推斷此專案聚焦於：DEEPX NPU SDK (DXNN) for edge AI: compile, quantize and deploy ONNX models on DEEPX NPUs

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
