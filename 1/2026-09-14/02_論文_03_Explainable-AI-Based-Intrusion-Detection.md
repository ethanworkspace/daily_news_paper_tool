# 論文 03：Explainable AI-Based Intrusion Detection Systems for IoT Environments: A Systematic Literature Review.

- 日期：2026-09-14
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
物聯網設備快速普及導致網路攻擊風險顯著增加，入侵偵測系統（IDS）成為保護 IoT 網路的關鍵方案。雖然機器學習與深度學習為基礎的 IDS 在攻擊偵測準確率上表現優異，但其決策過程缺乏透明度，嚴重影響可靠性與可解釋性。為解決此問題，可解釋人工智慧（XAI）技術被引入 IDS 中。本文旨在系統性回顧針對 IoT 環境的 XAI 啟用 IDS 文獻，評估深度學習模型、輕量化設計、可解釋性方法與驗證、資料隱私保護及資料集使用等面向，提供未來研究可靠、可解釋且實用的 IoT 入侵偵測系統的基礎資源，並提出一個研究評估框架以系統性評估方法學充分性、實驗可重現性、輕量化部署、XAI 技術與 XAI 驗證。

## 方法
本研究採用系統性文獻回顧方法，針對 IoT 環境下結合 XAI 的 IDS 相關文獻進行篩選與分析。核心方法包含：1) 問題設定與篩選準則：界定研究問題為「現有 XAI-based IDS 在 IoT 環境的設計現況、缺口與未來方向」，輸入為學術資料庫文獻，輸出為分類評估報告。2) 評估框架建構：作者提出一個研究評估框架，包含五大評估維度：方法學充分性、實驗可重現性、輕量化部署可行性、XAI 技術類型與應用方式、XAI 驗證機制。3) 文獻編碼與分類：依據上述維度對納入文獻進行編碼，記錄所用深度學習模型架構（如 CNN、RNN、Transformer 等）、輕量化策略（模型剪枝、知識蒸餾、量化等）、採用的 XAI 方法（如 SHAP、LIME、Grad-CAM、注意力機制視覺化等）、XAI 驗證方式（定量指標、用戶研究、專家評估）、隱私保護手段（聯合學習、差分隱私、同態加密）以及使用的資料集（如 CICIDS2017、Bot-IoT、NSL-KDD 等）。4) 綜合分析與歸納：統計各維度分佈，識別研究趨勢、常見缺口（如輕量化與解釋性權衡、隱私保護與模型效能平衡、XAI 驗證標準化不足），並提出未來研究建議。此方法強調系統性、可重現性與多維度評估，區別於傳統敘述性回顧。

## 結果
摘錄未提供可驗證數字。定性結論顯示：當前研究不僅關注攻擊偵測準確率，更致力於設計兼具輕量化、可解釋性與隱私保護的 IDS 方案。文獻中常見深度學習模型包括 CNN、LSTM、自編碼器等；輕量化策略以模型壓縮與知識蒸餾為主；XAI 方法以 SHAP、LIME 及注意力視覺化最常用；隱私保護多採用聯合學習架構。然而，XAI 驗證多缺乏標準化量化指標，實驗可重現性資訊不足，且輕量化部署於資源受限 IoT 設備的實測案例較少。本文建立的評估框架可作為後續研究的基準。

## 限制與展望
本文為系統性文獻回顧，未提出新模型或實驗，故無法直接驗證具體方法效能。評估框架雖涵蓋五大維度，但權重分配與評分標準未在摘錄中詳細說明，可能存在主觀性。納入文獻的時間範圍、資料庫來源與篩選流程未於摘錄中揭露，可能影響回顧的完整性。XAI 驗證方式多樣且缺乏統一基準，導致跨研究比較困難。未來研究可致力於：建立標準化 XAI 評估指標、探索輕量化與解釋性的聯合優化機制、在真實 IoT 邊緣設備上進行部署驗證、以及整合隱私保護與可解釋性的理論框架。
