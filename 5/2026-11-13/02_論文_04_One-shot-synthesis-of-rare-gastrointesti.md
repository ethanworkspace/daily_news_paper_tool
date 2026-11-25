# 論文 04：One-shot synthesis of rare gastrointestinal lesions improves diagnostic accuracy and clinical training.

- 日期：2026-11-13
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
罕見胃腸道病變在常規內視鏡中極少出現，導致可用於訓練可靠 AI 模型與新手醫師的資料極度稀缺。現有方法多需大量標註樣本或重新訓練生成模型，難以滿足臨床快速部署與教學需求。本研究旨在提出一種單樣本、免重訓練的生成框架 EndoRare，能從單一參考影像合成多樣化病變範例，以解決資料稀缺、提升下游分類器效能並輔助新手內視鏡醫師學習，填補罕見病變資料增強與教學的缺口。

## 方法
問題設定：輸入為單一內視鏡參考影像（含目標罕見病變），輸出為多張臨床合理且多樣化的合成病變影像。整體架構採用語言引導的概念解離機制，先利用文本描述或標註引導模型將病變的病徵特徵（pathognomonic features）與非診斷性屬性（如光照、背景黏膜紋理、器械干擾）分離。核心模組包含：(1) 原型嵌入學習器，將病徵特徵編碼為可學習的原型向量；(2) 屬性變異模組，對非診斷性屬性採樣或生成多樣化風格代碼；(3) 生成器，以原型向量與風格代碼為條件合成影像。資料前處理僅需單張參考影像，無需大規模資料集或微調。訓練目標與損失函數在摘錄中未詳細揭露，僅知框架為免重訓練，推測可能採用預訓練的視覺‑語言模型進行零樣本推理。推論流程：給定參考影像 → 編碼病徵原型 → 多次採樣風格代碼 → 生成多張合成影像。與既有方法的關鍵差異在於：單樣本即可生成、無需針對新病變重新訓練生成模型、並透過語言引導實現病徵與非病徵特徵的顯式解離，確保合成影像保留診斷關鍵特徵同時具備多樣性。

## 結果
專家評估認為 EndoRare 產生的合成影像具備臨床合理性。將合成資料用於下游分類器的資料增強後，分類器在低假陽性率下的真陽性率顯著提升（摘錄未提供可驗證數字）。探索性讀者研究顯示，接觸過 EndoRare 生成病例的新手內視鏡醫師在影像層級辨識表現有所改善。整體結論支持 EndoRare 作為資料高效的罕見病變教學與模型增強工具，但仍需前瞻性對照驗證。

## 限制與展望
本研究僅在四種罕見病變上驗證，樣本數與病變類型有限，難以推廣至所有罕見胃腸道病變。專家評分與讀者研究屬主觀評估，缺乏大規模、盲法、前瞻性對照實驗。框架的免重訓練特性雖具優勢，但未說明對極端影像品質、不同內視鏡設備或病變外觀變異的魯棒性。此外，摘錄未提供損失函數、訓練細節與程式碼，限制可重現性與後續改進。未來需進行多中心前瞻性試驗、量化生成品質指標並釋出模型權重。
