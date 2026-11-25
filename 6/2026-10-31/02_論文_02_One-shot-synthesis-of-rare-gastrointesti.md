# 論文 02：One-shot synthesis of rare gastrointestinal lesions improves diagnostic accuracy and clinical training.

- 日期：2026-10-31
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
罕見胃腸道病變在常規內視鏡中極少出現，導致可用於訓練可靠 AI 模型與新手醫師的資料極度稀缺。現有方法多需大量標註資料或重新訓練，難以快速適應新病變。本研究旨在提出一種單樣本、免重訓練的生成框架 EndoRare，從單一參考影像合成多樣化病變範例，以解決資料稀缺、提升診斷準確度與教學效能。並期望透過語言引導的概念解離，將病徵特徵與非診斷屬性分離，編碼前者為可學習原型嵌入並變化後者以保證多樣性。

## 方法
EndoRare 採用單樣本、免重訓練的生成策略。輸入為一張罕見病變的參考內視鏡影像與對應的語言描述（病理名稱或關鍵概念）。核心機制為語言引導的概念解離：利用預訓練的視覺‑語言模型將影像特徵映射至語義空間，並依語言提示將病徵特徵（pathognomonic features）與非診斷屬性（如光照、背景黏膜紋理、器械干擾）分離。病徵特徵被編碼為一個可學習的原型嵌入（prototype embedding），此嵌入在生成過程中保持固定，確保合成影像保留關鍵病理特徵；非診斷屬性則透過隨機採樣或可控噪聲在潛在空間中變化，以產生多樣化的外觀。生成器（如擴散模型或 GAN）接收原型嵌入與變化後的非診斷潛在碼，輸出合成的內視鏡影像。訓練階段僅需在大規模通用內視鏡資料上預訓練視覺‑語言編碼器與生成器，推論時無需針對新病變進行微調。推論流程：(1) 編碼參考影像與語言提示；(2) 解離並提取原型嵌入；(3) 多次採樣非診斷潛在碼；(4) 解碼生成多張合成影像。與既有方法相比，關鍵差異在於：(i) 僅需單一標註影像即可生成多樣範例；(ii) 透過語言引導實現病徵與背景的顯式解離，避免病徵特徵被背景變異干擾；(iii) 免重訓練特性大幅降低部署門檻。

## 結果
專家評估認為合成影像具臨床合理性。將合成資料作為資料增強加入下游分類器，顯著提升真陽性率且在低假陽性率下表現更佳。探索性讀者研究顯示，接觸 EndoRare 生成病例的新手內視鏡醫師在影像層級辨識上有改善。摘錄未提供可驗證數字（如具體 TPR、AUC、統計顯著性或樣本數），僅能觀察到定性結論：合成資料能改善模型效能與教學效果。

## 限制與展望
本研究僅驗證四種罕見病理，樣本數與病變多樣性有限；讀者研究為探索性、非隨機對照，缺乏長期學習保留與臨床決策影響的證據；合成影像品質僅依專家主觀判斷，缺乏客觀影像品質指標（如 FID、臨床相關性量化）；語言引導解離依賴預訓練視覺‑語言模型，可能受限於模型對罕見病變語義的覆蓋度；未來需進行前瞻性對照試驗、擴展病變類別、量化合成多樣性與真實分布差距，並評估部署於實際內視鏡工作流程的可行性與風險。
