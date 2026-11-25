# 論文 05：Democratizing reliable knowledge-seeking with MyGPT: a privacy-first, open-source retrieval-augmented generation platform.

- 日期：2026-11-19
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
大型語言模型（LLM）已改變知識發現方式，但在涉及隱私敏感領域（如醫療、政策）時，資料外洩風險與模型在訓練資料外產生幻覺，嚴重限制其可靠應用。現有商業 LLM 服務多需雲端傳輸資料，難以滿足機構內部合規與離線環境需求。本文旨在提出 MyGPT，一個完全開源、隱私優先的檢索增強生成（RAG）平台，利用開源 LLM 在本地或安全機構環境中運行，讓使用者能針對自訂文獻庫（生物醫學文獻、機密臨床文件、多語言全球衛生政策）進行查詢，並確保敏感資料不離開安全環境，提供成本效益高、模組化的替代方案，推動知識獲取的普及化。

## 方法
MyGPT 採用檢索增強生成（RAG）架構，核心流程包含： 1. 問題設定與輸入輸出：使用者提供自然語言查詢，系統從使用者自建的文獻庫中檢索相關片段，再由開源 LLM 生成回答並附帶引用來源。 2. 整體系統架構：平台為模組化設計，包含文件攝取與索引模組、向量檢索模組、開源 LLM 推理模組、信心度評估模組與前端介面。所有模組均可在本地或受控網路環境部署，無需外部 API 呼叫。 3. 核心模組與演算法機制： - 文件前處理：將 PDF、文字等轉為統一格式，切分為固定長度區塊並產生嵌入向量（具體嵌入模型未於摘錄說明）。 - 向量檢索：以相似度檢索回傳 Top‑k 相關片段，作為 LLM 的上下文。 - 開源 LLM 生成：載入可公開取得的 LLM 權重（如 Llama、Mistral 等，具體模型未指明），在本地進行推理。 - 信心度指標：引入「相關性分數」衡量檢索片段與查詢的匹配程度，以及「幻覺指數」估算生成內容超出檢索證據的比例；兩指標計算細節未於摘錄揭露。 - 來源引用：生成回答時自動標註對應檢索片段的文獻識別碼，供使用者驗證。 4. 訓練目標與最佳化：摘錄未提及對 LLM 進行微調或額外訓練，推測採用零樣本或少樣本推理，損失函數與最佳化策略未提供。 5. 推論執行流程：使用者查詢 → 向量檢索 → 構建提示（含檢索片段） → LLM 生成 → 計算相關性分數與幻覺指數 → 回傳回答與引用。 6. 與既有方法差異：強調完全開源、資料不出機構、提供雙重信心度指標與單一介面引用，區別於需雲端傳輸且缺乏可驗證引用的商業 RAG 服務。

## 結果
摘錄未提供可驗證數字。作者報告 MyGPT 為成本效益高、模組化的開源替代方案，能在無網路的偏遠設施運作，並透過相關性分數與幻覺指數提升回答可信度，實現多領域（生物醫學、臨床、全球衛生政策）的知識查詢普及化。定性結論顯示平台滿足隱私合規與離線需求，但缺乏具體基線比較、準確率、召回率或使用者研究數據。

## 限制與展望
依目前可取得資料，無法確認 MyGPT 在檢索品質、生成準確度、擴展性、多語言表現及長文脈處理上的具體限制。潛在風險包括：開源 LLM 基礎能力可能不足以支撐高專業領域問答；向量嵌入與檢索策略未公開，難以評估召回率；幻覺指數計算透明度不足，可能產生誤導性信心；部署於資源受限裝置時的推理延遲與記憶體需求未說明。後續研究建議：公開完整技術細節、提供標準基線比較、進行臨床或政策實務場景的用戶研究、探索模型蒸餾與量化以提升邊緣部署效能。
