# 論文 03：Trans-MMVAE: A transformer-based multi-modal variational autoencoder for interpretable multi-omics target prioritization in allergic rhinitis.

- 日期：2026-10-01
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
過敏性鼻炎（AR）呈現高度異質的多組學景觀，傳統深度學習方法常缺乏生物學脈絡，難以轉化為臨床干預。現有方法多為通用資料挖掘工具，缺乏針對多模態臨床與組學資料整合並可解釋的目標發現框架。本研究旨在提出 Trans‑MMVAE，結合 Transformer 與多模態變分自編碼器，直接整合異質臨床與多組學資料，並透過專用回歸頭將潛在空間映射至臨床評分，建立可解釋的多組學標靶優先排序方法。

## 方法
問題設定：輸入為多模態資料，包含臨床評分（如總鼻部症狀分數）與多組學測量（脂質代謝、轉錄體、蛋白質組等），輸出為潛在空間表示與對應臨床評分預測，並產生跨模態重要性分數以優先排序候選基因。模型架構：採用 Transformer 編碼器分別處理各模態序列化特徵，透過多頭自注意力捕捉模態內與跨模態依賴；各模態編碼器輸出均值與對數方差，構成變分自編碼器的概率潛在變數，再經由重參數化取樣獲得共享潛在向量。核心模組：1) 模態專屬 Transformer 編碼器；2) 共享潛在空間的 VAE 結構，損失包含重建損失（各模態解碼器重建原始特徵）與 KL 散度正則化；3) 專用回歸頭（全連接層）接在潛在向量後，直接預測臨床評分，損失採用均方誤差；總損失為重建損失、KL 項與回歸損失的加權和。資料前處理：各組學特徵經標準化、缺失值插補，並依生物學路徑分組輸入 Transformer。訓練策略：使用 Adam 優化器，學習率衰減，採用早停法；交叉驗證與獨立外部隊列驗證。推論流程：將新樣本經編碼器得到潛在向量，送入回歸頭得臨床分數，並利用解碼器權重與注意力權重計算跨模態貢獻分數，進而對基因進行排序。關鍵差異：不同於單純多模態 VAE 或黑箱深度網路，Trans‑MMVAE 結合 Transformer 的全域注意力與可解釋回歸頭，實現從分子特徵到表型嚴重度的直接映射，並提供跨模態重要性評估。

## 結果
摘錄未提供可驗證數字。作者報告在真實 AR 隊列中，Trans‑MMVAE 成功重現經典脂質代謝標靶 ALOX15 與 ALOX5，作為生物學陽性對照驗證模型從嚴重雜訊中提取真實功能訊號的能力。進一步透過跨模態整合評分，模型擴展了這些已知標靶的交互網絡，揭示脂質代謝與色氨酸-犁氨酸途徑的多層代謝-免疫交談，系統性優先排序出犁氨酸途徑關鍵酵素 KMO 與 HAAO，並將上皮源性細胞因子 TSLP、IL33 識別為下游協同節點。模型在交叉驗證折疊與獨立外部隊列均表現一致，確立了從單一標靶重發現轉向系統性多組學景觀繪製的新範式。

## 限制與展望
研究僅使用有限數量的 AR 隊列，樣本量與族群多樣性不足，外部驗證僅單一獨立隊列，泛化能力仍待大規模多中心研究確認。模型雖提供跨模態重要性分數，但解釋機制依賴注意力權重與解碼器參數，缺乏實驗層面的因果驗證。訓練目標中回歸損失權重設定未公開，可能影響潛在空間與臨床評分的對齊。此外，缺乏與其他多模態整合基線（如 MOFA、Multi‑Omics VAE）的定量比較，消融實驗細節未揭露。部署上需考慮異質資料前處理管線標準化與計算資源需求。後續研究應擴大隊列、引入因果推論、進行系統性基線比較與消融分析。
