# GitHub 專案 03：alibaba/MNN

- 日期：2026-11-19
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16592  |  Forks：2545  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-22T13:23:18+00:00
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MNN 是一個由阿里巴巴開發的輕量級、高效能深度學習推理引擎，專為行動裝置與邊緣設備設計。它支援多種主流框架模型的轉換與量化，提供本地大型語言模型（LLM）與擴散模型的執行環境，目標使用者為行動開發者、邊緣 AI 工程師以及需要在資源受限平台上部署 AI 模型的研究者，解決模型在手機、IoT 與嵌入式裝置上推論延遲高、體積大且依賴重的問題。

## 技術
MNN 以 C++ 實作核心運算核心，提供 Python API 以及命令列工具（MNN‑Converter、MNN‑Compress、MNN‑Express、MNN‑CV、MNN‑Train）支援 TensorFlow、Caffe、ONNX、TorchScript 模型的匯入與圖形優化。內建 FP16、BF16、INT8/INT4 量化路徑，並針對 CPU（ARMv7/ARMv8/ARMv9、x86/x64 SIMD、Winograd 卷積）、GPU（Metal、OpenCL、Vulkan、CUDA）以及 NPU（Hexagon、CoreML、QNN 等）提供後端實作，使模型能在異質硬體上進行高效推論。

## 架構
MNN 的架構分為前端模型轉換與優化層、執行時期的後端調度層與上層應用套件。使用者先透過 MNN‑Converter 將外部框架模型轉換為 MNN 內部格式，經過圖形壓縮與算子融合優化後得到 .mnn 模型；運行時，MNN Runtime 根據目標裝置偵測選擇適當的後端（CPU、GPU 或 NPU），載入算子核心（含經過組織化的 Assembly、Winograd 卷積或 tensorcore 實作），執行前向推論並回傳結果。上層提供 MNN‑LLM 與 MNN‑Diffusion 套件，分別在同一引擎上實現大型語言模型與擴散模型的本地化部署。若 README 未詳細說明後端調度細節，則此部份為基於可見模組與工具的合理推斷。

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
