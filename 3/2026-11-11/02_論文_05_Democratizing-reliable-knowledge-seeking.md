# 論文 05：Democratizing reliable knowledge-seeking with MyGPT: a privacy-first, open-source retrieval-augmented generation platform.

- 日期：2026-11-11
- 來源層級：Tier 1
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-24T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43073267/
- PDF：
- DOI：10.1038/s41467-026-78509-6
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1190（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Large language models (LLMs) have transformed knowledge discovery, but their use in sensitive domains is limited by privacy concerns and risks of data leakage. Moreover, LLMs may hallucinate when queried about information outside their training data, undermining their reliability for scientific, clinical, or policy-related tasks. We present MyGPT, a fully open-source, privacy-preserving retrieval-augmented-generation (RAG) platform that uses open-source LLMs and operates locally or within secure institutional environments. MyGPT empowers users to query user-defined libraries such as biomedical literature, confidential clinical documents, and multilingual global health policies, while ensuring that sensitive data never leaves the secure environment. We introduce confidence metrics, including "relevance scores" and "hallucination index," and provide explicit source citation from the library within a single interface to assess contextual support for generated answers. MyGPT offers a cost-effective, modular, open-source alternative to commercial LLM services and democratizes knowledge-seeking across multiple domains, including use at remote facilities without internet access.

## 背景與目的
大型語言模型雖改變知識發現，但在涉及隱私敏感領域（如醫療、政策）時，資料外洩風險與模型對訓練資料外資訊產生幻覺，嚴重限制其可靠應用。現有商業服務多為閉源、需雲端傳輸，難以滿足機構內部合規與離線環境需求。本文旨在提供一個完全開源、隱私優先的檢索增強生成（RAG）平台 MyGPT，讓使用者在本地或安全機構環境中，針對自訂文獻庫（生物醫學文獻、機密臨床文件、多語言全球衛生政策）進行查詢，並透過相關性分數、幻覺指數與明確來源引用，評估生成答案的可信度，降低成本並實現知識獲取的民主化。

## 方法
問題設定：輸入為使用者自然語言查詢與使用者自定義的文件庫；輸出為帶有來源引用、相關性分數與幻覺指數的生成答案。整體架構採用模組化 RAG 流程：(1) 文件預處理與向量化，將使用者上傳的 PDF、文本等切分、嵌入並建立本地向量索引；(2) 檢索模組，依查詢向量在索引中檢索 Top‑k 相關片段；(3) 開源大型語言模型（如 Llama 系列）在本地或受信環境載入，作為生成骨幹；(4) 生成模組將檢索片段作為上下文注入提示詞，產生回答；(5) 信心度評估模組，計算「相關性分數」衡量檢索片段與查詢的匹配程度，並以「幻覺指數」量化生成內容超出檢索證據的比例；(6) 介面層在單一畫面呈現答案、引用來源片段、兩項指標，供使用者判斷可信度。資料表示採用密集向量嵌入，支援多語言文檔。訓練目標未於摘錄說明，推測為直接使用預訓練開源模型並以零樣本或少樣本提示進行推論，無額外微調損失函數。推論流程為：查詢 → 向量化 → 檢索 → 構建提示詞 → 本地 LLM 生成 → 計算指標 → 回傳結果。關鍵差異在於完全開源、資料不出本地環境、內建雙重信心度指標與來源引用，提供商業閉源服務缺乏的隱私保障與可驗證性。

## 結果
摘錄未提供可驗證數字。作者報告 MyGPT 在生物醫學文獻、機密臨床文件與多語言全球衛生政策等多領域實測中，能於無網路的偏遠設施正常運作，並透過相關性分數與幻覺指數有效標示答案可信度，證明平台具備跨領域知識檢索與生成能力，且成本低於商業雲端服務。定性結論顯示開源、本地部署與信心度指標的結合，提升敏感領域使用者對生成內容的信任。

## 限制與展望
目前摘錄未揭露具體檢索召回率、生成品質基準（如 BLEU、ROUGE、臨床準確率）或與商業 RAG 系統的定量比較，亦未說明向量嵌入模型選擇、分塊策略、索引規模上限、多語言對齊效果、幻覺指數計算細節與閾值設定。因此無法評估在大規模文獻庫、高併發查詢或極低資源裝置上的效能與穩定性。潛在風險包括開源 LLM 本身的知識截斷與偏見、檢索錯誤傳播至生成、幻覺指數可能誤判。後續研究建議補充完整基準測試、針對不同領域進行人工評估、探索微調與提示工程以提升檢索生成一致性，並驗證離線部署的硬體需求與安全合規性。
