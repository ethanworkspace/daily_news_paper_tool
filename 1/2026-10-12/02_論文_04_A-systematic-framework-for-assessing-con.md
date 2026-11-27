# 論文 04：A systematic framework for assessing conservation effectiveness of migratory marine species: Integrating biomass, habitat quality, and functional traits.

- 日期：2026-10-12
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
全球「30×30」目標推動海洋保護區（MPA）快速擴張，但傳統效能評估多仰賴靜態生物量指標，無法捕捉遷徙性海洋物種動態遷徙路徑與靜態保護區邊界的時空錯位，導致結構性族群危機被掩蓋。現有方法缺乏對季節性遷徙走廊、深水越冬棲地及功能性狀（如繁殖力、營養級）退化的量化評估，使保護成效常被高估。本研究旨在建立整合生物量、棲地品質與功能性狀的系統性評估框架，以小黃魚（Larimichthys polyactis）在黃海與東海為實證案例，提供可移植的科學範式以優化全球 MPA 網絡。

## 方法
研究將問題設定為：給定 1995‑2024 年漁業獨立調查與環境資料，輸出各季節、各保護區類型的生物量狀態、棲地品質指數與功能性狀趨勢。整體架構包含四大核心模組：(1) 機器學習模型（如隨機森林或梯度提升）利用海表溫度、鹽度、葉綠素濃度等環境變數預測物種分布概率，作為後續空間分析的輸入層；(2) 核密度估計（KDE）將預測分布轉換為連續密度面，量化各季節的高密度棲地核心區；(3) 電路理論將海域視為電阻網絡，以棲地品質為電導率，計算遷徙走廊的連通性指標（如電流密度、最小阻力路徑），識別關鍵遷徙瓶頸；(4) 族群動力學模型（年齡結構模型或生物量動態模型）結合捕撈壓力、繁殖力與營養級資料，模擬長期族群軌跡並輸出生物量、體長、繁殖力、營養級等功能性狀時間序列。資料前處理包括將調查站點標準化至統一網格、插值缺失環境層、以對數轉換生物量以穩定方差。訓練目標為最小化機器學習模型的交叉驗證均方誤差，並透過貝葉斯資訊準則選擇族群動力學模型最優參數組合。推論流程依序執行：環境變數→機器學習分布預測→KDE 密度面→電路理論連通性→族群動力學模擬，最終輸出各保護區類型（全年生態型 MPA、漁具限制區、季節性漁業型 MPA）在春、夏、秋、冬四季的綜合效能指標。與既有單一生物量評估相比，關鍵差異在於同時量化空間連通性與功能性狀退化，揭示數量恢復與品質惡化的悖論。

## 結果
摘錄未提供可驗證數字。定性結論顯示：自 2010 年代起，隨著保護與漁業管理措施加強，生物量狀態與棲地品質在 2020 年代明顯回升；全年性生態型 MPA 與漁具限制區在春季表現優於季節性漁業型 MPA（S‑MPA）。然而，體長雖部分恢復，關鍵功能性狀（繁殖力、營養級）持續下降，顯示族群以脆弱的新生個體為主。季節性不對稱嚴重：現行措施對春夏產卵族群保護較好，但對深水越冬地與遷徙走廊保護不足，導致夏季休漁帶來的生物增益被冬季捕撈壓力抵消，S‑MPA 冬季生物量持續下降。

## 限制與展望
資料限於單一物種與特定海域，難以直接推廣至其他遷徙物種或海域。機器學習模型與電路理論參數選擇缺乏敏感度分析說明，模型不確定性未量化。族群動力學模型假設參數恆定，未考慮氣候變遷對環境承載力的長期影響。評估僅涵蓋至 2024 年，缺乏長期驗證與管理情境模擬。後續研究建議：擴展多物種、多尺度驗證；引入動態海洋管理情境與氣候預測；量化模型不確定性並發展自適應管理指標。
