# 論文 03：The accuracy-safety trade-off of large reasoning models in clinical diagnostics.

- 日期：2026-11-20
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
大型推理模型（LRM）在臨床診斷上被期望優於標準大型語言模型（LLM），但其效用與安全性仍不明確。現有方法多聚焦於單一模型表現，缺乏系統性基準測試以量化準確度與安全性的權衡。本研究構建 AIMS-LDR 長文本診斷推理基準，基於真實電子健康記錄，涵蓋 12 專科與六組配對模型，旨在揭示 LRM 與 LLM 在主要診斷準確度、鑑別診斷相關性、假陽性率與可重現性上的差異，並提出結構化醫師協作模型以緩解風險，為臨床決策支援提供實證依據。

## 方法
問題設定為長文本臨床診斷推理，輸入為真實電子健康記錄（EHR），輸出為主要診斷與鑑別診斷列表。系統整體包含：(1) AIMS-LDR 基準建構：從真實 EHR 抽取長文本病例，涵蓋 12 專科，設計標準化評估協議。(2) 模型配對：選擇六組 LRM 與其對應 LLM 同源模型，確保架構與訓練數據可比性。(3) 評估範式：採用多種提示詞設計、模型超參數與評估指標（主要診斷準確度、鑑別診斷臨床相關性、假陽性率、可重現性）進行跨條件驗證。(4) 結構化協作模型：LRM 負責擴展診斷覆蓋（生成廣泛鑑別），臨床醫師負責驗證可靠性（篩選假陽性），形成人機協同流程。(5) 驗證研究：招募 15 位醫師於回顧性病例上測試協作模型。核心差異在於引入醫師驗證機制，將 LRM 的高覆蓋特性與人類專業判斷結合，以降低假陽性並提升整體準確度。資料前處理、特徵表示、訓練目標與損失函數等細節於摘錄中未說明。

## 結果
實驗顯示 LRM 相較 LLM：主要診斷準確度更高、鑑別診斷臨床相關性更強，但假陽性診斷增加超過 34%，可重現性降低約 40%。此權衡在不同提示詞、超參數與評估範式下均一致存在。結構化協作模型於 15 醫師驗證研究中，使診斷準確度提升 20%，假陽性減少 44%。摘錄未提供可驗證的基線模型名稱、各專科細分數字、統計顯著性檢定結果，亦未報告消融實驗細節。定性結論為：LRM 擴展診斷廣度但引入噪聲，醫師驗證可有效抑制假陽性並保留準確度增益。

## 限制與展望
研究限制包括：(1) 僅在回顧性、受控條件下驗證，缺乏前瞻性臨床試驗證據，部署風險未充分評估。(2) 基準僅涵蓋 12 專科與六組模型配對，泛化性有待擴展。(3) 醫師驗證研究樣本量小（15 人），可能存在選擇偏誤與主觀差異。(4) 未探討不同嚴重度疾病、罕見病或多重合併症場景下的表現。(5) 模型內部推理過程透明度、不確定性量化與可解釋性未深入分析。後續研究應進行前瞻性多中心驗證、擴大專科與模型覆蓋、量化醫師認知負荷、建立動態監測機制，並探討倫理法律責任歸屬。
