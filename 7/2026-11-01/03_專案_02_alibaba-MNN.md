# GitHub 專案 02：alibaba/MNN

- 日期：2026-11-01
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16605  |  Forks：2547  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-23T15:39:48+00:00
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MNN 是由阿里巴巴開發的輕量級、高效能的深度學習推理引擎，專為行動裝置與嵌入式平台設計。它支援多種模型格式的轉換與本地執行，特別針對大型語言模型（LLM）與擴散模型提供運行時解決方案，幫助開發者在智慧手機、PC、IoT 設備上實現低延遲、低記憶體占用的 AI 推理，目標使用者為行動應用開發者、AI 工程師以及需要端側運算的產品團隊。核心在於解決資源受限環境下模型推理速度慢、體積大的問題。

## 技術
MNN 以 C++ 實作，提供跨平台後端：CPU（ARMv7/ARMv8/ARMv9、x86/x64 SIMD、RISC‑V）、GPU（Metal、OpenCL、Vulkan、CUDA）、Hexagon DSP 以及其他 NPU。支援模型格式包括 TensorFlow、Caffe、ONNX、TorchScript，並內建 Winograd 卷積、半精度（FP16/BF16）與量化（INT8/INT4）優化。工具鏈含 MNN‑Converter、MNN‑Compress、MNN‑Express、MNN‑CV 與 MNN‑Train，以及基於 MNN 的 LLM 與擴散模型運行時。

## 架構
MNN 的架構分為前端模型轉換與後端執行兩層。前端使用 MNN‑Converter 將外部模型轉為 MNN 的靜態圖，進行圖優化與算子融合；接著根據目標硬體選擇對應後端（CPU、GPU、Hexagon 等）執行計算流程。資料流為：輸入張量 → 後端核心運算（利用 SIMD、向量指令或 GPU kernel） → 輸出張量。上層提供 MNN‑LLM、MNN‑Diffusion、MNN‑Express 等模組，分別負責語言模型、圖像生成與通用計算。由於 README 未詳細說明內部調度與線程模型，此部分需要進一步原始碼檢視才能確定。

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
