# GitHub 專案 03：modelscope/mcore-bridge

- 日期：2026-11-20
- URL：https://github.com/modelscope/mcore-bridge
- 描述：MCore-Bridge: Providing Megatron-Core model definitions for state-of-the-art large models and making Megatron training as simple as Transformers — with support for 300+ large language models (Qwen3-Next, GLM-5.3, Deepseek-V4, MiniMax-2.7, ...) and 200+ multimodal large models (Qwen3.8, Qwen3-Omni, Gemma4, ...).
- Stars：107  |  Forks：56  |  Language：Python
- License：Apache-2.0
- Topics：deepseek-r1, deepseek-v4, gemma4, glm-5, gpt-oss, llama4, llm, lora, megatron, minimax, ms-swift, peft, qwen3-5, qwen3-omni, qwen3-vl, transformers
- 更新時間：2026-11-11T12:50:57+00:00
- 配對論文：
- 品質分數：9/10 [implementation_signals]

## 在做什麼
MCore-Bridge: Providing Megatron-Core model definitions for state-of-the-art large models and making Megatron training as simple as Transformers — with support for 300+ large language models (Qwen3-Next, GLM-5.3, Deepseek-V4, MiniMax-2.7, ...) and 200+ multimodal large models (Qwen3.8, Qwen3-Omni, Gemma4, ...).
MCore-Bridge: Providing Megatron-Core model definitions for state-of-the-art large models and making Megatron training as simple as Transformers — with support for 300+ large language models (Qwen3-Next, GLM-5.3, Deepseek-V4, MiniMax-2.7, ...) and 200+ multimodal large models (Qwen3.8, Qwen3-Omni, Gemma4, ...).

主要語言：Python；Topics：deepseek-r1, deepseek-v4, gemma4, glm-5, gpt-oss, llama4, llm, lora；Stars：107；License：Apache-2.0

## 技術
實作語言以 Python 為主。
從 topics 可見技術方向：deepseek-r1, deepseek-v4, gemma4, glm-5, gpt-oss, llama4, llm, lora。
專案描述：MCore-Bridge: Providing Megatron-Core model definitions for state-of-the-art large models and making Megatron training as simple as Transformers — with support for 300+ large language models (Qwen3-Next, GLM-5.3, Deepseek-V4, MiniMax-2.7, ...) and 200+ multimodal large models (Qwen3.8, Qwen3-Omni, Gemma4, ...).

## 架構
README 未明確提供架構章節；依描述推斷此專案聚焦於：MCore-Bridge: Providing Megatron-Core model definitions for state-of-the-art large models and making Megatron training as simple as Transformers — with support for 300+ large language models (Qwen3-Next, GLM-5.3, Deepseek-V4, MiniMax-2.7, ...) and 200+ multimodal large models (Qwen3.8, Qwen3-Omni, Gemma4, ...).

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
