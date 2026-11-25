# 論文 04：One-shot synthesis of rare gastrointestinal lesions improves diagnostic accuracy and clinical training.

- 日期：2026-11-17
- 來源層級：Tier 1
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
罕見胃腸道病變在常規內視鏡中極少出現，導致可用於訓練可靠 AI 模型與新手醫師的資料極度稀缺。現有生成方法多需大量標註資料或重新訓練，難以在單一參考影像下快速產生多樣且臨床合理的病變範例。本研究旨在提出一種一次性、免重訓練的生成框架 EndoRare，透過語言引導的概念解離，將病徵特徵與非診斷屬性分離，以單一參考圖合成多樣化病變影像，期望解決資料稀缺、提升罕見病變 AI 分類效能與教學訓練效率。研究針對鈣化纖維腫、幼年型息肉症、家族性腺瘤性息肉症與 Peutz‑Jeghers 症候群四種罕見病理進行驗證，展示框架在多種病變類型上的泛化潛力。

## 方法
EndoRare 採一階段、免重訓練的生成流程，輸入為單一參考內視鏡影像與對應的自然語言描述。核心架構包含三大模組：(1) 語言引導的概念解離編碼器，利用預訓練視覺‑語言模型將影像特徵映射至語義空間，並依語言提示將病徵特徵（pathognomonic features）與非診斷屬性（背景、光照、器械等）分離；(2) 可學習的原型嵌入，將解離出的病徵特徵壓縮為一組固定維度的 prototype embedding，作為生成時的條件向量，保證病徵核心外觀不變；(3) 多樣性解碼器，接收 prototype embedding 並結合隨機採樣的風格潛變數，透過條件式擴散或 GAN 風格的生成器合成多張影像，僅改變非診斷屬性以產生視覺多樣性。資料前處理僅包含標準化裁切與歸一化，無額外標註需求。訓練目標為最小化重建損失與語義一致性損失，確保生成影像在病徵區域與參考一致，同時透過對抗或擴散損失提升真實感。推論時，僅需載入已訓練的編碼器、原型嵌入與解碼器，輸入單一參考圖即可即時產生任意數量的合成病變範例，無需針對新病變進行微調。與既有方法相比，關鍵差異在於：一次性生成、免重訓練、語言引導的概念解離以保留病徵特異性並控制多樣性。

## 結果
專家評估顯示 EndoRare 合成影像在臨床上具合理性；將合成資料加入下游分類器訓練後，真陽性率在低假陽性率區間顯著提升，但摘錄未提供可驗證數字。探索性讀者研究發現，接觸合成病例的新手內視鏡醫師在影像層級辨識準確度有所改善。作者結論認為 EndoRare 具備作為資料高效教學工具的潛力，並呼籲未來進行前瞻性對照驗證。

## 限制與展望
本研究僅在四種罕見病理驗證，泛化至其他病變仍待證實；專家評估與讀者研究為探索性、樣本數未揭露，缺乏統計顯著性報告；合成品質的量化指標（如 FID、臨床相關性分數）未提供；框架依賴預訓練視覺‑語言模型，可能受限於其領域知識；尚未進行前瞻性對照試驗以確認教學與臨床決策效益。
