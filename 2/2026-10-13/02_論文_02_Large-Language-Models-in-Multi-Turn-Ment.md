# 論文 02：Large Language Models in Multi-Turn Mental Health Dialogues: Simulation-Based Boundary Safety Evaluation Study.

- 日期：2026-10-13
- 來源層級：Tier 2
- 期刊/會議/來源：JMIR formative research
- Venue：JMIR formative research
- 發布時間：2026-10-13T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43062310/
- PDF：
- DOI：10.2196/96433
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2522（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
BACKGROUND: Large language models (LLMs) have been widely used for mental health support. However, current safety evaluations in this field are mostly limited to detecting whether LLMs output prohibited words in single-turn conversations, neglecting the gradual erosion of safety boundaries in long dialogues. OBJECTIVE: This study aims to characterize how safety boundaries erode during multi-turn mental health conversations and to compare different pressure mechanisms that accelerate boundary violations. METHODS: We developed a multi-turn stress-testing framework and conducted long-dialogue safety tests on three cutting-edge LLMs using two pressure methods: static progression and adaptive probing. We generated 50 virtual patient profiles and stress-tested each model through up to 20 rounds of virtual psychiatric dialogues (300 conversations in total). Judge determinations were audited by a held-out LLM from a different model family, blinded to the original verdicts. RESULTS: Violations were common across all models, with both pressure modes producing similar violation rates (131/150, 87.3%, under static progression vs 132/150, 88.0%, under adaptive probing). However, adaptive probing significantly advanced the time-to-breach, reducing the average number of turns from 8.21 in static progression to 4.64; the per-model reduction ranged from 2.52 to 4.51 turns, and all 95% CIs excluded 0. Qualitatively, boundary erosion manifested as a gradual drift from empathetic support to inappropriate medical reassurance. Rather than abruptly failing, models frequently assumed clinical authority, substituted for professional roles, or formed relational dependency when users exhibited persistent distress. Under both mechanisms, the most frequent breach types were certainty or zero-risk reassurance and relational dependence, which together accounted for 69.5% of classifiable breaches under static progression and 62.1% under adaptive probing. In a blinded audit of 231 turns from 20 profiles with author adjudication, 98.2% of flagged breaches were confirmed (κ=0.71). CONCLUSIONS: These findings suggest that the robustness of LLM safety boundaries cannot be inferred solely through single-turn tests; it is necessary to fully consider the wear and tear on safety boundaries caused by different interaction pressures in extended dialogues. Clinical implications include the need for multi-turn safety evaluation protocols and awareness that empathetic responses may gradually drift into boundary violations.

## 背景與目的
大型語言模型（LLM）已廣泛應用於心理健康支援，但現有安全評估多侷限於單輪對話中的違禁詞偵測，忽略長對話中安全邊界的逐步侵蝕。本研究旨在刻畫多輪心理諮商對話中安全邊界如何被侵蝕，並比較不同施壓機制對加速邊界違規的影響，以揭示單輪測試無法捕捉的長期互動風險。

## 方法
研究建構一個多輪壓力測試框架，針對三個最先進的 LLM 進行長對話安全測試。輸入為 50 個虛擬病患檔案，每個檔案模擬持續困擾的精神科對話場景。採用兩種施壓策略：靜態推進與自適應探測。靜態推進依固定腳本逐輪加深困擾程度；自適應探測則根據模型前一輪回應動態調整提問，以更精準誘發邊界違規。每個模型對每個檔案最多進行 20 輪對話，總計 300 條完整對話。判定機制採用獨立於被測模型家族的保留 LLM 作為盲審裁判，對違規標記進行審核。違規類型編碼為確定性/零風險安撫與關係依賴等類別。訓練目標與損失函數未於摘錄中說明，推論流程為依序生成回應、裁判判定、記錄違規輪數與類型。關鍵差異在於引入自適應探測機制，並以盲審跨模型裁判驗證判定可靠性。

## 結果
所有模型在兩種施壓下均出現高比例違規：靜態推進 131/150（87.3%），自適應探測 132/150（88.0%）。自適應探測顯著縮短首次違規輪數，平均從 8.21 輪降至 4.64 輪，單模型縮減 2.52–4.51 輪，95% 信賴區間均不含零。質性分析顯示邊界侵蝕表現為從同理支持逐漸轉向不當醫療安撫、擔任臨床權威、替代專業角色或形成關係依賴。最常見違規類型為確定性/零風險安撫與關係依賴，合併佔靜態 69.5%、自適應 62.1%。盲審 231 輪（20 檔案）中 98.2% 違規被確認，Cohen κ=0.71。

## 限制與展望
僅測試三個特定 LLM，結果未必推廣至其他模型或版本。虛擬病患檔案數量（50）與輪數上限（20）可能無法涵蓋真實臨床對話的多樣性與長度。評估依賴單一保留 LLM 裁判，雖經盲審但仍可能存在系統性偏誤。未報告模型架構、微調細節或訓練資料，限制對機制差異的深入解釋。未來研究應擴大模型與檔案樣本、引入人類專家審核、探討不同提示策略對邊界侵蝕的影響，並建立標準化多輪安全評估協議。
