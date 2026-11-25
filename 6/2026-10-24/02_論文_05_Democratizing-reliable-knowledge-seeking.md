# 論文 05：Democratizing reliable knowledge-seeking with MyGPT: a privacy-first, open-source retrieval-augmented generation platform.

- 日期：2026-10-24
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
大型語言模型（LLM）雖改變知識發現，但在涉及隱私敏感領域（如生物醫學、臨床、政策文件）時，面臨資料外洩風險與模型幻覺問題，導致可靠性不足。現有商業 LLM 服務多需雲端傳輸資料，難以滿足機構內部安全與離線需求。本文旨在提供一個完全開源、隱私優先的檢索增強生成（RAG）平台 MyGPT，讓使用者在本地或安全機構環境中，針對自訂文獻庫進行查詢，並引入相關性分數與幻覺指數等信心指標，提供明確來源引用，以低成本、模組化方式普及可信知識檢索。

## 方法
問題設定與輸入輸出：使用者提供自訂文獻庫（生物醫學文獻、機密臨床文件、多語言全球衛生政策等），系統接收自然語言查詢，輸出生成式回答並附帶來源引用與信心指標。整體架構：採用標準 RAG 流程，包含文件索引、檢索器、開源 LLM 生成器、信心評估模組與統一介面。核心模組與機制：(1) 文件前處理與向量化，將文獻庫切分、嵌入並建立向量索引；(2) 檢索器依查詢語意檢索最相關片段；(3) 開源 LLM（如 Llama 系列）在本地或安全環境載入，根據檢索片段生成回答；(4) 信心指標計算：相關性分數衡量檢索片段與查詢匹配度，幻覺指數評估生成內容與檢索證據的一致性；(5) 介面整合來源引用，讓使用者即時驗證。資料表示：文件以向量嵌入表示，查詢同樣嵌入後進行相似度檢索。訓練目標與損失：論文未提及額外微調或訓練，直接使用預訓練開源 LLM，故無自訂損失函數。推論流程：查詢→嵌入→向量檢索→上下文組裝→LLM 生成→計算相關性分數與幻覺指數→回傳回答與引用。關鍵差異：完全開源、資料不出安全環境、支援離線部署、內建雙重信心指標與單一介面引用，區別於需雲端 API 的商業 RAG 服務。

## 結果
摘錄未提供可驗證數字。本文提出 MyGPT 為完全開源、隱私優先的 RAG 平台，採用開源 LLM 於本地或安全機構環境運行，確保敏感數據不外洩。系統支援生物醫學文獻、機密臨床文件及多語言全球衛生政策等用戶自定義知識庫查詢。引入「相關性分數」與「幻覺指數」等信心指標，並提供單一介面內的明確來源引用，以評估生成答案的上下文支撐程度。定性結論指出 MyGPT 為商業 LLM 服務提供具成本效益、模組化的開源替代方案，並能在無網路的偏遠設施運作，實現跨領域知識尋求的普及化。

## 限制與展望
論文未揭露實驗基線、評估資料集規模、檢索與生成品質的量化指標，亦未說明開源 LLM 版本、嵌入模型選擇、索引更新機制、多語言處理細節與擴展性測試。潛在風險包括：開源模型效能可能落後商業模型、檢索品質依賴嵌入與切分策略、幻覺指數有效性缺乏獨立驗證、部署維護需技術人力。後續研究可著重於標準化基準比較、信心指標校準、自動化知識庫更新與輕量化部署優化。
