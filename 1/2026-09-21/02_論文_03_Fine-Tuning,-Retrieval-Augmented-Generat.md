# 論文 03：Fine-Tuning, Retrieval-Augmented Generation, and Hybrid Adaptation of Language Models for Clinical Decision-Making in Health Care: Systematic Review.

- 日期：2026-09-21
- 來源層級：Tier 2
- 期刊/會議/來源：Journal of medical Internet research
- Venue：Journal of medical Internet research
- 發布時間：2026-09-17T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42753254/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13585368/
- DOI：10.2196/104092
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：3699（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
BACKGROUND: Large language models (LLMs) demonstrate strong performance on medical knowledge benchmarks, but their safe and effective use in clinical practice depends on posttraining adaptation rather than raw model capability. Fine-tuning, retrieval-augmented generation (RAG), and hybrid approaches are principal strategies for grounding language models in clinical evidence, yet their comparative effectiveness remains unclear. OBJECTIVE: This systematic review aims to synthesize evidence on fine-tuning, RAG, and hybrid posttraining strategies for clinical diagnosis and decision-support tasks and to identify strategy-task alignments and methodological features associated with improved performance. METHODS: We conducted a systematic review in accordance with PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) 2020 guidelines. PubMed/MEDLINE, Scopus, and Web of Science were searched from January 2018 through May 2026. Eligible studies evaluated transformer-based language models that underwent posttraining adaptation, retrieval augmentation, or both for clinical decision support, diagnosis, triage, risk stratification, or related health care applications. Studies evaluating nonadapted models, non-language-model AI systems, prompt engineering without performance evaluation, or nonclinical applications were excluded. Data extracted included model architecture, adaptation strategy, clinical domain, validation approach, and performance outcomes. Risk of bias was assessed using PROBAST+AI (Prediction model Risk of Bias Assessment Tool for AI). Studies were grouped according to the primary enhancement strategy (fine-tuning or parameter-efficient fine-tuning, RAG, or hybrid approaches), and findings were synthesized descriptively. RESULTS: Of 1890 identified records, 35 studies published between 2024 and 2026 met eligibility criteria. Enhancement strategies included RAG (17/35, 48.6%), fine-tuning or parameter-efficient fine-tuning (7/35, 20%), and hybrid approaches (11/35, 31.4%). Studies included diverse specialties from oncology, neurology, radiology, mental health, cardiology, ophthalmology, and surgical care. Fine-tuning demonstrated strong performance for task-specific applications, achieving area under the receiver operating characteristic curve values up to 0.912 for cancer detection and area under curve of 0.892 for major depressive disorder prediction, while matching clinician-level diagnostic performance in several studies. RAG improved guideline adherence and diagnostic accuracy, with increases from 71.1% to 92.1% and from 78.9% to 94.7% in guideline-based decision-support tasks. However, benefits were inconsistent across larger reasoning-capable models. Hybrid systems generally achieved the strongest performance in complex clinical workflows, with external validation accuracies exceeding 90% in stroke triage, dermatology, multimodal imaging, and oncology applications. Risk-of-bias assessment identified substantial methodological limitations, with 25 studies judged as high risk, 9 as unclear risk, and only 1 as low risk overall. Common concerns included inadequate external validation, lack of calibration assessment, nonrepresentative participant selection, and insufficient reporting of analytical methods. CONCLUSIONS: Adaptation strategies should align with task needs, using fine-tuning for narrow classification, RAG for guideline-grounded reasoning, and hybrid approaches for complex multimodal tasks. However, the evidence base remains largely retrospective or benchmark-based. Prospective studies with external validation, calibration, and standardized safety reporting are needed before broader clinical use.

## 背景與目的
大型語言模型在醫學知識基準上表現優異，但其在臨床實務中的安全有效應用，仰賴訓練後適應而非原始模型能力。微調、檢索增強生成（RAG）與混合策略是將模型錨定於臨床證據的主要途徑，然而三者的相對效益仍不明確。本系統性綜述旨在綜合微調、RAG 與混合後訓練策略於臨床診斷與決策支援任務的證據，辨識策略與任務的匹配及與績效提升相關的方法學特徵，為臨床部署提供實證導向的策略選擇依據。

## 方法
本研究依 PRISMA 2020 指南執行系統性綜述。檢索來源包含 PubMed/MEDLINE、Scopus 與 Web of Science，時間範圍自 2018 年 1 月至 2026 年 5 月。納入標準為：採用基於 Transformer 的語言模型，經過訓練後適應（微調或參數高效微調）、檢索增強、或兩者結合，並應用於臨床決策支援、診斷、分流、風險分層等醫療任務；排除未經適應的模型、非語言模型 AI 系統、無績效評估的提示工程研究及非臨床應用。資料抽取項目涵蓋模型架構、適應策略、臨床領域、驗證方式與績效指標。偏倚風險以 PROBAST+AI 工具評估。研究依主要增強策略分為微調/參數高效微調、RAG、混合三組，採描述性綜合呈現發現。此方法學設計確保了證據蒐集的系統性與可重現性，並透過標準化偏倚評估揭示現有研究的方法學缺口。

## 結果
共篩選 1890 筆記錄，納入 35 篇 2024‑2026 年研究。策略分布：RAG 17 篇（48.6%）、微調/參數高效微調 7 篇（20%）、混合 11 篇（31.4%），涵蓋腫瘤、神經、放射、心理、心臟、眼科、外科等專科。微調於特定任務表現優異，癌症偵測 AUC 達 0.912，重性憂鬱預測 AUC 0.892，多項研究達醫師級診斷表現。RAG 於指引型決策支援任務將指引遵循率從 71.1% 提升至 92.1%，診斷準確率從 78.9% 提升至 94.7%，惟在大型推理模型上效益不一。混合系統於複雜臨床流程中整體表現最佳，中風分流、皮膚科、多模態影像與腫瘤應用的外部驗證準確率均超過 90%。偏倚評估顯示 25 篇高風險、9 篇不明、僅 1 篇低風險，常見問題包括外部驗證不足、缺乏校準評估、樣本非代表性及分析方法報告不完整。

## 限制與展望
本綜述證據多為回顧性或基準測試，缺乏前瞻性臨床驗證；納入研究偏倚風險普遍偏高，外部驗證、模型校準、樣本代表性與方法報告均不足，導致結果泛化能力受限。此外，未對不同模型規模、檢索庫品質、微調資料量進行定量亞群分析，策略與任務的最佳匹配仍需更嚴謹的實證支持。未來研究應執行前瞻性、多中心外部驗證，納入校準與安全性標準化報告，並探討混合架構在真實臨床工作流程中的效益與風險。
