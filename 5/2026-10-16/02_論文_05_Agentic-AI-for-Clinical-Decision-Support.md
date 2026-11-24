# 論文 05：Agentic AI for Clinical Decision Support: Real-Time Diagnosis, Triage, and Treatment Planning

- 日期：2026-10-16
- 來源層級：Tier 1
- 期刊/會議/來源：International Journal of Scientific Research in Science, Engineering and Technology
- Venue：International Journal of Scientific Research in Science, Engineering and Technology
- 發布時間：2025-05-26T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/06288ad1bfce64cc068bba7e275a45bef4ddfd8f
- PDF：https://www.ijsrset.com/index.php/home/article/download/IJSRSET251265/IJSRSET251265
- DOI：10.32628/ijsrset251265
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：12
- 解析程度：fulltext / pdf
- 全文來源：https://www.ijsrset.com/index.php/home/article/download/IJSRSET251265/IJSRSET251265
- 全文字數：16958（pages=6, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Clinical decision-making often involves navigating complex data, rapidly changing patient conditions, and the need for precise, context-aware recommendations. Traditional clinical decision support systems (CDSS) provide rule-based assistance but frequently fall short in dynamic environments due to their lack of contextual understanding, adaptability, and real-time responsiveness. In this paper, we introduce an agentic AI framework designed specifically for clinical environments. By integrating autonomous AI agents with medical reasoning capabilities, seamless access to electronic health records (EHRs), and structured inter-agent communication, our system enables real-time diagnosis, triage prioritization, and personalized treatment planning. Using synthetic yet medically realistic patient datasets, we evaluate system performance in terms of diagnostic accuracy, triage precision, interpretability, system latency, and physician satisfaction. The results demonstrate substantial performance gains over traditional systems and lay the groundwork for a new era in clinical AI. The complexity of clinical decision-making continues to grow due to rapidly changing patient data and the demand for timely, context-aware responses. Traditional clinical decision support systems (CDSS) often fall short in dynamic environments. In this paper, we introduce an agentic AI framework that integrates autonomous agents with structured memory and EHR interoperability. The system supports real-time diagnosis, triage, and treatment planning. In comparative evaluations using synthetic patient datasets, our framework achieved 92.4% diagnostic accuracy, 95.2% triage precision, and reduced average response latency to 3.7 seconds—a 40% improvement over rule-based CDSS. The results highlight the transformative potential of agentic AI in augmenting clinical workflows.

## 背景與目的
臨床決策面臨複雜資料、病情快速變化與需即時、情境感知建議的挑戰。傳統臨床決策支援系統（CDSS）以規則為基礎，缺乏情境理解、適應性與即時回應能力，難以應對動態環境。本文提出一個專為臨床環境設計的代理式 AI 框架，整合具醫療推理能力的自主 AI 代理、無縫電子健康紀錄（EHR）存取與結構化代理間通訊，支援即時診斷、分流優先排序與個人化治療規劃。研究使用合成但醫學真實的病患資料集，評估診斷準確率、分流精確度、可解釋性、系統延遲與醫師滿意度，旨在展示代理式 AI 在臨床工作流中的變革潛力，並為新一代臨床 AI 奠定基礎。

## 方法
系統採用模組化、協作式多代理架構，包含五類代理：Intake Agent 透過 NLP 從結構化表單與自然語言筆記擷取症狀並轉為結構化輸入；Diagnosis Agent 結合決策樹、貝氏網路與 Transformer 模型，採差異診斷推理排序潛在診斷；Triage Agent 依生命徵象、檢驗值與 ESI、NEWS2 評分系統計算緊急度；Treatment Agent 整合藥物交互資料庫、NIH/WHO 指南，考量過敏、禁忌與併發症生成個人化治療方案；Coordinator Agent 負責工作流編排、記憶體同步、角色交接與稽核日誌。記憶層採雙層設計：短期記憶用 Redis 暫存易失性病患資料，長期記憶用 Neo4j 保存結構化病例歷程與決策日誌，支援跨代理記憶一致性。代理間通訊採用 OpenAI Agentic SDK 的 Model Context Protocol (MCP)，訊息附帶角色元資料與病患情境。工具整合包含 FHIR 實現 EHR 即時互操作、RAG 技術檢索 PubMed 文獻、第三方臨床工具（如 Infermedica）輔助症狀檢核與早期鑑別診斷。資料集以 MIMIC-III 與 Synthea 為靈感建構合成病患檔案，涵蓋人口統計、主訴、生命徵象、檢驗/影像摘要、併發症、過敏與用藥，跨五大診斷類別並植入邊緣案例。評估流程包含案例模擬、三位專科醫師盲測評分、規則型 CDSS 基線比較與壓力測試。指標定義：診斷準確率（首選診斷與金標準一致比例）、分流精確度（與 ESI/NEWS2 一致度）、治療有效性（符合指南程度）、延遲（端到端平均回應時間）、醫師滿意度（1-5 Likert 量表），各指標在 150 獨特案例上計算均值、標準差、信賴區間，並以雙尾 t 檢定（α=0.05）驗證顯著性。

## 結果
實驗結果顯示代理式 AI 系統在所有指標上優於傳統 CDSS：診斷準確率 92.4% 對 84.1%，分流精確度 95.2% 對 87.6%，治療有效性 90.5% 對 83.3%，平均延遲 3.7 秒對 6.2 秒（降低 40%），醫師滿意度 4.6/5 對 3.8/5。案例研究展示一 56 歲男性胸痛案例，系統在 4 秒內完成攝取、鑑別診斷（含不穩定型心絞痛、肺栓塞、GERD）、ESI Level 2 分流與治療建議（心電圖、肌鈷蛋白、阿斯匹靈），經醫師確認適當。定性上，系統在模糊症狀與併發症案例中展現更佳適應性與細緻度。

## 限制與展望
研究假設輸入資料品質高，真實部署需強健錯誤處理與自適應學習機制；EHR 整合度因機構異而影響互操作性；擴展至腫瘤學、精神科等專科需新增代理技能與領域知識庫。未來方向包括：多模態推理（影像、基因組）、聯邦學習實現隱私保護模型更新、面向病患的對話代理支援共同決策，並需增強系統在緊急、資料有限或快速演變情境下的韌性。此外，自動化偏誤風險須透過介面透明化與決策可追溯性緩解，審計追蹤與人工覆核機制為必要防護。
