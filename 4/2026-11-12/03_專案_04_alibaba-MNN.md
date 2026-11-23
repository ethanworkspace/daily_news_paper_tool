# GitHub 專案 04：alibaba/MNN

- 日期：2026-11-12
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16600  |  Forks：2546  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-23T07:04:03+00:00
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MNN 是由阿里巴巴開發的輕量級、高效能深度學習推理引擎，專注於在行動裝置、嵌入式設備及個人電腦上執行大型語言模型（LLM）與其他 AI 模型的離線推理與訓練。它已被整合進阿里巴巴多款應用（如淘寶、天貓、釘釘等），支援多種主流模型（Qwen、Baichuan、Zhipu、LLAMA 等），並提供 MNN‑LLM 與 MNN‑Diffusion 兩大運行時方案，旨在讓開發者能在手機、PC、IoT 平台上本地化部署高效 AI 服務。

## 技術
MNN 以 C++ 為核心實作，支援 TensorFlow、Caffe、ONNX、TorchScripts 模型格式的轉換與圖優化，提供 Python API 以簡化呼叫。在運算後端方面，CPU 支援 ARMv7/ARMv8/ARMv9（含 FP16、BF16、INT8/INT4 量化）與 x86/x64（SSE/AVX），GPU 後端包括 Metal、OpenCL、Vulkan 與 CUDA；NPU 後端則有 Hexagon、CoreML、NeuroPilot、HIAI、NNAPI、QNN 等。引擎內部使用 Winograd 卷積、向量化匯編與半精度計算來提升效能，並提供 MNN‑Converter、MNN‑Compress、MNN‑Express、MNN‑CV、MNN‑Train 等工具鏈。

## 架構
MNN 的架構分為前端模型轉換層與後端執行層。前端透過 MNN‑Converter 將外部模型（TensorFlow、Caffe、ONNX、TorchScripts）轉為 MNN 內部的靜態圖，同時執行圖優化（如算子融合、量化）。執行層由 Runtime 調度器負責根據目標硬體選擇適當的後端（CPU、GPU、NPU），將圖分解為 Tensor 運算序列，使用對應的核心函式（匯編優化、Winograd、半精度、整數量化）進行計算。MNN‑Express 提供控制流與一般目的計算能力，MNN‑CV 與 MNN‑Train 則分別提供輕量影像處理與訓練支援。整體資料流為：模型檔案 → 轉換與優化 → 後端分配 → Tensor 運算 → 結果輸出。若需更細部的模組細節，README 未提供完整圖解，僅根據上述描述進行推斷。

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
