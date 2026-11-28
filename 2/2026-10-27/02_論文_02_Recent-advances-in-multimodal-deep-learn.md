# 論文 02：Recent advances in multimodal deep learning for breast cancer diagnosis using data fusion vision language models and foundation models

- 日期：2026-10-27
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Discover Artificial Intelligence
- Venue：Discover Artificial Intelligence
- 發布時間：2026-10-27T00:00:00+00:00
- URL：https://doi.org/10.1007/s44163-026-02625-x
- PDF：https://link.springer.com/content/pdf/10.1007/s44163-026-02625-x.pdf
- DOI：10.1007/s44163-026-02625-x
- arXiv：
- 影響指標：2yr_mean_citedness=21.69, h_index=55, i10_index=365 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Discover Artificial Intelligence
- 引用數：0
- 解析程度：fulltext / pdf
- 全文來源：https://link.springer.com/content/pdf/10.1007/s44163-026-02625-x.pdf
- 全文字數：155750（pages=45, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Breast cancer remains one of the most prevalent cancers worldwide, underscoring the need for reliable diagnostic approaches that can support accurate and timely clinical assessment. Recent advances in artificial intelligence, particularly deep learning, have enabled the development of multimodal systems that integrate complementary data sources, including medical images, radiology reports, clinical information, and genomic data. Such approaches aim to exploit information that may not be fully captured by a single modality and have shown promising performance in breast cancer diagnosis and related prediction tasks. This review provides a comprehensive and critical overview of multimodal deep learning approaches for breast cancer diagnosis published between January 2021 and September 2026. It examines the principal data modalities used in multimodal systems, including mammography, ultrasound, magnetic resonance imaging, histopathology, radiology reports, clinical information, and genomic data. The review also analyzes major multimodal fusion strategies and traces the evolution of the field from conventional machine-learning and radiomics-based approaches to deep learning architectures, vision-language models, and foundation models. Recent multimodal models are discussed according to the data modalities employed, model architectures, fusion strategies, clinical or diagnostic tasks, datasets, and reported performance. Particular attention is given to approaches integrating medical imaging with radiology reports and other textual information, including emerging vision-language and foundation-model-based methods for breast imaging. Publicly available datasets and multimodal resources used in breast cancer research are also summarized and compared. Despite recent progress, important challenges remain, including the limited availability of large-scale multimodal datasets, restricted access to paired image–report datasets, missing modalities, limited external validation, uncertainty estimation, explainability, fairness, generalizability, and barriers to clinical workflow integration. Current evidence is still predominantly retrospective and technical; therefore, reported improvements in model performance should not be interpreted as demonstrated clinical benefit without prospective validation. Future research should focus on robust multimodal foundation models, explainable and trustworthy artificial intelligence, federated and privacy-preserving learning, standardized external validation, and prospective clinical evaluation. Overall, this review provides an updated synthesis of methodological developments, multimodal data integration strategies, emerging vision-language and foundation models, and translational challenges in multimodal artificial intelligence for breast cancer diagnosis.

## 背景與目的
乳癌為全球盛行率最高的癌症之一，早期精準診斷對臨床決策至關重要。傳統電腦輔助診斷系統多依賴單一影像模態（如乳房攝影、超音波、MRI 或病理切片），難以完整捕捉疾病異質性與患者特異性資訊。近年深度學習推動多模態融合發展，整合影像、放射科報告、臨床變數與基因組資料，但現有綜述多聚焦影像分類或特定融合策略，缺乏對視覺語言模型（VLM）與基礎模型在乳癌診斷中應用的系統性檢視。本文旨在提供 2021 年 1 月至 2026 年 9 月間多模態深度學習乳癌診斷研究的更新批判性綜述，涵蓋主要資料模態、融合策略、模型架構、公開資料集、新興 VLM 與基礎模型，並深入探討缺失模態、外部驗證、不確定性、可解釋性、公平性、泛化能力、隱私保護及臨床工作流整合等轉譯挑戰，以區分技術性能提升與臨床效益證據，指引未來研究優先方向。

## 方法
本研究採敘述性綜述方法，檢索範圍為 2021 年 1 月至 2026 年 9 月發表的多模態深度學習乳癌診斷文獻。問題設定為：系統性梳理並批判性分析多模態資料來源、融合策略、模型架構演進、公開資料集現況、視覺語言模型與基礎模型最新進展，以及臨床轉譯障礙。輸入為文獻庫檢索結果，輸出為結構化綜述框架。整體架構分為：(1) 資料模態分類：乳房攝影、超音波、MRI、組織病理影像、放射科報告、結構化臨床資訊、基因組資料；(2) 融合策略分析：早期融合（特徵層級串接）、晚期融合（決策層級集成）、混合融合（跨模態注意力、對比學習預訓練等）；(3) 模型演進脈絡：從傳統機器學習與放射組學手工特徵，至卷積神經網路、Transformer 混合架構，再到視覺語言模型（如影像-文本對比預訓練）與大型多模態基礎模型；(4) 公開資料集彙總與比較；(5) 新興 VLM 與基礎模型在病灶特徵化、多模態表徵學習、自動報告生成、診斷決策支援等任務的應用；(6) 關鍵挑戰與未來方向討論。核心分析模組包含：模態異質性表示學習、跨模態對齊機制、缺失模態處理、不確定性量化、可解釋性方法、聯邦學習隱私保護框架。與既有綜述的關鍵差異在於：整合影像-報告融合、乳癌專用 VLM、多模態基礎模型、公開多模態資源比較，並批判性檢視外部驗證、公平性、臨床工作流整合等轉譯議題，而非僅著重技術指標。

## 結果
綜述指出：多模態系統主要整合影像與結構化臨床資料、影像與放射科報告、影像與基因組資料等組合；融合策略從早期特徵串接演進至跨模態注意力機制與對比語言-影像預訓練。公開資料集（如 CBIS-DDSM、BUSI、BreastPathQ 等）多為單一模態或配對樣本有限，大規模配對影像-報告資源稀缺。視覺語言模型與基礎模型在病灶分類、報告生成、多模態檢索等任務展現潛力，但實證多為回顧性技術驗證。主要定性結論：(1) 多模態融合優於單一模態；(2) 缺乏大規模、多中心、多模態配對資料集；(3) 外部驗證極少，泛化能力未經充分證實；(4) 不確定性估計、可解釋性、公平性研究不足；(5) 臨床工作流整合障礙顯著。摘錄未提供可驗證數字。

## 限制與展望
本綜述屬敘述性非系統性檢索，可能遺漏相關文獻；覆蓋時效至 2026 年 9 月，後續進展未納入。領域層面限制：現有證據以回顧性技術研究為主，缺乏前瞻性臨床試驗驗證模型效益；資料集異質性大、標註品質參差、隱私法規限制資料共享；缺失模態處理、不確定性量化、可解釋性、公平性評估方法尚未標準化；聯邦學習與隱私保護框架在臨床部署可行性待證；外部驗證與標準化評估基準缺失。未來研究應聚焦：穩健多模態基礎模型建構、可信賴 AI、聯邦隱私保護學習、標準化外部驗證協議、前瞻性臨床評估。依目前可取得資料，無法確認具體模型在真實臨床環境的效益與風險。
