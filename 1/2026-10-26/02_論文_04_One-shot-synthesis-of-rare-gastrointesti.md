# 論文 04：One-shot synthesis of rare gastrointestinal lesions improves diagnostic accuracy and clinical training.

- 日期：2026-10-26
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
罕見胃腸道病變在常規內視鏡中極少出現，導致訓練可靠 AI 模型與新手醫師的資料嚴重不足。現有方法多需大量標註資料或重新訓練，難以快速適應稀有病灶。本研究旨在提出一種單樣本、免重訓練的生成框架 EndoRare，從單一參考影像合成多樣化病灶範例，以解決資料稀缺、提升診斷準確度與教學效能。

## 方法
EndoRare 採用一階段、免重訓練的生成流程。輸入為單一參考內視鏡影像與對應的自然語言描述。核心機制為語言引導的概念解離：利用文本編碼器提取病灶的病徵語義，將影像編碼器輸出的特徵分為「病徵原型嵌入」與「非診斷屬性」兩部分。病徵原型嵌入以可學習向量形式固定捕捉關鍵病理特徵；非診斷屬性（如背景黏膜紋理、光照、視角）則透過隨機採樣或風格調變產生多樣性。生成器接收原型嵌入與變化後的非診斷代碼，解碼合成新影像。訓練階段僅在大規模通用內視鏡資料上預訓練編碼器/生成器，推理時無需針對目標病灶微調。輸出為多張臨床合理的合成病灶影像，供下游分類器資料增強或教學使用。關鍵差異在於單樣本即可解離病徵與非病徵因子，且完全免重訓練。

## 結果
結果顯示，專家評估 EndoRare 合成影像具臨床合理性；資料增強顯著提升下游 AI 分類器性能，在低假陽性率下真陽性率上升（摘錄未提供可驗證數字）。探索性讀者研究發現，接觸合成病例後初學內視鏡醫師的影像級辨識能力改善。消融實驗證實語言引導概念解離對病變特徵保留與多樣性生成均有貢獻。整體支持 EndoRare 作為稀有病變教學的資料高效工具，並建議未來進行前瞻性對照驗證。

## 限制與展望
研究僅驗證四種罕見病理，泛化能力待更多病灶確認。讀者研究為探索性設計，缺乏隨機對照與長期追蹤，效果可能受期望偏差影響。合成多樣性度量、計算成本與部署細節未揭露。後續需進行前瞻性對照試驗、擴展病灶類別並量化生成品質指標。
