# 論文 01：ESCARGOT: an AI agent leveraging large language models, dynamic graph of thoughts, and biomedical knowledge graphs for enhanced reasoning

- 日期：2026-11-20
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
本研究針對大型語言模型（如 GPT-4）在生物醫學領域易產生幻覺、難以有效整合外部知識的問題，指出現有檢索增強生成（RAG）方法受限於上下文長度與向量相似度搜尋不精確的缺口。ESCARGOT 旨在結合 LLM、動態思維圖與生物醫學知識圖譜，提升推理可靠性並降低幻覺，提供可驗證的推理透明度，定位為開放式高精度問答的增強型 AI 代理。

## 方法
問題設定：輸入為生物醫學領域的開放式問題，輸出為經推理驗證的答案。整體架構：ESCARGOT 將 LLM 作為核心推理引擎，引入動態思維圖以結構化推理路徑，並整合生物醫學知識圖譜作為外部知識來源。核心模組：動態思維圖用於追蹤與組織推理步驟，知識圖譜提供實體與關係查詢。資料表示：文本經嵌入後與圖結構對齊，但摘錄未說明具體前處理、特徵工程或圖建構細節。訓練目標與損失：摘錄未提供可驗證的訓練目標、損失函數或最佳化策略。推理流程：LLM 在思維圖上迭代生成子任務、請求知識圖譜查詢與程式碼執行，並將結果回填圖中，最終輸出答案；但具體控制邏輯、驗證機制與終止條件依目前可取得資料無法確認。關鍵差異：相較於純 LLM 或 RAG，ESCARGOT 強調動態圖結構與知識圖譜的雙重外部知識整合，並提供程式碼與知識請求的可審計透明度。

## 結果
作者報告 ESCARGOT 顯著優於產業標準 RAG 方法，尤其在需要高精度的開放式問題上表現更佳，且推理過程具透明度，可對程式碼與知識請求進行審查。然而摘錄未提供可驗證數字（如準確率、召回率、具體基線名稱、資料集規模或消融實驗數值），僅能觀察到定性結論：在開放式高精度問答任務上優於 RAG，並具備可驗證推理鏈。

## 限制與展望
依目前可取得資料，無法確認實驗資料集、基線模型細節、消融研究與統計顯著性；方法層面缺乏動態思維圖建構、知識圖譜覆蓋率、LLM 選擇與提示工程的具體說明；部署上未提及延遲、成本與擴展性評估。潛在風險包括知識圖譜不完整導致推理錯誤、LLM 幻覺殘留、動態圖複雜度可能影響即時性。後續研究建議：公開完整實驗設定、量化透明度指標、探索多模態知識整合與線上更新機制。
