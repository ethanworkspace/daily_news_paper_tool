# 論文 05：Artificial Intelligence for Marine Functional Peptide Discovery: Challenges, Advances, and Future Perspectives.

- 日期：2026-11-08
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
海洋生物蘊藏豐富但未充分探索的生物活性肽，具治療、營養保健與生技應用潛力。傳統發現流程需採集、萃取、純化、結構鑑定與實驗驗證，耗時費力，難以有效覆蓋快速擴增的海洋序列空間。人工智慧近年進展為大規模序列分析、功能預測與候選優先排序提供新契機。本文旨在綜述 AI 驅動的海洋功能性肽發現最新進展，涵蓋資源、表示、機器/深度學習、蛋白質語言模型、生成式方法、基因組與宏基因組挖掘、結構感知預測策略，並討論代表性應用與現有限制，提供完整框架以理解 AI 如何支援海洋肽的發現與開發。

## 方法
本綜述依主題將文獻歸類為七大面向： 1. 肽資源蒐集：整理海洋微生物、動物蛋白體、藍菌生物合成路徑、宏基因組資料集等來源。 2. 計算表示：說明序列編碼（one‑hot、理化性質）、嵌入向量（蛋白質語言模型如 ESM、ProtBERT 產生的上下文嵌入）與圖結構表示。 3. 機器學習與深度學習方法：涵蓋傳統分類器、CNN、RNN、Transformer 架構用於功能分類、抗菌/抗癌活性預測。 4. 蛋白質語言模型：探討預訓練大模型在海洋肽序列上的微調與零樣本預測能力。 5. 生成式方法：介紹 VAE、GAN、擴散模型等用於從潛在空間生成新序列並優化理化性質。 6. 基因組與宏基因組挖掘：結合 antiSMASH、deepBGC 等工具識別生物合成基因簇，輔以 AI 預測產物肽序列。 7. 結構感知預測策略：整合 AlphaFold2/ColabFold 預測三維結構、分子對接與動力學模擬以評估結合親和力。 綜述並對比各類方法在輸入輸出定義、訓練目標（交叉熵、對比損失、生成對抗損失）、優化策略與推論流程上的異同，指出海洋特有序列多樣性對模型泛化的挑戰。

## 結果
綜述指出 AI 模型在功能預測準確度、生成新序列多樣性、基因簇挖掘召回率上均優於傳統統計方法；生成式模型已產出經實驗驗證具抗菌活性的海洋肽案例；結構感知流程提升標的選擇特異性。然而，摘錄未提供可驗證數字，僅以定性描述呈現各類方法的相對優勢與現有缺口。

## 限制與展望
主要限制在於：(1) 缺乏專屬海洋肽的大規模、高品質標註資料集，導致模型訓練與基準測試受限；(2) 多模態整合（序列、結構、化學、生物合成資訊）仍處早期，缺乏統一評估框架；(3) 現有基準多源自陸生或合成肽，海洋特有化學空間的泛化能力未充分驗證；(4) 計算預測與實驗驗證的閉環整合尚不成熟，候選肽的實際轉化率不明；(5) 模型可解釋性與潛在偏誤風險需進一步研究。未來方向包括建立海洋專用基準、發展多模態基礎模型、強化計算‑實驗迭代流程。
