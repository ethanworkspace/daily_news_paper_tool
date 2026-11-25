# 論文 05：Democratizing reliable knowledge-seeking with MyGPT: a privacy-first, open-source retrieval-augmented generation platform.

- 日期：2026-11-18
- 來源層級：Tier 1
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-24T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43073267/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13793616/
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
大型語言模型（LLM）雖改變知識發現，但在敏感領域因隱私與資料外洩風險而受限；且當查詢超出訓練資料時易產生幻覺，降低科學、臨床或政策任務的可靠性。本文提出 MyGPT，一個完全開源、保護隱私的檢索增強生成（RAG）平台，使用開源 LLM 並在本地或安全機構環境中運行，讓使用者能查詢自定義文獻庫（如生物醫學文獻、機密臨床文件、多語言全球衛生政策），確保敏感資料不離開安全環境，並引入「相關性分數」與「幻覺指數」等信心指標，提供單一介面中的明確來源引用，以評估生成答案的上下文支持。目標在提供低成本、模組化、開源的商業 LLM 服務替代方案，並讓無網路的偏遠設施也能進行知識檢索。

## 方法
問題設定：輸入為使用者以自然語言提出的查詢，輸出為帶有來源引用與信心指標的生成答案。系統整體架構採用檢索增強生成（RAG）管線：首先將使用者自定義的文獻庫（生物醫學文獻、機密臨床文件、多語言政策文件等）進行文件分段、向量嵌入並建立索引；查詢時先由檢索器根據語意相似度從索引中取回最相關的文件片段；再將查詢與檢索到的片段作為上下文餵入開源 LLM 進行生成。核心模組包含：(1) 文件預處理與嵌入索引模組，支援多語言與機密資料的本地化處理；(2) 檢索器，採用密集向量檢索（具體模型未於摘錄說明）；(3) 生成器，使用開源預訓練 LLM（具體架構未於摘錄說明），無額外微調訓練目標與損失函數描述；(4) 信心評估模組，計算「相關性分數」衡量檢索片段與查詢的匹配度，並計算「幻覺指數」以量化生成內容超出檢索證據的程度；(5) 引用生成模組，在單一介面中輸出對應來源片段的明確引用。推論流程為：查詢→嵌入→檢索→上下文組裝→LLM 生成→信心指標計算→帶引用答案輸出。與既有商業 RAG 服務的關鍵差異在於：完全開源、可在離線或機構內部環境本地部署、資料不出安全邊界、並內建雙重信心指標與來源引用功能。摘錄未提供具體嵌入模型、檢索演算法、LLM 架構、訓練細節或超參數等技術細節。

## 結果
摘錄未提供可驗證數字。作者報告 MyGPT 為低成本、模組化、開源的替代方案，能在無網路的偏遠設施運作，並透過相關性分數與幻覺指數提供答案可信度評估，且在單一介面給出明確來源引用。定性結論顯示平台可支援生物醫學文獻、機密臨床文件與多語言全球衛生政策等多領域查詢，並強調隱私保護與資料不外洩的優勢。

## 限制與展望
依目前可取得資料，無法確認 MyGPT 在檢索召回率、生成準確率、幻覺指數校準效能等關鍵指標上的實證表現；亦未說明開源 LLM 具體模型大小、推理延遲、硬體需求、多語言嵌入品質、以及長文脈處理能力。潛在風險包含：檢索品質對下游生成影響大、幻覺指數可能無法完全捕捉所有錯誤類型、本地部署對計算資源有門檻、且缺乏與主流商業 RAG 系統的大規模基準比較。後續研究可著重於標準化評測、微調開源 LLM 以提升領域適應性、改進信心指標的可解釋性，以及擴展至更多敏感領域的合規性驗證。
