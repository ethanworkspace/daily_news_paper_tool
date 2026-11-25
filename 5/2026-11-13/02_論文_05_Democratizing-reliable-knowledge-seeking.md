# 論文 05：Democratizing reliable knowledge-seeking with MyGPT: a privacy-first, open-source retrieval-augmented generation platform.

- 日期：2026-11-13
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
大型語言模型（LLM）雖改變知識發現，但在敏感領域應用受限於隱私顧慮與資料外洩風險；且當查詢超出訓練資料範圍時易產生幻覺，損害科學、臨床或政策任務的可靠性。本文提出 MyGPT，一個完全開源、保護隱私的檢索增強生成（RAG）平台，採用開源 LLM 並在本地或安全機構環境中運行。MyGPT 讓使用者能查詢自定義資料庫（如生物醫學文獻、機密臨床文件、多語言全球衛生政策），確保敏感資料不離開安全環境。引入「相關性分數」與「幻覺指數」等信心指標，並在單一介面提供明確來源引用，以評估生成答案的上下文支持度。MyGPT 提供具成本效益、模組化、開源的商業 LLM 服務替代方案，讓知識尋求跨領域普及，甚至適用於無網路的偏遠設施。

## 方法
問題設定與輸入輸出：使用者在安全環境中提供自定義文件庫（生物醫學文獻、臨床機密文件、多語言政策文件），系統接收自然語言查詢，輸出生成式答案、引用來源片段、相關性分數與幻覺指數。整體架構：採用檢索增強生成（RAG）流程，核心包含開源 LLM、本地/安全部署的檢索索引、信心評估模組。核心模組與機制：檢索器從使用者資料庫檢索相關段落；生成器以開源 LLM 根據檢索內容生成答案；信心評估模組計算「相關性分數」（衡量檢索內容與查詢的匹配度）與「幻覺指數」（估計生成內容偏離檢索證據的程度），並將來源引用嵌入答案。資料前處理與表示：文件經分段、向量化建立索引，支援多語言內容。訓練目標與損失函數：摘錄未提及具體訓練目標、損失函數或最佳化策略。推論流程：查詢 → 檢索相關段落 → 送入 LLM 生成答案 → 計算相關性分數與幻覺指數 → 附上來源引用回傳。關鍵差異：強調隱私優先（資料不出安全環境）、完全開源、模組化設計、內建信心指標與引用介面、支援離線部署。註：摘錄未提供模型架構細節、檢索演算法、向量化方式、幻覺指數計算公式等技術實作細節。

## 結果
摘錄未提供可驗證數字。作者僅定性描述 MyGPT 能在隱私敏感領域（生物醫學、臨床、政策）提供可靠知識尋求，具備相關性分數與幻覺指數以量化答案可信度，並以來源引用增強透明度；平台為開源、模組化、成本效益高，可在無網路的偏遠設施本地運行。未見與商業服務或其他 RAG 系統的量化比較、消融實驗或案例分析數據。

## 限制與展望
依目前可取得資料，無法確認實驗評估細節。潛在限制包括：缺乏標準基準上的量化效能驗證（檢索準確率、生成品質、幻覺指數有效性）；開源 LLM 表現依賴模型規模與微調，可能不及專有大模型；本地部署需足夠算力與儲存，對資源受限環境有門檻；多語言檢索與跨語言生成品質未經測試；幻覺指數計算方式未公開，難以獨立驗證。後續研究方向應包含大規模實證評估、指標可靠性分析、擴展領域適應性測試、優化資源消耗以支援邊緣裝置。
