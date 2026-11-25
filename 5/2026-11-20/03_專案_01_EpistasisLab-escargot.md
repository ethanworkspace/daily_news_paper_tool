# GitHub 專案 01：EpistasisLab/escargot

- 日期：2026-11-20
- URL：https://github.com/EpistasisLab/escargot
- 描述：
- Stars：40  |  Forks：6  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-09-23T21:12:16+00:00
- 配對論文：https://www.semanticscholar.org/paper/61d3f95318d52bd15ef36cdf93b25bae1fe135ef
- 品質分數：8/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
ESCARGOT 是一個結合大型語言模型（LLM）與動態圖形思維（Graph of Thoughts、GoT）以及知識圖譜的框架，旨在克服傳統 Retrieval‑Augmented Generation（RAG）在上下文長度限制與向量相似度搜尋不精確所導致的幻覺問題。透過動態生成可執行的 Python 程式碼、結合 Cypher 查詢與向量資料庫備援，ESCARGOT 提供更高的開放式問答正確性以及可審視的推理過程。其目標使用者包括需要高精度知識檢索與推論的研究人員、開發者及生物資訊科學家，特別適用於需要嚴謹驗證代碼與知識請求的場景。

## 技術
ESCARGOT 以 Python 實作，支援多種 LLM（如 GPT‑3.5 Turbo、GPT‑4o‑mini）作為推論引擎。核心包含動態 GoT 生成、知識圖譜（Memgraph）的 Cypher 查詢、向量資料庫備援搜尋、策略生成與評估、程式碼產生、XML 轉換以及直接 Python 執行。內建自偵錯機制可在執行錯誤時自行分析與修復程式碼，減少人工介入。透過 pip 安裝（pip install escargot）即可取得庫，並可手動提供知識圖譜 schema 以跳過自動擷取步驟。

## 架構
ESCARGOT 的架構包含：配置與初始化（讀取 LLM 與資料庫參數，選擇自動或手動載入知識圖譜 schema）、策略生成（根據問題產生候選解決方案）、策略評估（初步篩選可行策略）、程式碼生成（將策略轉為可執行 Python 程式碼）、XML 轉換（產生中間表示）、執行（呼叫 Python 解釋器運行程式碼）、知識檢索（優先使用 Cypher 查詢從 Memgraph 取得結構化資料，失敗時改用向量資料庫備援）、自偵錯（執行失敗時自動分析並修復程式碼，形成閉環迭代）。問答入口函式 ask() 串聯以上步驟，最終回傳經驗證的答案。由於 README 未提供詳細的類別劃分或訊息傳遞格式，上述流程僅基於文件中所述步驟進行合理推斷。

## README 摘錄（節選）
```text
# ESCARGOT
## Overview
LLMs like GPT-4, despite their advancements, often produce hallucinations and struggle with integrating
external knowledge effectively. While Retrieval-Augmented Generation (RAG) attempts to address this by incorporating
external information, it faces significant challenges such as context length limitations and imprecise vector similarity
search. ESCARGOT aims to overcome these issues by combining LLMs with a dynamic Graph of Thoughts and knowledge
graphs, improving output reliability and reducing hallucinations.
ESCARGOT significantly outperforms industry-standard RAG methods, particularly in open-ended questions
that demand high precision. ESCARGOT also offers greater transparency in its reasoning process, allowing for the vetting
of both code and knowledge requests, in contrast to the black-box nature of LLM-only or RAG-based approaches.
ESCARGOT significantly outperforms industry-standard RAG methods, particularly in open-ended questions that demand high precision. ESCARGOT also offers greater transparency in its reasoning process, allowing for the vetting of both code and knowledge requests, in contrast to the black-box nature of LLM-only or RAG-based approaches.
Link to Bioinformatics Application Note: https://academic.oup.com/bioinformatics/article/41/2/btaf031/7972741
## Results
| **Dataset** | **GPT 3.5 Turbo/GPT 4o-mini** | **Standard RAG (GPT3.5 Turbo/GPT4o-mini)** | **KRAGEN (GPT3.5 Turbo)** | **ESCARGOT (GPT3.5/GPT4o-mini)** |
|--------------------------------------------------|-------------------|----------|-------------|--------------------|
| Openended 1-hop (508 questions) | 3.3% / 4.2% | 50.2% / 55.5% | 53.1% | 81.0% / **88.4%** |
| Openended 2-hop (450 questions) | 3.5% / 4.9% | 12.8% / 23.1% | 19.9% | **91.8%** / 85.8% |
| True/False 1-hop (560 questions) | 55.9% / 60.5% | 73.0% / 85.2% | 80.2% | 80.7% / **90.9%** |
| True/False 2-hop (540 questions) | 26.7% / 59.4% | 64.4% / 75.6% | 62.4% | **77.6%** / 74.1% |
| Multiple Choice 1-hop (498 questions) | 42.6% / 58.2% | 77.7% / 88.8% | 65.1% | **94.6%** / 93.4% |
| Multiple Choice 2-hop (419 questions) | 49.9% / 61.3% | 81.9% / 86.4% | 62.2% | **94.2%** / 89.5% |
## Key Features
1. **Dynamic GoT Generation**: ESCARGOT dynamically generates a Python-executable Graph of Thoughts (GoT) that integrates with knowledge graphs. This dynamic approach ensures improved accuracy and contextual relevance compared to static GoT frameworks.
2. **Strategic Planning and Execution**: ESCARGOT's workflow includes strategy generation, assessment, code generation, XML conversion, and execution. This multi-step process ensures that each strategy is thoroughly evaluated and executed efficiently.
3. **Advanced Knowledge Retrieval**:
- **Cypher Queries**: ESCARGOT utilizes Cypher queries to extract structured and precise information from knowledge graphs like Memgraph, offering superior accuracy in data retrieval.
- **Vector Database Requests**: As a backup, ESCARGOT leverages vector databases for similarity searches, enhancing the system’s ability to handle diverse queries even if Cypher queries fail.
4. **Direct Python Execution**: The system supports direct Python execution for tasks requiring high precision. By converting knowledge into executable Python code, ESCARGOT ensures reliable and efficient computation, reducing the risk of errors and hallucinations.
5. **Self-Debugging and Adaptability**: ESCARGOT includes built-in self-debugging capabilities. It can autonomously analyze and revise code if errors occur during execution, ensuring resilience and reducing the need for manual intervention.
6. **Enhanced Accuracy and Reduced Hallucinations**: By integrating structured knowledge retrieval and direct code execution, ESCARGOT minimizes the risk of hallucinations and improves the overall accuracy of reasoning and computation.
--- 
## Quick Install Through Pip
`pip install escargot`
## Example Usage
Here's how to configure and use the `Escargot` library w
```
