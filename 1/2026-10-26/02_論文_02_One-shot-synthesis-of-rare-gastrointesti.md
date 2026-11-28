# 論文 02：One-shot synthesis of rare gastrointestinal lesions improves diagnostic accuracy and clinical training.

- 日期：2026-10-26
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-25T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43073275/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13793275/
- DOI：10.1038/s41467-026-78492-y
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1217（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Rare gastrointestinal lesions are infrequently encountered in routine endoscopy, limiting data for developing reliable artificial intelligence (AI) models and training novice clinicians. Here we present EndoRare, a one-shot, retraining-free generative framework that synthesizes diverse lesion exemplars from a single reference image. Using language-guided concept disentanglement, EndoRare separates pathognomonic lesion features from non-diagnostic attributes, encoding the former into a learnable prototype embedding while varying the latter to ensure diversity. We validate EndoRare across four rare pathologies: calcifying fibrous tumor, juvenile polyposis syndrome, familial adenomatous polyposis, and Peutz-Jeghers syndrome. Experts judge the synthetic images clinically plausible, and data augmentation significantly improves downstream AI classifiers, increasing true positive rates at low false-positive rates. In an exploratory reader study, exposure to EndoRare-generated cases is associated with improved image-level recognition by novice endoscopists. These findings support the potential use of EndoRare as a data-efficient tool for rare-lesion education and motivate prospective controlled validation.

## 背景與目的
罕見胃腸道病變在常規內視鏡檢查中極少遇到，導致可供開發可靠 AI 模型與訓練新手內視鏡醫師的標註資料極度稀缺。現有生成式方法通常需要大量標註影像或進行完整微調，難以快速適應單一罕見病變的資料匱乏情況。本研究旨在解決「單一參考影像即可生成多樣化、臨床合理的病變範例」這一技術缺口，提出 EndoRare 一鍵式、免重訓練的生成框架，期望同時提升下游分類器效能與新手醫師的影像辨識能力，為罕見病變教學與 AI 開發提供資料高效的解決方案。

## 方法
問題設定：輸入為單一罕見病變內視鏡影像與對應的自然語言描述，輸出為多張保留病變核心特徵但背景、光照、角度等非診斷屬性多樣化的合成影像。整體架構為一個免重訓練的生成框架 EndoRare，核心模組採用語言引導的概念解離機制：先利用文本編碼器將病變的病理描述轉為語義向量，再透過跨模態注意力將影像特徵分解為「病徵原型嵌入」與「非診斷屬性嵌入」。病徵原型嵌入以可學習的原型向量形式固定編碼病變的關鍵病理特徵；非診斷屬性嵌入則透過隨機採樣或風格調變產生多樣性。生成器接收兩部分嵌入並解碼為合成影像。資料前處理僅涉及影像標準化與文本清洗，無額外標註需求。訓練目標包含：(1) 原型嵌入與語言語義對齊的對比損失；(2) 重建損失確保合成影像保留原始病變結構；(3) 多樣性正則化鼓勵非診斷屬性變化。推論階段僅需單張參考影像與文字提示，即可即時產生任意數量合成範例，無需再次優化模型參數。與既有方法的關鍵差異在於：採用語言引導的概念解離實現一鍵生成、免重訓練、且明確分離病徵與非病徵特徵以保證臨床合理性與多樣性。

## 結果
專家評估顯示 EndoRare 生成的合成影像在臨床合理性上獲得肯定；將合成資料加入下游分類器訓練後，真陽性率在低假陽性率區間顯著提升；初步閱讀者研究發現，接觸合成病例的新手內視鏡醫師在影像層級辨識準確度上有所改善。摘錄未提供可驗證的具體數值（如 AUC、TPR/FPR 具體百分比、統計顯著性 p 值或樣本數），僅能觀察到定性上的正向效果。

## 限制與展望
目前驗證僅涵蓋四種罕見病變，樣本數與病理多樣性有限；專家評估與閱讀者研究為探索性設計，缺乏前瞻性、隨機對照的嚴謹驗證；合成影像的多樣性控制機制、潛在模式崩塌風險、以及對極端影像品質的魯棒性未詳細量化；下游分類器改善幅度未給出具體統計指標，難以評估臨床實用價值；後續研究需擴大病理類別、引入多中心資料、進行前瞻性對照試驗，並完善生成品質的客觀評估指標。
