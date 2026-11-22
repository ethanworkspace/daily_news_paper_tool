# GitHub 專案 02：modelscope/mcore-bridge

- 日期：2026-11-19
- URL：https://github.com/modelscope/mcore-bridge
- 描述：MCore-Bridge: Providing Megatron-Core model definitions for state-of-the-art large models and making Megatron training as simple as Transformers — with support for 300+ large language models (Qwen3-Next, GLM-5.3, Deepseek-V4, MiniMax-2.7, ...) and 200+ multimodal large models (Qwen3.8, Qwen3-Omni, Gemma4, ...).
- Stars：107  |  Forks：56  |  Language：Python
- License：Apache-2.0
- Topics：deepseek-r1, deepseek-v4, gemma4, glm-5, gpt-oss, llama4, llm, lora, megatron, minimax, ms-swift, peft, qwen3-5, qwen3-omni, qwen3-vl, transformers
- 更新時間：2026-11-11T12:50:57+00:00
- 配對論文：
- 品質分數：9/10 [implementation_signals]

## 在做什麼
MCore‑Bridge 是 ModelScope 社群基於 Megatron‑Core 構建的大語言模型與多模態大模型定義庫，旨在為 300+ 純文字及 200+ 多模態最先進模型提供 Megatron‑Core 相容的模型定義，使得訓練流程能像使用 Transformers 一樣簡單。適用於需要大規模預訓練或微調的研究者與工程師，解決 Megatron‑Core 使用門檻高、模型適配繁雜的問題。

## 技術
該專案以 Python 實作，基於 Megatron‑Core 提供模型定義，並整合 Transformers、PEFT（LoRA）與 ms‑swift 生態，支援完整參數訓練與 LoRA 微調。利用 Megatron‑Core 的張量、管線、序列、上下文、專家及虛擬管線並行策略，並加入 FP8 訓練、MTP、序列免填充與打包等多模態能力。可在 A10/A100/H100/B200、RTX 系列及國產 Ascend NPU 上運行，並能直接載入/儲存 safetensors 權重，相容於 vLLM、SGLang 等推理框架。

## 架構
MCore‑Bridge 的核心是一組 Megatron‑Core 相容的模型定義檔案（model.py），使用者透過腳本（如 test.py）載入對應模型類別，結合 ms‑swift 的訓練配置或自行編寫訓練迴圈，經 torchrun 啟動多卡並行訓練。訓練過程中，資料經過 Tokenizer 後送入模型，模型依據張量/管線/序列等並行策略分配計算，搭配 Optimizer（如 AdamW）與可選的 PEFT LoRA 更新。訓練完成後，可直接儲存完整或 LoRA 權重為 safetensors，亦可匯出至 Transformers 格式以供 vLLM、SGLang 等推理框架使用。整個流程依賴 Megatron‑Core 的運行時環境（Transformer Engine、APEX 等）與 ModelScope 的模型權重下載。

## README 摘錄（節選）
```text
# MCore-Bridge: Making Megatron training as simple as Transformers
--> 
Providing Megatron-Core model definitions for state-of-the-art large models
ModelScope
中文 &nbsp ｜ &nbsp English &nbsp
--> 
English Documentation &nbsp ｜ &nbsp 中文文档 &nbsp
--> 
## 📖 Table of Contents
- Groups (#-Groups)
- News (#-news)
- Installation (#%EF%B8%8F-installation)
- Model List (#-Model-List)
- Quick Start (#-quick-Start)
- License (#-License)
## ☎ Groups
You can contact us and communicate with us by adding our group:
| WeChat Group |
|:-------------------------:|
| |
## 📝 Introduction
** mcore-bridge** is a large language model and multimodal large model definition library built on the Megatron-Core ecosystem, developed by the ModelScope community. It currently supports 300+ text-only models and 200+ multimodal models, including large language models such as Qwen3-Next, GLM-5.1, DeepSeek-V4, Minimax-2.7, Kimi-K2.5, and GPT-OSS, as well as multimodal large models such as Qwen3.5, Qwen3-Omni, Gemma4, GLM4.6-V, InternVL3.5, and Ovis2.5.
------ 
** Why Choose mcore-bridge?**
- **Model Coverage**: Supports 300+ text-only large language models and 200+ multimodal large models, with Day 0 support for popular models.
- **Hardware Support**: Compatible with a wide range of hardware platforms, including A10/A100/H100/B200, RTX series, and domestic hardware such as Ascend NPU.
- **Training Methods**: Supports both full-parameter training and LoRA training, with compatibility with the PEFT ecosystem.
- **Parallelism Techniques**: Supports multiple parallelism strategies provided by Megatron-Core, including tensor parallelism, pipeline parallelism, sequence parallelism, context parallelism, expert parallelism, and virtual pipeline parallelism.
- **Multimodal Capabilities**: Supports multimodal FP8 training, MTP, sequence padding-free, and packing features.
- **Task Types**: Supports a variety of task types, including Causal LM, sequence classification, Embedding, and Reranker.
- **Ecosystem Compatibility**: Supports direct loading and saving of LoRA/full-parameter safetensors weights, with compatibility with mainstream inference frameworks such as Transformers, vLLM, and SGLang.
------ 
** Related Documentation:**
- Integrating Mcore-Bridge with ms-swift (https://swift.readthedocs.io/en/latest/Megatron-SWIFT/Mcore-Bridge.html)
- Supported Models List (https://swift.readthedocs.io/en/latest/Instruction/Supported-models-and-datasets.html)
- Custom Megatron Models (https://swift.readthedocs.io/en/latest/Megatron-SWIFT/Custom-Model.html)
- Qwen3.5 Training Best Practices (https://swift.readthedocs.io/en/latest/BestPractices/Qwen3_5-Best-Practice.html)
## 🎉 News
- 🎉 2026.03.30: MCore-Bridge is released! Providing Megatron-Core model definitions for state-of-the-art large models and making Megatron training as simple as Transformers.
## 🛠️ Installation
To install using pip:
[code block omitted]
To install from source:
[code block omitted]
Recommended Runtime Environment:
| | Range | Recommended | Notes |
|--------------|--------------|-------------|--------------------|
| python | >=3.10 | 3.12 | |
| cuda | | cuda12.8/13.0 | |
| torch | >=2.0 | 2.8.0/2.11.0 | |
| transformer-engine | >=2.3 | 2.14.1 | |
| apex | | 0.1 | Optional |
| megatron-core | >=0.18, =4.33 | 4.57.6/5.8.1 | |
| modelscope | >=1.23 | | |
| peft | >=0.11, qwen3, qwen3_moe, qwen3_next |
| DeepSeek | deepseek_v3, deepseek_v32, deepseek_v4 |
| GLM | glm4, glm4_moe, glm4_moe_lite glm_moe_dsa |
| MiniMax | minimax_m2 |
| Kimi | kimi_k2 |
| Bailing | bailing_moe, bailing_hybrid |
| InternLM | internlm3 |
| Llama | llama |
| GPT-OSS | gpt_oss |
| Hunyuan | hy_v3 |
| ERNIE | ernie4_5, ernie4_5_moe |
| MiMo | mimo |
| Dots | dots1 |
| OLMoE | olmoe |
** multimodal large models:**
| Series | model_type |
| -------- | ------------------------------------------------------------ |
| Qwen | qwen2_vl, qwen2_5_vl, qwen2_5_omni qwen3_vl, qwen3_vl_moe, qwen3_omni_moe, qwen3_asr qwen3_5, qwen3_5_moe |
| Gemma | ge
```
