# GitHub 專案 03：alibaba/MNN

- 日期：2026-11-20
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16593  |  Forks：2545  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-22T13:58:13+00:00
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MNN 是阿里巴巴開發的輕量級、高效能的深度學習推理引擎，專為行動裝置與嵌入式平台設計。它支援多種主流模型格式（TensorFlow、Caffe、ONNX、Torchscript），並提供 LLM、擴散模型等應用的本地運行解決方案，目標使用者為需要在智慧手機、平板、IoT 設備上實現低延遲、低功耗 AI 推論的開發者與產品團隊，核心問題是解決資源受限環境下模型推論的速度與記憶體佔用。

## 技術
MNN 的核心以 C++ 實作，提供跨平台後端包括 CPU（ARM/x86，利用 Winograd、SSE/AVX、NEON 等優化指令）、GPU（Metal、OpenCL、Vulkan、CUDA）以及 Hexagon DSP、NPU 等專用加速器。它能直接匯入 TensorFlow、Caffe、ONNX、Torchscript 模型，經過圖優化與量化（FP16、INT8、INT4）後執行。此外，MNN 還附帶 Python API、模型轉換工具（MNN‑Converter）、壓縮工具（MNN‑Compress）、支援控制流的 MNN‑Express、輕量級電腦視覺庫 MNN‑CV 以及訓練框架 MNN‑Train。

## 架構
MNN 的架構由核心推理引擎與多種後端組成。使用者先透過 MNN‑Converter 將外部模型轉換為 MNN 內部格式，隨後經過 MNN‑Compress 進行量化或剪枝以減少模型大小。運行時，MNN 會根據裝置偵測結果選擇適當的後端（CPU、GPU、Hexagon DSP 或 NPU），將計算圖分解為基本算子，並呼叫對應的優化內核（如 ARM 彙編、Winograd 卷積、Metal/Vulkan 着色器）進行執行。中間結果以 Tensor 形式在記憶體中流動，最終輸出預測值。若要支援控制流或自定義運算，可使用 MNN‑Express；若需影像前處理，可調用 MNN‑CV。訓練則透過 MNN‑Train 完成。由於 README 未詳細說明後備切換的具體決策邊界與記憶體管理細節，此部分需要進一步原始碼檢視才能確定。

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
