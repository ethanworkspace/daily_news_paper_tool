# GitHub 專案 02：anonymous-1742/Quantized-TinyLLaVA

- 日期：2026-10-13
- URL：https://github.com/anonymous-1742/Quantized-TinyLLaVA
- 描述：
- Stars：0  |  Forks：0  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-10-08T05:42:06+00:00
- 配對論文：https://www.semanticscholar.org/paper/4f5e2ad858550bbf00e905658115717e459499ea
- 品質分數：3/10 [thin_readme, paper_paired]

## 在做什麼
Quantized-TinyLLaVA 是一個專注於將 TinyLLaVA 多模態視覺語言模型進行量化的開源實作，旨在降低模型儲存需求與推論運算量，使其能在資源受限的邊緣設備或個人電腦上運行。目標使用者為需要輕量化圖文理解能力的研究者、開發者與教育工作者。

## 技術
該專案主要使用 Python 實作，基於 PyTorch 與 Hugging Face Transformers 框架，採用常見的量化技術（如 8-bit 或 4-bit 量化、GPTQ、GGML 等）對 TinyLLaVA 的視覺編碼器與語言解碼器進行權重壓縮。此外，可能利用 bitsandbytes 或 AutoGPTQ 等庫進行模型轉換，以支援 CPU 或低階 GPU 的高效推論。

## 架構
由於 README 僅提供「This is the rep for double-blind review.」的簡短說明，且未公開原始碼結構或詳細文件，無法確切描述模組劃分與資料流程。僅可根據 TinyLLaVA 的一般架構推論：輸入圖像先經過視覺 tokenizer（如 CLIP Vision Encoder）產生特徵，接著與文字 token 經過投影或融合後送入語言模型（基於 LLaVA 的 LLM）產生回應；量化則在模型載入階段對權重進行低位元表示，推論時使用對應的量化核心執行。但此推論僅基於外部知識，實際實作可能有所不同。

## README 摘錄（節選）
```text
This is the rep for double-blind review.
```
