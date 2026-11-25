# 論文 04：AI Assistance in Medical Decision-Making: The Role of Recommendations and Explanations in Simulated Clinical Cases

- 日期：2026-10-24
- 來源層級：Tier 1
- 期刊/會議/來源：ACM Transactions on Computing for Healthcare
- Venue：ACM Transactions on Computing for Healthcare
- 發布時間：2026-10-24T00:00:00+00:00
- URL：https://doi.org/10.1145/3788685
- PDF：
- DOI：10.1145/3788685
- arXiv：
- 影響指標：2yr_mean_citedness=7.04, h_index=38, i10_index=156 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: ACM Transactions on Computing for Healthcare
- 引用數：4
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1386（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Healthcare is a sector that can greatly benefit from AI due to the critical nature of medical decisions and the demand for accuracy and efficiency. Advances in AI algorithms have shown promise in diagnosing conditions at early stages. To improve the transparency of such systems, Explainable AI (XAI) techniques have been explored. However, if not properly integrated, AI and XAI can introduce new challenges, such as reduced cognitive engagement or overreliance on AI-system outputs. While prior research has mainly focused on isolated tasks, such as AI-assisted diagnosis, this study takes a holistic approach by examining the impact of AI recommendations and explanations across multiple sequential decision points within clinical case scenarios. Thirty-four medical students completed two simulated clinical cases with varying levels of AI assistance. The scenarios reflected realistic workflows, requiring participants to prescribe diagnostic exams and make final diagnoses. Results indicate that AI recommendations and explanations can enhance medical performance but do not consistently improve efficiency. In simpler cases, AI assistance supported appropriate exam prescription and reduced decision-making time. In more complex cases, explanations significantly improved diagnostic accuracy but also led to higher resource use, with participants ordering more unnecessary exams.

## 背景與目的
醫療決策關鍵且需兼顧準確與效率，AI 演算法在早期診斷展現潛力，惟若缺乏透明度易導致認知投入降低或過度依賴。既有研究多聚焦單一診斷任務，缺乏對臨床連續決策點的整體探討。本研究旨在模擬真實臨床流程，檢視 AI 推薦與可解釋 AI（XAI）說明在多階段決策（處方檢查與最終診斷）中的影響，填補整體工作流層面的實證缺口。

## 方法
問題設定為模擬臨床案例的連續決策任務：輸入為病人基本資料、病史與初步檢查結果；系統提供兩種 AI 輔助層級——（1）僅給出檢查建議與診斷推薦，（2）在建議之外附加 XAI 產生的解釋（如特徵重要度或規則說明）。輸出為參與者開立的檢查項目清單與最終診斷。研究招募 34 位醫學生，各完成兩個複雜度不同的模擬案例，案例設計反映真實臨床工作流，要求依序決定檢查處方與確診。核心模組包含 AI 推薦引擎與 XAI 解釋生成器，但摘錄未揭露其架構、訓練資料、損失函數或最佳化策略。推論流程為參與者閱讀案例、查看 AI 輸出、決定檢查、再查看更新後的 AI 輸出、給出最終診斷。與既有方法的關鍵差異在於採用整體、多決策點的實驗設計，而非單一診斷任務；然而，關於模型結構、特徵表示、訓練目標等技術細節，依目前可取得資料，無法確認。

## 結果
作者報告 AI 推薦與解釋能提升醫療表現，但不穩定改善效率。較簡單案例中，AI 協助使檢查處方更恰當並縮短決策時間；較複雜案例中，解釋顯著提高診斷準確率，卻也導致資源使用增加，參與者開立更多非必要檢查。摘錄未提供可驗證數字，僅能觀察到上述定性趨勢。

## 限制與展望
樣本僅 34 位醫學生，缺乏真實醫師與臨床環境驗證，外推性有限；模擬案例無法完整反映真實病人變異與時間壓力；AI 系統架構、訓練資料、XAI 方法未揭露，難以評估可重現性與偏誤風險；未測量長期學習效果、信任度變化或患者預後影響。後續研究需擴大樣本、引入真實臨床場景、公開模型細節並進行長期追蹤。
