# 論文 03：Democratizing reliable knowledge-seeking with MyGPT: a privacy-first, open-source retrieval-augmented generation platform.

- 日期：2026-10-28
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
大型語言模型（LLM）雖改變知識發現，但在敏感領域受限於隱私洩漏風險與模型幻覺，導致科學、臨床或政策任務可靠性不足。現有商業服務多需上傳資料至雲端，難以滿足機構內部資料不出環境的需求。本文提出 MyGPT，旨在提供完全開源、隱私優先的檢索增強生成（RAG）平台，支援本地或安全機構環境部署，讓使用者能查詢自定文獻庫（生物醫學文獻、機密臨床文件、多語言全球衛生政策），並以相關性分數與幻覺指數等信心指標、明確來源引用，評估生成答案的上下文支撐，降低成本並實現知識獲取的民主化。

## 方法
問題設定：輸入為使用者查詢與自定文檔庫；輸出為帶有來源引用的回答及信心指標。整體架構採模組化 RAG 流程：(1) 文檔預處理與向量化，將 PDF、文字等切分、嵌入為向量並建立索引；(2) 檢索模組依查詢向量檢索 Top‑k 相關片段；(3) 開源 LLM（如 Llama 系列）在本地或安全環境載入，作為生成器；(4) 生成階段將檢索片段作為上下文注入提示，產生答案；(5) 信心評估模組計算「相關性分數」（relevance score）衡量檢索片段與查詢匹配度，並計算「幻覺指數」（hallucination index）估算生成內容超出檢索證據的程度；(6) 介面整合顯示答案、引用來源片段與兩項指標。資料表示採用密集向量嵌入，具體嵌入模型、切分策略、檢索演算法（如 FAISS、BM25 混合）於摘錄未說明。訓練目標與損失函數：平台使用預訓練開源 LLM，未進行額外微調，故無訓練損失；推論流程為單次查詢→檢索→生成→指標計算→回傳。關鍵差異在於完全開源、資料不出本地、提供雙重信心指標與單一介面引用，區別於商業雲端 RAG 服務。

## 結果
摘錄未提供可驗證數字。作者報告 MyGPT 在生物醫學文獻、機密臨床文件與多語言全球衛生政策三類庫上的測試，顯示平台能在無網路環境下本地運行，生成答案並附帶來源引用；相關性分數與幻覺指數可協助使用者判斷回答可信度。定性結論指出：開源模型與本地部署有效降低隱私風險，模組化設計便於擴展新資料源，且成本遠低於商業 API 服務。

## 限制與展望
限制與展望：(1) 摘錄未揭露具體嵌入模型、檢索演算法、LLM 版本與硬體需求，難以評估效能上限；(2) 幻覺指數計算細節缺失，無法驗證其可靠性；(3) 僅以三類領域示範，泛化至其他敏感領域尚待實證；(4) 開源模型推理速度與記憶體佔用在邊緣裝置可能受限；(5) 未來研究可探討微調開源 LLM 以提升領域適應性、改進指標解釋性、以及建立標準化基準進行跨平台比較。
