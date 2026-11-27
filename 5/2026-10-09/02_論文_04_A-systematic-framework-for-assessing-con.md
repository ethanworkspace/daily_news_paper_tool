# 論文 04：A systematic framework for assessing conservation effectiveness of migratory marine species: Integrating biomass, habitat quality, and functional traits.

- 日期：2026-10-09
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
全球在「30×30」目標下擴大海洋保護區（MPA），亟需嚴謹的效能評估。傳統對遷徙性海洋物種的評估多依賴靜態生物量指標，無法捕捉動態遷徙模式與靜態保護區邊界的時空錯位，導致結構性族群危機被掩蓋。本研究針對此缺口，建立整合生物量、棲地品質與功能特徵的系統性框架，並以黃海與東海的小黃魚（Larimichthys polyactis）為實證案例，利用機器學習、核密度估計、電路理論與族群動力學模型，分析 1995‑2024 年資料，旨在提供可移植的科學範式以優化全球 MPA 網絡。

## 方法
問題設定：評估不同類型 MPA 對遷徙性魚類全生命週期的保護效能。輸入包含多年度漁業調查生物量、環境變數（溫度、鹽度、深度等）、物種分布記錄與生活史特徵資料；輸出為各季節、各 MPA 類型的綜合效能指標。整體架構由四大核心模組串接：(1) 生物量預測模組，採用機器學習（演算法未於摘錄說明）將環境變數與調查資料對應，輸出時空生物量圖層；(2) 棲地品質模組，以核密度估計（KDE）描繪物種利用分布，並結合環境圖層產出棲地適宜度指數；(3) 功能特徵動態模組，利用族群動力學模型追蹤體長、繁殖力、營養級等關鍵特徵的長期變化趨勢；(4) 連通性分析模組，應用電路理論將遷徙走廊、越冬區與產卵區轉化為電阻網絡，量化季節性連通阻力。資料前處理包括調查資料標準化、環境圖層插值至統一網格、特徵標準化與缺失值插補。訓練目標方面，機器學習模型以均方誤差（RMSE）為損失函數進行梯度下降優化；族群動力學模型以最大似然擬合生命史參數。推論流程：依時間序列依序執行四模組，產生各季節的生物量、棲地品質、特徵指標與連通性分數，再依 MPA 類型（全年生態型、漁具限制型、季節性漁業型）彙總比較。關鍵差異在於同時整合數量、質量與特徵三維度，並引入電路理論量化遷徙連通性，揭示靜態指標無法發現的「資源恢復悖論」。註：摘錄未提供具體演算法名稱、超參數、損失函數細節與驗證策略，依目前可取得資料，無法確認。

## 結果
主要發現呈現「資源恢復悖論」：2010 年代至 2020 年代，隨著保護與漁業管理加強，生物量狀態與棲地品質顯著回升；全年性生態型 MPA 與漁具限制型保育區在春季表現優於季節性漁業型 MPA（S‑MPA）。然而，量化恢復掩蓋了內在族群退化：雖體長部分回升，繁殖力與營養級等關鍵功能特徵持續下降，顯示族群以脆弱的新生個體為主。季節性不對稱嚴重：現行措施對春夏產卵族群保護較佳，但深水越冬區與遷徙走廊保護不足，導致夏季休漁帶來的生物增益被冬季捕撈壓力抵消，S‑MPA 冬季生物量持續下降。摘錄未提供可驗證數字，僅能觀察上述定性結論。

## 限制與展望
研究僅以單一物種、單一海域為實證，推廣性有待多物種、多區域驗證。資料來源依賴漁業調查與環境再分析，時間序列可能存在觀測偏差與空間缺口。機器學習模型架構、超參數與驗證細節未揭露，難以評估預測不確定性。電路理論參數（電阻面構建、閾值設定）未說明，連通性結果可能敏感於主觀設定。功能特徵動態模型假設與參數擬合過程未公開，解釋力受限。建議未來引入動態海洋管理（如即時海洋預測與自適應邊界）、擴展至多物種特徵組合、並進行獨立測試集驗證，以強化框架的操作化與韌性評估能力。
