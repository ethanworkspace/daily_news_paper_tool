# 論文 05：Implementing a Cognitively Grounded Artificial Moral Advisor: A Multi-LLM Multi-Agent Approach Based on the Cognitive-Reflective Equilibration Model.

- 日期：2026-09-15
- 來源層級：Tier 2
- 期刊/會議/來源：Journal of Intelligence
- Venue：Journal of Intelligence
- 發布時間：2026-09-02T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42783572/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13608209/
- DOI：10.3390/jintelligence14090212
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1943（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Large language model (LLM)-based artificial intelligence is increasingly used in ethically consequential human decision-making, yet fully autonomous machine ethics remains unrealistic, motivating architectures that support rather than replace human ethical judgment. This study introduces the Cognitive-Reflective Equilibration Architecture (CREA), a cognitively grounded artificial moral advisor that operationalizes the Cognitive-Reflective Equilibration Model (CREM), in which reflective reasoning guides ethical judgment from intuitive cognition toward a more advanced equilibrium among competing values, drawing on Piaget and Rawls. CREA implements CREM's 20-step process through four stage-aligned reasoning agents-Cognitive, Reflective, Equilibration, and Evaluation-coordinated via multi-LLM orchestration, in which auxiliary models independently explore principles, generate counterarguments, and score supporting and opposing considerations to externalize reflective deliberation. The architecture was empirically evaluated by comparing four configurations-single-agent, multi-agent, multi-LLM, and multi-LLM with knowledge- and reasoning-bank augmentation-across four indicators of advice quality using 500 matched execution units per configuration. All comparisons are system-internal: advice quality was scored by CREA's own multi-LLM measurement pipeline rather than by human ethicists, so the findings reflect relative differences among architectures under LLM-based self-evaluation, not normative validity. Within that scope, distributing reflective reasoning across multiple models was associated with higher reason-giving (justifiability) and normative-alignment scores relative to simpler configurations. CREA therefore offers an empirically characterized, auditable advisor architecture whose potential to scaffold human ethical judgment remains a hypothesis for user-centered validation rather than a demonstrated outcome.

## 背景與目的
大型語言模型（LLM）已廣泛介入具倫理後果的人類決策，但完全自主的機器倫理仍不切實際，亟需輔助而非取代人類倫理判斷的架構。現有方法缺乏認知科學基礎的反思平衡機制，難以將直覺認知引導至價值競爭的高階平衡。本研究旨在建構認知基礎的人工道德諮詢架構（CREA），將認知反思平衡模型（CREM）的 20 步驟流程具體化，透過多 LLM 多代理協作外顯化反思審議，提供可稽核、經實證特徵化的諮詢系統，為後續以使用者為中心的驗證奠定基礎。

## 方法
問題設定：輸入為倫理決策情境，輸出為包含理由給予、規範對齊等指標的建議品質評分。整體架構包含四個階段對齊的推理代理——認知、反思、平衡、評估——透過多 LLM 編排協調。核心模組：輔助模型獨立探索原則、生成反駁論點、對支持與反對考量進行評分，將反思審議外部化。資料表示：採用 500 個匹配執行單元，每單元對應一個決策情境，四種配置（單代理、多代理、多 LLM、多 LLM 加知識與推理庫）各自獨立執行。訓練目標與損失函數：摘錄未提及訓練階段、損失函數或最佳化策略，系統屬推理階段架構。推理流程：依 CREM 20 步驟依序經認知代理提取直覺判斷、反思代理生成原則與反駁、平衡代理整合競爭價值達致平衡、評估代理對理由給予與規範對齊打分。關鍵差異：將反思推理分散至多個 LLM 並引入知識/推理庫增強，相較單一代理或無增強的多代理配置，能更充分外顯化審議過程。

## 結果
摘錄未提供可驗證數字。定性結論顯示，將反思推理分散於多個模型的配置，在理由給予（正當性）與規範對齊兩項指標上顯著優於較簡單的配置。所有比較均為系統內部自我評估，由 CREA 自身的多 LLM 測量管線打分，未經人類倫理學家驗證，故結果僅反映架構間在 LLM 自我評估下的相對差異，不具規範效度。

## 限制與展望
評估僅依賴系統內部的多 LLM 自我評分管線，缺乏人類專家或真實使用者的外部驗證，發現僅限於相對架構差異，無法推論規範有效性。實驗僅涵蓋四種配置、500 執行單元，未與外部基準比較，泛化能力未知。知識與推理庫的具體構建細節、檢索機制未揭露。CREA 輔助人類倫理判斷的潛力仍屬假設，需後續以使用者為中心的研究驗證。部署風險包含自我評估偏誤放大、缺乏可解釋性保證。
