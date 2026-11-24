# 論文 04：Explainable AI-Based Intrusion Detection Systems for IoT Environments: A Systematic Literature Review.

- 日期：2026-09-15
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
物聯網(IoT)設備快速普及，導致網路攻擊風險顯著增加。入侵偵測系統(IDS)成為保護IoT網路的關鍵方案。雖然機器學習與深度學習為基礎的IDS在攻擊偵測準確率上表現優異，但模型決策過程缺乏透明度，嚴重影響可靠性與可解釋性。為解決此問題，可解釋人工智慧(XAI)方法被引入IDS。本文旨在系統性回顧針對IoT環境的XAI啟用IDS文獻，評估深度學習模型、輕量化設計、可解釋性方法與驗證、資料隱私保護及資料集等面向，提供未來研究可靠、可解釋且實用的IoT入侵偵測系統之基礎資源，並提出研究評估框架以系統性評估方法學適切性、實驗可重現性、輕量化部署、XAI技術與XAI驗證。

## 方法
本研究屬系統性文獻回顧，問題設定為針對IoT環境下採用XAI的IDS相關文獻進行全面檢視。輸入為已發表的研究論文，輸出為對這些研究在五大維度的系統性評估：(1)使用的深度學習模型；(2)輕量化模型設計；(3)可解釋性方法與驗證方式；(4)資料隱私保護策略；(5)採用的資料集。整體架構包含文獻搜尋、篩選、資料萃取、品質評估與綜合分析。核心模組為作者提出的「研究評估框架」，用以系統性評估五項指標：方法學適切性、實驗可重現性、輕量化部署可行性、XAI技術應用、XAI驗證完整性。資料前處理與特徵表示屬於各被評估原始研究的內容，本回顧不直接處理原始資料。訓練目標、損失函數、最佳化策略等不適用於回顧本身。推論/執行流程為：依預定檢索策略(摘錄未具體說明資料庫、關鍵字、時間範圍)檢索文獻，依納入/排除標準(摘錄未詳細列出)篩選，萃取上述五維度資訊，套用評估框架打分，最後綜合敘述趨勢與缺口。與既有回顧的關鍵差異在於：明確將XAI驗證與輕量化部署納入評估框架，並聚焦IoT場景下的隱私保護需求。然而，摘錄未提供檢索式、納入文獻數量、具體XAI技術(如SHAP、LIME)分布、評估框架的量化權重等細節，依目前可取得資料，無法確認完整方法學細節。

## 結果
回顧結果顯示，當前研究不僅追求攻擊偵測準確率，更致力於設計輕量化、可解釋且保護隱私的IDS解決方案。本文提供基礎資源以指導未來研究，識別現有研究問題並凸顯文獻限制。提出的評估框架可系統性評估方法學適切性、實驗可重現性、輕量化部署、XAI技術與XAI驗證。摘錄未提供可驗證數字(如納入論文篇數、各維度得分分布、基線模型比較數值)，僅能觀察到定性結論：研究趨勢朝向多目標優化(準確度、輕量化、可解釋性、隱私)，且缺乏統一的XAI驗證標準。

## 限制與展望
本回顧受限於已發表文獻，可能遺漏最新預印本或灰色文獻；評估框架的指標選擇與權重設定可能存在主觀性，摘錄未說明框架建構過程與專家驗證細節；檢索策略、納入排除標準、文獻篩選流程圖(PRISMA)未在摘錄中呈現，影響回顧本身的可重現性；未進行量化元分析，無法給出效果大小或統計顯著性；潛在發表偏倚與語言偏倚未討論。後續研究可擴大檢索範圍、細化評估框架並引入量化綜合方法，另可實證驗證框架在實際IoT IDS部署中的適用性。
