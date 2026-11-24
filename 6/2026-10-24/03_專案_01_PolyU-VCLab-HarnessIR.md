# GitHub 專案 01：PolyU-VCLab/HarnessIR

- 日期：2026-10-24
- URL：https://github.com/PolyU-VCLab/HarnessIR
- 描述：HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration
- Stars：39  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-16T02:11:09+00:00
- 配對論文：https://arxiv.org/abs/2610.10133
- 品質分數：8/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
HarnessIR 是一種利用多模態基礎模型（MFM）作為統一執行器，通過感知診斷、按需工具調用、提詞組成、單次執行以及驗證驅動的精煉五個階段，實現通用真實世界圖像修復的框架。它不依賴預先排程的修復工具鏈，而是讓多模態模型僅根據圖像與文本提示進行編輯，適合需要處理各種未知退化的研究者與開發者。

## 技術
該專案以 Python 實作，核心依賴多模態基礎模型（如 Nano Banana 2 與 GPT-Image-2.5-Sunburst）作為圖像編輯執行器，並呼叫本地檢查點中的輔助工具（如去噪、去模糊等）產生圖像證據。透過 harness/settings.py 設定 API 端點、金鑰與模型 ID，使用 manifest（JSON/JSONL）描述輸入圖像與可選的修復意圖，四個腳本分別提供基線直接使用、完整 harness 流程、全參考與無參考圖像品質評估，以及 D‑Score、F‑Score 與 DF‑Score 的計算。整個流程僅在推論階段進行，不涉及訓練。

## 架構
HarnessIR 的執行流程分為五個階段：首先，感知診斷階段使用 VLM 讀取低質量圖像，辨識退化類型並決定需要調用的輔助工具；其次，按需工具調用階段僅執行被選中的工具，產生圖像特定的證據圖或特徵；第三，提詞組成階段將這些證據與使用者意圖組合成單一的文本提詞，說明何處需要修復、何處必須保持不變；第四，執行階段將原始低質量圖像與該提詞一次性送入多模態基礎模型，得到修復結果；第五，驗證驅動的精煉階段根據預設的修復需求（如去除退化、保留內容）判斷結果是否達標，若不達標則從原始低質量圖像重新開始執行階段（可透過 --redo 啟用）。整個過程中，輔助工具僅提供證據用於提詞撰寫，不直接參與圖像編輯，且多模態模型僅接受圖像與文本作為輸入。

## README 摘錄（節選）
```text
# HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration
Restoration by harnessing an MFM executor, not by scheduling restoration tools.
(https://arxiv.org/abs/2610.10133)
(https://huggingface.co/datasets/VCLab-PolyU/HarnessIR/tree/main)
(https://pan.baidu.com/s/1CIGdo-hMLsedI-Q0yUT-Iw?pwd=ngjt)
(https://polyu-vclab.github.io/HarnessIR/)
Xiangtao Kong (https://scholar.google.com/citations?user=lueNzSgAAAAJ) 1,2 |
Shuaizheng Liu (https://scholar.google.com/citations?user=wzdCc-QAAAAJ) 1,2 |
Rongyuan Wu (https://scholar.google.com/citations?user=A-U8zE8AAAAJ) 1,2 |
Lingchen Sun (https://scholar.google.com/citations?user=ZCDjTn8AAAAJ) 1,2 |
Zhengqiang Zhang (https://scholar.google.com/citations?user=UX26wSMAAAAJ) 1,2 |
Jixin Zhao (https://scholar.google.com/citations?user=0Z89rfUAAAAJ) 1,2 |
Yuhui Wu (https://scholar.google.com/citations?user=Qt4WlSkAAAAJ) 1,2 |
Lei Zhang (https://www4.comp.polyu.edu.hk/~cslzhang/) 1,2,&dagger;
1 The Hong Kong Polytechnic University
2 OPPO Research Institute
&dagger; Corresponding author.
## &#x1F4CC; Quick Links
- &#x1F4F0; News (#news)
- &#x1F9F0; HarnessIR (#method)
- &#x1F4CA; Evaluation Protocol and Metrics (#evaluation)
- &#x1F5BC;&#xFE0F; Experimental Results (#results)
- &#x1F50D; Visual Results (#visual)
- &#x1F3CB;&#xFE0F; Deployment (#deployment)
- &#x1F4EE; Contact (#contact)
- &#x1F4DA; Citation (#citation)
## &#x1F4F0; News
- **2026-10-07**: Released the code, benchmark and visual results of HarnessIR.
--- 
## &#x1F9F0; HarnessIR
Click to expand the pipeline description
Prior agentic IR methods apply task-specific restoration models in sequence, and are therefore bounded by those tools. HarnessIR keeps **one MFM as the executor** and varies only the prompt it is given. Five stages:
1. **Perception and diagnosis** &mdash; a VLM reads the content and its degradations, and names which auxiliary tools to consult.
2. **On-demand tool invocation** &mdash; only the planned tools run, returning image-specific evidence.
3. **Prompt composition** &mdash; the evidence is composed into one prompt stating what to treat and what must survive untouched.
4. **Execution** &mdash; the MFM receives the original LQ image and that prompt, in a single pass.
5. **Verification-driven refinement** &mdash; the result is judged against the restoration requirements, and re-executed **from the original LQ input** only when it fails.
Two choices distinguish it from prior pipelines: **no restoration tool is scheduled** (the auxiliary tools supply evidence for writing the prompt, not links in a restoration chain), and **the executor sees only the image and text** (diagnostic maps inform the prompt writer but are never passed to the editor, which would otherwise copy their colours into the output). HarnessIR is **inference-only**.
--- 
## &#x1F4CA; Evaluation Protocol and Metrics
Click to expand the evaluation protocol
Fidelity is measured with full-reference metrics (PSNR, SSIM, LPIPS, DISTS) and image quality with no-reference metrics (MANIQA, CLIP-IQA, MUSIQ, TOPIQ, AFINE-NR).
A higher NR-IQA score does not by itself indicate better restoration: a model that repaints text or fabricates structure can still outscore its own ground truth. Therefore, for images with GT, we calculate the absolute difference between their NR-IQA scores and those of the corresponding GT images. We also report an independent VLM evaluator, giving **D-Score** for degradation removal and **F-Score** for content preservation (both 0&ndash;100), combined as their per-image geometric mean, **DF-Score** &mdash; taken per image and then averaged, so one image's strong D-Score cannot offset another image's broken F-Score:
$$\mathrm{DF\text{-}Score} = \frac{1}{N}\sum_{i=1}^{N}\sqrt{D_i \cdot F_i}$$
The evaluator's criteria come from each image's degradation type, never from the prompt the method was given: a method must not be able to change the yardstick by changing what it asks for.
--- 
## &#x1F5BC;&#xFE
```
