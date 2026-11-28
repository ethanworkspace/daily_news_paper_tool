# GitHub 專案 01：alibaba/MNN

- 日期：2026-11-28
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16634  |  Forks：2554  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-27T18:12:21+00:00
- 論文層級：未對應論文
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
MNN 是一個由阿里巴巴開發的輕量級、高效能的深度學習推理引擎，專為行動裝置與嵌入式平台設計。它支援多種模型格式的轉換、量化與訓練，使開發者能在智慧型手機、平板、IoT 設備上本地執行包括大型語言模型、擴散模型在內的 AI 工作負載，解決資源受限環境下的推理延遲與記憶體佔用問題。目標使用者為行動應用開發者、AI 工程師以及需要設備端 AI 計算的產品團隊。

## 技術
MNN 以 C++ 實作，提供 CPU 後端（支援 ARMv7/v8/v9、x86/x64 SIMD 包含 SSE4.1、AVX2、AVX512、Winograd 以及 FP16/INT8/INT4 量化），GPU 後端（Metal、OpenCL、Vulkan、CUDA），以及 NPU 後端（Hexagon、CoreML 等）。模型可經 MNN-Converter 從 TensorFlow、Caffe、ONNX、Torchscript 轉換，並可使用 MNN-Compress 進行大小與速度優化。框架亦提供 MNN-Express（控制流運算）、MNN-Train、MNN-CV 與 Python API，支援 Transformer、LLM、擴散模型等常見網路結構。

## 架構
MNN 的架構分為前端模型轉換與壓縮層（MNN-Converter、MNN-Compress）、核心推理引擎與後端抽象層（CPU、GPU、NPU），以及上層應用庫（MNN-Express、MNN-Train、MNN-CV、Python API）。使用者首先將原始模型轉換為 MNN 格式，可選擇進行量化或壓縮以減少模型大小與提升速度；接著在運行時根據目標平台選擇適當的後端，引擎內部使用優化的彙編核心、Winograd 卷積、半精度 FP16 計算或整數張量執行運算，最後透過相應的介面回傳推論結果。若需訓練或控制流運算，則可透過 MNN-Train 或 MNN-Express 進行圖級別的修改與梯度計算。README 未提供詳細的模組間介面圖，因此上述流程基於文件中所述的工具與後端描述進行合理推斷。

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
