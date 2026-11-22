# GitHub 專案 02：PolyU-VCLab/HarnessIR

- 日期：2026-11-01
- URL：https://github.com/PolyU-VCLab/HarnessIR
- 描述：HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration
- Stars：39  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-16T02:11:09+00:00
- 配對論文：https://arxiv.org/abs/2610.10133
- 品質分數：8/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration
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
Zhengqiang Zhan

主要語言：Python；Stars：39；License：MIT

## 技術
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

## 架構
Click to expand the pipeline description
Two choices distinguish it from prior pipelines: **no restoration tool is scheduled** (the auxiliary tools supply evidence for writing the prompt, not links in a restoration chain), and **the executor sees only the image and text** (diagnostic maps inform the prompt writer but are never passed to the editor, which would otherwise copy their colours into the output). HarnessIR is **inference-only**.
A higher NR-IQA score does not by itself indicate better restoration: a model that repaints text or fabricates structure can still outscore its own ground truth. Therefore, for images with GT, we calculate the absolute difference between their NR-IQA scores and those of the corresponding GT images. We also report an independent VLM evaluator, giving **D-Score** for degradation removal and **F-Score** for content preservation (both 0&ndash;100), combined as their per-image geometric mean, **DF-Score** &mdash; taken per image and then averaged, so one image's strong D-Score cannot offset another image's broken F-Score:

相關論文/文件：https://arxiv.org/abs/2610.10133

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
