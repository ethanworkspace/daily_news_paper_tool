# 論文 01：Assessment of LLMs on basic bioinformatics tasks requiring multi-step reasoning and code writing.

- 日期：2026-10-28
- 來源層級：Tier 2
- 期刊/會議/來源：Bioinformatics (Oxford, England)
- Venue：Bioinformatics (Oxford, England)
- 發布時間：2026-10-02T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42958757/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13722031/
- DOI：10.1093/bioinformatics/btag749
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1902（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/SiwoResearch/lllm-bioinformatics
- 配對 Repo：SiwoResearch/lllm-bioinformatics

## 摘要
MOTIVATION: Large Language Models (LLMs), AI agents and co-scientists promise to accelerate scientific discovery across fields ranging from chemistry to biology. Bioinformatics-the analysis of DNA, RNA and protein sequences plays a crucial role in biological research and is especially amenable to AI-driven automation given its computational nature. Here, we assess the bioinformatics capabilities of popular general-purpose LLMs on a set of tasks covering basic analytical questions that include code writing and multi-step reasoning in the domain. RESULTS: Utilizing questions from Rosalind, a bioinformatics educational platform, we compare the performance of the LLMs on 104 questions relative to expert ground truth and 68 760 humans with varying levels of expertise. Among the frontier LLMs evaluated (GPT-5.2, GPT-4o, GPT-3.5, Llama-3-70B, Llama-4 and Claude Sonnet 4.6), GPT-5.2 exhibited top performance, providing correct answers for 80/104 (77%) questions followed by Claude Sonnet 4.6. LLM performance varied widely depending on the biological categories of questions. While the latest generation of frontier LLM models showed overall improvements in performance, their performance in specific categories of biological questions was lower than first generation models. Overall, LLMs performance mirrored that of humans with lower performance in tasks in which humans had low performance and vice versa. However, LLMs also failed in some instances where most humans were correct and, in a few cases, LLMs excelled where most humans failed. To the best of our knowledge, this presents the first assessment of general purpose LLMs on basic bioinformatics tasks in distinct areas relative to both expert and non-expert ground truths. AVAILABILITY AND IMPLEMENTATION: The complete analysis was implemented in Python; all code is available at https://github.com/SiwoResearch/lllm-bioinformatics.

## 背景與目的
大型語言模型（LLM）被視為加速科學發現的關鍵工具，生物資訊學作為 DNA、RNA 與蛋白質序列分析的核心領域，具高度計算導向特性，適合 AI 自動化。然而，現有研究缺乏針對通用 LLM 在基礎生物資訊任務（含程式撰寫與多步推理）的系統性評估，尤其缺少與專家標準答案及大規模非專業人類表現的對比。本研究旨在填補此缺口，利用 Rosalind 教學平台的 104 道題目，比較多款前沿 LLM 與 68,760 位人類參與者的表現，提供首份針對通用 LLM 在不同生物學類別基本任務上的綜合基準。

## 方法
研究方法包含四個主要步驟。首先，從 Rosalind 平台蒐集 104 道基礎生物資訊學問題，涵蓋序列操作、動態規劃、圖論等類別，皆需撰寫程式碼並進行多步邏輯推理。其次，建立專家標準答案作為地面真值，並收集 68,760 位不同專業程度人類參與者的提交記錄作為人類基準。第三，選取六款前沿通用 LLM（GPT-5.2、GPT-4o、GPT-3.5、Llama-3-70B、Llama-4、Claude Sonnet 4.6）進行推理，摘錄未說明具體提示詞、少樣本設置或程式碼執行環境，僅以模型輸出答案與專家答案比對，計算答對題數與準確率。第四，按生物學類別與模型世代（第一代與最新一代）進行分層統計，分析 LLM 整體表現、類別差異、與人類表現的相關性，並記錄 LLM 在人類多數答對卻答錯、以及人類多數答錯卻答對的個案。整個分析流程以 Python 實作，程式碼公開於 GitHub。

## 結果
實驗結果顯示，GPT-5.2 以 80/104（77%）準確率領先，Claude Sonnet 4.6 緊隨其後；其餘四款模型的具體答對數字摘錄未提供可驗證數字。LLM 在不同生物學類別表現差異大，最新一代模型整體準確率較第一代提升，但在特定類別上反而低於第一代。整體而言，LLM 表現與人類高度相關：人類表現較差的類別 LLM 也較差，反之亦然。然而，存在少數情況 LLM 在多數人類答對時答錯，亦有極少數情況 LLM 在多數人類答錯時答對。

## 限制與展望
研究限制包括：僅測試 104 道基礎教學題目，未涵蓋真實研究級任務；評估模型僅為通用 LLM，未含領域微調模型；摘錄未揭露提示策略、程式碼執行驗證細節與統計顯著性檢定；人類基準混合不同專業程度，可能引入雜訊；資料集可能被模型訓練資料污染。後續研究可擴大題目規模、引入程式碼執行結果驗證、比較微調模型，並進行更嚴謹的統計分析。
