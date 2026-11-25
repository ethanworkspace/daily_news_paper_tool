# 論文 03：Leveraging prompt-driven generative AI for systematic reviews in digital psychiatry: A stage-matched comparative proof-of-concept for healthcare researchers and clinicians.

- 日期：2026-09-12
- 來源層級：Tier 2
- 期刊/會議/來源：PLOS digital health
- Venue：PLOS digital health
- 發布時間：2026-09-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42721190/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13561331/
- DOI：10.1371/journal.pdig.0001666
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2438（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
The scale and pace of evidence generation in digital psychiatry increasingly exceed the capacity of traditional systematic literature review (SLR) methods. Large language models (LLMs) are gaining traction in evidence synthesis, yet limited guidance exists for integrating generative AI into transparent, reproducible SLR workflows. To develop and evaluate a prompt-driven, modular decision-making framework for adaptable SLR workflows in digital psychiatry, and to compare stage-matched performance relative to a consensus-based human reference process. We conducted a mixed-methods, stage-matched comparative evaluation of three GPT-5 mode variants (Auto, Agent, and Deep Research) against a consensus-based human-led SLR workflow using a registered digital psychiatry review (PROSPERO CRD42025648122) as a case example. Nine SLR tasks were implemented within the ChatGPT interface using structured RISEN prompts: preliminary searches; research question, eligibility criteria, and search strategy development; article screening; data extraction; article summarization; critical appraisals; and descriptive results synthesis. Performance was evaluated using task-specific assessments of accuracy, sensitivity, specificity, inter-rater agreement, reporting compliance, hallucination monitoring, and workflow feasibility. All GPT-5 mode variants were feasible across SLR stages, although performance varied by task and mode. No fabricated study-level content was identified during structured hallucination auditing. Auto mode performed best for structured rule-based tasks requiring efficiency and implementation-ready outputs (e.g., eligibility criteria). Agent mode excelled in conceptual integration and interpretive tasks (e.g., research question generation, critical appraisals, descriptive synthesis). Deep Research mode most closely approximated human reasoning for higher-order synthesis tasks, performing best in full-text article screening, article summarization, and narrative synthesis. Prompt-driven LLM workflows are feasible and semi-efficacious for selected SLR tasks in digital psychiatry when deployed within a modular, human-in-the-loop decision-support framework. Findings support task-specific deployment of an adaptable modular framework, enabling healthcare researchers and clinicians to modify LLM workflows according to methodological appropriateness, confidence in performance, and institutional review practices.

## 背景與目的
數位精神醫學領域的證據產生速度與規模已超出傳統系統性文獻回顧（SLR）的處理能力。大型語言模型（LLM）雖受關注，但缺乏將生成式 AI 融入透明、可重現 SLR 流程的指引。本研究旨在開發並評估一個提示驅動、模組化的決策框架，以適應數位精神醫學的 SLR 工作流程，並與基於共識的人工參考流程進行階段匹配的效能比較。研究採用混合方法，針對已註冊的數位精神醫學回顧（PROSPERO CRD42025648122）作為案例，設計九項 SLR 任務，並在 ChatGPT 介面中使用結構化 RISEN 提示實作，以系統性評估各模式在準確度、敏感度、特異度、評分者一致性、報告合規性、幻覺監控與工作流程可行性等指標上的表現。

## 方法
問題設定與輸入輸出：以已註冊的系統性回顧為案例，輸入為研究主題、納入/排除標準、檢索式等文本資料；輸出為九個 SLR 階段的結構化產出（初步檢索、研究問題與資格標準制定、檢索策略、文獻篩選、資料萃取、文章摘要、關鍵鑑賞、描述性結果綜合）。模型與系統架構：在 ChatGPT 介面中部署三種 GPT‑5 模式——Auto、Agent、Deep Research，分別代表自動化規則執行、代理式推理與深度研究推理。核心模組：採用結構化 RISEN 提示框架（Role、Instruction、Steps、Example、Negative constraints）將每項任務拆解為固定步驟，確保提示一致性與可重現性。資料前處理與表示：將全文 PDF 轉為純文本，切分為段落並保留標題結構，作為模型輸入的上下文；對於篩選與萃取任務，另建立結構化表格模板以引導輸出格式。訓練目標與最佳化：本研究不涉及模型微調，僅透過提示工程與人工回饋迭代調整提示詞，以提升任務特定指標（準確度、敏感度、特異度、評分者一致性、報告合規性、幻覺發生率）。推論流程：每項任務依序執行，人工專家在關鍵節點（如資格標準確定、全文篩選結果）進行審核與共識判斷，形成人機協作的決策回路。與既有方法差異：傳統 SLR 完全依賴人工；既有 LLM 輔助多為單一任務或非結構化提示；本框架強調模組化、階段匹配、多模式並行評估與結構化提示，提供可依方法學適宜性彈性調整的決策支援。

## 結果
實驗結果顯示，三種 GPT‑5 模式在所有九項 SLR 任務上均具可行性，但效能隨任務與模式而異。結構化幻覺審計未發現捏造的研究層級內容。Auto 模式在需高效率、規則明確且輸出可直接實作的任務（如資格標準制定）表現最佳；Agent 模式在概念整合與詮釋性任務（研究問題生成、關鍵鑑賞、描述性綜合）表現優異；Deep Research 模式最接近人類高階推理，於全文篩選、文章摘要與敘述性綜合任務達到最佳表現。整體而言，提示驅動的 LLM 工作流程在數位精神醫學 SLR 中具備半效能，適合在人機協作的模組化框架下依任務特性部署。

## 限制與展望
本研究僅以單一已註冊的數位精神醫學回顧為案例，樣本量與領域範圍有限，難以推廣至其他醫學領域或更大規模的系統性回顧。評估僅涵蓋 GPT‑5 的三種模式，未納入其他 LLM 或開源模型進行比較。效能指標雖包含準確度、敏感度等，但缺乏統計顯著性檢定與信賴區間，且人工共識流程本身可能存在主觀偏誤。幻覺審計僅針對研究層級內容，未檢查細節層級（如數值、統計結果）的錯誤。未來研究需擴大案例數、引入多模型基線、採用更嚴謹的統計比較，並探討長文本處理、隱私保護與機構審查委員會（IRB）合規性等部署層面的挑戰。
