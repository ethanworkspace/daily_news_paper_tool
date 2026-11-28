# 論文 03：The accuracy-safety trade-off of large reasoning models in clinical diagnostics.

- 日期：2026-11-17
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-29T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43099011/
- PDF：
- DOI：10.1038/s41467-026-78520-x
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1156（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Large reasoning models (LRMs) offer potential advantages for clinical diagnosis over standard large language models (LLMs), yet their utility and safety remain unclear. Here we show, on AIMS-LDR, a long-context diagnostic reasoning benchmark built upon real-world electronic health records, covering six matched model pairs and 12 specialties, that LRMs generate over 34% more false positive diagnoses and show approximately 40% lower reproducibility than their LLM counterparts, while making more accurate primary diagnoses and more clinically relevant differentials. Experiments confirm this trade-off across prompt designs, model hyperparameters, and evaluation paradigms. A structured collaboration model, in which the LRM broadens diagnostic coverage and the clinician verifies reliability, increases diagnostic accuracy by 20% and reduces false positives by 44% in a 15-physician validation study. These results, obtained under controlled retrospective conditions, suggest that pairing LRM reasoning with physician oversight may support safer and more accurate diagnostic decision-making, warranting prospective validation before clinical deployment.

## 背景與目的
大型推理模型（LRM）在臨床診斷上被期望優於標準大型語言模型（LLM），但其效用與安全性仍不明確。現有研究缺乏系統性、長文脈、真實電子病歷為基礎的基準來量化兩者在主要診斷準確度、鑑別診斷相關性、假陽性率與可重現性上的差異。本文旨在於 AIMS-LDR 基準上，針對六組配對模型、涵蓋 12 個專科，全面評估 LRM 與 LLM 的診斷表現，並提出結構化醫師協作模式以緩解準確度與安全性的權衡，提供部署前的實證依據。

## 方法
研究設定為長文脈診斷推理任務，輸入為真實電子病歷文本，輸出為主要診斷與鑑別診斷清單。建立 AIMS-LDR 基準，包含 12 專科、六組配對的 LRM 與 LLM（相同架構、參數量但訓練目標不同），以確保公平比較。評估指標涵蓋主要診斷準確率、鑑別診斷臨床相關性、假陽性診斷比例、以及跨重複推理的一致性（可重現性）。實驗設計包括：(1) 多種提示詞設計（零樣本、少樣本、思維鏈）；(2) 模型超參數變化（溫度、top‑p、生成長度）；(3) 不同評估範式（單次推理、多次聚合）。核心協作模式採雙階段流程：第一階段 LRM 生成廣泛鑑別清單以擴大覆蓋；第二階段臨床醫師依專業判斷驗證並篩選，形成最終診斷。驗證研究招募 15 位醫師，於回顧性病例上進行盲測，記錄準確度與假陽性變化。所有實驗在受控回顧環境執行，確保資料洩漏風險最小。

## 結果
在 AIMS-LDR 上，LRM 的主要診斷準確度優於 LLM，鑑別診斷臨床相關性亦較高，但假陽性診斷增加超過 34%，可重現性下降約 40%。此準確度與安全性的權衡在各類提示詞、超參數與評估範式中均一致出現。結構化醫師協作模式於 15 醫師驗證中，使診斷準確度提升 20%，假陽性降低 44%。摘錄未提供可驗證的絕對數值（如基準準確率、AUC 等），僅呈現相對百分比改善。

## 限制與展望
研究僅在回顧性、受控環境與單一基準（AIMS-LDR）上進行，病例多樣性、時間漂移與真實臨床工作流程未被涵蓋。驗證樣本僅 15 位醫師，統計功效有限，且未評估不同經驗層級醫師的效果差異。模型配對數量與專科覆蓋雖具代表性，但無法推廣至所有臨床領域或更大規模模型。未來需進行前瞻性、多中心、真實部署研究，並探討協作介面設計、醫師認知負荷與法律責任分配等問題。
