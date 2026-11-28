# 論文 03：CADS: a comprehensive anatomical dataset and segmentation for whole-body anatomy in computed tomography.

- 日期：2026-10-28
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-28T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43098994/
- PDF：
- DOI：10.1038/s41467-026-78732-1
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1297（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Volumetric computed tomography (CT) segmentation supports quantitative image analysis, but most AI-based methods remain organ-specific, with fragmented models, inconsistent label definitions, and heterogeneous training and evaluation protocols. Here we present CADS, a unified data-model framework for scalable and generalizable whole-body CT segmentation. We construct a SNOMED-CT-referenced anatomical label space harmonizing heterogeneous cohorts from over 100 imaging centers, yielding complete annotations of 167 structures across 22,022 CT volumes and markedly expanding anatomical coverage and scale beyond existing resources. To complete labels on sparsely annotated CTs, we combine self-training with shape-informed quality control based on neural implicit functions, curating high-quality pseudo-labels. Trained on this resource, CADS shows robust whole-body segmentation across distribution shifts and improved performance relative to state-of-the-art approaches across 18 public datasets. We further validate it in an independent, expert-reviewed real-world oncology cohort of 2864 CTs. The curated dataset, pretrained models, and user-friendly software together provide an accessible, reproducible foundation for large-scale anatomical segmentation and computational anatomy research.

## 背景與目的
體積計算斷層（CT）分割支援定量影像分析，但現有 AI 方法多為器官專用，模型碎片化、標籤定義不一、訓練與評估協議異質，導致跨資料集泛化困難。本研究旨在建立一個統一的資料‑模型框架 CADS，解決標籤空間不統一、大規模完整標註稀缺、以及模型在分佈偏移下表現不穩等核心缺口，為全身解剖結構的可擴展、可重現分割提供基礎設施。

## 方法
問題設定：輸入為 3D CT 體積，輸出為 167 解剖結構的體素級分割標籤。 整體架構：CADS 為統一資料‑模型框架，包含（1）標籤空間建構、（2）稀疏標註補全與品質控制、（3）大規模訓練與推論流程。 標籤空間：採用 SNOMED-CT 術語參考，整合超過 100 家影像中心的異質隊列，建立涵蓋 167 結構的統一標籤集，完成 22,022 例 CT 的完整標註。 稀疏標註補全：對僅部分結構有標註的體積，採用自訓練策略，結合基於神經隱式函數的形狀感知品質控制，產生高品質偽標籤，擴充訓練集覆蓋度。 訓練目標與最佳化：摘錄未詳細描述具體網路架構、損失函數或最佳化超參數，僅說明在整理後的大規模資料集上進行訓練以獲得整體分割模型。 推論流程：模型直接對新 CT 體積輸出 167 結構的分割圖，支援跨機構、跨協議的分佈偏移情境。 關鍵差異：以 SNOMED-CT 為錨點統一標籤定義、引入神經隱式函數輔助偽標籤品質控管、並釋出完整資料集、預訓練模型與易用軟體，形成可重現的全身分割基線。

## 結果
作者報告 CADS 在 18 個公開資料集上優於當前最先進方法，並經由獨立專家審核的 2,864 例真實腫瘤學隊列驗證，展現跨分佈偏移的穩健全身分割能力。摘錄未提供可驗證的具體數值指標（如 Dice、HD95），僅能觀察到定性結論：整體解剖覆蓋範圍與規模顯著擴大、偽標籤品質控制有效提升訓練資料完整性、模型在多中心、多協議下表現一致。

## 限制與展望
資料層面：雖整合超過 100 中心、22,022 例 CT，但未說明各解剖結構的標註平衡度、罕見病變或病理變異的覆蓋情況。方法層面：摘錄未揭露具體網路架構、損失函數、訓練超參數與推論速度，難以評估計算效率與部署可行性。評估層面：缺乏定量指標與統計顯著性檢定，僅以定性優於 SOTA 陳述，外部驗證僅限單一腫瘤學隊列。潛在風險包括偽標籤錯誤傳播、標籤空間擴展時的語義一致性維護。後續研究建議：公開完整訓練細節、提供標準化基準測試、探索持續學習以納入新結構與病理標註。
