# 論文 01：Privacy-preserving intrusion detection in IoT smart homes using a federated hybrid 1D-CNN-LSTM model with explainable AI.

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
智慧家庭中 IoT 設備大量部署，極大擴大了網路攻擊面，特別是僵屍網路驅動的 DDoS 攻擊。傳統集中式入侵偵測系統（IDS）因侵犯用戶隱私、單點故障與高通訊開銷而不適用。聯邦學習（FL）提供保護隱私的替代方案，但現有 FL‑IDS 多僅單獨使用卷積或循環模型、缺乏人類可解釋輸出，或忽略實際部署限制。本文旨在提出 FedShield‑IDS，結合一維 CNN 與 LSTM 於聯邦框架下同時捕捉流量空間指紋與長程時間攻擊動態，並整合 SHAP 提供可解釋警示，驗證於大規模 CICIoT2023 與跨資料集 Edge‑IIoTset，以達高準確度、低延遲與可信任的智慧家庭安全防護。

## 方法
問題設定：輸入為各邊緣裝置收集的網路流量流記錄，輸出為八大攻擊家族（DDoS、DoS、Mirai、Reconnaissance、Spoofing、Injection、Malware 等）之多類別標籤。 整體架構：採用聯邦學習範式，七個虛擬 IoT 客戶端各自在本地訓練混合 1D‑CNN‑LSTM 模型，經過五輪通訊由伺服器以 Federated Averaging 聚合加密後的模型更新，全程不交換原始流量資料，並定義正式威脅模型以保證資料機密性。 核心模組：1D‑CNN 以多尺度核心擷取流量特徵的空間指紋；LSTM 單元捕捉序列中的長程時間相依性，兩者串接形成混合編碼器，最後接全連接分類層。 資料前處理：每個客戶端獨立執行多階段管線——無限值填補、對數特徵縮放、Min‑Max 正規化、時間窗口切分、以及針對極端類別不平衡的局部 SMOTE 過採樣，以緩解非 IID 分佈與類別失衡。 訓練目標與最佳化：使用交叉熵損失，配合 Adam 最佳化器於本地端進行若干 epochs 訓練；聚合時採用加密模型更新的加權平均。 推論流程：邊緣裝置接收全域模型，對即時流量經相同前處理後推論，若預測分數超過緩解閾值則觸發緩解機制，並同步產生 SHAP 解釋以提供人類可讀的異常理由。 關鍵差異：相較既有 FL‑IDS，本文同時整合空間與時間混合網路、針對非 IID 與類別不平衡的本地化預處理、正式威脅模型下的加密聚合、以及全程 SHAP 可解釋輸出，並實證亞 500 ms 緩解延遲。

## 結果
實驗顯示 Mirai 類別 F1‑score 達 0.99，DDoS 類別 Precision 達 0.97，八類整體加權 F1‑score 為 0.76。消融實驗驗證核心大小、架構組合與預處理各環節皆為必要。跨資料集於 Edge‑IIoTset 基準達 98.58% 準確率，證明泛化能力。緩解閾值敏感度分析確認威脅緩解延遲低於 500 ms，且每條警示皆產生 SHAP 解釋，滿足可解釋性需求。摘錄未提供更細緻的各類別 Recall、AUC 或通訊開銷數字。

## 限制與展望
資料方面僅在 CICIoT2023 與 Edge‑IIoTset 驗證，真實家庭環境的異質流量、加密協議與設備數量變化未涵蓋。方法上假設七個虛擬客戶端與五輪通訊，實際部署時客戶端數量、非 IID 程度、頻寬限制可能更嚴重。評估僅報告部分指標，缺乏完整混淆矩陣、偽陽性率與資源消耗（記憶體、CPU、能耗）分析。部署風險包括模型更新被惡意竄改、SHAP 計算額外延遲、以及加密聚合的金鑰管理複雜度。後續研究可探索自適應通訊輪數、異構模型聚合、真實邊緣裝置上的輕量化推論與持續學習機制。
