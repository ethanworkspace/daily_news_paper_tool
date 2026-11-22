# GitHub 專案 03：alibaba/MNN

- 日期：2026-11-17
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16591  |  Forks：2545  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-22T10:50:56+00:00
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MNN 是由阿里巴巴開發的輕量級、高效能的深度學習推理引擎，專注於在行動裝置、嵌入式設備及邊緣節端上運行各種神經網路模型，特別是大型語言模型（LLM）與擴散模型。它提供模型轉換、量化、壓縮及多後端（CPU、GPU、NPU）支援，目標使用者為行動應用開發者、邊緣 AI 工程師以及需要在設備端低延遲、低資源併發執行 AI 模型的研究與產品團隊，解決模型在資源受限環境下難以即時推送的問題。

## 技術
MNN 以 C++ 實作，支援 TensorFlow、Caffe、ONNX、TorchScript 等模型格式的轉換與優化。其核心引擎提供 CPU 後端（ARMv7/ARMv8/ARMv9、x86/x64 含 SSE4.1、AVX2、AVX512 指令優化、Winograd 卷積）、GPU 後端（Metal、OpenCL、Vulkan、CUDA）以及 NPU/Hexagon 等專用加速器。引擎內建 FP16、INT8、INT4 量化路徑，可透過 MNN‑Compress 進行模型壓縮與加速。此外，MNN 提供 MNN‑Converter、MNN‑Express（支援控制流）、MNN‑CV（輕量級圖像處理）與 MNN‑Train 等工具鏈，以及專門的 LLM 與擴散模型運行時（MNN‑LLM、MNN‑Diffusion）。

## 架構
MNN 的架構分為前端模型轉換與優化層、運行時執行層與後端硬體抽象層三大部分。模型首先經由 MNN‑Converter 轉換為 MNN 內部的靜態圖，並透過圖優化（如算子融合、常數折疊、Winograd 替換）得到經過優化的模型檔案。運行時則載入該模型，根據目標裝置偵測到的可用後端（CPU、GPU、NPU）選擇對應的執行器，將圖分解為基本算子並調用各後端的優化核心（例如 ARM 彙編、Metal/Vulkan 着色器、CUDA Tensor Core）。資料流由輸入 Tensor 經過各算子的計算產出中間特徵圖，最終產出預測結果。若需控制流（如迴圈、條件分支），MNN‑Express 提供圖層的程式化描述。整體設計強調低依賴、易於嵌入，核心函式庫在 Android 約 800KB、iOS 約 12MB，可透過 MNN_BUILD_MINI 進一步縮小。

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
