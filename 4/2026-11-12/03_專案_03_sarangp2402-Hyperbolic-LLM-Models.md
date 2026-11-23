# GitHub 專案 03：sarangp2402/Hyperbolic-LLM-Models

- 日期：2026-11-12
- URL：https://github.com/sarangp2402/Hyperbolic-LLM-Models
- 描述：A collection of latest Hyperbolic LLM Models with the corresponding paper titles, years of publication, links to the code, and dataset links.
- Stars：14  |  Forks：1  |  Language：unknown
- License：
- Topics：
- 更新時間：2026-10-25T16:28:56+00:00
- 配對論文：https://doi.org/10.1137/25m1795248
- 品質分數：5/10 [no_language, paper_paired]

## 在做什麼
本專案彙整最新的雙曲線大語言模型（Hyperbolic LLM）研究論文，提供論文標題、出版年份、期刊/會議、程式碼連結與資料集連結，旨在協助對雙曲幾何在語言模型中的應用感興趣的研究者快速檢索與比較相關工作。

## 技術
該專案以純文字 Markdown 形式維護，利用 GitHub 儲存庫進行版本控制，內容僅包含超連結至論文、原始程式碼與資料集，未涉及任何模型訓練或推論程式碼，技術重點在於資料的組織與連結呈現。

## 架構
檔案結構為單一 README.md，依照主題分節（如 Hybrid Hyperbolic‑Euclidean Models、Hyperbolic Fine‑tuned Models 等），每節以表格列出論文資訊；若需進一步擴展，可透過新增子目錄或檔案來分類不同年份或應用領域。由於僅為靜態資料彙整，沒有執行流程或模組間資料傳遞，架構推斷依據為 README 的章節與表格組織。

## README 摘錄（節選）
```text
# Hyperbolic-LLM-Models
A comprehensive collection of research papers on Hyperbolic Large Language Models with paper titles, publication years, code links, and dataset links.
## Table of Contents
- HypLLMs (#hypllms)
- Hybrid Hyperbolic-Euclidean Models (#hybrid-hyperbolic-euclidean-models)
- Hyperbolic Fine-tuned Models (#hyperbolic-fine-tuned-models)
- Fully Hyperbolic Models (#fully-hyperbolic-models)
- Hyperbolic State-Space Models (#hyperbolic-state-space-models)
- Foundations, Theory and Applications (#foundations-theory-and-applications)
- Hyperbolic Geometry Foundations (#hyperbolic-geometry-foundations)
- Background/Motivation (#backgroundmotivation)
- Hyperbolic Graph Neural Networks (#hyperbolic-graph-neural-networks)
- Riemannian Optimization Techniques (#riemannian-optimization-techniques)
- Numerical Stability and Challenges (#numerical-stability-and-challenges)
- Specialized Techniques and Methods (#specialized-techniques-and-methods)
- Core LLM, Transformer and Mamba Foundations (#core-llm-transformer-and-mamba-foundations)
- Brain Networks and Neuroscience Applications (#brain-networks-and-neuroscience-applications)
- Biomedical and Healthcare Applications (#biomedical-and-healthcare-applications)
--- 
## HypLLMs
### Hybrid Hyperbolic-Euclidean Models
Models that integrate hyperbolic geometry with traditional Euclidean operations, typically using exponential/logarithmic mappings.
| Paper Title | Year | Journal/ Conference | Code Link | Dataset Link |
|-------------|------|---------|-----------|--------------|
| ANTHEM: Attentive hyperbolic entity model for product search (https://dl.acm.org/doi/abs/10.1145/3488560.3498456) | 2022 | WSDM | Code (https://github.com/amazon-science/hyperbolic-embeddings) | E-commerce search data |
| Coneheads: Hierarchy aware attention (https://arxiv.org/abs/2306.00392) | 2023 | NeurIPS | Code (https://github.com/tsengalb99/coneheads) | IWSLT (https://huggingface.co/datasets/bbaaaa/iwslt14-de-en), ImageNet (https://image-net.org/index.php), Cora (https://graphsandnetworks.com/the-cora-dataset/), PPI (https://snap.stanford.edu/graphsage/#datasets)|
| Hyperbolic pre-trained language model (https://ieeexplore.ieee.org/document/10542420) | 2024 | IEEE | Code (https://github.com/thunlp/hyperbolic_llm) | GAP (https://github.com/google-research-datasets/gap-coreference), DPR (https://huggingface.co/datasets/coref-data/dpr_raw), WSC (https://huggingface.co/datasets/ErnestSDavis/winograd_wsc), WG (https://github.com/uclanlp/corefBias/tree/master/WinoBias/wino), PDP, FIGER (https://github.com/xiaoling/figer), Open Entity (https://www.cs.utexas.edu/~eunsol/html_pages/open_entity.html), CoNLL-2003 (https://www.clips.uantwerpen.be/conll2003/ner/), Few-NERD (https://ningding97.github.io/fewnerd/), TACRED (https://nlp.stanford.edu/projects/tacred/), TACREV (https://github.com/DFKI-NLP/tacrev), Re-TACRED (https://github.com/gstoica27/Re-TACRED), MRQA (https://mrqa.github.io/2019/shared.html)|
| Language models as hierarchy encoders (https://openreview.net/forum?id=GJMYvWzjE1&referrer=%5Bthe%20profile%20of%20Yuan%20He%5D(%2Fprofile%3Fid%3D~Yuan_He5)) | 2024 | NeurIPS | Code (https://github.com/KRR-Oxford/HierarchyTransformers) | WordNet (https://zenodo.org/records/14036213), FoodOn (https://zenodo.org/records/14036213), DOID (https://zenodo.org/records/14036213), SNOMED (https://zenodo.org/records/14036213) |
| Vision-language understanding in hyperbolic space (https://www.amazon.science/publications/vision-language-understanding-in-hyperbolic-space) | 2024 | SIGIR |- | Food-101 (https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/), CIFAR-10 (https://www.cs.toronto.edu/~kriz/cifar.html), CIFAR-100 (https://www.cs.toronto.edu/~kriz/cifar.html), CUB-200-2011 (https://www.vision.caltech.edu/datasets/cub_200_2011/), SUN397 (https://vision.princeton.edu/projects/2010/SUN/), Aircraft (https://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/), DTD (https://www.robots.ox.ac.uk/~vgg/data/dtd/), Pets (h
```
