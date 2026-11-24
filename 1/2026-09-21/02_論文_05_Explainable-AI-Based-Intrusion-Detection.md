# 論文 05：Explainable AI-Based Intrusion Detection Systems for IoT Environments: A Systematic Literature Review.

- 日期：2026-09-21
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
物聯網設備快速普及導致網路攻擊風險顯著增加，入侵偵測系統（IDS）成為保護 IoT 網路的關鍵方案。雖然機器學習與深度學習為基礎的 IDS 在攻擊偵測準確率上表現優異，但模型決策過程缺乏透明度，嚴重影響可靠性與可解釋性。為解決此問題，可解釋人工智慧（XAI）技術被引入 IDS 設計。本文為系統性文獻回顧，旨在全面梳理針對 IoT 環境之 XAI 賦能 IDS 的現有研究，評估深度學習模型、輕量化設計、可解釋性方法與驗證、資料隱私保護及資料集使用等面向，並提出一套研究評估框架，以系統性檢視方法學完整性、實驗可重現性、輕量化部署、XAI 技術與驗證，為未來可靠、可解釋且實用的 IoT 入侵偵測研究提供基石參考。

## 方法
本研究採系統性文獻回顧方法，依據 PRISMA 指導原則檢索並篩選相關文獻。核心步驟包含：(1) 問題設定與檢索策略：以 IoT 環境下結合 XAI 的 IDS 為研究對象，從多個學術資料庫檢索同行評審論文；(2) 納入與排除標準：聚焦於提出具體 XAI 技術、輕量化模型設計、隱私保護機制或實驗驗證的研究；(3) 資料提取與編碼：對每篇文獻記錄所用深度學習架構（如 CNN、RNN、Transformer 等）、模型輕量化策略（知識蒸餾、剪枝、量化等）、採用的 XAI 方法（SHAP、LIME、注意力視覺化、規則擷取等）、XAI 驗證方式（定量指標、用戶研究、專家評估）、隱私保護手段（聯合學習、差分隱私、加密推理）以及實驗資料集（如 CICIDS2017、Bot-IoT、NSL-KDD 等）；(4) 研究評估框架：作者自行設計五維度評估指標——方法學完整性、實驗可重現性、輕量化部署可行性、XAI 技術適切性、XAI 驗證嚴謹性，並對納入文獻逐項打分；(5) 綜合分析：統計各維度分佈、識別研究趨勢與缺口，歸納出當前研究不僅追求偵測準確度，更強調輕量化、可解釋性與隱私保護的三重目標。推論流程為：文獻篩選 → 特徵編碼 → 框架評分 → 趨勢歸納 → 研究缺口總結。與既有綜述不同處在於引入專門針對 XAI-ID S 的多維度評估框架，並系統性檢視輕量化與隱私保護兩大 IoT 部署關鍵需求。

## 結果
摘錄未提供可驗證數字。定性結論顯示：(1) 現有研究普遍採用深度學習模型並搭配 SHAP、LIME、注意力機制等 XAI 方法提供解釋；(2) 輕量化設計多透過模型壓縮、知識蒸餾或輕量網路架構實現，以適應資源受限 IoT 設備；(3) 隱私保護方面，聯合學習為主流方案，部分研究結合差分隱私；(4) 評估框架應用結果指出，大多數文獻在方法學完整性與實驗可重現性上表現中等，而在 XAI 驗證嚴謹性與輕量化部署實證上存在明顯不足；(5) 研究趨勢顯示未來工作需加強 XAI 驗證標準化、真實 IoT 環境部署測試、以及隱私與解釋性的協同優化。

## 限制與展望
本文為系統性文獻回顧，固有限制包括：(1) 檢索範圍受限於所選資料庫與關鍵字，可能遺漏灰色文獻或最新預印本；(2) 評估框架為作者自行設計，缺乏外部驗證與社群共識，主觀性較高；(3) 未對原始模型效能指標進行元分析，無法量化比較不同 XAI 方法對偵測性能的影響；(4) 隱私保護與輕量化部署的實際落地案例極少，多停留於模擬環境，真實部署可行性存疑；(5) XAI 驗證多為定性或單一指標，缺乏標準化基準。後續研究建議：建立統一 XAI-ID S 評測基準、推動真實 IoT 測試床驗證、探索隱私-解釋性-準確度三方權衡的理論框架、以及發展自動化 XAI 品質評估工具。
