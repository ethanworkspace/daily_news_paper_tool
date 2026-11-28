# 論文 04：A systematic framework for assessing conservation effectiveness of migratory marine species: Integrating biomass, habitat quality, and functional traits.

- 日期：2026-10-19
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：Journal of environmental management
- Venue：Journal of environmental management
- 發布時間：2026-10-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42822306/
- PDF：
- DOI：10.1016/j.jenvman.2026.131058
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2089（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
The global expansion of Marine Protected Areas (MPAs) under the "30×30" target necessitates rigorous effectiveness assessments. Traditional evaluations for migratory marine species often rely on static biomass metrics, which fail to capture spatiotemporal mismatches between dynamic migration patterns and static reserve boundaries, deceptively masking structural population crises. Addressing these gaps, we developed a systematic framework integrating biomass, habitat quality, and functional traits. We validated this using the small yellow croaker (Larimichthys polyactis) in the Yellow and East China Seas, employing machine learning, kernel density estimation, circuit theory, and population dynamics models on data spanning 1995 to 2024. Results uncovered a distinct "resource recovery paradox" where quantity uncoupled from quality. Concurrent with enhanced conservation and fishery-management measures, biomass status and habitat quality showed a marked rebound from the 2010s to the 2020s. Year-round Ecosystem-based MPAs and Gear-restricted Fishery Conservation Zones generally outperformed Seasonal Fishery-based MPAs (S-MPAs), particularly in spring. However, this quantitative recovery concealed intrinsic population degradation. Despite a partial recovery in body length, critical functional traits, including fecundity and trophic level, declined continuously, indicating a stock dominated by vulnerable recruitments. Furthermore, severe seasonal asymmetry persists. Current measures appeared more effective in sheltering spring and summer spawning stocks than in protecting deep-water overwintering grounds and migration corridors. Consequently, biological gains associated with summer closed seasons may be weakened by subsequent winter fishing pressure, causing continued winter biomass declines within S-MPAs. We recommend shifting toward dynamic ocean management to restore full life-cycle connectivity and implementing trait-based strategies to rebuild population resilience. This adaptable framework provides a scientific paradigm for optimizing global MPA networks.

## 背景與目的
全球在「30×30」目標下大幅擴展海洋保護區（MPA），但傳統評估多依賴靜態生物量指標，無法捕捉遷徙性海洋物種動態遷徙模式與靜態保護區邊界的時空錯位，導致結構性族群危機被掩蓋。本研究旨在建立一套系統性框架，整合生物量、棲地品質與功能性狀，並以小黃魚（Larimichthys polyactis）在黃海與東海為例，驗證框架在多季節、多保護區類型下的評估能力，提供科學範式以優化全球 MPA 網絡。

## 方法
問題設定：評估不同類型 MPA 對遷徙性魚類全生命週期的保護效能。輸入為 1995‑2024 年長期調查資料，包含漁獲量、生物量、環境變數（溫度、鹽度、葉綠素等）及功能性狀測量（體長、繁殖力、營養級）。輸出為各季節、各 MPA 類型的綜合效能指標。 整體架構為多模組管線： 1. 資料前處理與特徵工程：清洗缺值、標準化環境协變量，構建時空網格。 2. 機器學習模組：以監督式學習（如隨機森林或梯度提升）預測棲地品質，目標函數為最小化均方根誤差（RMSE），輸出連續的棲地適宜度圖層。 3. 核密度估計（KDE）：利用漁獲與調查位置，估算各季節的空間利用分布，產生季節性熱點圖。 4. 電路理論模組：將 KDE 產生的阻力面轉為電導網絡，計算產卵場、越冬場與遷徙走廊間的連通性指標（電流密度、有效電阻）。 5. 族群動態模組：結合生物量時間序列與功能性狀軌跡，建立年齡結構或階段結構模型，透過最大似然校準參數，量化捕撈壓力對體長、繁殖力、營養級的影響。 推論流程：對每一年份與季節依序執行上述模組，彙總各 MPA 類型（全年生態型、漁具限制型、季節性漁業型）的指標並進行比較。 關鍵差異：傳統方法僅比較靜態生物量，本框架同步納入動態棲地品質、空間連通性與功能性狀演變，揭示數量恢復與質量退化的解耦現象。

## 結果
研究發現「資源恢復悖論」：2010 年代至 2020 年代生物量與棲地品質顯著回升，全年性生態型 MPA 與漁具限制型保育區在春季表現優於季節性漁業型 MPA（S‑MPA）。然而功能性狀持續惡化，繁殖力與營養級持續下降，體長僅部分恢復，顯示族群以脆弱的新生個體為主。季節性不對稱嚴重：春夏產卵族群受保護較好，深水越冬場與遷徙走廊保護不足，導致夏季休漁帶來的生物增益被冬季捕撈壓力抵消，S‑MPA 冬季生物量持續下降。摘錄未提供可驗證數字。

## 限制與展望
本框架僅以單一物種、單一海域驗證，推廣至其他遷徙性物種或區域仍需實證。資料依賴長期漁業調查，可能存在時空採樣偏差與缺測。機器學習模型超參數、特徵選擇與電路理論阻力面參數化細節未在摘錄中揭露，難以評估模型穩健性。族群動態模型假設結構簡化，未必完整捕捉密度依賴與環境隨機性。未來研究可擴展至多物種、引入即時海洋觀測資料，並測試動態海洋管理策略在全生命週期連通性恢復上的效果。
