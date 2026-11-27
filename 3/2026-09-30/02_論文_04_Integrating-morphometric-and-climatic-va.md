# 論文 04：Integrating morphometric and climatic variables into the mapping of land use and vegetation cover in the Caatinga biome.

- 日期：2026-09-30
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：Environmental monitoring and assessment
- Venue：Environmental monitoring and assessment
- 發布時間：2026-09-29T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42809057/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13624018/
- DOI：10.1007/s10661-026-15949-z
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1413（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Recent landscape transformations resulting from the replacement of natural areas with anthropogenic uses have had an impact on the semi-arid region of Brazil. The objective of the research was to evaluate a land use and land cover classification model in the Caatinga biome, using machine learning techniques integrated with multiple environmental and climatic covariates. The area was segmented into six subunits, based on a combination of hydrographic regions and geomorphological domains. The random forest algorithm on the Google Earth Engine platform was used to process the supervised classification, considering predictor variables, including spectral bands and indices, tasseled cap transformation, image fractions, surface temperature, precipitation, morphometric variables, and geographic location. The results indicated that geomorphological compartmentalization increased separability between land use classes and bare soil. The model achieved an average global accuracy of 0.83 and a kappa index of 0.80. The forest vegetation and rivers, lakes, and ocean classes showed high precision, while salt marshes and herbaceous restinga indicated inconsistencies. The most relevant variables were spatial position, altitude, and climatic conditions. In this perspective, incorporating this set of elements into the machine-learning classifier proved to be an innovative and scientifically relevant approach.

## 背景與目的
研究針對巴西半乾旱區 Caatinga 生物群落近年因人為土地利用擴張導致自然植被快速轉換的問題。現有土地覆蓋分類多僅依賴光譜資訊，缺乏地形、氣候等環境協變量，導致裸土與植被類別難以有效分離。本文旨在評估結合多源環境與氣候協變量的機器學習分類模型，並透過地貌區劃提升類別可分性，提供科學上具創新性的製圖方法。

## 方法
問題設定為監督式土地利用/土地覆蓋分類，輸入為多波段影像與環境協變量，輸出為六大類別標籤。整體流程： 1. 研究區依水文區與地貌域結合劃分為六個子單元，作為地貌區劃基礎。 2. 在 Google Earth Engine 平台建立隨機森林分類器。 3. 預測變數包含：光譜波段與指數、Tasseled Cap 變換分量、影像分解分量、地表溫度、降水、地形變量（如高程、坡度、坡向等）、地理位置座標。 4. 使用標註樣本訓練隨機森林，目標為最小化分類誤差（隱含 Gini 不純度最小化），採用預設樹數與節點分裂策略。 5. 推論階段對各子單元獨立套用模型，再拼接為全區分類圖。 關鍵差異在於將地形與氣候協變量納入特徵集，並以地貌區劃作為空間分層策略，增強裸土與植被類別的可分性。

## 結果
模型整體平均總體準確率達 0.83，Kappa 指數 0.80。森林植被與河流、湖泊、海洋類別精度較高；鹽沼與草本休息區類別出現不一致，分類表現較弱。變數重要性排序顯示空間位置、高程與氣候條件為最關鍵預測因子。地貌區劃確實提升類別可分性，證明多源協變量整合的有效性。

## 限制與展望
僅採用單一隨機森林模型，未與其他分類器比較；樣本選取與驗證細節未揭露，難以評估泛化能力；鹽沼與草本休息區分類不穩定，顯示特徵表達或樣本不足；研究範圍限於 Caatinga，結論推廣性有待驗證；程式碼與資料未公開，重現性受限。後續可嘗試集成學習、深度學習或增加高解析度時間序列資料以改善弱勢類別表現。
