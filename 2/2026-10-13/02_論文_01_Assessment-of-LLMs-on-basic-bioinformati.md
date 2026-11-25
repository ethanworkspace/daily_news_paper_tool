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
本研究旨在評估通用大型語言模型（LLM）在基礎生物資訊學任務上的表現，這類任務涉及程式碼撰寫與多步驟推理。生物資訊學分析 DNA、RNA 與蛋白質序列，屬計算密集型領域，極適合 AI 自動化。然而，現有研究缺乏針對通用 LLM 在基礎生物資訊學問題上、且同時以專家標準答案與大規模非專家人類表現為基準的系統性評估。本文填補此空白，利用 Rosalind 教學平台的 104 道題目，比較六款前沿 LLM（GPT-5.2、GPT-4o、GPT-3.5、Llama-3-70B、Llama-4、Claude Sonnet 4.6）的表現，提供首份針對不同生物類別、對照專家與 68,760 位人類解題者的綜合基準分析。

## 方法
問題設定：輸入為 Rosalind 平台的 104 道基礎生物資訊學題目，涵蓋多個生物類別，需模型撰寫程式碼並進行多步驟推理以產出答案；輸出為模型給出的最終答案。評估對象：六款通用 LLM（GPT-5.2、GPT-4o、GPT-3.5、Llama-3-70B、Llama-4、Claude Sonnet 4.6）。基準真值：專家提供的標準答案，以及平台上 68,760 位不同專業程度使用者的歷史解題紀錄。資料處理：題目直接以自然語言提示詞形式餵入模型，摘錄未說明是否採用 few-shot、chain-of-thought 或特定提示工程策略，亦未描述程式碼執行環境、錯誤重試機制或答案比對細節。模型推論：各模型獨立生成答案，再與專家真值比對正確性。評估指標：單題正確率與整體正確題數。核心差異：本研究為首次將通用 LLM 置於基礎生物資訊學任務中，並同時引入專家與大規模人類群體作為雙重基準，而非僅比較模型間相對表現。摘錄未提供訓練目標、損失函數或最佳化策略，因實驗屬推理階段評估，非模型微調。

## 結果
主要結果：GPT-5.2 表現最佳，104 題中答對 80 題（77%），Claude Sonnet 4.6 緊隨其後；其餘模型具體正確數未於摘錄給出。各生物類別間表現差異大，最新一代前沿模型整體雖有提升，但在特定類別上反而不如第一代模型。LLM 整體表現與人類群體趨勢一致：人類正確率低的任務 LLM 也較差，反之亦然。但也發現 LLM 在多數人類答對的題目中失敗，少數情況下 LLM 卻在多數人類失敗的題目中成功。摘錄未提供可驗證數字（如各模型分類別準確率、統計顯著性、消融實驗數據），僅能觀察上述定性結論。

## 限制與展望
資料限制：僅 104 道 Rosalind 教學題目，可能無法代表真實生物資訊學研究的複雜度與多樣性。方法限制：未描述提示詞設計、程式碼執行環境、錯誤處理流程，難以重現或推廣。評估限制：人類基準來自平台用戶，專業程度參差不齊，且缺乏專業生物資訊學家的獨立驗證。部署風險：基礎任務表現良好不代表能勝任實際科研流程中的開放式、多工具協作問題。後續方向：擴大題庫至進階任務、引入代理式工作流、評估模型在真實資料集上的泛化能力、分析錯誤模式以改進提示策略。
