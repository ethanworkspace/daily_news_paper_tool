# 論文 01：TAE-IDS: a trust-aware explainable intrusion detection framework using attention-based meta-ensemble learning with blockchain validation.

- 日期：2026-09-16
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
現有入侵偵測系統多依賴機器學習與深度學習，但普遍缺乏可解釋性、決策過程為黑箱，且缺少對入侵記錄的可信驗證機制，導致分析師難以信任與審計警報。本文旨在解決上述三大缺口，提出 TAE-IDS，結合注意力機制的元集成學習、SHAP 解釋與區塊鏈式防竄改驗證，提供透明、可追溯且具信任保障的入侵偵測框架。

## 方法
問題設定為對網路流量進行二元與多類別入侵分類，輸入為預處理後的特徵向量，輸出為入侵類別標籤與可解釋的貢獻度。整體架構分三層：基礎分類器層、元分類器層、驗證與解釋層。基礎分類器採用異質模型：Logistic Regression (LR)、Extra Trees (ET)、XGBoost (XGB)，分別捕捉線性、樹狀集成與梯度提升特性。每個基礎模型輸出 logits、置信度分數與熵值，組成不確定性感知的元特徵向量。元分類器採用雙向 LSTM (BiLSTM) 搭配注意力機制，依序建模元特徵的時序與上下文關係，並自適應加權聚合基礎模型預測，產生最終入侵判斷。訓練目標為最小化交叉熵損失，並可加入正則化以穩定注意力權重。推論流程：流量特徵 → 三基礎模型並行推論 → 提取元特徵 → BiLSTM‑Attention 元分類器 → 最終標籤。解釋層引入 SHAP，計算全域特徵重要度與單樣本局部貢獻，提供分析師可視化依據。驗證層採用區塊鏈啟發的防竄改機制：每筆偵測結果經 SHA‑256 雜湊串聯成鏈，確保日誌不可竄改、可審計與取證。關鍵差異在於將不確定性元特徵、注意力元集成、XAI 與密碼學驗證整合於單一框架，既提升檢測準確度又強化信任與可追溯性。

## 結果
作者在 UNSW‑NB15 與 CICIDS2017 兩基準資料集上進行二元與多類別實驗，報告 TAE‑IDS 達到強健的入侵偵測效能、可解釋的推理結果，且區塊鏈輔助驗證有效防範日誌竄改。摘錄未提供可驗證數字，僅能觀察到定性結論：整合 XAI 與區塊鏈驗證提升透明度、取證追溯性與記錄完整性，為未來實際網路環境部署奠基。

## 限制與展望
目前評估僅限於兩個公開基準集，缺乏真實營運網路流量與即時部署的驗證；區塊鏈式雜湊鏈在高吞吐量環境下的延遲與儲存開銷未量化；未與最新 SOTA 深度學習 IDS 或其他集成方法進行直接數值比較；SHAP 計算成本於大規模流量可能成為瓶頸；模型超參數敏感度與跨資料集泛化能力尚未充分探討。後續研究可著重於線上串流偵測、輕量化驗證機制、更大規模異質資料集實驗以及正式安全審計標準的對接。
