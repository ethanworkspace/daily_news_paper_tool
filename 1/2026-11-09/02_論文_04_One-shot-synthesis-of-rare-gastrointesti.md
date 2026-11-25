# 論文 04：One-shot synthesis of rare gastrointestinal lesions improves diagnostic accuracy and clinical training.

- 日期：2026-11-09
- 來源層級：Tier 1
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-25T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43073275/
- PDF：
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
罕見胃腸道病變在常規內視鏡中極少出現，導致可用於訓練可靠 AI 模型及新手醫師的資料極度稀缺。現有方法多需大量標註資料或重新訓練，難以滿足臨床快速部署需求。本文提出 EndoRare，一種單樣本、免重訓練的生成框架，旨在從單一參考影像合成多樣化病變範例，解決資料稀缺並支援教學與輔助診斷。

## 方法
問題設定：輸入為單一罕見病變的內視鏡影像，輸出為多張臨床合理且多樣化的合成影像。整體架構採用語言引導的概念解離機制，先利用預訓練的視覺‑語言模型提取病變的病徵描述，將病徵特徵（pathognomonic features）與非診斷性屬性（如光照、背景黏膜紋理）分離。核心模組包含：1) 可學習的原型嵌入，將病徵特徵編碼為固定向量；2) 屬性變異模組，對非診斷性屬性進行隨機採樣或條件控制以產生多樣性；3) 生成器（如擴散或 GAN），以原型嵌入與變異屬性為條件合成影像。資料前處理僅需單張參考圖，無需大規模資料集。訓練目標為在不更新生成器權重的情況下，透過優化原型嵌入使合成影像保留病徵語意，同時損失函數包含語意一致性損失與多樣性正則化。推論時，固定原型嵌入，反覆採樣屬性變異即可產生大量範例。關鍵差異在於：單樣本即可部署、免重訓練、語言引導解離病徵與背景，較既有需大量資料或微調的方法更具資料效率。

## 結果
專家評估認為合成影像具臨床合理性；將合成資料作為資料增強後，下游 AI 分類器在低假陽性率下的真陽性率顯著提升。探索性讀者研究顯示，接觸 EndoRare 生成病例的新手內視鏡醫師在影像層級辨識表現有所改善。摘錄未提供可驗證的具體數值（如 AUC、TPR/FPR 具體數字），僅能觀察到定性上的正向結論。

## 限制與展望
僅驗證四種罕見病變，泛化性未經大規模病理驗證；讀者研究為探索性、非隨機對照，樣本量與統計效力不明；合成影像品質缺乏客觀指標（如 FID、臨床專家評分細節）；框架依賴預訓練視覺‑語言模型，可能引入語言偏誤；未進行前瞻性臨床驗證，部署風險尚待評估。後續研究需擴大病理類別、引入嚴謹對照實驗、量化生成品質並評估長期教學效果。
