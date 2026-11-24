# 論文 01：Assessment of LLMs on basic bioinformatics tasks requiring multi-step reasoning and code writing.

- 日期：2026-10-13
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
大型語言模型（LLM）被視為加速科學發現的關鍵工具，生物資訊學因其計算導向特性極適合 AI 自動化。然而，現有研究缺乏針對基礎生物資訊任務（需多步推理與程式撰寫）的系統性評估，無法量化通用 LLM 在專家與非專家基準上的表現差距。本文旨在填補此缺口，首次以 Rosalind 教學平台的 104 道題目為基準，比較多款前沿 LLM 與 68,760 位人類解題者的正確率，並分析不同生物類別的表現變異。

## 方法
問題設定：輸入為 Rosalind 平台的 104 道基礎生物資訊題目（涵蓋 DNA、RNA、蛋白質序列分析），要求模型輸出正確答案或可執行程式碼。評測模型包括 GPT‑5.2、GPT‑4o、GPT‑3.5、Llama‑3‑70B、Llama‑4、Claude Sonnet 4.6 等六款通用 LLM。基準真值包含專家標註答案與 68,760 位不同專業程度人類的解題紀錄。評估指標為答案正確與否（二元判斷），並統計各模型在各生物類別的正確率。實驗流程以 Python 實作，所有程式碼公開於 GitHub。摘錄未提供提示詞設計、採樣溫度、程式碼執行驗證、統計顯著性檢定等細節，亦未說明模型微調或檢索增強策略。

## 結果
GPT‑5.2 以 80/104（77%）正確率領先，Claude Sonnet 4.6 緊隨其後；其餘模型具體分數摘錄未提供可驗證數字。整體表現隨生物類別差異大，最新一代模型雖總分提升，但在特定類別表現反而不如第一代模型。LLM 正確率與人類群體表現呈正相關：人類難題 LLM 也較易錯，人類易題 LLM 多正確；但也存在 LLM 錯誤而多數人類正確、以及 LLM 正確而多數人類錯誤的個案。

## 限制與展望
基準僅含 104 道教學題目，難以代表真實研究級生物資訊任務的複雜度與多樣性。評測對象限於通用 LLM，未涵蓋領域微調或專用代理系統。人類樣本來源、專業分布及解題環境未詳述，可能引入選擇偏誤。缺乏提示詞、解碼參數、程式碼執行驗證等實驗控制細節，導致可重現性與統計效力受限。後續研究可擴大題庫、引入程式碼執行驗證、比較領域適配模型，並進行統計顯著性分析。
