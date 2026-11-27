# 論文 03：Trans-MMVAE: A transformer-based multi-modal variational autoencoder for interpretable multi-omics target prioritization in allergic rhinitis.

- 日期：2026-10-12
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Science progress
- Venue：Science progress
- 發布時間：2026-01-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43017800/
- PDF：
- DOI：10.1177/00368504261507153
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2308（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
BackgroundAllergic rhinitis (AR) presents a highly heterogeneous multi-omics landscape, necessitating advanced computational frameworks to uncover underlying disease mechanisms and facilitate precise clinical interventions. Conventional deep learning approaches often lack the biological context required for translational application.MethodsWe propose Trans-MMVAE, a transformer-based multi-modal variational autoencoder engineered specifically as an interpretable computational framework for multi-omics target discovery rather than a general data mining tool. Our architecture directly integrates heterogeneous clinical and multi-omics data. By utilizing a specialized Regression Head, the framework maps high-dimensional latent space representations directly to clinical scores, effectively bridging the gap between molecular profiles and phenotypic severity.ResultsUpon rigorous evaluation with real-world AR cohorts, Trans-MMVAE accurately recaptured canonical lipid metabolism targets, particularly ALOX15 and ALOX5. Serving as robust biological positive controls, these identifications validated the model's capacity to isolate true functional signals from severe multi-omics noise. Crucially, the framework expanded the interactome of these known targets by delineating the multi-layered metabolic-immune crosstalk linking lipid metabolism and the tryptophan-kynurenine pathway in the context of AR. Through integrated cross-modal scoring, the model systematically prioritized KMO and HAAO-enzymes in the kynurenine pathway previously implicated in broader allergic inflammation-and positioned them as potential mechanistic bridges between lipid dysregulation and Th2 immune activation in AR specifically. Epithelial-derived cytokines TSLP and IL33 were concurrently identified as synergistic downstream nodes within this integrated network.ConclusionBy shifting the paradigm from single-target rediscovery to systemic multi-omics landscape mapping, Trans-MMVAE demonstrates consistent performance across cross-validation folds and an independent external cohort. It establishes a systematic computational methodology for multi-modal data integration that generates testable mechanistic hypotheses regarding metabolic-immune crosstalk in AR, which require validation in larger, multi-center studies.

## 背景與目的
過敏性鼻炎（AR）呈現高度異質的多組學景觀，傳統深度學習方法常缺乏生物學脈絡，難以直接轉化為臨床干預。現有計算框架多為通用資料挖掘工具，缺乏將分子特徵與臨床嚴重度量化連結的機制。本研究旨在建立一個可解釋的多模態變分自編碼器，專門用於多組學標靶發現，整合臨床與多組學異質資料，並透過迴歸頭將潛在空間映射至臨床評分，填補分子表型與表型嚴重度之間的鴻溝。

## 方法
Trans-MMVAE 採用基於 Transformer 的多模態變分自編碼器架構。輸入包含臨床評分與多組學資料（如脂質代謝、色胺酸-犁氨酸途徑等），經過各模態專屬編碼器映射至共享潛在空間。核心模組為多頭自注意力機制，捕捉跨模態特徵依賴關係；變分推斷層對潛在變數施加高斯先驗，並以證據下界（ELBO）作為訓練目標，包含重建損失與 KL 散度正則化。特別設計的 Regression Head 直接從潛在表示預測臨床嚴重度分數，實現分子特徵至表型的端到端映射。推論階段先將新樣本編碼至潛在空間，再經 Regression Head 輸出臨床分數，並利用跨模態評分機制對基因/蛋白進行優先排序。與既有方法差異在於：(1) 以 Transformer 處理異質模態序列化表示；(2) 明確引入臨床迴歸頭實現可解釋的標靶優先化；(3) 強調生物學正向對照（ALOX15、ALOX5）驗證模型捕捉真實功能訊號。

## 結果
在真實 AR 群隊交叉驗證與獨立外部群隊中，模型成功重現經典脂質代謝標靶 ALOX15 與 ALOX5，作為生物學正向對照證明其從嚴重雜訊中提取真實訊號的能力。進一步透過跨模態整合評分，系統性優先化了犁氨酸途徑關鍵酵素 KMO 與 HAAO，並將其定位為連結脂質失調與 Th2 免疫激活的潛在機制橋樑；上皮源性細胞激素 TSLP 與 IL33 亦被識別為該整合網路下游協同節點。摘錄未提供可驗證數字，僅呈現定性結論。

## 限制與展望
目前公開資料僅含摘要層級描述，缺乏模型超參數、訓練細節、損失函數具體形式、資料集樣本數、基線方法名稱及量化指標（如 AUC、精確率）等關鍵資訊，無法全面評估泛化能力與計算效率。外部驗證僅限單一獨立群隊，樣本量與多中心多樣性未說明，潛在選擇偏誤風險存在。後續研究需於更大規模、多中心隊列中驗證 KMO、HAAO、TSLP、IL33 等預測標靶的功能性，並探討模型在不同種族、嚴重度分層下的穩健性與可解釋性。
