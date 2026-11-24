# 論文 01：Assessment of LLMs on basic bioinformatics tasks requiring multi-step reasoning and code writing.

- 日期：2026-10-06
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
大型語言模型（LLM）被視為加速科學發現的潛力工具，生物資訊學因其計算導向特性，極適合 AI 自動化。然而，現有研究缺乏針對基礎生物資訊任務（含多步推理與程式撰寫）的系統性評估，亦未將模型表現與專家及大量非專家人類基準同步比較。本文旨在填補此缺口，建立首個針對通用 LLM 在基本生物資訊問題上的綜合基準，並量化其相對人類表現的優劣，為後續 AI 輔助生物研究提供實證依據。

## 方法
問題設定：從 Rosalind 教學平台挑選 104 道涵蓋 DNA、RNA、蛋白質序列分析的基礎題目，每題要求模型輸出正確答案（通常為程式碼執行結果或文字解答）。輸入為題目描述，輸出為模型生成的答案。資料集：僅使用這 104 道題目，並收集 68,760 位不同專業程度人類的解答作為非專家基準，另以專家標準答案為地面真值。模型選擇：評測六款前沿通用 LLM，包含 GPT-5.2、GPT-4o、GPT-3.5、Llama-3-70B、Llama-4、Claude Sonnet 4.6。評測流程：對每個模型逐題提示，收集其輸出，自動與專家答案比對正確性；同時統計人類群體正確率。實作：全部分析以 Python 完成，程式碼公開於 GitHub。提示策略、程式碼執行環境、錯誤重試機制等細節在摘錄中未說明。與既有方法差異：首次將通用 LLM 置於基礎生物資訊多步推理與程式撰寫任務中，並同時引入專家與大規模非專家人類基準進行三方比較。

## 結果
在 104 道題目中，GPT-5.2 正確率最高，解對 80 題（77%），緊隨其後為 Claude Sonnet 4.6。各生物類別表現差異大，最新一代模型整體進步，但在特定類別上反而不如第一代模型。LLM 整體表現與人類群體趨勢一致：人類正確率低的任務，模型也較差；反之亦然。但也觀察到模型在多數人類答對的題目上失敗，以及極少數模型超越大多數人類的案例。摘錄未提供可驗證的各模型完整數字、統計顯著性或消融實驗結果。

## 限制與展望
僅涵蓋 Rosalind 104 道基礎教學題目，無法推廣至真實研究級生物資訊分析。評測未揭示提示詞設計、程式碼執行驗證、錯誤處理等關鍵細節，難以重現或判斷模型極限。人類基準雖龐大但專業度分布不明，可能混淆專家與新手表現。未進行統計檢定、信心區間或多輪對話評估。模型清單僅含六款前沿模型，缺乏開源微調模型或領域適應模型對比。後續研究可擴大任務範圍、標準化提示流程、引入程式碼執行驗證與統計分析，並探討領域微調對多步推理的提升。
