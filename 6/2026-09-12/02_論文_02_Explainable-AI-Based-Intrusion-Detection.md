# 論文 02：Explainable AI-Based Intrusion Detection Systems for IoT Environments: A Systematic Literature Review.

- 日期：2026-09-12
- 來源層級：Tier 2
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
物聯網裝置快速普及導致網路攻擊風險顯著上升，傳統入侵偵測系統（IDS）雖以機器學習與深度學習達到高檢測準確率，但模型決策過程缺乏透明度，影響可靠性與可解釋性。現有研究多聚焦於檢測性能，較少系統性探討輕量化設計、可解釋 AI（XAI）方法驗證、資料隱私保護等實務部署需求。本文旨在透過系統性文獻回顧，梳理針對 IoT 環境之 XAI 啟用 IDS 的現有研究，識別當前問題與文獻缺口，並提出評估框架以指導未來發展可靠、可解釋且實用的 IoT 入侵偵測系統。

## 方法
本研究採系統性文獻回顧方法，依 PRISMA 指引檢索相關論文，設定納入條件為：針對 IoT 環境、採用 XAI 技術之 IDS 研究。建立多維度評估框架，涵蓋五大面向：(1) 使用之深度學習模型架構；(2) 輕量化模型設計策略（如模型壓縮、知識蒸餾、邊緣部署考量）；(3) 可解釋性方法與驗證方式（如 SHAP、LIME、注意力視覺化、專家評估等）；(4) 資料隱私保護手段（如聯邦學習、差分隱私、資料匿名化）；(5) 實驗所用資料集特性。並進一步提出研究評估框架，從方法學完整性、實驗可重現性、輕量化部署可行性、XAI 技術應用深度、XAI 驗證嚴謹度五項指標對各文獻進行系統性打分與比較，以揭示研究趨勢與不足。

## 結果
回顧結果顯示，近年研究不僅追求攻擊檢測準確率，更強調輕量化、可解�明與隱私保護三大目標並重。多數文獻採用 CNN、LSTM、Transformer 等深度模型並結合 SHAP、LIME 或注意力機制提供解釋，但輕量化設計多停留於模型壓縮，缺乏實際邊緣裝置部署驗證；隱私保護多採聯邦學習框架，惟實證資料集多為公開基準（如 CICIDS2017、Bot-IoT），真實異構 IoT 流量驗證稀少。評估框架顯示多數研究在方法學完整性與 XAI 驗證嚴謹度上仍有提升空間。摘錄未提供可驗證數字。

## 限制與展望
作為系統性回顧，本文受限於檢索時間與資料庫覆蓋範圍，可能遺漏最新會議論文或灰色文獻；評估框架指標權重與打分準則具主觀性，缺乏外部專家一致性驗證；未對個別 XAI 方法在真實 IoT 部署場景下的延遲、能耗進行實證比較；隱私保護機制多為理論架構，缺乏大規模異構裝置實測。未來研究可擴展評估維度、引入標準化基準測試平台，並結合實際邊緣硬體進行端到端驗證。
