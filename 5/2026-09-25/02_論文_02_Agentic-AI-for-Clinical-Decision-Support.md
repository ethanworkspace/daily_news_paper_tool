# 論文 02：Agentic AI for Clinical Decision Support: Real-Time Diagnosis, Triage, and Treatment Planning

- 日期：2026-09-25
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
臨床決策面臨資料複雜、病情快速變化與需即時、情境感知建議的挑戰。傳統臨床決策支援系統（CDSS）多為規則基礎，缺乏情境理解、適應性與即時回應能力。本文提出一個專為臨床環境設計的代理式 AI 框架，整合具醫療推理能力的自主代理、電子病歷（EHR）無縫存取與結構化代理間通訊，以實現即時診斷、分流優先排序與個人化治療規劃，並以合成但醫學真實的病患資料集評估系統表現，旨在展示代理式 AI 在臨床工作流中的變革潛力。

## 方法
系統採用模組化、協作式多代理架構，包含五類代理： 1. 入院代理：透過結構化表單與自然語言輸入擷取症狀，利用 NLP 將醫護筆記轉為結構化資料。 2. 診斷代理：結合決策樹、貝氏網路與 Transformer 模型，執行鑑別診斷推理並對可能診斷排序。 3. 分流代理：依生命徵象、檢驗結果與既定評分系統（ESI、NEWS2）計算緊急度。 4. 治療代理：存取藥物交互資料庫、NIH/WHO 指南，綜合過敏、禁忌與共病生成個人化治療計畫。 5. 協調代理：負責工作流編排、記憶同步、角色交接與稽核日誌。 記憶層採雙層設計：短期記憶以 Redis 暫存互動期的易變病患資料；長期記憶以 Neo4j 保存結構化病例歷程與決策日誌，支援回溯分析與追蹤。代理間通訊採用 OpenAI Agentic SDK 的 Model Context Protocol (MCP)，訊息附帶角色元資料與病患情境以確保無縫切換。工具整合方面，系統透過 FHIR 實現 EHR 互通，採用檢索增強生成（RAG）查詢 PubMed 等醫學文獻庫，並整合 Infermedica 等第三方臨床工具輔助症狀檢核與早期鑑別診斷。 評估使用合成資料集，涵蓋五大診斷類別（呼吸窘迫、腹痛、胸痛、神經缺損、老人多重用藥），共 150 筆獨特病例，並由臨床醫師審查確保真實性。評估流程分四階段：病例模擬完整管線、三位專科醫師盲測評分、與規則型 CDSS 基線比較、壓力測試邊界案例。指標包含診斷準確率、分流精確度、治療有效性、端到端延遲（秒）與醫師滿意度（李克特 1–5 分），並以雙尾 t 檢定（α=0.05）驗證顯著性。

## 結果
代理式 AI 系統在所有指標均優於傳統 CDSS。診斷準確率 0.924 對 0.841；分流精確度 0.952 對 0.876；治療有效性 0.905 對 0.833；平均延遲 3.7 秒對 6.2 秒（降低 40%）；醫師滿意度 4.6/5 對 3.8/5。案例研究顯示一名 56 歲男性胸痛伴呼吸困難，系統在 4 秒內完成從症狀擷取、鑑別診斷（不穩定型心絞痛、肺栓塞、GERD）、ESI Level 2 分流到建議心電圖、肌鈣蛋白檢測與阿斯匹靈啟始，經醫師確認適當。定性上，系統在模糊症狀與共病情境展現更佳適應力與推理細緻度。

## 限制與展望
本研究假設輸入資料品質高，實際部署需面對不完整、雜訊資料與異構 EHR 介面的互通性差異。目前代理技能與知識庫針對五大類別設計，擴展至腫瘤、精神科等專科需新增領域特定代理與知識庫。未來工作包括：多模態推理（影像、基因組）、聯邦學習以保護隱私進行模型更新、面向病患的對話代理支援共同決策，以及在資源受限或緊急情境下的韌性增強。倫理層面仍需持續強化可解釋性、稽核追蹤與人工覆核機制，以避免自動化偏誤。
