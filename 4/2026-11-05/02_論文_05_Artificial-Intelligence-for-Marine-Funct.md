# 論文 05：Artificial Intelligence for Marine Functional Peptide Discovery: Challenges, Advances, and Future Perspectives.

- 日期：2026-11-05
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：Marine drugs
- Venue：Marine drugs
- 發布時間：2026-10-28T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43083138/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13804885/
- DOI：10.3390/md24110383
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1622（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Marine organisms represent a rich but underexplored source of bioactive peptides with potential applications in therapeutics, nutraceuticals, and biotechnology. However, conventional marine peptide discovery relies on labor-intensive workflows involving specimen collection, extraction, purification, structural characterization, and experimental validation, limiting the efficient exploration of the rapidly expanding marine sequence space. Recent advances in artificial intelligence (AI) provide new opportunities to accelerate peptide discovery by enabling large-scale sequence analysis, functional prediction, and candidate prioritization. This review summarizes recent advances in AI-driven marine functional peptide discovery, covering peptide resources, computational representations, machine-learning and deep-learning methods, protein language models, generative approaches, genome and metagenome mining, and structure-aware prediction strategies. We further discuss representative applications involving marine microorganisms, animal proteomes, cyanobacterial biosynthetic pathways, metagenomic datasets, and marine-derived peptide candidates, highlighting current achievements and limitations. Finally, we analyze key challenges and future perspectives, including marine-specific datasets, multimodal AI models integrating sequence, structural, chemical, and biosynthetic information, rigorous benchmarking, and computational-experimental integration. This review provides a comprehensive framework for understanding how AI can support the discovery and development of functional peptides from marine resources.

## 背景與目的
海洋生物蘊含豐富但未被充分探索的生物活性肽，具治療、營養保健與生技應用潛力。傳統發現流程依賴費時費力的採集、萃取、純化、結構鑑定與實驗驗證，難以有效覆蓋快速擴增的海洋序列空間。近年人工智慧進展提供大規模序列分析、功能預測與候選優先排序的新契機。本文為綜述文章，旨在整合 AI 驅動海洋功能性肽發現的最新進展，涵蓋資源、表示、機器/深度學習、蛋白質語言模型、生成式方法、基因組與宏基因組挖掘、結構感知預測等面向，並討論代表性應用與現有限制，提出未來挑戰與展望，為該領域提供綜合框架。

## 方法
本文為綜述性研究，並未提出單一新模型或系統架構，而是系統性梳理 AI 輔助海洋功能性肽發現的方法學脈絡。問題設定為：給定海洋來源的序列、基因組、宏基因組或蛋白質組資料，預測或生成具特定生物活性的肽段。輸入包括肽序列、結構資訊、生物合成基因簇、理化性質等多模態特徵；輸出為功能標籤、活性評分或新序列候選。綜述涵蓋的核心方法類別包括：(1) 計算表示：氨基酸組成、理化指標、嵌入向量（如 ProtBERT、ESM 等蛋白質語言模型產生的表示）；(2) 機器學習與深度學習：傳統分類器（SVM、隨機森林）、CNN、RNN、Transformer 等架構用於功能分類與活性預測；(3) 生成式方法：變分自編碼器（VAE）、生成對抗網路（GAN）、擴散模型、基於語言模型的條件生成，用於從頭設計或優化肽序列；(4) 基因組與宏基因組挖掘：結合反饋式搜尋、抗生素生物合成基因簇識別（如 antiSMASH）、深度學習預測酶結構域與產物結構；(5) 結構感知策略：整合 AlphaFold2/ESMFold 預測結構、分子動力學模擬、對接評分以輔助功能推斷。訓練目標多為監督式分類/迴歸損失、對比學習、生成式似然最大化或強化學習獎勵函數。推論流程通常包含資料清洗、特徵編碼、模型預測、候選排序與實驗驗證回饋。與既有方法的關鍵差異在於強調海洋特有資料來源、多模態融合與生物合成邏輯的整合，但摘錄未提供具體模型超參數、訓練細節或基準測試設定。

## 結果
本文為綜述，摘錄未提供可驗證的量化實驗數字、基線模型名稱或統計顯著性結果。作者定性總結指出：AI 方法已在海洋微生物、動物蛋白質組、藍菌生物合成路徑、宏基因組資料集中成功鑑定多個具抗菌、抗氧化、抗癌、抗高血壓等活性的候選肽；蛋白質語言模型與生成式模型顯著擴展了可探索的化學空間；結構感知預測提升了功能標註準確度。然而，現有研究多缺乏統一基準測試、跨資料集泛化驗證與大規模實驗閉環驗證，多數成果停留於計算機預測階段。

## 限制與展望
綜述指出關鍵限制：(1) 缺乏海洋專屬、高品質、標註完整的基準資料集，現有資料多源自陸生生物，領域適應性不足；(2) 多模態融合（序列、結構、化學、生物合成）仍處早期，缺統一表示與聯合訓練範式；(3) 缺嚴謹標準化基準測試與評估指標，難公平比較；(4) 計算預測與實驗驗證脫節，鮮少形成閉環迭代；(5) 模型可解釋性、泛化至新分類群與新功能能力未充分驗證。後續方向建議建立海洋肽專用資料庫、發展多模態基礎模型、推動社群共享基準與自動化實驗平台整合。潛在風險含預測偽陽性導致資源浪費、生物合成可行性評估不足、數據偏差放大。
