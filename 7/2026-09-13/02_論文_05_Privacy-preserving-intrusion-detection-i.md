# 論文 05：Privacy-preserving intrusion detection in IoT smart homes using a federated hybrid 1D-CNN-LSTM model with explainable AI.

- 日期：2026-09-13
- 來源層級：Tier 2
- 期刊/會議/來源：Scientific reports
- Venue：Scientific reports
- 發布時間：2026-09-02T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42686802/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13538480/
- DOI：10.1038/s41598-026-67450-9
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2650（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
The proliferation of Internet of Things (IoT) devices in smart home environments has dramatically expanded the attack surface for cyber threats, particularly botnet-driven Distributed Denial of Service (DDoS) attacks. Centralized Intrusion Detection Systems (IDS) are ill-suited to this domain because they violate user privacy, introduce single points of failure, and incur prohibitive communication overhead. Federated Learning (FL) offers a compelling privacy-preserving alternative, yet existing FL-based IDS solutions either deploy convolutional or recurrent models in isolation, lack human-interpretable outputs, or neglect real-world deployability constraints. This paper proposes FedShield-IDS, a novel federated intrusion detection framework that integrates a hybrid one-dimensional Convolutional Neural Network with Long Short-Term Memory units to simultaneously capture spatial traffic fingerprints and long-range temporal attack dynamics across IoT edge devices. Model interpretability is addressed through the integration of SHapley Additive exPlanations (SHAP), enabling administrators to receive human-readable justifications for every detected anomaly. The system is trained and evaluated on the large-scale CICIoT2023 dataset, comprising 712,311 flow records spanning eight attack families including DDoS, DoS, Mirai, Reconnaissance, Spoofing, Injection, and Malware. A multi-stage preprocessing pipeline combining infinite-value imputation, logarithmic feature scaling, Min-Max normalization, temporal windowing, and localized SMOTE oversampling is applied within each federated client to address non-IID data and extreme class imbalance. Federated Averaging aggregates encrypted model updates across seven virtual IoT client nodes over five communication rounds without exchanging raw traffic data, under a formal threat model characterizing the system's adversarial assumptions and data-confidentiality guarantees. Experimental results demonstrate a Mirai F1-score of 0.99, a DDoS precision of 0.97, and a global weighted F1-score of 0.76 across all eight classes. Comprehensive kernel-size, architecture, and preprocessing ablations confirm the necessity of each design choice, and independent cross-dataset evaluation on the Edge-IIoTset benchmark achieves 98.58% accuracy, demonstrating strong generalization beyond CICIoT2023. The framework achieves sub-500 ms threat mitigation, empirically confirmed via a mitigation-gate threshold sensitivity analysis, and generates SHAP-gated explanations for every alert, bridging the gap between high-accuracy detection and the transparency required for trustworthy smart-home security.

## 背景與目的
物聯網裝置在智慧家庭大量部署，極大擴大了僵屍網路驅動的 DDoS 攻擊面。傳統集中式入侵偵測系統（IDS）因侵犯隱私、單點故障與高通訊開銷而不適用。聯邦學習（FL）提供保護隱私的替代方案，但現有 FL‑IDS 多僅採用單一卷積或循環模型、缺乏人類可解釋輸出，且忽略實際部署限制。本文提出 FedShield‑IDS，旨在結合混合 1D‑CNN‑LSTM 捕捉空間流量指紋與長程時間攻擊動態，並整合 SHAP 提供可讀性解釋，解決隱私、準確性與可信度的三重需求。

## 方法
問題設定：在七個虛擬 IoT 邊緣節點上進行聯邦訓練，輸入為 CICIoT2023 的網路流量流記錄，輸出為八大攻擊家族的多類別標籤。 模型架構：採用混合一維卷積神經網路（1D‑CNN）與長短期記憶（LSTM）串接，CNN 先提取局部空間特徵（流量指紋），LSTM 再建模長距離時序依賴，最後接全連接層輸出類別機率。 資料前處理：每個客戶端獨立執行多階段管線——無限值填補、對數特徵縮放、Min‑Max 正規化、時間窗口切分、局部 SMOTE 過採樣，以緩解非 IID 分佈與極端類別不平衡。 訓練目標與最佳化：使用交叉熵損失，採用 Adam 優化器；聯邦輪次採用 FedAvg，五輪通訊中僅交換加密後的模型更新，原始流量不出本地。 威脅模型：正式定義對手能力與資料機密性保證，確保模型更新在傳輸過程中不可被逆向推導原始資料。 推論流程：邊緣節點本地前處理 → 本地模型推論 → 若信心分數超過緩解閾值則觸發緩解動作，並同步產生 SHAP 值以解釋每個異常警報的關鍵特徵貢獻。 關鍵差異：同時整合空間與時間混合網路、聯邦加密聚合、本地化 SMOTE 處理非 IID、SHAP 即時解釋，並針對實時緩解閾值進行敏感度分析。

## 結果
實驗顯示 Mirai 類別 F1‑score 達 0.99、DDoS 精確率 0.97、全域加權 F1‑score 0.76（八類）。消融實驗證實核大小、混合架構與前處理各環節皆不可或缺。跨資料集於 Edge‑IIoTset 達 98.58% 準確率，顯示泛化能力。系統威脅緩解延遲低於 500 ms，並對每條警報產生 SHAP 解釋，滿足高準確度與透明度雙重需求。

## 限制與展望
僅在 CICIoT2023 與 Edge‑IIoTset 兩個基準上驗證，真實家庭流量分佈可能更複雜；虛擬七節點與五輪聯邦設定為模擬，實際部署時通訊延遲、異質硬體與加密開銷未量化；SHAP 計算於邊緣裝置可能增加推論負擔；威脅模型假設半誠實伺服器，若伺服器惡意竄改聚合則安全性未經證實；後續研究可探討自適應聯邦輪次、輕量化解釋模組與真實邊緣環境的壓力測試。
