# 論文 01：ESCARGOT: an AI agent leveraging large language models, dynamic graph of thoughts, and biomedical knowledge graphs for enhanced reasoning

- 日期：2026-11-18
- 來源層級：Tier 2
- 期刊/會議/來源：Bioinformatics
- Venue：Bioinformatics
- 發布時間：2025-01-22T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/61d3f95318d52bd15ef36cdf93b25bae1fe135ef
- PDF：https://academic.oup.com/bioinformatics/advance-article-pdf/doi/10.1093/bioinformatics/btaf031/61561980/btaf031.pdf
- DOI：10.1093/bioinformatics/btaf031
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：32
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1023（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/EpistasisLab/ESCARGOT
- 配對 Repo：EpistasisLab/escargot

## 摘要
Abstract Motivation LLMs like GPT-4, despite their advancements, often produce hallucinations and struggle with integrating external knowledge effectively. While Retrieval-Augmented Generation (RAG) attempts to address this by incorporating external information, it faces significant challenges such as context length limitations and imprecise vector similarity search. ESCARGOT aims to overcome these issues by combining LLMs with a dynamic Graph of Thoughts and biomedical knowledge graphs, improving output reliability, and reducing hallucinations. Result ESCARGOT significantly outperforms industry-standard RAG methods, particularly in open-ended questions that demand high precision. ESCARGOT also offers greater transparency in its reasoning process, allowing for the vetting of both code and knowledge requests, in contrast to the black-box nature of LLM-only or RAG-based approaches. Availability and implementation ESCARGOT is available as a pip package and on GitHub at: https://github.com/EpistasisLab/ESCARGOT.

## 背景與目的
大型語言模型（如 GPT-4）雖已大幅進步，但仍常產生幻覺，且難以有效整合外部知識。現有的檢索增強生成（RAG）雖嘗試引入外部資訊，卻面臨上下文長度限制與向量相似度搜尋不精確等問題。ESCARGOT 旨在結合 LLM、動態思維圖與生物醫學知識圖譜，以提升輸出可靠性並降低幻覺。

## 方法
輸入為自然語言問題。核心機制包含三層：(1) 動態思維圖，將推理步驟表示為節點與邊，支援迭代擴展與修剪；(2) 生物醫學知識圖譜，提供結構化實體與關係供查詢；(3) LLM 作為控制器，根據圖狀態生成程式碼或知識請求，並可被人工審核。推論流程為：問題 → 初始化思維圖 → 反覆向 LLM 發送子任務、從知識圖譜檢索、更新圖 → 產生最終答案。

## 結果
摘錄未提供可驗證數字。論文聲稱 ESCARGOT 在開放式、高精度需求的問題上顯著優於業界標準 RAG 方法，並因思維圖與知識請求可被審核，提供比純 LLM 或 RAG 更透明的推理過程。

## 限制與展望
論文未公開具體基準資料集、消融實驗或計算成本，亦未說明知識圖譜覆蓋率對效能的影響。動態圖的擴展可能導致推理延遲，且依賴外部 KG 品質，若 KG 不完整或錯誤將傳遞至答案。未來需補充大規模實證與擴展性評估。
