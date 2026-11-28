# 論文 01：Impression-R1 for radiological impression generation with multicenter benchmarking and prospective evaluations.

- 日期：2026-10-28
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-28T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43099050/
- PDF：
- DOI：10.1038/s41467-026-79102-7
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1695（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Radiological impressions are critical for clinical decision-making, yet expertise is unevenly distributed, and current large language models lack domain-specific reliability. We develop and evaluate Impression-R1, a domain-specialized large reasoning model for radiological impression generation, trained through an Imitation-Reasoning-Reinforcement pipeline integrating large-scale supervised learning, clinically conditioned reasoning, and radiology-aware reward optimization. Across 11,884 cases from six institutions and three public datasets spanning imaging modalities, anatomical regions, and diseases, including cross-lingual testing on English-language benchmarks, Impression-R1 outperforms or matches state-of-the-art general-purpose models. In a 200-case head-to-head evaluation, Impression-R1 shows stronger objective agreement with institution-derived reference impressions than all participating radiologists and subjective performance within the range of less-experienced radiologists under the study evaluation framework. Prospectively, radiologists rate its reasoning and clinical relevance highly. In a randomized within-reader study of 360 interpretations, AI assistance improves report quality (adjusted difference 0.28, 95% CI, 0.10-0.46) and reduces completion time by 27% (95% CI, 19.0%-33.9%); harmlessness scores are not significantly different (adjusted difference 0.08, 95% CI, -0.11-0.28). Here we show that Impression-R1 exemplifies a clinically informed framework for developing and evaluating domain-specialized reasoning models and can improve radiological reporting quality and efficiency, while requiring continued validation before broader clinical deployment.

## 背景與目的
放射科印象報告對臨床決策至關重要，但專業知識分布不均，現有大型語言模型缺乏領域特定可靠性。本研究旨在開發並驗證 Impression-R1，一個針對放射印象生成的領域專用大型推理模型，透過模仿‑推理‑強化三階段訓練管線，整合大規模監督學習、臨床條件推理與放射科感知獎勵優化，以提升報告品質與效率，並進行多中心、多模態、跨語言的基準測試與前瞻性評估。

## 方法
問題設定為給定影像檢查的發現段落，生成結構化印象。輸入為多機構、多模態（CT、MRI、X 光等）與多解剖部位的放射報告文本，輸出為印象段落。模型架構未於摘錄中詳細描述，僅知為領域專用大型推理模型。訓練管線包含三階段：(1) 模仿階段：以 11,884 例來自六家機構與三個公開資料集的大規模監督資料進行預訓練/微調，涵蓋多種疾病與跨語言（英文）基準；(2) 推理階段：引入臨床條件推理機制，使模型能依臨床邏輯串聯發現並產生推理鏈；(3) 強化階段：設計放射科感知獎勵函數，針對臨床相關性、準確性與無害性進行獎勵優化。資料前處理與特徵表示細節、具體損失函數、優化器設定、推理解碼策略等技術細節在提供摘錄中未公開。推論流程為單輪生成，並以機構衍生的參考印象作為客觀一致性評估基準。與既有方法的關鍵差異在於整合臨床推理條件與放射科專用獎勵的三階段訓練，而非單純監督微調。

## 結果
在 11,884 例多中心測試中，Impression-R1 優於或匹配當前最先進通用模型。200 例頭對頭評估顯示，其與機構參考印象的客觀一致性優於所有參與放射科醫師，主觀表現處於經驗較淺醫師範圍內。前瞻性評估中，放射科醫師對其推理與臨床相關性給予高分。隨機化讀者內研究（360 例）顯示，AI 協助使報告品質提升（調整差異 0.28，95% CI 0.10‑0.46），完成時間縮減 27%（95% CI 19.0%‑33.9%），無害性分數無顯著差異（調整差異 0.08，95% CI -0.11‑0.28）。

## 限制與展望
摘錄未提供模型架構、參數量、具體損失函數、超參數等技術細節，難以評估可重現性。評估雖涵蓋多中心與跨語言，但樣本數與機構數仍有限，且前瞻性研究僅為單盲、讀者內設計，可能存在選擇偏誤。無害性指標未達統計顯著改善，長期臨床安全性與泛化至其他語言、罕見疾病仍待驗證。部署前需進一步進行大規模、多中心、隨機對照試驗，並建立持續監測與模型更新機制。
