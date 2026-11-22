# 論文 03：SegEarth-R1: Geospatial Pixel Reasoning via Large Language Model

- 日期：2026-11-20
- 來源層級：Tier 3
- 期刊/會議/來源：ArXiv
- Venue：ArXiv
- 發布時間：2025-04-13T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/eab0e7a7082dd467eee45b66d15df841da8ccec2
- PDF：
- DOI：10.48550/arxiv.2504.09644
- arXiv：2504.09644
- 影響指標：N/A (preprint)
- 影響指標來源：preprint (not peer-reviewed journal/conference)
- 引用數：60
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2504.09644
- 全文字數：66094（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/earth-insights/SegEarth-R1
- 配對 Repo：earth-insights/SegEarth-R1

## 摘要
Remote sensing has become critical for understanding environmental dynamics, urban planning, and disaster management. However, traditional remote sensing workflows often rely on explicit segmentation or detection methods, which struggle to handle complex, implicit queries that require reasoning over spatial context, domain knowledge, and implicit user intent. Motivated by this, we introduce a new task, \ie, geospatial pixel reasoning, which allows implicit querying and reasoning and generates the mask of the target region. To advance this task, we construct and release the first large-scale benchmark dataset called EarthReason, which comprises 5,434 manually annotated image masks with over 30,000 implicit question-answer pairs. Moreover, we propose SegEarth-R1, a simple yet effective language-guided segmentation baseline that integrates a hierarchical visual encoder, a large language model (LLM) for instruction parsing, and a tailored mask generator for spatial correlation. The design of SegEarth-R1 incorporates domain-specific adaptations, including aggressive visual token compression to handle ultra-high-resolution remote sensing images, a description projection module to fuse language and multi-scale features, and a streamlined mask prediction pipeline that directly queries description embeddings. Extensive experiments demonstrate that SegEarth-R1 achieves state-of-the-art performance on both reasoning and referring segmentation tasks, significantly outperforming traditional and LLM-based segmentation methods. Our data and code will be released at https://github.com/earth-insights/SegEarth-R1.

## 背景與目的
遙感影像廣泛應用於環境監測、城市規劃與災害管理，但傳統語義分割與指向分割依賴固定類別與明確指令，難以處理隱性推理查詢。本文提出地理空間像素推理任務，建構首個大規模基準 EarthReason（5,434 張影像、超過 3 萬組隱性問答），並提出 SegEarth-R1 基線模型，整合層級視覺編碼器、大型語言模型解析指令與專用遮罩生成器，針對超高解析度影像進行激進視覺 token 壓縮、描述投影模組融合多尺度特徵，實現語言引導的像素級推理。

## 方法
SegEarth-R1 採用層級視覺編碼器提取多尺度特徵，經由激進視覺 token 壓縮降低超高解析度影像的 token 數量；大型語言模型負責解析自然語言指令並產生描述嵌入；描述投影模組將語言嵌入與多尺度視覺特徵對齊融合；最後以精簡的遮罩預測管線直接查詢描述嵌入，輸出目標區域的像素級遮罩，整個流程為端到端訓練與推理。

## 結果
摘錄未提供可驗證數字。論文指出經大量實驗，SegEarth-R1 在地理空間像素推理與指向分割兩項任務上均達到最先進表現，顯著優於傳統分割方法與其他基於 LLM 的分割基線。

## 限制與展望
資料集僅涵蓋 28 類場景與 5,434 張影像，解析度範圍雖廣但樣本數相對有限；模型對極端尺度變化、密集小目標及複雜空間關聯的泛化能力仍待進一步驗證；且依賴大型語言模型推理，計算成本與部署門檻較高。
