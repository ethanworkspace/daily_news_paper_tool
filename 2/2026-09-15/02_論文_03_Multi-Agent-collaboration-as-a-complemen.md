# 論文 03：Multi-Agent collaboration as a complementary architecture for AI-generated medical examination items.

- 日期：2026-09-15
- 來源層級：Tier 4（一般期刊）
- 期刊/會議/來源：NPJ digital medicine
- Venue：NPJ digital medicine
- 發布時間：2026-09-14T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42736348/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13575248/
- DOI：10.1038/s41746-026-03187-z
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：552（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Qian et al. showed single LLMs can generate acceptable knowledge-based questions but struggle with higher-order reasoning. We argue this is architectural: decomposing item development into specialized agents for drafting, critique, and iterative adversarial refinement improves quality. In blinded evaluation for China's National Medical Licensing Examination, multi-agent outputs received 57.7% of expert preferences, compared with 42.3% for the single-model baseline, indicating a viable path to surpass current limits in AI-assisted item generation.

## 背景與目的
本研究針對 AI 生成醫學考試試題的品質問題，指出單一大型語言模型（LLM）雖能產出可接受的知識型題目，但在高階推理題目上表現不足，歸因於架構限制。現有方法多採單一模型端到端生成，缺乏結構化的起草、評審與迭代修正機制，導致試題深度與準確度受限。本文提出將試題開發分解為專門化代理（起草、評審、迭代對抗修正）的多代理協作架構，旨在透過分工與對抗式優化提升生成品質，為 AI 輔助醫學出題提供可行路徑。

## 方法
問題設定：輸入為醫學考試大綱或知識點，輸出為符合中國國家醫師資格考試標準的選擇題。整體架構採多代理協作流程，包含三大核心模組：(1) 起草代理，負責根據輸入生成初版試題；(2) 評審代理，對初版進行批判性分析，指出邏輯缺口、知識錯誤或不符考試規範之處；(3) 迭代對抗修正機制，讓起草代理根據評審回饋進行多輪修正，直到滿足品質門檻。資料表示方面，試題以結構化文本（題幹、選項、答案、解析）呈現，代理間透過自然語言交換意見。訓練目標與損失函數：摘錄未提供具體最佳化策略、損失函數或模型微調細節。推論流程為：起草→評審→修正→再評審，形成閉環，最終輸出經多輪對抗優化的試題。關鍵差異在於將單一模型的單通道生成拆解為專業分工與迭代對抗，類似人類出題專家團隊的協作模式，但具體代理實現方式（如提示詞設計、模型選擇、停止條件）摘錄未詳細說明。

## 結果
在中國國家醫師資格考試的盲測專家偏好評估中，多代理輸出獲得 57.7% 專家偏好，單一模型基線獲得 42.3%，顯示多代理架構在專家主觀品質判斷上具顯著優勢。摘錄未提供可驗證的量化指標（如準確率、召回率、F1 分數）或統計顯著性檢定結果，僅能觀察到定性結論：多代理協作能有效提升高階推理試題的生成品質，超越單一模型基線。

## 限制與展望
評估範圍僅限於中國國家醫師資格考試，泛化性至其他醫學考試或語言環境尚待驗證；專家偏好屬主觀指標，缺乏客觀品質指標（如醫學準確性、心理測量屬性）支撐；未揭露代理具體模型架構、提示詞工程、迭代輪數上限及計算成本，難以評估部署可行性；潛在風險包含對抗迭代可能產生幻覺放大、評審代理盲點導致系統性錯誤。後續研究需擴大評估基準、引入自動化量化指標、探討代理協作的最佳化策略與安全性機制。
