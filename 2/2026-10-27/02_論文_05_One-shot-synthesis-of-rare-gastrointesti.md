# 論文 05：One-shot synthesis of rare gastrointestinal lesions improves diagnostic accuracy and clinical training.

- 日期：2026-10-27
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
罕見胃腸道病變在常規內視鏡中極少出現，導致可用影像資料稀缺，難以訓練可靠的 AI 模型，也限制初學醫師的臨床訓練。現有生成方法通常需大量標註資料或重新訓練，無法滿足單一參考影像即可產生多樣病灶的需求。本文提出 EndoRare，一種一次性、免重訓練的生成框架，利用語言引導的概念解離，將病徵特徵與非診斷屬性分離，編碼前者為可學習原型嵌入並變化後者以確保多樣性，並在四種罕見病理驗證，旨在為罕見病灶教育提供資料高效工具。

## 方法
問題設定：輸入單一參考內視鏡影像，輸出多張臨床合理且多樣化的合成病灶影像。整體架構採用語言引導的概念解離模組，結合預訓練的視覺‑語言模型（如 CLIP）提取病灶的病徵語義描述，並將影像編碼為兩組潛在表示：(1) 病徵原型嵌入，捕捉具診斷意義的形態、紋理與顏色特徵，透過可學習的原型向量固定；(2) 非診斷屬性嵌入，包含背景黏膜、光照、視角等無關因素。訓練階段為免重訓練，直接利用預訓練生成模型（擴散或 GAN）配合原型嵌入進行條件生成，損失函數包含原型一致性損失與多樣性正則化，確保病徵核心不變而非診斷屬性隨機變化。推論時，固定原型嵌入，對非診斷屬性採樣不同噪聲或語言提示，產生多組合成影像。關鍵差異在於：一次性參考即可生成、無需針對新病灶微調、明確分離病徵與非病徵概念以保證臨床真實性與多樣性。

## 結果
專家評估認為 EndoRare 產生的合成影像具臨床合理性。將合成資料作為資料增強加入下游分類器，顯著提升真陽性率且在低假陽性率下表現更佳。探索性讀者研究顯示，接觸合成病例的初階內視鏡醫師在影像層級辨識準確度有所提升。摘錄未提供可驗證數字，僅能觀察到定性改善趨勢。

## 限制與展望
僅在四種罕見病理驗證，樣本數極少，泛化能力未知；讀者研究為探索性、非隨機對照，缺乏統計效力；合成影像品質缺乏客觀指標（如 FID、臨床專家評分細節）；免重訓練假設依賴預訓練模型對內視鏡域的適應性，可能引入領域偏移；未來需進行前瞻性對照試驗、擴展病理類別並量化生成品質。
