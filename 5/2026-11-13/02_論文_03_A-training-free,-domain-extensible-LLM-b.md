# 論文 03：A training-free, domain-extensible LLM-based approach for automated extraction of standardized preparation procedures.

- 日期：2026-11-13
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-29T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43099016/
- PDF：
- DOI：10.1038/s41467-026-78605-7
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1148（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Millions of synthesis procedures have been published, but their meta-analysis, important for identifying successful synthesis patterns, is difficult due to varied reporting structures. Using this information requires converting unstructured text into a precise sequence of actions, which requires understanding domain jargon, a challenge usually addressed by fine-tuning models on labeled data. We present a simple, training-free workflow for laboratory action extraction that works across fields, encoding domain knowledge through explicit action sets and using powerful, readily available Large Language Models, or LLMs. Applied to zeolite synthesis, a widely used class of porous materials, our approach outperforms existing open-source tools and delivers context-aware results with open, locally runnable LLMs. It also matches state-of-the-art, field-specific models in their own domains, highlighting the generalization capabilities of current LLMs. The methodology showcased, along with the open algorithms made available, allow chemists to evaluate action sets, screen LLMs, and digitize laboratory procedures accurately with minimal effort.

## 背景與目的
背景與目的：文獻中存在數百萬篇合成程序，但因報告結構多樣，難以進行大規模元分析以發現成功合成模式。現有方法通常需在標註資料上微調模型以理解領域術語，成本高且難以跨領域推廣。本研究旨在提出一個免訓練、可跨領域擴展的工作流程，利用明確的動作集合編碼領域知識，並結合現成的大型語言模型（LLM），實現實驗室操作的自動化抽取與標準化，降低化學家數位化文獻的門檻。此工作流程不需任何標註資料即可部署，透過提示工程引導 LLM 依照預先定義的動作集合輸出結構化步驟，並可在本地端運行開源模型，保護資料隱私。

## 方法
方法：問題設定為從非結構化的實驗室合成文本中抽取標準化的操作序列。輸入為原始論文段落或實驗記錄，輸出為依預先定義動作集合排序的結構化步驟（如「加入」、「攪拌」、「加熱」、「過濾」等）。整體架構包含三大模組：(1) 動作集合建構模組，由領域專家列舉該領域常見操作並賦予唯一識別碼，作為 LLM 的輸出標籤空間；(2) 提示工程模組，將輸入文本與動作集合說明組合成提示詞，引導 LLM 逐句判斷並輸出對應動作標籤與參數；(3) 後處理與驗證模組，將 LLM 回傳的標籤序列進行格式檢查、參數單位統一與邏輯一致性檢查。資料前處理僅進行斷句、去除多餘空白與特殊符號，不進行特徵工程。本方法為免訓練範式，無損失函數與梯度優化，直接呼叫開源或商業 LLM 進行推論；推論流程為單輪或多輪對話，視提示長度而定。與既有微調式方法的關鍵差異在於：不需標註資料、可透過修改動作集合快速遷移至新領域、可在本地端運行開源模型保護隱私。摘錄未提供具體提示詞範例、動作集合大小、LLM 選型細節或推論超參數。

## 結果
結果：作者在沸石合成領域測試，發現該免訓練工作流程優於現有開源工具，並能與該領域最先進的專用模型表現相當，且在本地端開源 LLM 上仍能產出具上下文感知的結構化步驟。摘錄未提供可驗證的數值指標（如精確率、召回率、F1），僅以定性描述說明泛化能力。此外，開放的演算法讓化學家能自行評估動作集合、篩選適合的 LLM，並以極低人力成本完成大量文獻的數位化。雖然缺乏量化基準，但定性結果顯示該方法具備跨領域擴展潛力。

## 限制與展望
限制與展望：僅在沸石合成單一領域驗證，未涵蓋其他材料或化學合成類型；動作集合品質高度依賴專家知識，若定義不完整將影響抽取完整性；LLM 推論結果具隨機性，缺乏系統性不確定性量化；評估僅以定性比較為主，缺乏標準化基準與統計顯著性測試；後續研究可擴展至多領域基準、引入自動動作集合學習、探討提示詞優化與模型蒸餾以降低部署成本。
