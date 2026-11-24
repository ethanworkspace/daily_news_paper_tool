# 論文 05：Implementing a Cognitively Grounded Artificial Moral Advisor: A Multi-LLM Multi-Agent Approach Based on the Cognitive-Reflective Equilibration Model.

- 日期：2026-09-14
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
大型語言模型（LLM）已廣泛介入具倫理影響的人類決策，但完全自主的機器倫理仍不切實際，現有方法缺乏能輔助而非取代人類倫理判斷的架構。本研究提出認知反思平衡架構（CREA），將認知反思平衡模型（CREM）具體化，依據皮亞傑與羅爾斯理論，讓反思推理引導倫理判斷從直覺認知走向多價值競爭下的進階平衡。研究目標在建構可審計、經實證特徵化的道德諮詢架構，貢獻在於以多 LLM 多代理協作外顯化反思審議，並提供系統內部的相對品質比較基準。

## 方法
問題設定：輸入為需倫理判斷的情境，輸出為具理由支撐的道德建議。整體架構：CREA 依 CREM 的 20 步驟流程，部署四個階段對齊的推理代理——認知、反思、平衡、評估，透過多 LLM 編排協調。核心模組：輔助模型獨立探索原則、生成反駁論點、對支持與反對考量評分，以外顯化反思審議。資料表示：摘錄未說明具體前處理、特徵或表示方式。訓練目標與損失：摘錄未提及訓練階段、損失函數或最佳化策略，推測為基於提示的零樣本推論。推論流程：四代理依序處理，經多 LLM 管線評分建議品質。關鍵差異：將反思推理分散至多模型協作，並引入知識與推理庫增強，區別於單代理或單一 LLM 基線。

## 結果
實驗比較四種配置（單代理、多代理、多 LLM、多 LLM 加知識與推理庫），每配置 500 個匹配執行單元，以四項建議品質指標評估。摘錄未提供可驗證數字。定性結論：將反思推理分散於多模型協作，在理由給予（正當性）與規範一致性分數上顯著優於較簡單配置；但所有比較皆為系統內部自我評估，未經人類倫理學家驗證，僅反映架構間相對差異，不代表規範效度。

## 限制與展望
評估僅限系統內部 LLM 自我評分，缺乏人類專家與真實用戶驗證，規範效度未證；20 步驟細節與代理內部機制未公開，難以複現；資料集來源、情境多樣性與泛化能力未說明；潛在風險包括 LLM 評分偏誤、反思過程透明度不足；後續研究需進行以用戶為中心的實證驗證，並探討部署於真實決策情境的可行性與倫理風險。
