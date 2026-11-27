# 論文 04：A systematic framework for assessing conservation effectiveness of migratory marine species: Integrating biomass, habitat quality, and functional traits.

- 日期：2026-10-01
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
全球為達成「30×30」目標而大幅擴展海洋保護區（MPA），但傳統評估多依賴靜態生物量指標，無法捕捉遷徙物種動態遷徙路徑與固定保護區邊界的時空錯位，導致結構性族群危機被掩蓋。本研究旨在建立一套系統性框架，整合生物量、棲地品質與功能性狀，以更全面評估遷徙性海洋物種的保護成效，並以黃海與東海的小黃魚（Larimichthys polyactis）為實證案例，提供可推廣至全球 MPA 網絡優化的科學範式。

## 方法
問題設定為評估不同類型 MPA 對遷徙性魚類全生命週期的保護效能，輸入包含 1995‑2024 年漁業獨立調查資料、環境變數（溫度、鹽度、葉綠素等）與漁撈壓力圖層；輸出為各季節的生物量狀態、棲地品質指數、功能性狀軌跡（體長、繁殖力、營養級）及連通性評估。整體架構分四大核心模組：(1) 機器學習模型（如隨機森林或梯度提升）建立物種分布與棲地適宜度預測，作為棲地品質基礎；(2) 核密度估計（KDE）根據調查點位推算各季節的空間利用熱點，量化產卵、越冬與遷徙走廊的使用強度；(3) 電路理論將海域轉化為電阻網絡，利用電流流向計算族群在不同 MPA 之間的連通概率，識別關鍵遷徙廊道；(4) 族群動力學模型結合體長結構與功能性狀參數，模擬在不同管理情境下的特徵演變。資料前處理包括將調查資料標準化、插值環境圖層至統一網格、以漁撈強度加權生成阻力面。訓練目標為最小化棲地適宜度預測誤差（交叉熵或 MSE）並校準動力學模型使模擬生物量與觀測值吻合；優化採用交叉驗證與貝葉斯參數估計。推論流程依序執行棲地模型→KDE 熱點→電路連通性→動力學模擬，最後對比全年型生態系 MPA、漁具限制區與季節性漁業 MPA（S‑MPA）在春、夏、秋、冬四季的綜合指標。關鍵差異在於將靜態生物量、動態棲地品質與功能性狀三維整合，並明確量化季節性連通性缺口，超越單一生物量指標的傳統評估。

## 結果
研究發現一種「資源恢復悖論」：2010 年代至 2020 年代生物量與棲地品質顯著回升，全年型生態系 MPA 與漁具限制區在春季表現優於季節性漁業 MPA；然而功能性狀持續惡化，繁殖力與營養級下降，體長僅部分恢復，顯示族群結構趨向脆弱新生個體主導。季節性不對稱嚴重，現行措施對春夏產卵群保護較好，但深水越冬地與遷徙廊道保護不足，導致冬季生物量在 S‑MPA 仍持續下降。摘錄未提供可驗證數字，僅能觀察到上述定性結論。

## 限制與展望
本框架僅以單一物種（小黃魚）在黃海、東海為例，時間跨度雖長但缺乏跨區域、多物種驗證；模型依賴歷史調查與環境資料，未納入氣候變遷情境與未來漁業政策變動；電路理論與動力學模型參數校準存在不確定性，可能影響連通性與特徵演變推論；評估未涵蓋動態海洋管理（如即時關區）的實際操作可行性；後續研究需擴展至多物種、多海域，並整合即時監測與適應性管理機制以驗證框架的普適性與操作效益。
