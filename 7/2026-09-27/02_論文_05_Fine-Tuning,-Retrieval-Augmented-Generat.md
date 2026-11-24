# 論文 05：Fine-Tuning, Retrieval-Augmented Generation, and Hybrid Adaptation of Language Models for Clinical Decision-Making in Health Care: Systematic Review.

- 日期：2026-09-27
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
這篇系統性回顧探討大型語言模型（LLM）在臨床決策支援中的後訓練適應策略。雖然 LLM 在醫學知識基準測試表現優異，但其在臨床實踐中的安全有效應用取決於微調、檢索增強生成（RAG）與混合方法等後訓練適應，而非原始模型能力。現有研究對這三類策略的比較效果仍不明確。本文旨在綜合微調、RAG 與混合策略在臨床診斷與決策支援任務上的證據，找出策略與任務的對應關係，以及與性能提升相關的方法學特徵。

## 方法
本系統性回顧遵循 PRISMA 2020 指南，檢索 PubMed/MEDLINE、Scopus、Web of Science（2018 年 1 月至 2026 年 5 月）。納入標準為：採用基於 Transformer 的語言模型，經過後訓練適應、檢索增強或兩者兼具，用於臨床決策支援、診斷、分流、風險分層等醫療應用；排除未適應模型、非語言模型 AI 系統、無效能評估的提示工程、非臨床應用。資料擷取項目包括模型架構、適應策略、臨床領域、驗證方法、效能結果。偏倚風險以 PROBAST+AI 評估。研究依主要增強策略分組（微調/參數高效微調、RAG、混合方法），採描述性綜合分析。問題設定為比較三類後訓練策略在臨床任務上的效能；輸入為文獻資料，輸出為策略-任務對應與方法學特徵。核心機制在於系統性分組與偏倚評估，而非單一模型架構。與既有方法差異在於聚焦後訓練適應策略的比較效能，並納入參數高效微調與混合方法。

## 結果
共 1890 筆記錄，納入 35 篇 2024-2026 年研究。策略分布：RAG 17 篇（48.6%）、微調/PEFT 7 篇（20%）、混合 11 篇（31.4%），涵蓋腫瘤、神經、放射、心理、心臟、眼科、外科等專科。微調在特定任務表現優異：癌症偵測 AUROC 達 0.912，重性憂鬱症預測 AUC 0.892，多項研究達醫師級診斷表現。RAG 提升指引依從性與診斷準確度：指引型決策支援任務從 71.1% 升至 92.1%、78.9% 升至 94.7%，但較大推理模型效果不一。混合系統在複雜臨床流程表現最強，中風分流、皮膚科、多模態影像、腫瘤等外部驗證準確率超過 90%。偏倚評估顯示 25 篇高風險、9 篇不明、1 篇低風險；常見問題包括外部驗證不足、缺乏校準評估、參與者選擇無代表性、分析方法報告不足。

## 限制與展望
本綜合證據多為回顧性或基準測試研究，缺乏前瞻性驗證；僅 1 篇研究偏倚風險低，大多數存在外部驗證不足、校準評估缺失、樣本代表性不足、分析方法報告不完整等問題；RAG 在大型推理模型上的效益不一致，機制未明；混合方法雖在複雜任務表現佳，但具體架構細節與可擴展性未深入探討；未來需前瞻性研究、標準化安全報告、校準評估與外部驗證，才能支援更廣泛臨床應用。依目前可取得資料，無法確認具體模型架構、訓練超參數、資料集規模與基線比較細節。
