# 論文 04：AI-driven cybersecurity for industrial internet of things: architectures, challenges, datasets, and future research directions.

- 日期：2026-09-12
- 來源層級：Tier 2
- 期刊/會議/來源：Frontiers in big data
- Venue：Frontiers in big data
- 發布時間：2026-01-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42769675/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13592189/
- DOI：10.3389/fdata.2026.1938279
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1887（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
While the Industrial Internet of Things (IIoT) has a wide range of applications in the modern era, including smart manufacturing, healthcare, transportation, energy, and critical infrastructure, the multitude of devices and distributed communication, alongside the convergence of cyber and physical systems, makes these environments vulnerable to more advanced cyber-attacks. Traditional signature or pattern-based security solutions continue to be ineffective against new, sneaky, and zero-day attack strategies, fueling the interest in AI-powered cybersecurity. This review aims to analyze the latest developments systematically in intelligent threat detection and defense in IIoT environments. The review critically analyzes the cybersecurity research published over the past few years (2020-2026) on cyber threats across the various layers of the IIoT architecture, publicly available cybersecurity datasets, evaluation practices, and AI-based intrusion detection methods, such as machine learning, deep learning, hybrid architectures, transformers, graph neural networks, federated learning, reinforcement learning, and explainable AI. High benchmark performance alone is not sufficient to claim cybersecurity effectiveness, as the synthesis shows persistent limitations in cross-domain generalization, computational overhead, explainability, adversarial robustness, edge deployment, and operational validation. Emerging research priorities included in this review are lightweight edge intelligence, continual and adaptive learning, explainable federated intelligence, digital-twin-enabled security, foundation-model-driven cyber intelligence, autonomous cyber defense, and trustworthy AI. This review provides a pathway toward resilient, adaptive, and operationally deployable cybersecurity solutions for next-generation IIoT and highlights the PRISMA-based identification process.

## 背景與目的
工業物聯網（IIoT）廣泛應用於智慧製造、醫療、運輸、能源與關鍵基礎設施，但大量異質裝置與分散式通訊，加上網物融合特性，使其面臨更進階的網路攻擊。傳統基於特徵碼或模式比對的防護方案，對新型、隱匿與零日攻擊失效，推動 AI 驅動網安研究。本文為系統性綜述，旨在分析 2020-2026 年 IIoT 環境下智慧威脅偵測與防禦的最新發展，涵蓋 IIoT 架構各層的網安威脅、公開資料集、評估實務，以及機器學習、深度學習、混合架構、Transformer、圖神經網路、聯邦學習、強化學習與可解釋 AI 等入侵偵測方法，並指出單純基準效能不足以代表實戰有效性，歸納跨域泛化、計算開銷、可解釋性、對抗魯棒性、邊緣部署與營運驗證等持續缺口，提出輕量化邊緣智慧、持續自適應學習、可解釋聯邦智慧、數位雙生安全、基礎模型驅動網安智慧、自主網安防禦與可信 AI 等新興研究優先方向，提供下一代 IIoT 韌性、自適應且可部署網安解決方案的路徑。

## 方法
本研究採用 PRISMA 系統性文獻回顧流程，鎖定 2020 至 2026 年發表的 IIoT 網安研究。方法包含四大分析維度：(1) 威脅建模：依 IIoT 架構分層（感知層、網路層、平台層、應用層等）歸納各層常見攻擊向量與漏洞類型；(2) 資料集盤點：蒐集公開可用的 IIoT 網安資料集，記錄其資料來源、攻擊類別、流量特徵、標註品質與適用場景，並討論資料集間的異質性與代表性問題；(3) 評估實務審視：檢視現有研究常用的評估指標（準確率、F1、AUC 等）、資料分割方式、跨域驗證策略與實驗環境設定，指出缺乏標準化基準與實戰模擬的缺失；(4) AI 入侵偵測方法分類與綜合：將方法歸類為傳統機器學習、深度學習（CNN、RNN、AE 等）、混合架構、Transformer 基礎模型、圖神經網路（GNN）、聯邦學習、強化學習與可解釋 AI（XAI），並對比其在特徵表示（原始封包、流統計、圖結構、多模態融合）、訓練目標（監督式、半監督式、非監督式、自監督式）、損失函數設計、最佳化策略與推論延遲上的差異。綜合階段採用質性敘述綜合，提煉跨研究的共性限制：跨域泛化能力不足、模型龐大難以在資源受限邊緣裝置部署、缺乏可解釋性導致操作員難以信任、對抗樣本脆弱、缺乏實地營運驗證。最後，依據文獻空白推導七大新興研究優先方向，並提出包含資料、模型、部署、治理四面向的未來路線圖。

## 結果
綜述發現：單純追求高基準效能（Accuracy、F1 等）不足以保證 IIoT 實戰網安有效性。主要結論包括：(1) 現有方法普遍存在跨域泛化不足、計算與記憶體開銷過大、可解釋性缺失、對抗魯棒性薄弱、邊緣部署困難、缺乏實地營運驗證六大持續限制；(2) 公開資料集多為舊有 IT 網路流量改造，缺乏真實 IIoT 物理過程語義與多階段攻擊樣本，導致模型在真實環境表現下降；(3) 評估實務多採隨機分割同分布資料，忽略時序漂移與跨廠跨協定泛化；(4) 新興方向共識為：輕量化邊緣智慧、持續自適應學習、可解釋聯邦智慧、數位雙生輔助安全、基礎模型驅動網安、自主防禦與可信 AI。摘錄未提供可驗證的具體實驗數字、資料集規模或基線比較表現。

## 限制與展望
本綜述為文獻歸納性質，受限於檢索範圍（2020-2026）與 PRISMA 篩選標準，可能遺漏未公開或非英文研究。資料集分析僅依文獻描述，未實測資料品質；方法分類依賴作者原文定義，缺乏統一實驗平台的量化對比。新興研究優先方向為質性推論，尚無實證驗證其可行性與效益。潛在風險包括：綜述本身可能因出版偏誤高估特定技術成熟度；提出的路線圖缺乏具體技術路徑與里程碑。後續研究建議：建立標準化 IIoT 網安基準測試平台、開展大規模跨域實證、研發輕量化可解釋模型、探索基礎模型在網安領域的微調與對齊、制定可信 AI 治理框架。
