# 論文 04：ESCARGOT: an AI agent leveraging large language models, dynamic graph of thoughts, and biomedical knowledge graphs for enhanced reasoning

- 日期：2026-10-22
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
- 配對 Repo：EpistasisLab/ESCARGOT

## 摘要
Abstract Motivation LLMs like GPT-4, despite their advancements, often produce hallucinations and struggle with integrating external knowledge effectively. While Retrieval-Augmented Generation (RAG) attempts to address this by incorporating external information, it faces significant challenges such as context length limitations and imprecise vector similarity search. ESCARGOT aims to overcome these issues by combining LLMs with a dynamic Graph of Thoughts and biomedical knowledge graphs, improving output reliability, and reducing hallucinations. Result ESCARGOT significantly outperforms industry-standard RAG methods, particularly in open-ended questions that demand high precision. ESCARGOT also offers greater transparency in its reasoning process, allowing for the vetting of both code and knowledge requests, in contrast to the black-box nature of LLM-only or RAG-based approaches. Availability and implementation ESCARGOT is available as a pip package and on GitHub at: https://github.com/EpistasisLab/ESCARGOT.

## 背景與目的
大型語言模型（如 GPT-4）雖在自然語言理解與生成上表現優異，但仍常產生幻覺，且難以有效整合外部生物醫學知識。現有的檢索增強生成（RAG）雖嘗試引入外部資訊，卻面臨上下文長度限制與向量相似度檢索不精確等問題。本研究旨在解決上述缺口，提出 ESCARGOT，結合大型語言模型、動態思維圖（Graph of Thoughts）與生物醫學知識圖譜，以提升推理可靠性、降低幻覺並提供可驗證的推理透明度。

## 方法
問題設定：輸入為開放式生物醫學問答或推理任務，輸出為經過驗證的答案與推理軌跡。整體架構包含三大核心模組：(1) 大型語言模型作為基礎推理引擎，負責生成候選思維節點與程式碼請求；(2) 動態思維圖，將模型產生的思維節點以圖結構組織，支援節點間的依賴、修剪與迭代擴展，實現多步推理的動態規劃；(3) 生物醫學知識圖譜，提供結構化的實體與關係查詢，供思維圖在需要外部知識時即時檢索。資料前處理與特徵表示方面，摘錄未說明具體的向量化、實體連結或圖嵌入細節。訓練目標與損失函數：文中未提及額外的微調或損失設計，推測主要採用零樣本或少樣本提示方式，利用 LLM 內部知識與外部圖譜互補。推理流程：LLM 先產生初步思維節點，動態思維圖根據任務需求擴展或修訂節點，遇到知識缺口時向知識圖譜發送查詢，取回結果後再由 LLM 繼續推理，直至得到最終答案；全程保留思維圖與查詢記錄，供人工審核。與既有 RAG 的關鍵差異在於：(a) 採用動態圖結構而非單一線性檢索上下文，(b) 直接整合結構化知識圖譜而非向量相似度檢索，(c) 提供完整推理軌跡與程式碼/知識請求的可驗證性。

## 結果
作者宣稱 ESCARGOT 在開放式高精度問題上顯著優於業界標準 RAG 方法，並強調其推理過程具備更高透明度，可對程式碼與知識請求進行審核。然而摘錄未提供可驗證的具體數字（如準確率、F1、召回率、基線名稱、資料集規模等），僅能觀察到定性結論：在開放式問答任務上表現優於傳統 RAG，且具備可審計的推理軌跡。

## 限制與展望
依目前可取得資料，無法確認模型的訓練細節、超參數、計算資源需求、部署延遲與擴展性。評估僅以開放式問題為主，缺乏多樣化基線與統計顯著性測試，難以判斷泛化能力。動態思維圖的規模增長可能導致記憶體與推理時間增加，知識圖譜的覆蓋率與更新機制未說明，可能影響長期維護。後續研究可著重於：量化實驗與消融分析、針對大規模知識圖譜的高效檢索策略、以及將框架擴展至其他領域的可行性驗證。
