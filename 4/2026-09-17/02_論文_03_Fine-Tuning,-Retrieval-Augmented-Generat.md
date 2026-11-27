# 論文 03：Fine-Tuning, Retrieval-Augmented Generation, and Hybrid Adaptation of Language Models for Clinical Decision-Making in Health Care: Systematic Review.

- 日期：2026-09-17
- 來源層級：Tier 4（一般期刊）
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
大型語言模型在醫學知識基準測試表現優異，但其在臨床實務的安全有效應用，仰賴訓練後適應而非原始模型能力。微調、檢索增強生成（RAG）與混合策略是將模型錨定於臨床證據的主要途徑，惟三者相對效能仍不明確。本系統性綜述依 PRISMA 2020 指引，檢索 2018 年至 2026 年 5 月 PubMed/MEDLINE、Scopus、Web of Science，納入經訓練後適應、檢索增強或兩者兼具之 Transformer 架構語言模型，針對臨床決策支援、診斷、分流、風險分層等任務之研究，排除未適應模型、非語言模型 AI、無效能評估之提示工程及非臨床應用。萃取模型架構、適應策略、臨床領域、驗證方式與效能指標，以 PROBAST+AI 評估偏誤風險，並依主要增強策略分組進行描述性綜合，旨在釐清策略與任務的對應關係及提升效能的方法學特徵。

## 方法
問題設定為比較三類訓練後適應策略——微調（含參數高效微調）、RAG 及混合方法——在臨床診斷與決策支援任務上的效能差異。輸入為經預訓練之 Transformer 語言模型與特定臨床語料或知識庫；輸出為診斷分類、風險分層、指引遵循率等效能指標。整體架構分三層：(1) 模型層，涵蓋 BERT、GPT、LLaMA 等不同規模架構；(2) 適應層，微調採用全參數或 LoRA/Adapter 等參數高效技術，RAG 採用密集向量檢索（如 FAISS）搭配生成器，混合系統則串接微調模型與檢索模組，並常引入多模態編碼器處理影像與文本；(3) 評估層，採用內部交叉驗證、外部獨立資料集、校準曲線與決策曲線分析。資料前處理包含去識別化、標準化術語映射（UMLS/SNOMED）、文本分塊與向量化。訓練目標視任務而定：分類任務採用交叉熵損失，生成任務採用序列級負對數似然，部分研究加入對比學習或知識蒸餾損失以強化檢索相關性。最佳化採用 AdamW，學習率排程含 warm‑up 與 cosine decay。推理流程：微調模型直接前向傳播；RAG 先檢索 top‑k 片段再送入生成器；混合系統先經微調編碼器獲取任務特徵，再融合檢索上下文進行生成或分類。關鍵差異在於微調強調任務特定參數內化，RAG 強調外部證據即時注入，混合策略試圖兼具領域知識內化與動態證據檢索。

## 結果
共篩選 1890 筆記錄，納入 35 篇 2024‑2026 年研究。策略分布：RAG 17 篇（48.6%）、微調/參數高效微調 7 篇（20%）、混合 11 篇（31.4%），涵蓋腫瘤、神經、放射、心理、心臟、眼科、外科等領域。微調在癌症偵測達 AUC 0.912、重性憂鬱預測 AUC 0.892，多項研究達醫師級表現。RAG 使指引遵循率從 71.1% 提升至 92.1%，診斷準確率從 78.9% 提升至 94.7%，惟在大型推理模型上效益不一。混合系統在中風分流、皮膚科、多模態影像、腫瘤等複雜流程的外部驗證準確率均超過 90%。偏誤評估顯示 25 篇高風險、9 篇不明、僅 1 篇低風險，常見問題為缺乏外部驗證、未評估校準、樣本非代表性及分析方法報告不足。

## 限制與展望
本綜述受限於納入研究多為回顧性或基準測試，缺乏前瞻性臨床試驗與真實世界部署數據；外部驗證樣本量小、異質性高，難以推廣；多數研究未報告模型校準、決策曲線或安全性指標，風險偏誤評估多屬高風險。未來需進行多中心前瞻驗證、標準化報告框架、長期監測與人機協作效能研究，以確立各策略在實際臨床路徑中的效益與安全性。
