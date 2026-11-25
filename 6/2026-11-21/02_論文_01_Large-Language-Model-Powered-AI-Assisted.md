# 論文 01：Large Language Model-Powered AI-Assisted Simulated Patient for Nursing Education: Quasi-Experimental Study.

- 日期：2026-11-21
- 來源層級：Tier 2
- 期刊/會議/來源：JMIR nursing
- Venue：JMIR nursing
- 發布時間：2026-11-19T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43068358/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13784698/
- DOI：10.2196/98543
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2512（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
BACKGROUND: Large language model (LLM)-powered virtual patient systems are gaining popularity in nursing education but also face persistent challenges, such as hallucinations and role inconsistency. OBJECTIVE: This paper reports the model architecture design, technical considerations, implementation challenges, and evaluation of an LLM-powered AI-assisted simulated-patient system integrated into a nursing triage simulation game. METHODS: The system integrated a Unity-based game client, with GPT-4o hosted through Microsoft AI Foundry to support real-time simulated-patient dialogue in Traditional Chinese using Cantonese syntax. This developmental study comprised exploratory model selection, formative student feedback-informed enhancement from Version 1 to Version 2, development-stage script-fidelity evaluation, and evaluation of system usability and the Net Promoter Score in 2 tutorial cohorts of nursing students. RESULTS: Key technical contributions include a layered hallucination mitigation architecture that combines grounded prompt inclusion, few-shot conversational exemplars, negative role constraints, and calibrated model parameters. In the predefined script-fidelity evaluation, script-inconsistent responses occurred in 78 of 125 (62.4%) Version 1 outputs and 21 of 125 (16.8%) Version 2 outputs-an absolute difference of 45.6 percentage points. The implementation process also addresses stateless API memory management, cloud-based safety filter calibration for domain-specific clinical prompts, and prompt engineering strategies to prevent role drift and hidden scenario information leakage. GPT-4o was selected as the production model through exploratory development testing that considered script consistency, Cantonese-language suitability, response latency, technical reliability, deployment feasibility, cost considerations, and Unity integration compatibility; 45 of 50 (90%) assessed GPT-4o responses were rated fully script-consistent. CONCLUSIONS: This study demonstrates the development and real-world tutorial deployment of a Cantonese-language, LLM-powered simulated-patient system for nursing triage education. Integrating formative student feedback with structured technical debugging enabled iterative refinement of dialogue fidelity, role consistency, protected-information handling, and game interaction functions. The resulting Version 2 system provides a practical, contextually tailored approach to supporting scalable simulated-patient dialogue in nursing education.

## 背景與目的
大型語言模型（LLM）驅動的虛擬病患系統在護理教育中日益普及，但仍面臨幻覺與角色不一致等持續性挑戰。本研究旨在報告一個整合於護理分流模擬遊戲中的 LLM 輔助模擬病患系統之模型架構設計、技術考量、實作難點與評估，期望透過結構化技術除錯與學生回饋迭代優化，提升對話保真度、角色一致性、受保護資訊處理與遊戲互動功能，為可擴展的護理模擬病患對話提供實務導向的解決方案。

## 方法
系統架構包含 Unity 遊戲客戶端與透過 Microsoft AI Foundry 託管的 GPT-4o，支援以繁體中文並採用廣東話語法的即時模擬病患對話。開發流程分四階段：(1) 探索性模型選擇，依腳本一致性、廣東話適用性、回應延遲、技術可靠性、部署可行性、成本與 Unity 整合相容性綜合評估，最終選定 GPT-4o；(2) 依學生形成性回饋從 Version 1 迭代至 Version 2；(3) 開發階段腳本保真度評估；(4) 於兩組護理學生教學班群進行系統可用性與淨推薦值（NPS）評估。核心技術貢獻為分層幻覺緩解架構，結合：(a) 接地提示詞納入，(b) 少樣本對話範例，(c) 負向角色約束，(d) 校準模型參數。另解決無狀態 API 記憶體管理、雲端安全過濾器對臨床領域提示詞的校準、防止角色漂移與隱藏情境資訊洩漏的提示詞工程策略。推論流程為：遊戲客戶端發送使用者輸入至 GPT-4o，經分層提示詞處理後回傳回應，再由 Unity 顯示於模擬病患介面。

## 結果
預定義腳本保真度評估顯示，Version 1 出現 78/125（62.4%）腳本不一致回應，Version 2 降為 21/125（16.8%），絕對差異 45.6 個百分點。探索性測試中，GPT-4o 經評估的 50 條回應有 45 條（90%）被判定為完全腳本一致。可用性與 NPS 於兩組教學班群收集，摘錄未提供可驗證數字，但定性結論指出迭代優化後對話保真度、角色一致性、受保護資訊處理與遊戲互動功能均顯著改善。

## 限制與展望
研究僅在兩組教學班群進行小規模部署，樣本數有限，難以推廣至更大或不同文化語言環境；系統依賴專有 GPT-4o 且透過雲端服務，成本、延遲與資料隱私為潛在風險；無狀態 API 限制長對話記憶，可能影響多輪臨床情境連貫性；安全過濾器校準可能誤攔合理臨床提示詞；未進行長期學習成效追蹤，亦缺乏與其他開源或商用模型的直接比較。後續研究可擴大樣本、引入多語言支援、探討本地化部署與長期教學效益評估。
