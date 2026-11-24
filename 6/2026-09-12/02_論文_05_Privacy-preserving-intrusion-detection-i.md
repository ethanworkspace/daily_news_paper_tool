# 論文 05：Privacy-preserving intrusion detection in IoT smart homes using a federated hybrid 1D-CNN-LSTM model with explainable AI.

- 日期：2026-09-12
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
物聯網裝置在智慧家庭大量部署，極大擴大攻擊面，特別是僵屍網路驅動的 DDoS 攻擊。傳統集中式入侵偵測系統（IDS）因侵犯隱私、單點故障與高通訊開銷而不適用。聯邦學習（FL）提供保護隱私的替代方案，但現有 FL‑IDS 多僅單獨使用卷積或循環模型、缺乏人類可解釋輸出，或忽略實際部署限制。本文提出 FedShield‑IDS，旨在結合混合 1D‑CNN‑LSTM 捕捉空間流量指紋與長程時間攻擊動態，並整合 SHAP 提供可解釋警報，解決隱私、準確性與透明度三大需求。

## 方法
問題設定：輸入為網路流量流記錄（CICIoT2023，712,311 筆，八大攻擊家族），輸出為多類別攻擊標籤。整體架構採用聯邦學習框架，七個虛擬 IoT 邊緣節點各自在本地訓練混合模型，經加密後以 Federated Averaging 聚合，進行五輪通訊，不交換原始流量。核心模組為 1D‑CNN 疊加 LSTM：CNN 以多尺度核擷取流量特徵的空間指紋，LSTM 再建模長距離時間相依性以識別攻擊動態。資料前處理管線包含無限值填補、對數特徵縮放、Min‑Max 正規化、時間窗口切分與本地化 SMOTE 過採樣，解決非 IID 分佈與極端類別不平衡。訓練目標採用交叉熵損失（分類任務），最佳化器未於摘錄明確說明。推論流程：邊緣節點接收流量窗口 → 本地模型前向傳播 → 輸出攻擊機率 → 全域聚合模型更新 → SHAP 計算特徵貢獻 → 產生人類可讀解釋並觸發緩解閘門。關鍵差異在於同時整合空間卷積與時間循環、於聯邦環境下引入 SHAP 解釋、並針對非 IID 與類別不平衡設計本地化預處理。

## 結果
實驗顯示 Mirai 類別 F1‑score 達 0.99，DDoS 精確度 0.97，八類整體加權 F1‑score 為 0.76。核大小、架構與預處理的消融實驗證明各設計必要。跨資料集於 Edge‑IIoTset 獨立評估達 98.58% 準確率，顯示泛化能力。威脅緩解延遲低於 500 ms，經閾值敏感度分析驗證。每條警報皆產生 SHAP 解釋，滿足可信智慧家庭安全的透明度需求。

## 限制與展望
僅於 CICIoT2023 與 Edge‑IIoTset 兩資料集驗證，真實家庭流量分佈可能不同。聯邦模擬僅使用七個虛擬節點與五輪通訊，未評估真實異質裝置、網路延遲與加密開銷。本地化 SMOTE 可能引入合成樣本偏差，非 IID 處理效果在大規模部署仍待證實。威脅模型假設為半誠實伺服器，若存在惡意客戶端或模型投毒攻擊，安全性保證需進一步加強。SHAP 計算於邊緣裝置可能增加推論延遲與能耗，實際部署需權衡。後續研究可探索更輕量解釋方法、真實邊緣硬體測試、抗投毒機制與動態聯邦聚合策略。
