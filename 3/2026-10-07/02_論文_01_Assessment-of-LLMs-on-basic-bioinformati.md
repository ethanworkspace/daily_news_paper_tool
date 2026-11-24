# 論文 01：Assessment of LLMs on basic bioinformatics tasks requiring multi-step reasoning and code writing.

- 日期：2026-10-07
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
本研究旨在評估通用大型語言模型（LLM）在基礎生物資訊學任務上的能力，這類任務涉及多步推理與程式碼撰寫。生物資訊學分析 DNA、RNA 與蛋白質序列，對生物研究至關重要，且因其計算本質適合 AI 自動化。現有方法缺乏系統性基準，將通用 LLM 置於專家真值與大規模人類表現（68,760 人）下進行比較。本文貢獻在於首次針對不同生物類別的基礎任務，建立專家與非專家雙重真值的評估框架，揭示 LLM 在特定領域的強弱項。

## 方法
問題設定：輸入為 Rosalind 平台的 104 道生物資訊學題目，涵蓋多步推理與程式碼撰寫；輸出為模型生成的答案與程式碼。模型選擇：評估六款前沿 LLM（GPT-5.2、GPT-4o、GPT-3.5、Llama-3-70B、Llama-4、Claude Sonnet 4.6）。評估流程：以專家提供的標準答案為真值，並收集 68,760 位不同專業程度人類的解答作為非專家真值。資料表示：題目以自然語言描述，模型需產出可執行程式碼並給出最終答案。推論機制：摘錄未詳細說明提示策略、程式碼執行環境或多輪互動細節。與既有方法差異：首次引入大規模人類基線與專家真值雙重比較，並按生物類別細分表現。依目前可取得資料，無法確認訓練目標、損失函數、最佳化策略等模型內部機制。

## 結果
主要結果：GPT-5.2 於 104 題中答對 80 題（77%），居首位；Claude Sonnet 4.6 緊隨其後。LLM 表現隨生物類別差異大：最新一代模型整體提升，但在特定類別表現不如第一代模型。LLM 整體表現與人類表現呈鏡像關係——人類表現差的任務 LLM 也較差，反之亦然。但也發現 LLM 在多數人類答對的題目中失敗，少數情況下 LLM 超越多數人類。摘錄未提供各模型完整數字、消融實驗或統計顯著性數據。

## 限制與展望
限制：僅測試 104 道 Rosalind 題目，可能無法代表真實生物資訊學工作流程的複雜度；人類基線專業度分布未細述；評估僅以正確率為指標，未考慮程式碼效率、可讀性或錯誤類型；模型版本標記（如 GPT-5.2、Claude Sonnet 4.6）可能非官方命名，需謹慎解讀。風險：過度依賴 LLM 可能導致關鍵生物分析錯誤。後續方向：擴大基準規模、引入真實專案級任務、分析錯誤模式、改進提示與工具使用策略。
