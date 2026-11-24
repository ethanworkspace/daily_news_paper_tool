# 論文 01：Elastic Ranking-Driven Time Series Feature Optimization for Aeroengine Remaining Useful Life Prediction.

- 日期：2026-09-29
- 來源層級：Tier 2
- 期刊/會議/來源：Entropy (Basel, Switzerland)
- Venue：Entropy (Basel, Switzerland)
- 發布時間：2026-09-28T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42940790/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13703398/
- DOI：10.3390/e28101067
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1864（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
This paper proposes a hierarchical recurrent neural network framework that leverages a context-gated mechanism and the elastic sorting of time series indicators, addressing the strong dynamic coupling characteristics of aeroengine operational time series data. This framework addresses the coupling of multi-physical field signals and the interleaved cross-scale degradation characteristics of engine time series data. The framework achieves high-precision predictions of residual service life under complex operating conditions by deeply integrating multi-modal feature engineering with hierarchical time series modeling. An elastic ranking algorithm for time series indexes is designed to adaptively fuse multiple sensors' time domains, frequency domains, and nonlinear characteristics, thereby constructing a dynamic feature space sensitive to load conditions. This approach addresses the limitations of traditional fixed feature combinations in characterizing variable load conditions. Additionally, a multi-scale stack dilation convolution module is introduced to exponentially enlarge the receptive field, allowing for the capture of long-range dependencies in weakly degraded signals. A bidirectional time-frequency converter decomposes the signal into low-frequency trend components and high-frequency anomaly components, enabling coupling characterization through cross-scale feature interactive gating. Furthermore, context-gated cyclic units based on hierarchical cyclic networks are constructed to hierarchically integrate multi-modal features while dynamically adjusting time-dependent weights, thereby enhancing the model's causal reasoning ability for long sequence degradation patterns. In four typical experiments conducted on the C-MAPSS dataset, the ERCG-HRNN demonstrates significant improvements in RMSE and Score compared to existing methods.

## 背景與目的
航空發動機在複雜工況下運行的多物理場訊號呈現強動態耦合與跨尺度退化交織特性，傳統固定特徵組合難以適應變載荷條件，導致剩餘使用壽命（RUL）預測精度受限。本研究旨在解決多模態特徵融合與長序列時間依賴建模的缺口，提出一種結合彈性排序驅動的時間序列特徵優化與層級循環神經網路的框架（ERCG-HRNN），以提升在複雜工況下的高精度 RUL 預測能力。

## 方法
問題設定：輸入為多傳感器的時間序列原始訊號，輸出為發動機的剩餘使用壽命標量。整體架構採用層級循環神經網路（HRNN）為骨幹，包含三大核心模組： 1. 彈性排序演算法：對每個傳感器的時域、頻域與非線性指標進行自適應排序與加權融合，構建對載荷條件敏感的動態特徵空間，克服固定特徵組合的侷限。 2. 多尺度堆疊膨脹卷積模組：利用指數級擴大感受野的膨脹卷積堆疊，捕捉微弱退化訊號中的長距依賴。 3. 雙向時頻轉換器：將訊號分解為低頻趨勢分量與高頻異常分量，並透過跨尺度特徵互動閘控實現耦合表徵。 此外，基於層級循環網路建構上下文閘控循環單元，逐層整合多模態特徵並動態調整時間依賴權重，增強模型對長序列退化模式的因果推理能力。資料前處理方面，僅說明採用 C-MAPSS 資料集的四個子集進行實驗，未詳細描述歸一化、滑動窗口或特徵標準化細節。訓練目標採用均方誤差（RMSE）與 NASA Score 函數作為損失函數進行聯合最佳化，具體優化器、學習率排程等超參數在摘錄中未提及。推論流程為：原始訊號經彈性排序融合 → 多尺度膨脹卷積提取長程特徵 → 雙向時頻分解與跨尺度閘控 → 層級上下文閘控循環單元逐步編碼 → 全連接層輸出 RUL 預測值。與既有方法的關鍵差異在於：動態彈性特徵排序、指數級感受野的膨脹卷積、雙向時頻分解與跨尺度閘控、以及層級上下文閘控機制的綜合整合。

## 結果
作者在 C-MAPSS 四個典型子集上進行實驗，聲稱 ERCG-HRNN 在 RMSE 與 Score 指標上均顯著優於現有基線方法。然而，摘錄未提供可驗證數字（如具體 RMSE、Score 數值、基線名稱、統計顯著性檢定結果），亦未呈現消融實驗或案例分析的定量細節。可觀察到的定性結論為：彈性排序與層級上下文閘控有效提升了對變載荷與長距退化模式的建模能力，進而改善預測精度。

## 限制與展望
研究僅在單一公開資料集（C-MAPSS）的四個子集驗證，缺乏跨資料集、真實飛行數據或不同發動機型號的泛化證據。方法論細節如超參數設定、訓練時間、模型參數量、推論延遲、記憶體佔用等部署指標未揭露，難以評估工程落地可行性。消融實驗與各模組貢獻度量化缺失，無法確認彈性排序、膨脹卷積、時頻分解或上下文閘控的相對重要性。潛在風險包括：動態特徵排序可能引入額外計算開銷，且對感測器缺失或雜訊敏感度未探討。後續研究建議擴展至多源異構數據、引入不確定性量化、進行詳細消融與計算效率分析，並驗證於實際發動機健康管理系統中。
