# GitHub 專案 04：zjunlp/MemTrace

- 日期：2026-09-18
- URL：https://github.com/zjunlp/MemTrace
- 描述：MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems
- Stars：86  |  Forks：5  |  Language：Python
- License：MIT
- Topics：agent, agent-tracing, artificial-intelligence, attributing-errors, debugging, large-language-models, memory-system, memtrace, natural-language-processing, tool, tracing, tracing-errors
- 更新時間：2026-11-23T15:53:33+00:00
- 配對論文：https://arxiv.org/abs/2605.28732
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
MemTrace 是一個用於追蹤與歸因大型語言模型記憶系統錯誤的工具。它記錄記憶系統的完整執行過程為操作‑變數執行圖，讓開發者能從錯誤答案逆向追蹤至最可能導致失誤的操作（如遺漏事實、記憶被覆寫或錯誤檢索），並提供 MemTraceBench 基準、圖形化自動歸因、診斷報告與記憶自動優化功能，目標使用者為 LLM 記憶系統的研究者與開發者，核心問題在於記憶系統失敗原因不透明。

## 技術
MemTrace 以 Python 3.12+ 實作，使用 smartcomment 工具包從現有記憶系統中擷取執行圖；依賴 OpenAI‑相容的 API 金鑰進行大型語言模型呼叫，並可透過 vLLM 部署嵌入模型（如 Qwen3‑Embedding‑4B）進行偽來源證據檢索；支援稀疏、密集或混合檢索方式，提供多種探索策略（operation_block_search、long_context 等）與批次處理；透過 AgentScope Studio 可視化執行圖；利用 LLM 生成診斷報告與優化提示詞。

## 架構
系統主要包含四個模組：(1) 基於 smartcomment 的追蹤模組，將記憶系統的使用者訊息、事實抽取、記憶更新、刪除、檢索與答案生成等步驟記錄為操作‑變數執行圖；(2) 資料模組，提供 MemTraceBench 基準資料集與可選的 LoCoMo 數據；(3) 歸因與報告模組，執行圖上進行子圖探索以定位最可能的錯誤操作並預測錯誤類型，然後呼叫大型語言模型產生診斷報告；(4) 自動優化模組，採閉環流程：抽樣軌跡、在追蹤狀態下構建與檢索記憶、使用歸因結果重寫可優化的提示詞，並迭代更新。資料流從輸入的 API 設定、嵌入模型與資料集進入追蹤模組產生執行圖，進入歸因模組得到錯誤定位，再分別送至報告生成或優化腳本。若說明不足，則說明推斷依據為 README 中所述的腳本與資料流描述。

## README 摘錄（節選）
```text
Tracing and Attributing Errors in Large Language Model Memory Systems
Paper |
MemTraceBench |
MemBase |
smartcomment
--- 
## Table of Contents
- News (#news)
- Overview (#overview)
- Installation Guide (#installation-guide)
- Prepare Data and Models (#prepare-data-and-models)
- Quick Example (#quick-example)
- Error Attribution (#error-attribution)
- Diagnostic Report for Memory Systems (#diagnostic-report-for-memory-systems)
- Automatic Optimization of Memories (#automatic-optimization-of-memories)
- Retrieval Performance (#retrieval-performance)
- Annotation Interface (#annotation-interface)
- Acknowledgement (#acknowledgement)
- Citation (#citation)
- License (#license)
## News
- **[2026-11-23]**: 🚀 **MemTrace is now integrated into EverOS (https://github.com/EverMind-AI/EverOS)** — a local-first, Markdown-native memory runtime for AI agents. Error tracing and attribution for memory systems are now available as part of the EverOS ecosystem.
- **[2026-07-17]**: 🚀 We update the paper with a long-context baseline for error attribution and a no-attribution baseline for prompt optimization. We also release the code for studying query construction during starting-point initialization.
- **[2026-06-09]**: 🚀 We open-source **MemTrace**, including the experiment code and the source code of the annotation interface.
- **[2026-06-07]**: 🚀 We release the **MemTraceBench** (https://huggingface.co/datasets/zjunlp/MemTraceBench) dataset, a benchmark for tracing and attributing failures in LLM memory systems, built from execution graphs and curated failure annotations.
- **[2026-06-03]**: 🚀 **MemBase** (https://github.com/zjunlp/MemBase) now integrates **smartcomment** (https://github.com/zjunlp/smartcomment) to trace memory construction, retrieval, and usage. We also provide the reproduction scripts and configs (https://github.com/zjunlp/MemBase/tree/main/examples/trace_memory_lifecycle_with_membase) for generating the execution-graph data used by **MemTraceBench**.
- **[2026-06-01]**: 🚀 We release the **smartcomment** (https://github.com/zjunlp/smartcomment) toolkit, a lightweight Python toolkit for recording execution graphs from existing systems.
## Overview
** MemTrace** helps developers understand why an LLM memory system gives a wrong answer. A memory system may read many user messages, extract facts, update stored memories, delete outdated memories, retrieve relevant memories, and finally generate an answer. When the final answer is wrong, the real cause is often hidden in an earlier step: a fact may be missed, a memory may be overwritten, or the wrong memory may be retrieved.
MemTrace records this whole process as an **operation-variable execution graph**. Variables are the concrete things produced during execution, such as user messages, memories, retrieved results, prompts, and predictions. Operations are the steps that create or use them, such as extraction, update, deletion, retrieval, filtering, and answer generation. With this graph, MemTrace can trace a failed case backward and identify which operation most likely introduces the error.
The project includes:
- **smartcomment-based tracing** for recording execution graphs from existing memory systems.
- **MemTraceBench**, a benchmark of human-annotated failure cases from Long-Context, RAG, Mem0, and EverMemOS.
- **Graph-based automatic attribution**, which inspects operation subgraphs to locate the decisive faulty operation and predict the error type.
- **Diagnostic reporting and memory optimization**, which turn attribution results into system-level reports and prompt updates.
## Installation Guide
MemTrace requires Python `>=3.12`.
Clone the repository first:
[code block omitted]
** Option A: Install with pip**
[code block omitted]
** Option B: Install with uv**
[code block omitted]
Prepare an OpenAI-compatible API config file, such as `input_files/api_config.json`:
[code block omitted]
You can provide multiple API keys and base URLs by adding more entries to both lists. Me
```
