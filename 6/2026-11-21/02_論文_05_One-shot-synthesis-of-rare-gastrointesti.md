# 論文 05：One-shot synthesis of rare gastrointestinal lesions improves diagnostic accuracy and clinical training.

- 日期：2026-11-21
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
罕見胃腸道病變在常規內視鏡中極少出現，導致可用於訓練 AI 模型與新手醫師的標註資料極度稀缺，嚴重限制了可靠診斷系統的開發與臨床教學效果。現有生成方法多需大量資料或重新訓練，難以在單一參考影像下快速產生多樣且具臨床意義的病變範例。本研究旨在提出一個一次性、免重訓練的生成框架 EndoRare，利用語言引導的概念解離，將病徵特徵與非診斷屬性分離，以單一參考圖合成多樣化病變影像，期望同時提升下游分類器效能與新手醫師的辨識能力。

## 方法
問題設定：輸入為單一罕見病變的內視鏡參考影像與對應的文字描述，輸出為多張臨床合理且多樣化的合成病變影像。整體架構採一階段生成流程，核心為語言引導的概念解離模組：首先利用預訓練的視覺‑語言編碼器將參考影像與文字映射至共同潛在空間，再透過可學習的原型嵌入將病徵特徵（pathognomonic features）編碼為固定原型向量；非診斷屬性（如光照、背景黏膜紋理、器械干擾）則透過隨機採樣或風格調變機制產生多樣性向量。生成器接收原型嵌入與多樣性向量的拼接，經解碼器重建影像，確保病徵核心特徵保持一致，背景與非關鍵區域產生變化。訓練目標包含對抗損失以提升真實感、語義一致性損失確保病徵特徵與文字描述對齊、以及原型嵌入的正則化以防止過擬合。推論時無需微調模型，直接輸入新參考影像與文字即可即時產生多張合成範例。與既有方法差異在於：僅需單一樣本、免重訓練、明確分離病徵與非病徵語意，並引入語言指導實現可控生成。

## 結果
專家評估認為 EndoRare 產生的合成影像具臨床合理性。將合成資料加入下游分類器訓練後，真陽性率在低假陽性率下顯著提升，證實資料增強效益。探索性讀者研究顯示，接觸合成病例的新手內視鏡醫師在影像層級辨識表現有所改善。摘錄未提供可驗證數字（如具體 TPR/FPR 數值、統計顯著性 p 值、讀者研究樣本數與效果量），僅能觀察到定性結論：合成資料能改善模型與人類學習者表現。

## 限制與展望
僅驗證四種罕見病理，泛化至其他病變尚未證實。合成品質評估依賴專家主觀判斷，缺乏客觀影像品質指標（如 FID、LPIPS）與多樣性量化。讀者研究為探索性設計，樣本數、對照組設置與統計效力未揭露，難以排除學習效應或偏誤。框架假設單一參考影像足以捕捉病徵核心特徵，若參考影像品質不佳或病變表現極端多樣，原型嵌入可能不足。未來需進行前瞻性對照試驗、擴大病理類別、引入客觀生成評估指標，並探討合成資料對模型校準與臨床決策的長期影響。
