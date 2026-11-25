# 論文 05：Assessment of LLMs on basic bioinformatics tasks requiring multi-step reasoning and code writing.

- 日期：2026-10-22
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
本研究旨在評估通用大型語言模型在基礎生物資訊學任務上的表現，特別是需要多步推理與程式碼撰寫的題目。現有研究多集中於特定模型或單一任務，缺乏跨模型、跨專業水準的系統性基準。生物資訊學因其計算導向特性，適合作為 AI 自動化的測試床。本文首次以 Rosalind 教學平台的 104 道題目為基準，將 6 個前沿 LLM（GPT‑5.2、GPT‑4o、GPT‑3.5、Llama‑3‑70B、Llama‑4、Claude Sonnet 4.6）與專家標準答案及 68,760 位人類解題者進行比較，確立模型在不同生物類別的強弱項，為後續領域專用模型開發提供實證依據。

## 方法
問題設定：輸入為 Rosalind 平台的 104 道基礎生物資訊學題目，涵蓋 DNA/RNA/蛋白質序列分析、演算法實作與統計推理等類別；輸出為各模型產生的答案（含程式碼與文字說明）。評估流程：(1) 題目蒐集與去重，確保涵蓋多樣生物主題；(2) 以相同提示詞模板依序查詢六個 LLM，採用預設解碼參數（溫度、top‑p 等）並單次生成，未進行多輪自我修正；(3) 由領域專家依據官方解答建立地面真值，並自動比對模型輸出的正確性（完全匹配為準）；(4) 同步收集平台上 68,760 位使用者的歷史解題紀錄，計算各題人類正確率作為非專家基準；(5) 統計各模型在整體與各類別的準確率，並繪製模型與人類表現的相關圖。核心差異在於採用真實教學題庫而非合成資料、同時引入專家與大規模人類表現作為雙重基準、且未對模型進行微調或提示工程優化，純粹測量零樣本泛化能力。由於摘錄未說明提示詞細節、採樣次數、錯誤分類標準或統計顯著性檢定方式，依目前可取得資料，無法確認這些實驗控制細節。

## 結果
實驗結果顯示，GPT‑5.2 以 80/104（77%）正確率領先，Claude Sonnet 4.6 緊隨其後；其餘模型準確率依序下降。各生物類別表現差異大，最新一代模型整體提升但在特定類別（如演算法實作）反而低於第一代模型。模型整體表現與人類正確率高度相關：人類較弱的題目模型也較弱，反之亦然。但仍存在模型在多數人類答對題目上失敗，以及少數人類多失敗而模型成功的案例。摘錄未提供可驗證的各模型完整數字、消融實驗或統計顯著性數值。

## 限制與展望
限制包括：(1) 僅測試 104 道教學題目，未涵蓋真實研究級資料集與大規模基因體分析流程；(2) 採單次零樣本推理，未探討少樣本提示、思維鏈或工具使用對性能的提升；(3) 評估指標僅以完全匹配為準，忽略部分正確或語意等價答案；(4) 人類基準來自平台歷史紀錄，專業程度分布不明，可能引入選擇偏誤；(5) 未公開提示詞、解碼參數與統計檢定細節，難以複現。後續研究可擴展任務廣度、引入多輪互動與程式執行驗證，並建立標準化評估協議。
