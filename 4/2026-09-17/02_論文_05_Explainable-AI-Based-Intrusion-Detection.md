# 論文 05：Explainable AI-Based Intrusion Detection Systems for IoT Environments: A Systematic Literature Review.

- 日期：2026-09-17
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
物聯網(IoT)裝置快速普及導致網路攻擊風險顯著增加，入侵偵測系統(IDS)成為保護關鍵基礎設施的重要手段。雖然機器學習與深度學習為基礎的 IDS 在攻擊偵測準確率上表現優異，但其決策過程缺乏透明度，嚴重影響可靠性與可解釋性。為解決此問題，可解釋人工智慧(XAI)技術被引入 IDS 設計。本文為系統性文獻回顧，旨在全面梳理面向 IoT 環境的 XAI 啟用 IDS 研究現況，並從深度學習模型、輕量化設計、可解釋性方法與驗證、資料隱私保護、資料集等五大維度進行系統評估，同時提出並應用一套研究評估框架，以檢視方法學完整性、實驗可重現性、輕量化部署、XAI 技術與 XAI 驗證等關鍵指標，期望為未來可靠、可解釋且實用的 IoT 入侵偵測系統研究提供基石資源。

## 方法
本研究採系統性文獻回顧方法，具體步驟包括：(1) 依據預先定義的納入/排除標準，從相關學術資料庫檢索面向 IoT 環境之 XAI 啟用 IDS 文獻（具體資料庫名稱、檢索式、時間範圍依目前可取得資料，無法確認）；(2) 建立研究評估框架，包含五大評估維度：方法學完整性、實驗可重現性、輕量化部署可行性、XAI 技術類型與應用方式、XAI 驗證機制（如人為評估、定量指標等）；(3) 對納入文獻進行編碼分類，記錄所用深度學習模型架構（如 CNN、RNN、Transformer 等）、輕量化策略（知識蒸餾、模型剪枝、量化等）、可解釋性方法（SHAP、LIME、注意力視覺化、規則擷取等）、隱私保護手段（聯邦學習、差分隱私、同態加密等）以及實驗使用資料集（如 CICIDS2017、Bot-IoT、NSL-KDD 等）；(4) 統計分析各維度分佈趨勢，識別研究缺口與共同限制。推論流程為：文獻篩選 → 特徵編碼 → 框架評分 → 綜合分析 → 歸納未來研究方向。與既有綜述相比，關鍵差異在於引入結構化評估框架並同時涵蓋輕量化、隱私保護與 XAI 驗證三大實務導向維度。

## 結果
摘錄未提供可驗證數字（如納入文獻篇數、各類模型/方法佔比、評估框架評分分佈等）。定性結論顯示：當前研究不僅追求偵測準確率，更強調輕量化部署、可解釋性與隱私保護的協同優化；XAI 方法以事後解釋（SHAP、LIME）為主，內建可解釋模型較少；XAI 驗證多缺乏標準化量化指標，多依賴專家主觀判斷；輕量化設計常以模型壓縮為主，鮮少結合硬體加速器驗證；隱私保護多採聯邦學習框架，但通訊開鍵與異質資料挑戰仍待解決。作者提出之評估框架可作為後續研究品質把關的參考依據。

## 限制與展望
本綜述受限於摘要資訊，無法確認文獻檢索的完整性、編碼者一致性檢定結果、評估框架的效度與信度驗證細節。潛在風險包括：出版偏誤可能導致正面結果過度代表；評估框架指標權重設定可能存在主觀性；未涵蓋灰色文獻與最新會議論文；輕量化與隱私保護的實際部署效能缺乏實證比較。後續研究建議：建立標準化 XAI 驗證基準、探索輕量化與解釋性的聯合優化機制、針對異質 IoT 環境設計自適應聯邦學習架構、並進行大規模實地部署驗證。
