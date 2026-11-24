# 論文 01：SegEarth-R1: Geospatial Pixel Reasoning via Large Language Model

- 日期：2026-10-29
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
遙感影像廣泛應用於環境監測、都市規劃與災害管理，但傳統工作流程多依賴固定分類體系的語意分割或需明確指令的指向分割，難以處理需結合空間脈絡、領域知識與隱性使用者意圖的複雜隱性查詢。本文提出「地理空間像素推理」新任務，允許模型從隱性自然語言查詢推理並產生目標區域遮罩。為支援此任務，作者建構首個大規模基準資料集 EarthReason，包含 5,434 張人工標註遮罩、超過 30,000 組隱性問答對、28 類場景、空間解析度 0.5m–153m，並從分類資料集（AID、fMoW）蒐集影像以避免資料洩漏。本文目標在於建立任務定義、提供基準資料，並提出針對遙感特性設計的基線模型 SegEarth-R1，整合階層視覺編碼器、大型語言模型解析指令、客製化遮罩生成器，解決超高解析度、多尺度物體與空間相關性推理等挑戰。

## 方法
SegEarth-R1 為語言引導分割基線，整合三大核心組件：(1) 階層視覺編碼器：提取多尺度視覺特徵，應對遙感影像極大尺度變化與密集小物體；(2) 大型語言模型（LLM）：解析隱性自然語言查詢，進行指令理解與推理；(3) 客製化遮罩生成器：針對空間相關性設計，直接查詢描述嵌入預測遮罩。 針對遙感領域特性，提出三項關鍵適配機制： - 激進視覺 Token 壓縮：針對超高解析度影像（高達 7617×7617），大幅減少視覺 Token 數量，降低計算負擔並保留關鍵空間資訊。 - 描述投影模組：將 LLM 輸出的語言描述嵌入與多尺度視覺特徵融合，建立跨模態對齊，支援隱性查詢所需的領域知識推理。 - 精簡遮罩預測管線：直接以描述嵌入查詢視覺特徵圖，避免額外解碼器，實現端到端像素級預測。 輸入為遙感影像與隱性自然語言問題，輸出為目標區域二值遮罩。訓練目標、損失函數與最佳化策略於摘錄中未明確說明。推理流程：影像經視覺編碼器提取多尺度特徵，經 Token 壓縮後與 LLM 解析的指令嵌入經描述投影模組融合，最後由遮罩生成器直接查詢融合特徵產生遮罩。與既有方法差異在於：首創支援隱性查詢推理的地理空間像素推理任務；模組專為遙感超高解析度、多尺度與空間相關性設計；採用分類資料集來源並人工標註，避免現有分割資料集的資料洩漏風險。

## 結果
摘錄未提供可驗證數字。作者報告 SegEarth-R1 在 EarthReason 推理分割任務與現有指向分割資料集上達到最先進效能，顯著優於傳統分割方法與其他基於 LLM 的分割基線。定性結論顯示：模型能處理隱性查詢（如依坡度、植被覆蓋、基礎設施鄰近度推測山崩風險區）、適應多樣空間解析度與影像尺寸、支援空目標情況（隱性目標不在影像中），並在未見類別上展現泛化能力。消融實驗與案例分析細節於摘錄中未提供。

## 限制與展望
資料集僅涵蓋 28 類場景，空間解析度雖廣但仍受限於 AID 與 fMoW 分類資料集分佈；人工標註成本高，資料規模（5,434 張）相對自然影像推理資料集較小；問答對由 GPT-4o 生成可能引入偏差；模型依賴 LLM 進行指令解析，推理延遲與計算資源需求較大；激進 Token 壓縮可能遺失精細空間細節；未針對即時部署、邊緣裝置或極端天氣/雲霧干擾情境驗證。後續研究可擴展類別與地理覆蓋、探索輕量化架構、引入多時相與多光譜資訊、改進隱性查詢生成品質與評估指標。
