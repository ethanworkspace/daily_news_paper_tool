# GitHub 專案 03：alibaba/MNN

- 日期：2026-11-20
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16591  |  Forks：2545  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-22T10:50:56+00:00
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MNN 是由阿里巴巴開發的輕量級、高效能深度學習推理引擎，專注於在行動電話、個人電腦與嵌入式裝置上本地運行大型語言模型（LLM）與擴散模型等 AI 工作負載。它支援多種模型格式（TensorFlow、Caffe、ONNX、TorchScript），並提供跨平台的 CPU、GPU 與 NPU 後端，使開發者能在資源受限的設備上實現低延遲、高吞吐的模型推理，同時也提供訓練、模型壓縮與轉換工具，目標使用者為需要在終端設備部署 AI 模型的移動應用開發者、嵌入式系統工程師以及阿里巴巴內部各業務線。

## 技術
MNN 以 C++ 實作核心運算引擎，支援 TensorFlow、Caffe、ONNX、TorchScript 模型格式的轉換與執行。在 CPU 端利用 ARM/x86 SIMD、Winograd 卷積及手寫組合語言核心進行 FP16、INT8、INT4 量化運算；GPU 端透過 Metal、OpenCL、Vulkan 與 CUDA 提供硬體加速；NPU 端則對應 CoreML、Hexagon、NeuroPilot 等平台。此外提供 MNN-Converter、MNN-Compress、MNN-Express（支援控制流與通用運算）、MNN-CV（輕量級影像處理）與 MNN-Train 訓練工具，並附有 Python API 讓開發者免除直接撰寫 C++。

## 架構
MNN 的架構分為前端模型轉換層、核心執行階段與後端硬體加速層。使用者先透過 MNN-Converter 將外部模型轉為 MNN 內部格式；運行時，MNN 根據裝置偵測結果選擇適當的後端（CPU、GPU 或 NPU），並載入對應的核心函式庫（如 ARM 組合語言卷積、Metal/Vulkan 着色器或 Hexagon DSP 內核）。計算流程中，張量資料經過圖形優化後依序經過各算子的內核，支援動態形狀、多輸入/輸出以及控制流；針對 LLM，MNN-LLM 進一步管理 KV 快取與 token 生成 loop；針對擴散模型，則透過 MNN-Diffusion 進行去噪步驟的迭代執行。整體設計強調模組化與零依賴，以便在行動與嵌入式平台上快速部署。

## README 摘錄（節選）
```text
--- 
(LICENSE.txt)
(https://mnn-docs.readthedocs.io/en/latest/)
(README_CN.md)
(README_TW.md)
(README_JP.md)
(http://www.mnn.zone)
(https://zread.ai/alibaba/MNN)
(./apps/Android/MnnLlmChat/README.md)
(./apps/Android/Mnn3dAvatar/README.md)
(./apps/sana/README.md)
## News 🔥
- [2026/11/04] We released **MNN-Pocket-0.3B**, a **300M-parameter mobile-app-native language model** for Chinese/English instruction following. The MNN team co-designed its architecture, training methods, and inference engine around smartphone apps' task requirements and resource budgets. It supports **32K context**; the INT4 (W4A16) QAT MNN build occupies only **173 MB** and achieves **350 tok/s** decode throughput in tests on iPhone 18 Pro. Released under **Apache 2.0**.
ModelScope (https://modelscope.cn/collections/MNN/MNN-Pocket-03B) | Hugging Face (https://huggingface.co/collections/taobao-mnn/mnn-pocket-03b) | Technical report (https://arxiv.org/pdf/2611.12311)
History News
- [2026/07/22] MNN 3.6.1 is released with a new 🚀 Hexagon backend, enabling accelerated model inference on Qualcomm Hexagon DSPs. Learn more (./source/backend/hexagon/README.md).
- [2026/03/05] Support Qwen3.5 Series.
- [2026/02/13] MNN-Sana-Edit-V2 is now available at apps (./apps/sana/README.md), offering cartoon-style photo editing based on Sana.
- [2025/10/16] Support Qwen3-VL Series.
- [2025/06/11] New App MNN TaoAvatar released, you can talk with 3DAvatar offline with LLM, ASR, TTS, A2BS and NNR models all run local on your device!! MNN TaoAvatar (./apps/Android/Mnn3dAvatar/README.md)
- [2025/05/12] android app support qwen2.5 omni 3b and 7b MNN Chat App (./apps/Android/MnnLlmChat/README.md#releases).
- [2025/04/30] android app support qwen3 and dark mode MNN Chat App (./apps/Android/MnnLlmChat/README.md#releases).
- [2025/02/18] iOS multimodal LLM App is released MNN LLM iOS (./apps/iOS/MNNLLMChat/README.md).
- [2025/02/11] android app support for deepseek r1 1.5b (./apps/Android/MnnLlmChat/README.md#releases).
- [2025/01/23] We released our full multimodal LLM Android App:MNN-LLM-Android (./apps/Android/MnnLlmChat/README.md). including text-to-text, image-to-text, audio-to-text, and text-to-image generation.
## Intro
MNN is a highly efficient and lightweight deep learning framework. It supports inference and training of deep learning models and has industry-leading performance for inference and training on-device. At present, MNN has been integrated into more than 30 apps of Alibaba Inc, such as Taobao, Tmall, Youku, DingTalk, Xianyu, etc., covering more than 70 usage scenarios such as live broadcast, short video capture, search recommendation, product searching by image, interactive marketing, equity distribution, security risk control. In addition, MNN is also used on embedded devices, such as IoT.
MNN-LLM (./transformers/README.md) is a large language model runtime solution developed based on the MNN engine. The mission of this project is to deploy LLM models locally on everyone's platforms(Mobile Phone/PC/IOT). It supports popular large language models such as Qianwen, Baichuan, Zhipu, LLAMA, and others. MNN-LLM User guide (https://mnn-docs.readthedocs.io/en/latest/transformers/llm.html)
MNN-Diffusion (https://github.com/alibaba/MNN/tree/master/transformers/diffusion) is a stable diffusion model runtime solution developed based on the MNN engine. The mission of this project is to deploy stable diffusion models locally on everyone's platforms. MNN-Diffusion User guide (https://mnn-docs.readthedocs.io/en/latest/transformers/diffusion.html)
Inside Alibaba, MNN (https://mp.weixin.qq.com/s/5I1ISpx8lQqvCS8tGd6EJw) works as the basic module of the compute container in the Walle (https://mp.weixin.qq.com/s/qpeCETty0BqqNJV9CMJafA) System, the first end-to-end, general-purpose, and large-scale production system for device-cloud collaborative machine learning, which has been published in the top system conference OSDI’22. The key design principles of MNN and the extensive benchmark
```
