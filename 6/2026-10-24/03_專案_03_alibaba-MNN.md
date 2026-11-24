# GitHub 專案 03：alibaba/MNN

- 日期：2026-10-24
- URL：https://github.com/alibaba/MNN
- 描述：MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
- Stars：16612  |  Forks：2546  |  Language：C++
- License：Apache-2.0
- Topics：arm, convolution, deep-learning, embedded-devices, llm, machine-learning, ml, mnn, transformer, vulkan, winograd-algorithm
- 更新時間：2026-11-24T09:10:59+00:00
- 配對論文：https://arxiv.org/abs/2611.12311
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MNN 是阿里巴巴開源的輕量級深度學習推理引擎，專為移動終端、嵌入式設備和邊緣 AI 場景設計。它提供模型轉換、量化、GPU/CPU 混合加速以及本地大語言模型（LLM）運行支援，目標使用者包括需要在手機、平板、IoT 設備上實現低延遲、低功耗推理的開發者與產品團隊，核心問題是解決傳統框架在資源受限裝置上的體積大、速度慢及依賴複雜的部署困難。

## 技術
MNN 以 C++ 實作，提供跨平台靜態庫與動態庫（iOS ~12MB，Android core.so ~800KB），支援 TensorFlow、Caffe、ONNX、TorchScript 模型轉換及 178+ TensorFlow、52+ Caffe、163+ TorchScript、158+ ONNX 算子。內建 CPU 優化（ARM NEON、x86 SSE/AVX/AVX512、SME2、RVV），GPU 後端使用 Metal、OpenCL、Vulkan、CUDA，並提供 INT4/W4A16 量化、FP16/BF16 精度路徑。此外，MNN-LLM 與 MNN-Diffusion 分別基於該引擎實現本地 LLM 與擴散模型推理。

## 架構
MNN 架構由核心推理引擎、模型轉換工具（MNN‑Converter）、模型壓縮工具（MNN‑Compress）、表達式編程框架（MNN‑Express）、輕量級影像處理庫（MNN‑CV）與訓練套件（MNN‑Train）組成。使用者先將 TensorFlow、Caffe、ONNX 或 TorchScript 模型轉換為 MNN 格式，然後透過 MNN Interpreter 建立 Session，選擇 CPU（支援 ARM NEON、x86 SSE/AVX/AVX512、SME2、RVV）或 GPU（Metal、OpenCL、Vulkan、CUDA）後端執行，亦可透過 Hexagon DSP 或 CoreML 等 NPU 加速。計算過程中，張量在內部緩衝區流動，支援靜態與動態形狀、多輸入/輸出以及控制流。最終結果經過後處理返回給上層應用。

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
