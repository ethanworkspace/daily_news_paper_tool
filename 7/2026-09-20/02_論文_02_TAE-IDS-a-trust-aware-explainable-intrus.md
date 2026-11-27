# 論文 02：TAE-IDS: a trust-aware explainable intrusion detection framework using attention-based meta-ensemble learning with blockchain validation.

- 日期：2026-09-20
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Frontiers in artificial intelligence
- Venue：Frontiers in artificial intelligence
- 發布時間：2026-01-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42698774/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13541755/
- DOI：10.3389/frai.2026.1903112
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2197（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Recent intrusion detection systems (IDS) increasingly rely on machine learning (ML) and deep learning techniques to detect sophisticated cyberattacks. However, many existing frameworks still suffer from limited explainability, black-box decision-making, and the absence of secure trust verification mechanisms for intrusion records. To address these challenges, this paper proposes TAE-IDS, a Trust-Aware Explainable Intrusion Detection Framework that integrates attention-based meta-ensemble learning, SHapley Additive exPlanations (SHAP)-driven explainability, and blockchain-inspired tamper-evident validation within a unified cybersecurity architecture. The proposed framework employs heterogeneous base classifiers, namely Logistic Regression (LR), Extra Trees (ET), and XGBoost (XGB), to capture diverse network traffic characteristics. Uncertainty-aware meta-features, including logits, confidence scores, and entropy representations, are extracted from the base learners and processed by an adaptive Bidirectional Long Short-Term Memory (BiLSTM) attention-based meta-classifier for contextual intrusion reasoning and adaptive ensemble aggregation. To enhance transparency and analyst trust, SHAP-based explainability is incorporated to provide both global and local interpretations of intrusion predictions. Furthermore, a blockchain-inspired tamper-evident validation mechanism based on SHA-256 cryptographic hashing is integrated to enable tamper-proof intrusion logging, immutable auditing, and secure forensic verification of IDS outputs. The proposed framework was evaluated on the UNSW-NB15 and CICIDS2017 benchmark datasets under both binary and multiclass intrusion detection settings. Experimental results demonstrate that TAE-IDS achieves strong intrusion detection performance, interpretable intrusion reasoning, and effective blockchain-assisted tamper-evident validation on the evaluated benchmark datasets. The integration of explainable artificial intelligence (XAI) and blockchain-assisted validation enhances transparency, forensic traceability, and the integrity of intrusion records while providing a foundation for future validation in operational network environments.

## 背景與目的
現有入侵偵測系統（IDS）多仰賴機器學習與深度學習，但普遍缺乏可解釋性、決策過程為黑箱，且缺少對入侵記錄的安全信任驗證機制。本文旨在解決上述問題，提出 TAE-IDS，一個信任感知可解釋入侵偵測框架，整合基於注意力的元集成學習、SHAP 驅動的可解釋性，以及區塊鏈啟發的防篡改驗證，構建統一的網路安全架構，提升透明度、取證追溯與記錄完整性。

## 方法
TAE-IDS 採用異質基礎分類器組合，包含邏輯回歸（LR）、Extra Trees（ET）與 XGBoost（XGB），分別捕捉網路流量的多樣特徵。從各基礎學習器提取不確定性感知的元特徵，包括 logits、信心分數與熵表示，作為後續元分類器的輸入。核心為自適應雙向長短期記憶（BiLSTM）注意力機制的元分類器，透過注意力權重對序列化的元特徵進行上下文推理與自適應集成聚合，輸出最終入侵判斷。為增強透明度，引入 SHAP（SHapley Additive exPlanations）提供全域與局部解釋，量化各特徵對預測的貢獻。此外，整合區塊鏈啟發的防篡改驗證模組，採用 SHA-256 密碼雜湊將入侵記錄串聯成不可竄改鏈結構，支援防篡改日誌、不可變稽核與安全取證驗證。整體流程包含資料前處理、基礎模型訓練、元特徵擷取、BiLSTM-Attention 元分類器訓練、SHAP 解釋生成、區塊鏈式日誌寫入與推理階段的即時驗證。

## 結果
實驗於 UNSW-NB15 與 CICIDS2017 基準資料集，分別進行二元與多類別入侵偵測設定。作者報告 TAE-IDS 達到強健的入侵偵測效能、可解釋的推理過程，以及有效的區塊鏈輔助防篡改驗證。摘錄未提供可驗證數字（如準確率、F1、AUC 等具體指標），故無法量化比較優劣；定性結論顯示該框架整合 XAI 與區塊鏈驗證能提升透明度、取證追溯與記錄完整性。

## 限制與展望
摘錄未詳細說明資料集劃分、超參數設定、計算資源需求、區塊鏈模組的吞吐量與延遲、以及真實部署環境下的擴展性。潛在限制包括：僅於離線基準測試驗證，缺乏線上串流與對抗樣本評估；區塊鏈啟發機制非真實共識網路，可能無法完全代表去中心化信任模型；SHAP 計算成本在高維流量下可能成為瓶頸。後續研究可探討輕量化注意力模組、真實區塊鏈整合、對抗魯棒性與線上增量學習。
