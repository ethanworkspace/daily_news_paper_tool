# GitHub 專案 01：EpistasisLab/escargot

- 日期：2026-10-12
- URL：https://github.com/EpistasisLab/escargot
- 描述：
- Stars：40  |  Forks：6  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-09-23T21:12:16+00:00
- 配對論文：https://www.semanticscholar.org/paper/61d3f95318d52bd15ef36cdf93b25bae1fe135ef
- 品質分數：8/10 [paper_paired, implementation_signals]

## 在做什麼
ESCARGOT 是一個以 Python 實作的庫，目標是將大型語言模型 (LLM) 與動態圖形思考 (Graph of Thoughts, GoT) 以及知識圖譜結合，以減少幻覺並提升回答的正確性。它主要服務於需要高精度開放式問答的研究人員、開發者與資料科學家，特別是在單跳或多跳推理任務中，透過結構化知識檢索與可執行程式碼驗證模型輸出，提供比傳統 RAG 更透明的推理過程。

## 技術
ESCARGOT 以 Python 為主要實作語言，搭配 GPT-3.5 Turbo 或 GPT-4o-mini 等大型語言模型進行推理。其核心包含動態 GoT 生成、透過 Memgraph 知識圖譜使用 Cypher 查詢進行結構化檢索，以及以向量資料庫作為備援的相似度搜尋。系統支援直接將知識轉換為可執行的 Python 程式碼，並內建自除錯與自適應機制，以在執行錯誤時自行分析與修復程式，進一步降低幻覺與提升計算可靠性。

## 架構
ESCARGOT 的架構分為數個模組：首先是設定載入器，負讀取模型、資料庫連線與其他參數；接著是知識圖譜 schema 擷取器，可自動從 Memgraph 讀取節點與邊類型，亦支援手動配置以跳過自動擷取；隨後是策略產生器與評估器，根據使用者問題產生候選的 GoT 並評估其可行性；經評估後的策略進入程式碼產生器，將思考圖轉換為可執行的 Python 程式，並透過 XML 轉換器進行中間表示；最後是執行器，在 Memgraph 中執行 Cypher 查詢或向量檢索，執行產生的程式碼，並啟動自除錯迴圈偵測與修正執行錯誤；整個流程透過 ask 介面對外提供問答服務，回傳答案以及可選的除錯資訊。

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
