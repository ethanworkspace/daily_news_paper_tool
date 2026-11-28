# 論文 02：The accuracy-safety trade-off of large reasoning models in clinical diagnostics.

- 日期：2026-10-30
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
臨床診斷中大型推理模型（LRM）與標準大型語言模型（LLM）的效能與安全性權衡尚未充分量化。現有研究多聚焦單一模型或短文本場景，缺乏基於真實電子健康紀錄（EHR）的長文本、多專科基準測試，難以系統評估誤診率、重現性與鑑別診斷品質。本研究構建 AIMS-LDR 基準，涵蓋六組配對模型與十二個專科，旨在量化 LRM 與 LLM 在主要診斷準確度、假陽性比率、重現性及鑑別診斷臨床相關性上的差異，並提出結構化醫師協作模式以緩解安全性風險，為臨床部署前的前瞻性驗證提供實證基礎。

## 方法
問題設定：輸入為長文本 EHR 病例，輸出為主要診斷與鑑別診斷列表。方法核心包含三階段：(1) 基準建構：AIMS-LDR 從真實 EHR 抽取病例，涵蓋 12 專科，設計六組 LRM-LLM 配對模型（架構、參數量相近），確保比較公平性。(2) 評估範式：採用多種提示詞設計、模型超參數設定與評估指標（主要診斷準確率、假陽性率、重現性、鑑別診斷臨床相關性），跨範式驗證權衡穩健性。(3) 結構化協作模式：LRM 負責擴展診斷覆蓋面（生成廣泛鑑別），臨床醫師負責驗證可靠性（篩選與確認），形成人機協同決策流程。實驗在 15 位醫師參與的回顧性驗證研究中執行，測量協作前後的準確率與假陽性變化。摘錄未提供模型架構細節、訓練目標、損失函數或推論算法等技術內容，故無法進一步說明核心模組機制。

## 結果
主要結果顯示：LRM 相較 LLM 產生超過 34% 更多假陽性診斷，重現性降低約 40%，但主要診斷準確度較高且鑑別診斷更具臨床相關性。此權衡在不同提示詞、超參數與評估範式下均一致。結構化醫師協作模式在 15 位醫師驗證中，使診斷準確率提升 20%，假陽性降低 44%。所有結果基於受控回顧性條件取得。

## 限制與展望
研究限制：(1) 僅回顧性受控驗證，缺前瞻性臨床試驗；(2) 僅 15 位醫師參與，樣本量小，泛化性受限；(3) AIMS-LDR 建構細節（病例選取、專科分布、指標定義）未完整揭露，難評估代表性；(4) 未報告模型訓練資料、架構差異與推論成本，機制解釋受限；(5) 協作模式的臨床工作流整合、醫師認知負荷與法律責任尚待探討。後續需前瞻性多中心驗證、擴大醫師樣本、公開基準細節並評估部署可行性。
