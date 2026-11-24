# 論文 02：ESCARGOT: an AI agent leveraging large language models, dynamic graph of thoughts, and biomedical knowledge graphs for enhanced reasoning

- 日期：2026-10-14
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
大型語言模型（如 GPT-4）雖已取得顯著進展，但仍常產生幻覺，且難以有效整合外部知識。現有的檢索增強生成（RAG）雖嘗試引入外部資訊，卻面臨上下文長度限制與向量相似度搜尋不精確等問題。ESCARGOT 旨在結合 LLM、動態思維圖（Graph of Thoughts）與生物醫學知識圖譜，以提升輸出可靠性並降低幻覺，提供更透明的推理過程。

## 方法
問題設定：輸入為自然語言問題，輸出為經過推理驗證的答案與推理軌跡。整體架構包含三大核心組件：(1) 大型語言模型作為基礎推理引擎；(2) 動態思維圖，隨推理過程即時擴展節點與邊，記錄中間思維、子問題與決策路徑；(3) 生物醫學知識圖譜，提供結構化實體與關係供查詢。核心機制：LLM 先生成初步思維節點，系統依據節點內容向知識圖譜發起查詢，將檢索到的子圖嵌入思維圖，再由 LLM 根據更新後的圖進行下一步推理，形成迭代循環。資料表示：問題與思維節點以文本嵌入編碼；知識圖譜採用實體關係三元組，經圖神經網絡或嵌入向量化以支援快速檢索。訓練目標與損失：摘錄未提及具體損失函數或微調策略，推測可能採用提示工程與少樣本引導，無額外參數更新。推理流程：接收問題 → 初始化思維圖 → 重複（LLM 生成思維 → 知識圖譜查詢 → 更新思維圖）直到達到終止條件 → 輸出最終答案與完整思維圖供審核。關鍵差異：相較傳統 RAG 靜態檢索後直接生成，ESCARGOT 引入動態圖結構實現多輪推理與知識驗證，提升透明度並減少幻覺。

## 結果
作者宣稱 ESCARGOT 在開放式、高精度要求的問題上顯著優於業界標準 RAG 方法，並強調其推理過程具備更高透明度，可對程式碼與知識請求進行審核。然而摘錄未提供可驗證數字（如準確率、F1、召回率、基線名稱、資料集規模），故無法量化比較結果。僅能觀察到定性結論：在開放式問答表現較佳、推理可追蹤。

## 限制與展望
目前僅有摘要資訊，缺乏實驗資料集、評估指標、基線模型名稱、消融實驗與統計顯著性測試等細節，無法判斷泛化能力與計算成本。動態思維圖的擴展機制、知識圖譜覆蓋範圍、查詢延遲與記憶體消耗未揭露。部署面臨 LLM 推理延遲、知識圖譜更新維護與隱私合規風險。後續研究需公開完整實驗設定、基線對比、消融分析，並探討於不同生物醫學子領域的適用性。
