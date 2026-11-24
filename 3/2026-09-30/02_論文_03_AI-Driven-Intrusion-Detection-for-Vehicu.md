# 論文 03：AI-Driven Intrusion Detection for Vehicular Networks: A Comprehensive Survey of Techniques, Datasets, Deployment Architectures, and Future Directions.

- 日期：2026-09-30
- 來源層級：Tier 2
- 期刊/會議/來源：Sensors (Basel, Switzerland)
- Venue：Sensors (Basel, Switzerland)
- 發布時間：2026-09-30T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42884411/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13667682/
- DOI：10.3390/s26196211
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1752（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Intelligent transportation systems (ITSs), Vehicle-to-Everything (V2X) communication and autonomous driving technologies have brought about significant changes in the modern vehicular network. At the same time, the cyber-attack surface has grown, leading to new and existing advanced security threats for Vehicular Ad hoc Networks (VANETs) and the Internet of Vehicles (IoV). Traditional IDSs that employ static rule-based techniques are often insufficient in the context of the vehicular environment, characterized by dynamic, highly mobile systems with stringent low-latency requirements. Next generation IDS development has shifted to artificial intelligence (AI), which offers adaptive, scalable and data-driven detection capabilities. In this survey, the authors present a comprehensive overview of the state-of-the-art of AI-driven vehicle IDS in terms of machine learning (ML), deep learning (DL), federated learning (FL), reinforcement learning (RL), transformer-based techniques, and graph neural network (GNN) designs. We present a multidimensional taxonomy of vehicular attacks, an analysis of existing datasets and their weaknesses, an evaluation of the performance of AI techniques and a study of potential deployment architectures such as edge, fog and cloud. Furthermore, some of the most important open problems are identified, including data scarcity, adversarial robustness, real-time constraints, data utility-privacy conflicts, and standardization gaps. A research roadmap is provided, including 6G connectivity, blockchain-based IDS, explainable AI (XAI), Digital Twin technologies and post-quantum cryptography. This survey provides a common reference for the designers and developers of secure, efficient and interoperable VIDSs.

## 背景與目的
智慧運輸系統（ITS）、車聯網（V2X）與自駕技術推動車用網絡演進，同時擴大網攻面，使 VANET 與 IoV 面臨新型與進階威脅。傳統基於靜態規則的入侵偵測系統（IDS）難以因應車用環境的高動態、高移動性與嚴格低延遲需求。新一代 IDS 轉向人工智慧（AI），提供自適應、可擴展、數據驅動的偵測能力。本文為綜述論文，旨在提供 AI 驅動車用 IDS（VIDS）的全面概覽，涵蓋機器學習（ML）、深度學習（DL）、聯合學習（FL）、強化學習（RL）、Transformer 架構與圖神經網絡（GNN）等技術。貢獻包括：多維度車用攻擊分類法、現有資料集及其弱點分析、AI 技術效能評估、邊緣/霧/雲部署架構研究、關鍵開放問題識別（資料稀缺、對抗魯棒性、即時限制、資料效用與隱私衝突、標準化缺口），以及包含 6G、區塊鏈 IDS、可解釋 AI（XAI）、數位雙生與後量子密碼的研究路線圖，為安全、高效、可互操作的 VIDS 設計者提供共同參考。

## 方法
本文採用系統性文獻綜述方法，問題設定為對車用網絡中 AI 驅動 IDS 技術、資料集、部署架構與未來方向的綜合分析。輸入為現有學術論文、公開資料集、攻擊分類標準與部署案例研究；輸出為多維度攻擊分類法、資料集弱點總結、AI 技術效能比較、部署架構評估、開放問題清單與研究路線圖。核心模組包含：(1) 多維度攻擊分類法建構，依攻擊向量、目標層級、影響範圍等維度歸類車用網絡威脅；(2) 資料集分析框架，檢視現有車用 IDS 資料集的數據來源、標註品質、類別平衡、時空特徵覆蓋度等弱點；(3) AI 技術評估矩陣，將 ML、DL、FL、RL、Transformer、GNN 等範式納入，從檢測準確率、延遲、模型大小、通訊開銷、隱私保護等指標進行質性比較；(4) 部署架構研究，分析邊緣計算、霧計算、雲端計算在 VIDS 中的適用場景、資源限制與協同機制。方法論上採用定性綜合與歸納分析，無訓練目標、損失函數或最佳化策略。推論流程為文獻篩選→分類編碼→跨維度比較→差距識別→路線圖制定。與既有綜述的關鍵差異在於：同時涵蓋六大 AI 範式、引入多維度攻擊分類、系統性評估資料集弱點、結合部署架構視角、並提出具體研究路線圖。

## 結果
摘錄未提供可驗證數字。本文定性結論指出：AI 技術顯著優於傳統規則基礎 IDS，但在車用環境下仍面臨資料稀缺、對抗樣本脆弱、即時推論延遲、資料隱私與效用權衡、缺乏統一標準等核心挑戰。各 AI 範式各有優劣：DL 在特徵提取強但需大量標註資料；FL 緩解隱私卻引入通訊開銷；RL 適合動態決策但收斂難；Transformer 與 GNN 能捕捉時空依賴但計算複雜度高。部署架構方面，邊緣/霧計算可滿足低延遲需求，雲端適合全域模型訓練。研究路線圖提出 6G 融合、區塊鏈增強可信、XAI 提升可解釋性、數位雙生實現仿真驗證、後量子密碼應對量子威脅等五大方向。

## 限制與展望
作為綜述論文，本研究受限於文獻檢索截止時間，可能未涵蓋最新發表的模型與資料集；資料集分析僅基於公開可得資料，私有或區域性資料集未納入；AI 技術效能比較缺乏統一實驗基準，結論多為質性歸納而非量化實證；部署架構研究偏向理論分析，缺乏大規模實地部署驗證；開放問題與路線圖雖具前瞻性，但具體技術實現路徑、標準化進程與法規遵循仍待後續研究探索。潛在風險包括：過度依賴特定 AI 範式導致單點失效、對抗攻擊對安全關鍵系統的災難性後果、隱私保護與偵測效能的不可調和衝突。後續研究建議聚焦於跨域資料集構建、輕量化對抗防禦、異構邊緣協同推論、標準化測試床建立與法規技術共同演進。
