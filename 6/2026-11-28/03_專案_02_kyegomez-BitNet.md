# GitHub 專案 02：kyegomez/BitNet

- 日期：2026-11-28
- URL：https://github.com/kyegomez/BitNet
- 描述：Implementation of "BitNet: Scaling 1-bit Transformers for Large Language Models" in pytorch
- Stars：1951  |  Forks：175  |  Language：Python
- License：MIT
- Topics：artificial-intelligence, deep-neural-networks, deeplearning, gpt4, machine-learning, multimodal, multimodal-deep-learning
- 更新時間：2026-11-23T18:23:14+00:00
- 論文層級：未對應論文
- 配對論文：https://arxiv.org/abs/2310.11453
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
本專案實現了論文《BitNet: Scaling 1-bit Transformers for Large Language Models》提出的 1-bit 線性層（BitLinear），以 PyTorch 為基礎，提供可直接替換 nn.Linear 的模組，使研究者能在 Transformer 中使用極低精度權重進行訓練或微調，目標使用者為深度學習研究者與模型壓縮工程師，核心問題在於如何在不重新訓練大型模型的情況下，將權重壓縮至 1-bit 以顯著降低記憶體與計算成本，同時保持語言建模能力。

## 技術
該專案主要使用 Python 與 PyTorch 實作，核心為 BitLinear 模組，其流程為 layer normalisation → 二值化 → 絕對最大值量化 → 反量化；此外提供 BitAttention（採用 BitLinear 並結合 Multi‑Grouped Query Attention 以加速解碼與長上下文處理）、BitFeedForward、BitLora、BitMoE、BitMamba 等變體，並針對 BitLinear 提供經過 CUDA 優化的核心（python setup.py build_ext --inplace），支援 HuggingFace 模型載入與 drop‑in 替換現有 PyTorch 模型，訓練必須從頭或微調，無法直接套用於已訓練好的全精度模型。

## 架構
架構上，BitNetTransformer 由多個相同的 Transformer 區塊堆疊構成，每個區塊先經過層正規化，然後將輸入送入 BitAttention：BitAttention 內部的 query、key、value 投影皆使用 BitLinear（層正規化 → 二值化 → 絕對最大值量化 → 反量化），經過 Multi‑Grouped Query Attention 計算注意力分數後，再透過另一個 BitLinear 進行輸出投影，殘差相加後進入 BitFeedForward：BitFeedForward 由兩個 BitLinear 與 GELU 活化函數組成（Linear → GELU → Linear），同樣殘差相加並加上層正規化。所有區塊的輸出最終通過最後的層正規化與線性投影（亦可為 BitLinear）產生語言模型的 logits。若用於視覺或多模態任務，則將圖像 patch 嵌入作為序列輸入，其餘流程相同。由於 README 未提供完整圖示，以上說明基於文中對 BitLinear、BitAttention、BitFeedForward 的文字描述進行合理推斷。

## README 摘錄（節選）
```text
(https://discord.gg/qUtxnK2NMf)
# BitNet
PyTorch Implementation of the linear methods and model from the paper "BitNet: Scaling 1-bit Transformers for Large Language Models"
Paper link: (https://arxiv.org/pdf/2310.11453.pdf)
BitLinear = tensor -> layernorm -> Binarize -> abs max quantization -> dequant
"The implementation of the BitNet architecture is quite simple, requiring only the replacement of linear projections (i.e., nn.Linear in PyTorch) in the Transformer. " -- BitNet is really easy to implement just swap out the linears with the BitLinear modules!
## **NEWS**
- **New Iteration** 🔥 There is an all-new iteration from the paper "The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits (https://arxiv.org/abs/2402.17764)", we're implementing it now. Join the Agora discord and contribute! Join Here (https://discord.gg/hFzevCjG8c)
- **New Optimizations** The first `BitLinear` has been optimized and we now have a Bit Attention `BitMGQA` That implements BitLinear into the attention mechanism. Multi Grouped Query Attention is also widely recognized as the best attention for its fast decoding and long context handling, thanks to Frank for his easy to use implementation!
- **BitLinear 1.5 Launch 🔥**: The new BitLinear 1.5 is still in progress 🔥 [Here is the file]() There are still some bugs like with the dequantization algorithm and we still need to replace the multiplication with elementwisw addition, if you could help with this, this would be amazing.
- **NOTICE**: A model obviously needs to be finetuned from scratch to use BitLinear, just changing the linear methods in an already trained model isn't going to work. Finetune or train from scratch.
## Appreciation
- Dimitry, Nullonix for analysis and code review and revision
- Vyom, for providing 4080 to train!
## Installation
[code block omitted]
## Usage
We have a vast selection of example scripts here and in the examples folder: (/examples/), let me know if you want assistance with a use-case in the discord!
### `BitLinear`
- Example of the BitLinear layer which is the main innovation of the paper!
[code block omitted]
### BitLinearNew
[code block omitted]
---- 
### `BitNetTransformer`
- Fully implemented Transformer as described in the diagram with MHA, and BitFeedforwards
- Can be utilized not just for text but for images and maybe even video or audio processing
- Complete with residuals and skip connections for gradient flow
[code block omitted]
### `BitAttention`
This Attention has been modified to use BitLinear instead of the default linear projection. It's also using Multi-Grouped Query Attention instead of regular multi-head attention for faster decoding and longer context handling.
[code block omitted]
### `BitFeedForward`
- Feedforward as shown in the diagram with BitLinear and a GELU:
- Linear -> GELU -> Linear
- You can add dropouts, or layernorms, or other layers for a better ffn
[code block omitted]
## Inference
[code block omitted]
## Huggingface Usage
[code block omitted]
## Drop in Replacement for Pytorch Models
[code block omitted]
### Optimized Cuda Kernel
`python setup.py build_ext --inplace`
[code block omitted]
## `BitLora`
Implementation of BitLora!
[code block omitted]
## BitMamba
[code block omitted]
## `BitMoE`
[code block omitted]
### 1 Bit Vision Transformers
This idea came to me out of nowhere but it seems to be pretty fun, as you can leverage bitlinear for vision tasks for ultra-compression. It would be nice to train this on imagenet if you could make a script, we'll provide the compute. Then the next stage would be to train a join vision language model gpt-4o
[code block omitted]
# License
MIT
# Citation
[code block omitted]
# Todo
- [x] Double check BitLinear implementation and make sure it works exactly as in paper
- [x] Implement training script for `BitNetTransformer`
- [x] Train on Enwiki8, copy and past code and data from Lucidrains repos
- [x] Benchmark performance
- [x] Look into Straight Through Estimator for non-differentiable
```
