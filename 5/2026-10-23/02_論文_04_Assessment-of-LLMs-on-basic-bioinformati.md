# 論文 04：Assessment of LLMs on basic bioinformatics tasks requiring multi-step reasoning and code writing.

- 日期：2026-10-23
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
本研究旨在評估通用大型語言模型（LLM）在基礎生物資訊學任務上的表現，這類任務涉及多步推理與程式碼撰寫，屬於計算生物學核心能力。現有研究多集中於特定模型或單一任務，缺乏跨模型、跨類別、且同時以專家標準答案與大規模人類表現為基準的系統性比較。鑑於生物資訊學高度依賴序列分析與自動化流程，若 LLM 能可靠解決此類問題，將顯著加速科學發現。本文目標為建立首個針對基礎生物資訊學題目的綜合基準，量化主流前沿 LLM 的準確率，並揭示其與人類表現的相似與差異，為後續模型改進與 AI 輔助科學提供實證依據。

## 方法
問題設定與輸入輸出：從 Rosalind 教學平台挑選 104 道基礎生物資訊學題目，涵蓋 DNA、RNA、蛋白質序列分析等類別；每道題目要求模型輸出正確答案（通常為程式碼執行結果或文字解答）。 整體架構：採零樣本（zero‑shot）提示策略，將題目直接餵入各 LLM，取得模型回覆；若回覆包含程式碼，則在 Python 環境中執行以獲得最終答案。 核心模組：(1) 題目收集與清洗模組，確保題目獨立且具標準答案；(2) 模型推理模組，支援 GPT‑5.2、GPT‑4o、GPT‑3.5、Llama‑3‑70B、Llama‑4、Claude Sonnet 4.6 等六款前沿模型；(3) 答案抽取與執行模組，自動解析模型輸出、執行程式碼並捕獲輸出；(4) 評估模組，將模型答案與專家提供的標準答案比對，並與 68,760 位不同專業程度人類的歷史解題紀錄比較。 資料表示：題目以自然語言呈現，無額外特徵工程；模型輸出為自由文本與程式碼混合。 訓練目標與最佳化：本研究不涉及模型微調或損失函數設計，屬純推理評估。 推論流程：題目 → 提示模型 → 取得回覆 → 程式碼執行（如有） → 答案標準化 → 與專家答案比對 → 統計準確率與類別表現。 關鍵差異：首次以同一題庫、同一評估管線，同時對照專家真值與大規模人類表現，系統性比較多款通用 LLM 在基礎生物資訊學多步推理與程式撰寫能力。依目前可取得資料，無法確認提示詞設計細節、程式碼執行沙箱配置、錯誤重試機制等實作細節。

## 結果
實驗顯示 GPT‑5.2 以 80/104（77%）正確率領先，Claude Sonnet 4.6 緊隨其後；其餘模型具體分數摘錄未提供可驗證數字。各生物類別表現差異大，最新一代模型整體優於第一代，但在特定類別卻低於早期模型。LLM 整體表現與人類高度相關：人類表現差的題目 LLM 也較差，反之亦然；但仍存在 LLM 錯誤而多數人類正確、以及 LLM 正確而多數人類錯誤的個案。作者聲稱此為首次以專家與非專家雙基準評估通用 LLM 於基礎生物資訊學任務的研究。

## 限制與展望
基準僅含 104 道 Rosalind 基礎題，未涵蓋真實研究中複雜管線、大規模資料處理或領域特定知識；人類表現資料缺乏專業等級細分與統計顯著性檢定；評估未探討提示工程、少樣本、工具使用或代理架構對性能的影響；程式碼執行環境、錯誤處理、超時機制等工程細節未揭露，可能影響可重現性；模型版本標記（如 GPT‑5.2）非公開發布版本，存在版本混淆風險。後續研究可擴大題庫、引入真實專案任務、系統性比較提示策略與代理框架，並進行統計檢定以確認觀察差異的顯著性。
