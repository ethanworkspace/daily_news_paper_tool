# 論文 03：Trans-MMVAE: A transformer-based multi-modal variational autoencoder for interpretable multi-omics target prioritization in allergic rhinitis.

- 日期：2026-10-09
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
過敏性鼻炎（AR）呈現高度異質的多組學特徵，傳統深度學習方法常缺乏生物學脈絡，難以直接轉化為臨床決策。現有計算框架多專注於單一組學或單一標靶重發現，缺乏整合臨床評分與多層次分子資料的能力，導致難以揭示脂質代謝與免疫路徑的交互作用。本研究旨在建立一個可解釋的多模態變分自編碼器，結合臨床與多組學資料，將潛在空間映射至臨床嚴重度評分，從而系統性地優先排序潛在治療標靶，並生成可驗證的機制假設。

## 方法
根據摘要所述，Trans-MMVAE 採用 Transformer 架構作為多模態編碼器，分別處理臨床表型與多組學（如轉錄體、代謝體等）輸入，將其投影至共享的潛在空間。模型核心包含：(1) 多模態 Transformer 編碼器，捕捉跨模態的長距離依賴與特徵交互；(2) 變分自編碼器結構，透過重建損失與 KL 散度約束學習連續潛在表示；(3) 專用回歸頭，直接將高維潛在向量映射至臨床評分（如症狀嚴重度），實現分子特徵與表型的橋接；(4) 跨模態評分機制，整合各模態潛在表示以優先排序關鍵酵素（如 KMO、HAAO）與細胞因子（TSLP、IL33）。訓練目標推測為重建損失、KL 正則化與回歸損失的加權總和，但摘錄未提供具體損失權重、優化器、學習率或訓練輪數等超參數。推論階段先經編碼器獲得潛在向量，再由回歸頭輸出臨床評分，並依跨模態評分輸出標靶優先序。與既有方法的關鍵差異在於：強調可解釋性、直接映射臨床評分、並系統性揭示脂質代謝與色胺酸-犬尿氨酸路徑的交互網絡。

## 結果
在真實 AR 群隊中，Trans-MMVAE 成功重現經典脂質代謝標靶 ALOX15 與 ALOX5，作為生物學陽性對照驗證模型從高雜訊中提取真實功能訊號的能力。進一步透過跨模態評分，模型優先排序了犬尿氨酸路徑關鍵酵素 KMO 與 HAAO，並將其定位為連結脂質失調與 Th2 免疫激活的潛在機制橋樑；上皮源性細胞因子 TSLP 與 IL33 亦被識別為該整合網絡下游的協同節點。模型在交叉驗證與獨立外部群隊均表現一致，但摘錄未提供可驗證的數值指標（如 AUC、準確率、相關係數等）。

## 限制與展望
目前僅有摘要層級描述，缺乏模型架構細節（如 Transformer 層數、注意力頭數、潛在維度）、損失函數具體形式、超參數設定、資料集樣本數、組學模態種類與前處理流程，亦未給出定量實驗指標與統計顯著性檢定。評估僅限於單一疾病（AR）且外部驗證群隊規模未知，泛化性仍待多中心大規模研究確認。潛在風險包括：模型可能過擬合特定群隊、潛在空間解釋性依賴人工標註、跨模態評分機制缺乏獨立實驗驗證。後續研究需補充完整方法細節、擴大樣本量、進行功能實驗驗證預測標靶，並探討模型在其他異質性疾病中的適用性。
