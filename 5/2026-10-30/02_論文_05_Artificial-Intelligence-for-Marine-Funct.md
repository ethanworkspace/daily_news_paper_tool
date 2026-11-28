# 論文 05：Artificial Intelligence for Marine Functional Peptide Discovery: Challenges, Advances, and Future Perspectives.

- 日期：2026-10-30
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
海洋生物蘊藏大量具生物活性的功能性胜肽，可應用於藥物、營養補充劑與生技產品。傳統發現流程需經採集、萃取、純化、結構鑑定與實驗驗證，耗時費力，難以應對快速擴增的海洋序列空間。人工智慧近年在大規模序列分析、功能預測與候選優先排序上展現優勢，能加速胜肽發現。本文為綜述，旨在整理 AI 驅動海洋功能性胜肽發現的最新進展，涵蓋資源、表示、機器/深度學習、蛋白質語言模型、生成式方法、基因組與宏基因組挖掘、結構感知預測等，並討論代表性應用與現有限制，提供完整框架指導後續研究。

## 方法
本綜述將 AI 輔助海洋胜肽發現的方法體系化為七大面向：(1) 勝肽資源蒐集：整理來自海洋微生物、動物蛋白質體、藍菌生物合成路徑、宏基因組數據集等公開與專屬資料庫，建立序列與功能標註的基礎語料。(2) 計算表示：採用氨基酸組成、理化性質、one-hot、k-mer、嵌入向量（如 ProtBERT、ESM、ProtT5 等蛋白質語言模型產生的上下文嵌入）將變長序列轉為定長特徵。(3) 機器學習與深度學習預測模型：傳統分類器（SVM、隨機森林）結合手工特徵，以及 CNN、RNN、Transformer、圖神經網絡等端到端架構，輸入序列或嵌入，輸出生物活性類別或活性強度。(4) 蛋白質語言模型微調：利用大規模蛋白質語料預訓練的模型，在海洋胜肽標註集上進行微調或提示學習，提升少樣本泛化能力。(5) 生成式方法：變分自編碼器、生成對抗網絡、擴散模型或基於 Transformer 的自回歸生成器，條件於目標功能或結構約束，從潛在空間採樣新序列。(6) 基因組與宏基因組挖掘：結合反饋式基因簇預測工具與深度學習分類器，從組裝後的基因組/宏基因組中識別潛在生物合成基因簇並推導前體胜肽。(7) 結構感知預測：引入 AlphaFold2、RoseTTAFold 或等效結構預測模組，獲得三維構象，再以幾何深度學習（如 SE(3)-Transformer）評估結合親和力或酶切位點。訓練目標多為交叉熵、焦點損失、對比損失或生成式負對數似然；優化採用 AdamW、學習率暖啟與余弦退火。推論流程依序為：資料清洗→表示編碼→模型預測/生成→結構建模→候選排序→實驗驗證規劃。與既有單一任務模型不同，本綜述強調多模態融合（序列、結構、化學、生物合成資訊）與跨資料集基準測試的必要性。

## 結果
本文為綜述，未呈現單一實驗的量化指標。摘錄未提供可驗證數字。作者定性總結指出：AI 方法已在抗菌、抗氧化、抗癌、抗高血壓等功能預測上達到與實驗相當的準確率；生成式模型能產出具新穎序列且經實驗驗證的候選胜肽；結構感知模組顯著提升結合位點預測；但跨資料集泛化、負樣本稀缺、實驗驗證率低仍為共同瓶頸。

## 限制與展望
綜述指出四大關鍵限制：(1) 缺乏專屬海洋胜肽基準數據集，現有資料多來自陸生生物或非標註序列，導致模型評估不具代表性。(2) 多模態融合仍處早期，序列、結構、化學性質與生物合成邏輯的聯同表示缺乏統一框架。(3) 基準測試不嚴謹，缺少統一分割、負樣本構建與統計顯著性檢定，難以公平比較。(4) 計算預測與實驗驗證脫節，候選勝肽的合成與活性測試成本高，導致閉環驗證稀少。潛在風險包括生成序列的毒性、免疫原性未被充分篩選，以及模型對罕見海洋分類群的泛化不確定。後續研究建議建立開放海洋胜肽資料庫、發展多模態預訓練模型、制定標準化評估協議，並推動計算-實驗迭代平台。
