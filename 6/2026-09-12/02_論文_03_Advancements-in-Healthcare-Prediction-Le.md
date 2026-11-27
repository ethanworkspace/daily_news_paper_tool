# 論文 03：Advancements in Healthcare Prediction: Leveraging Machine Learning Models for Accurate Prognostication

- 日期：2026-09-12
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Journal of Artificial Intelligence and System Modelling
- Venue：Journal of Artificial Intelligence and System Modelling
- 發布時間：2026-09-01T00:00:00+00:00
- URL：https://doaj.org/article/68823cb1984247f6a7686c4c319bac4f
- PDF：
- DOI：10.22034/jaism.2026.583253.1209
- arXiv：
- 影響指標：2yr_mean_citedness=1.59, h_index=7, i10_index=4 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Journal of Artificial Intelligence and System Modelling
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1489（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Healthcare refers to the delivery of health care services through various medical practices for the purposes of preventing, diagnosing, and treating illnesses. The professionals who are involved in delivering healthcare include doctors, nurses, pharmacists, and others. This is usually carried out in various settings such as hospitals, clinics, and community health centers. The main purpose of providing healthcare services is to ensure good health and prevent diseases. There are various means through which healthcare services can be paid for, various political policies affecting healthcare, and various cultural values influencing healthcare. However, the primary objective of this paper is to utilize Machine Learning (ML) models, including Extreme Gradient Boosting Classification (XGBC), Adaptive-boost learning Classifier (ADAC), and Histogram Gradient Boosting Classification (HGBC), in tandem with the Rhizotomy Optimization Algorithm (ROA), for healthcare prediction. In the pursuit of enhancing prediction accuracy, the decision was made to integrate these models with the ROA optimizer. As shown by the results, for the instances with abnormal circumstances, the XGRO algorithm has performed outstandingly, achieving an accuracy of 81.19%, and hence surpassing the XGBC algorithm, which has an accuracy of 79.91%, and also the ADRO algorithm with an accuracy of 79.31%. This shows the effectiveness of hybrid machine learning algorithms coupled with optimization techniques.

## 背景與目的
本研究針對醫療預測問題，旨在提升對異常健康狀況的分類準確度。現有機器學習模型（如極端梯度提升分類器 XGBC、自適應提升分類器 ADAC、直方圖梯度提升分類器 HGBC）在醫療資料上表現有限，缺乏有效的超參數或結構優化機制。本文提出將根莖優化演算法（Rhizotomy Optimization Algorithm, ROA）與上述三種提升模型結合，形成混合演算法（如 XGRO、ADRO 等），以優化模型參數並增強預測能力。研究目標在於驗證混合優化策略是否能顯著提升醫療預測準確度，並為臨床決策支援提供更可靠的工具。

## 方法
問題設定：將醫療預測視為二元分類任務，輸入為患者相關特徵（摘錄未具體說明特徵類型、數量及前處理方式），輸出為正常與異常狀況標籤。模型架構：採用三種梯度提升分類器（XGBC、ADAC、HGBC）作為基礎學習器，並引入根莖優化演算法（ROA）進行參數優化。核心機制：ROA 為一種元啟發式優化演算法，模擬植物根莖生長特性以搜尋最優超參數組合（如學習率、樹深度、迭代次數等），但摘錄未揭露 ROA 具體數學公式、搜尋空間定義、適應度函數設計，亦未說明是否對模型結構進行聯合優化。資料表示：摘錄未提供特徵工程、缺失值處理、類別編碼或資料平衡策略。訓練目標與損失：推測以分類準確率或交叉熵為目標，但未明確給出損失函數、正則化項或最佳化演算細節（如梯度下降、早停條件）。推論流程：訓練完成後，使用經 ROA 優化的超參數固定模型，對新樣本進行預測。關鍵差異：相較於單獨使用 XGBC、ADAC、HGBC，本文強調混合優化策略，將 ROA 作為外層優化器提升基礎模型表現。然而，依目前可取得資料，無法確認具體優化流程、計算複雜度、超參數搜尋範圍、交叉驗證設置及是否進行模型融合。

## 結果
實驗結果顯示，在異常狀況樣本上，結合 ROA 的 XGRO 算法達到 81.19% 準確率，優於單獨 XGBC 的 79.91% 以及 ADRO 的 79.31%。摘錄未提供可驗證的其他評估指標（如精確率、召回率、F1、AUC）、資料集規模、分割比例、統計顯著性檢定、消融實驗或不同資料分布下的表現。定性結論指出，混合機器學習演算法搭配優化技術能有效提升醫療預測準確度。

## 限制與展望
研究限制包括：(1) 未描述資料來源、樣本數、特徵組成與類別分布，難以評估模型泛化能力；(2) 僅報告準確率單一指標，缺乏臨床相關指標與不確定性量化；(3) ROA 具體實作細節、超參數搜尋空間、計算資源消耗未公開，難以重現與比較；(4) 基線模型僅限三種提升樹，未涵蓋深度學習、集成學習或傳統統計模型；(5) 無外部驗證集或跨機構測試，臨床部署風險未知。後續研究建議：公開資料與代碼、補全多維度評估、探討模型可解釋性、進行前瞻性臨床驗證，並分析 ROA 在不同醫療場景的優化效益。
