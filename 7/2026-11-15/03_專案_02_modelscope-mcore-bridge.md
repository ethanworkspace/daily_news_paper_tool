# GitHub 專案 02：modelscope/mcore-bridge

- 日期：2026-11-15
- URL：https://github.com/modelscope/mcore-bridge
- 描述：MCore-Bridge: Providing Megatron-Core model definitions for state-of-the-art large models and making Megatron training as simple as Transformers — with support for 300+ large language models (Qwen3-Next, GLM-5.3, Deepseek-V4, MiniMax-2.7, ...) and 200+ multimodal large models (Qwen3.8, Qwen3-Omni, Gemma4, ...).
- Stars：107  |  Forks：56  |  Language：Python
- License：Apache-2.0
- Topics：deepseek-r1, deepseek-v4, gemma4, glm-5, gpt-oss, llama4, llm, lora, megatron, minimax, ms-swift, peft, qwen3-5, qwen3-omni, qwen3-vl, transformers
- 更新時間：2026-11-11T12:50:57+00:00
- 配對論文：
- 品質分數：9/10 [implementation_signals]

## 在做什麼
MCore-Bridge 是 ModelScope 社群基於 Megatron-Core 生態系統開發的大語言模型與多模態大模型定義庫，提供 300+ 純文字及 200+ 多模態模型的 Megatron-Core 實作，讓研究者與工程師能以類似 Transformers 的使用方式進行大規模模型的全參數或 LoRA 訓練，解決 Megatron-Core 模型定義繁雜、支援度不足的問題。

## 技術
技術上，MCore-Bridge 以 Python 實作，依賴 Megatron-Core 進行模型定義與訓練，支援 Transformers、PEFT、ms-swift 生態系統，可直接載入與儲存 safetensors 權重；提供完整參數訓練與 LoRA 訓練，並支援 Megatron-Core 的多種平行策略（張量、管線、序列、上下文、專家、虛擬管線），以及多模態 FP8 訓練、MTP、序列填充自由與打包功能，可與 vLLM、SGLang 等推理框架相容。

## 架構
架構方面，MCore-Bridge 主要由模型定義庫（提供繼承 Megatron-Core 的模型類別與註冊機制）、權重載入／儲存工具（支援 safetensors、LoRA 權重）、訓練整合層（與 ms-swift、PEFT 結合，透過 torchrun 啟動多卡訓練）以及範例腳本組成。使用者先建立模型實例，載入預訓練權重或初始化，然後在資料載器饋入批次，透過前向傳播計算 logits，依任務類型計算 loss，再利用 Megatron-Core 的張量／管線等平行策略進行反向傳播與參數更新；訓練完成後可匯出 LoRA 或完整權重供 vLLM、SGLang 等推理框架使用。README 未詳細說明推論服務的內部實作，僅提及可參考模型卡進行推論。

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
