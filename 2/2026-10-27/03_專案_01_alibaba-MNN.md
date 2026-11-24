# GitHub 專案 01：alibaba/MNN

- 日期：2026-10-27
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16613  |  Forks：2546  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-24T10:13:08+00:00
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MNN 是由阿里巴巴開發的輕量級、高效能的深度學習推理引擎，專為行動裝置、嵌入式設備和邊緣 AI 場景設計。它支援多種主流模型格式（TensorFlow、Caffe、ONNX、TorchScript）以及常見網路結構（CNN、RNN、Transformer、GAN），提供量化（FP16/INT8/INT4/BF16）與多後端（CPU、GPU、DSP、NPU）加速，使開發者能在資源受限的手機、平板、IoT 設備上本地運行大型語言模型、擴散模型等應用，解決模型部署延遲高、功耗大與依賴雲端的問題。

## 技術
MNN 以 C++ 實作核心運算核心，利用 ARM NEON、SSE/AVX、Winograd 等優化演算法；支援 GPU 後端包括 Metal、OpenCL、Vulkan 與 CUDA，以及 Qualcomm Hexagon DSP、各種 NPU（Core ML、NNAPI、QNN 等）。模型轉換工具（MNN‑Converter）可將 TensorFlow、Caffe、ONNX、TorchScript 模型轉為 MNN 格式並做圖優化；量化工具（MNN‑Compress）提供 FP16、INT8、INT4、BF16 路徑；MNN‑Express 提供控制流與一般目的運算；MNN‑Train 支持訓練；MNN‑CV 提供輕量級圖像處理；此外還提供 Python API 讓工程師免除直接撰寫 C++。

## 架構
MNN 架構分為前端（模型轉換與優化）、運行時（Session、Executor、Backend Dispatch）與後端核心（CPU、GPU、DSP、NPU 實作）。使用者首先透過 MNN‑Converter 將原始模型轉換為 MNN 的序列化格式，過程中會進行常見的圖優化（如算子融合、常數折疊）。運行時載入模型後，根據目標硬體選擇適當的後端，將計算圖分解為後端特定的核心（如 ARM 的 Winograd 卷積、GPU 的 Metal/Vulkan kernel、Hexagon 的向量指令），然後在 Session 中執行，輸出結果。工具鏈方面，MNN‑Compress 負責模型壓縮與量化，MNN‑Express 支援控制流與自訂運算，MNN‑Train 提供訓練迴路，MNN‑CV 提供圖像前處理與後處理。若 README 未詳細說明某些內部調度細節，則以上描述以文件中可見的模組與功能為依據進行合理推斷。

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
