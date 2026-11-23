# 論文 01：ESCARGOT: an AI agent leveraging large language models, dynamic graph of thoughts, and biomedical knowledge graphs for enhanced reasoning

- 日期：2026-11-16
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
大型語言模型（如 GPT-4）雖具強大生成能力，但常產生幻覺且難以有效整合外部知識。現有的檢索增強生成（RAG）雖引入外部資訊，卻面臨上下文長度限制與向量相似度檢索不精確等問題。ESCARGOT 旨在結合 LLM、動態思維圖（Graph of Thoughts）與生物醫學知識圖譜，以提升輸出可靠性、降低幻覺，並提供可驗證的推理透明度。

## 方法
問題設定為：輸入自然語言問題，輸出經推理驗證的答案。整體架構包含三大核心組件：(1) 預訓練 LLM 作為基礎推理引擎；(2) 動態思維圖，於推理過程中逐步擴展節點與邊，記錄中間思考步驟、假設與驗證路徑；(3) 生物醫學知識圖譜，提供結構化實體與關係供查詢。推理流程為：LLM 先依問題生成初步思維節點，系統依節點內容向知識圖譜發起查詢，將檢索到的子圖整合回思維圖，再由 LLM 根據更新後的圖進行下一輪推理，直至達成終止條件。資料前處理包含實體識別與鏈結至知識圖譜節點，思維圖以圖神經網路或注意力機制編碼節點表示（摘錄未詳細說明）。訓練目標與損失函數未於摘錄中描述，推測為零樣或少樣式推理，無額外微調。與傳統 RAG 關鍵差異在於：思維圖動態演化而非靜態檢索、知識圖譜提供結構化語義而非向量相似度、推理過程可逐步審查程式碼與知識請求，具備較高透明度。

## 結果
摘錄指出 ESCARGOT 在開放式、高精度要求的問題上顯著優於業界標準 RAG 方法，並具備更佳的推理透明度，可對程式碼與知識請求進行驗證。然而摘錄未提供可驗證的具體數字（如準確率、F1、召回率）、基線名稱、資料集規模或消融實驗結果，僅能觀察到定性結論：準確度提升與可解釋性增強。

## 限制與展望
目前可取得資料僅限於摘要，缺乏實驗設計細節、評估指標、基線模型、資料集描述、消融分析與計算資源需求。方法依賴知識圖譜覆蓋範圍，若圖譜不完整可能限制推理品質；動態思維圖擴展可能導致推理延遲與記憶體壓力；未說明是否需微調 LLM 或僅採零樣推理，部署成本不明。後續研究需補充完整實驗報告、擴展至更多領域知識圖譜、探討圖規模對效能的影響，並評估對抗性輸入下的穩健性。
