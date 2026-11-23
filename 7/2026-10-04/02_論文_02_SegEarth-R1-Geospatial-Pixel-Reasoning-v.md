# 論文 02：SegEarth-R1: Geospatial Pixel Reasoning via Large Language Model

- 日期：2026-10-04
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
遙感影像廣泛應用於環境監測、城市規劃與災害管理，但傳統語義分割與指向分割僅支援固定類別與明確指令，難以處理需結合空間脈絡、領域知識與隱性意圖的複雜查詢。本文提出「地理空間像素推理」新任務，允許使用隱性自然語言查詢並推理出目標區域遮罩。為支援此任務，作者建構首個大規模基準資料集 EarthReason，包含 5,434 張人工標註遮罩、超過 30,000 組隱性問答對、28 類場景、解析度 0.5m–153m、影像尺寸 1232²–7617²，並切分訓練/驗證/測試集（2,371/1,135/1,928）。研究目標在於設計能整合大型語言模型推理能力與遙感影像特性的基線模型 SegEarth-R1，填補隱性查詢推理與像素級分割的空白。

## 方法
SegEarth-R1 採三階段架構：(1) 階層式視覺編碼器提取多尺度影像特徵，針對超高解析度遙感影像引入積極視覺 token 壓縮機制，大幅降低 token 數量以適應長序列輸入；(2) 大型語言模型（LLM）負責指令解析，將隱性自然語言問題轉換為語言嵌入；(3) 專用遮罩生成器進行空間相關性建模。核心創新模組包含：描述投影模組，將 LLM 輸出的語言嵌入與視覺編碼器的多尺度特徵進行融合，產生描述嵌入；精簡遮罩預測管線，直接以描述嵌入查詢視覺特徵圖，輸出目標遮罩，避免額外解碼器帶來的計算負擔。訓練目標結合語言指導的分割損失（如 Dice + BCE）與 LLM 的指令遵循目標，採端到端優化。推理時，輸入影像與隱性問題，經視覺編碼器、LLM 解析、描述投影、遮罩生成器依序產生二值遮罩。與既有 LLM 分割方法（如 LISA、GeoPix）相比，關鍵差異在於：首創支援隱性查詢推理、針對遙感影像尺度變化與空間相關性設計 token 壓縮與描述投影、並直接以描述嵌入查詢遮罩，簡化管線。

## 結果
摘錄未提供可驗證數字。作者報告 SegEarth-R1 在 EarthReason 推理分割與現有指向分割基準上達到最先進性能，顯著優於傳統分割方法與其他 LLM 基礎分割模型。定性結論顯示模型能正確理解隱性查詢（如「易發生山崩區域」），結合坡度、植被、基礎設施鄰近度等空間脈絡輸出合理遮罩，且在空目標樣本上表現穩健。

## 限制與展望
資料集規模雖為領域首創，但 5,434 張影像可能不足以涵蓋所有地理場景與罕見類別；標註成本高、依賴專家人工標註，擴展性受限。方法端未在摘錄中揭露消融實驗細節、token 壓縮率具體數值、訓練超參數與計算資源需求，難以評估各模組貢獻。評估僅涵蓋 EarthReason 及部分指向分割資料集，泛化至其他遙感任務（如變化偵測、目標偵測）尚未驗證。部署面臨超高解析度影像記憶體壓力與 LLM 推理延遲問題。後續研究可探索更高效的視覺壓縮、多模態推理增強、以及與時序資料結合。
