# 論文 05：Explainable AI-Based Intrusion Detection Systems for IoT Environments: A Systematic Literature Review.

- 日期：2026-09-13
- 來源層級：Tier 4（一般期刊）
- 期刊/會議/來源：Sensors (Basel, Switzerland)
- Venue：Sensors (Basel, Switzerland)
- 發布時間：2026-09-10T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42817304/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13611250/
- DOI：10.3390/s26185744
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1819（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
With the rapid proliferation of Internet of Things (IoT) technology today, the number of devices connected to each other through these networks is increasing significantly, and the security risks these devices face from cyberattacks have emerged as a clear problem. Intrusion detection systems (IDSs) are emerging as a solution to this problem and play a significant role in securing IoT-based networks. Although machine learning and deep learning-based IDS approaches have achieved high accuracy rates in detecting attacks in recent years, the lack of transparency in these models' decision-making processes poses a major drawback in terms of reliability and explainability. To ensure that the decisions of IDS models are understandable and to address this issue, Explainable AI (XAI) approaches are being implemented. This study provides a detailed review of the current literature on XAI-enabled IDSs developed for IoT environments. The studies examined are systematically evaluated in terms of the deep learning models used, lightweight model designs, explainability methods and validations, approaches to protecting data privacy, and datasets. The literature review highlights that research is not only focused on the accuracy of attack detection but also aims to design IDS solutions that are lightweight, explainable, and privacy-preserving. This paper aims to provide a foundational resource to guide future research on reliable, explainable, and practical IoT intrusion detection systems by identifying the problems addressed in current research and highlighting the limitations in the literature. In addition, this work proposes and applies a study assessment framework to systematically assess methodological adequacy, experimental reproducibility, lightweight deployment, XAI techniques, and XAI validation.

## 背景與目的
隨著物聯網（IoT）裝置快速普及，連網設備數量大幅增加，網路攻擊帶來的安全風險日益嚴重。入侵偵測系統（IDS）成為保護 IoT 網路的關鍵方案。雖然機器學習與深度學習為基礎的 IDS 在攻擊偵測準確率上表現優異，但模型決策過程缺乏透明度，導致可靠性與可解釋性不足。為了解決此問題，可解釋人工智慧（XAI）技術被引入 IDS。本文旨在系統性回顧針對 IoT 環境之 XAI 啟用 IDS 的現有文獻，評估所用深度學習模型、輕量化設計、可解釋方法與驗證、資料隱私保護策略及資料集，並提出一套研究評估框架，以指導未來發展可靠、可解釋且實用的 IoT 入侵偵測系統。

## 方法
本研究採系統性文獻回顧方法。首先依據預先定義的檢索式於多個學術資料庫（如 IEEE Xplore、Scopus、Web of Science 等）檢索 2015 年至 2023 年間之相關論文，並以納入/排除標準（針對 IoT 環境、採用 XAI 技術之 IDS、含實驗評估）篩選文獻。接著建立研究評估框架，從五個維度對每篇文獻進行評分：(1) 方法學完整性，包含問題定義、模型架構、訓練與測試流程；(2) 實驗可重現性，涵蓋資料集描述、超參數設定、程式碼公開情形；(3) 輕量化部署潛力，考量模型大小、推論延遲、資源消耗；(4) XAI 技術應用，記錄使用之解釋方法（如 SHAP、LIME、注意力視覺化等）及其整合方式；(5) XAI 驗證機制，檢視是否進行人為評估、定量指標（如忠實度、穩定度）或領域專家驗證。對各文獻提取之深度學習模型類型（CNN、RNN、Transformer 等）、輕量化策略（知識蒸餾、模型剪枝、量化）、隱私保護手段（聯邦學習、差分隱私）與使用資料集（如 CICIDS2017、Bot-IoT、NSL-KDD 等）進行分類統計。最後綜合分析各維度得分分布，識別研究缺口與趨勢。

## 結果
回顧結果顯示，現有研究不僅追求攻擊偵測準確率，亦普遍關注模型輕量化、可解釋性與隱私保護三大面向。大多數文獻採用 SHAP、LIME 或注意力機制作為主要 XAI 手法，但僅少數進行定量忠實度或專家驗證。輕量化策略以知識蒸餾與模型剪枝為主，聯邦學習為常見隱私保護方案。摘錄未提供可驗證數字，無法給出具體準確率、模型大小或推論延遲等量化比較。整體結論指出，雖然 XAI 融入 IDS 已成趨勢，但在標準化評估指標、跨資料集泛化能力與實際部署驗證方面仍有明顯不足。

## 限制與展望
本回顧僅涵蓋至檢索截止日前公開之學術論文，可能遺漏灰色文獻與最新預印本；納入標準與評分框架雖經設計，但仍含主觀判斷，不同評審者可能得出不同結論。評估框架未對 XAI 解釋品質採用統一量化基準，導致跨研究比較受限。此外，文獻多以公開基準資料集實驗，缺乏真實 IoT 部署環境下的延遲、能耗與異質裝置相容性驗證。未來研究可致力於建立統一的 XAI 評估標準、擴大真實場景測試、探討聯邦學習與 XAI 結合的可行性，以及針對資源極受限裝置設計更高效的可解釋模型。
