# 論文 02：Multi-Agent collaboration as a complementary architecture for AI-generated medical examination items.

- 日期：2026-09-15
- 來源層級：Tier 2
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
本研究針對醫學考試題目自動生成任務，指出單一大型語言模型雖能產出可接受的知識型題目，但在高階推理題目上表現不足，歸因於架構限制。現有方法多採單一模型端到端生成，缺乏結構化的起草、審閱與迭代修正機制，導致題目品質難以達到專業考試標準。本文提出多代理協作架構，將題目開發分解為專門代理負責起草、評論與迭代對抗式修正，旨在透過架構創新突破單一模型極限，為AI輔助醫學出題提供可行路徑。

## 方法
問題設定：輸入為醫學知識主題或大綱，輸出為符合國家醫師資格考試標準的選擇題項目。整體架構採多代理協作系統，包含三大核心角色：起草代理負責根據輸入生成初版題目；評論代理對題目進行批判性審查，檢查醫學正確性、推理深度、干擾項品質等；迭代對抗式修正機制讓兩代理多輪交互，評論代理指出缺失，起草代理據以修訂，直至滿足品質門檻。核心演算機制在於將單一模型的單通道生成拆解為專業分工與對抗優化流程，模擬人類出題專家的審閱修訂循環。資料前處理與特徵表示方式、具體模型骨幹、訓練目標、損失函數、最佳化策略、推論時的輪數控制與停止條件，摘錄均未提供。與既有單一模型基線的關鍵差異在於引入專門化代理分工與多輪對抗修正，而非單次生成。

## 結果
在中國國家醫師資格考試的盲測評估中，多代理系統產出的題目獲得專家偏好 57.7%，單一模型基線為 42.3%，顯示多代理協作在專家評價上具優勢。作者結論此架構為突破 AI 輔助出題當前極限的可行路徑。摘錄未提供可驗證數字如評測題目總數、參與專家人數、統計檢定細節、自動化指標或消融實驗結果，僅能觀察到定性結論：多代理輸出在專家盲測中被更傾向選擇。

## 限制與展望
資料限制：僅在中國國家醫師資格考試情境驗證，其他考試體系泛化性未知。方法細節缺失：代理具體模型架構、提示詞設計、迭代輪數上限、計算成本未揭露，難以復現。評估局限：僅採專家偏好單一指標，缺乏自動化品質指標、心理測驗屬性分析，樣本量與統計效力未報告。潛在風險：多代理迭代可能放大幻覺、引入系統性偏誤，對抗過程收斂性無保證。後續方向：擴展至更多考試類型、引入心理測驗模型輔助評估、研究代理角色組合影響、建立自動化評估基準。
