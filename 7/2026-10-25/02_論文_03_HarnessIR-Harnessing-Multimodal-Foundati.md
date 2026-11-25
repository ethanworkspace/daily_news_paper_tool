# 論文 03：HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration

- 日期：2026-10-25
- 來源層級：Tier 3
- 期刊/會議/來源：arXiv
- Venue：arXiv preprint
- 發布時間：2026-10-07T00:00:00+00:00
- URL：https://arxiv.org/abs/2610.10133
- PDF：https://arxiv.org/pdf/2610.10133
- DOI：10.48550/arxiv.2610.10133
- arXiv：2610.10133
- 影響指標：N/A (repository/preprint)
- 影響指標來源：Repository source has no journal impact factor
- 引用數：1
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2610.10133
- 全文字數：95887（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/PolyU-VCLab/HarnessIR
- 配對 Repo：PolyU-VCLab/HarnessIR

## 摘要
Real-world low-quality images suffer from complex mixed degradations, including but not limited to noise, blur, atmospheric effects, etc. Recent agentic methods usually model real-world image restoration (Real-IR) as a sequential tool calling problem over task-specific single-degradation restoration models. This paradigm, however, is fundamentally limited because complex real-world degradations cannot be cleanly undone degradation by degradation, and the tool used for task-specific models caps the capability of the agent system. In this work, we present HarnessIR, an agentic framework for Real-IR by harnessing a multimodal foundation model (MFM) as the executor. HarnessIR consists of five stages: perception and diagnosis, on-demand tool invocation, prompt composition, execution, and verification-driven refinement. Unlike prior agentic Real-IR methods that rely on tool chains assembled from task-specific models, HarnessIR feeds the restoration requirements, the perceptual diagnosis, and the evidence into an MFM that performs restoration in a single pass, followed by verification stages to determine whether the result warrants further processing. Under our harness, off-the-shelf MFMs handle restoration tasks remarkably well, achieving state-of-the-art results on the widely used MiO100 synthetic benchmark. More importantly, by exploiting the strong generalization ability of MFMs, HarnessIR delivers compelling restoration quality on challenging real-world scenes where previous agentic IR systems often struggle. Codes is available at https://github.com/PolyU-VCLab/HarnessIR.

## 背景與目的
真實世界低品質影像常包含雜訊、模糊、大氣效應等複雜混合退化，傳統單一退化修復方法與全能型模型多假設單一退化類型，難以處理耦合退化。近期代理式影像修復雖引入任務特定模型作為工具鏈，但將混合退化近似為序列化操作，導致資訊損失且工具泛化能力受限，於真實場景表現不佳。本文旨在解決此缺口，提出 HarnessIR，利用多模態基礎模型（MFM）作為執行器，結合感知診斷、按需工具調用、提示組合、單次執行與驗證驅動修正，釋放 MFM 強大泛化能力，實現通用真實世界影像修復。

## 方法
HarnessIR 採五階段流程：(1) 感知與診斷：凍結的視覺語言模型（VLM）作為診斷器，輸入低品質影像與使用者修復請求，輸出內容與退化診斷，並規劃需調用的輔助工具集（OCR、人臉偵測、深度估計、語意分割）。(2) 按需工具調用：依診斷結果執行輔助工具，取得影像特定證據（如辨識文字、人臉框、深度圖、分割圖），證據不直接送入執行器。(3) 提示組合：同一 VLM 扮演組合器，將原始影像、請求、診斷與結構化證據轉化為單一自然語言提示，內含退化處理指令、內容保留約束及空間條件（如依深度調整去霧強度），並融入領域知識需求（如去雨不移除路面積水）。(4) 執行：凍結的 MFM（如 Nano Banana 2、GPT-Image-2.5-Sunburst）接收原始影像與組合提示，單次生成修復結果。(5) 驗證驅動修正：驗證器（同 VLM 不同角色）依無參考品質指標、亮度色彩統計、SSIM 等測量值與修復需求判斷結果是否接受；若失敗則修訂提示重新執行，且每輪均從原始影像起始，避免錯誤傳播。關鍵差異在於不排程修復工具，而是以證據引導 MFM 提示，將代理動作原語從工具鏈轉為 MFM 駕馭。

## 結果
作者報告 HarnessIR 在合成混合退化基準 MiO100 上超越現有全能型與代理式修復方法，達到最先進效能；於具挑戰性的真實世界單一與混合退化影像上，亦大幅優於先前代理系統。消融實驗指出修復增益主要源於駕馭框架而非執行器本身。摘錄未提供可驗證數字，僅呈現雷達圖與視覺化定性比較。

## 限制與展望
方法依賴專有 MFM（Nano Banana 2、GPT-Image-2.5）與 VLM，部署成本與可重現性受限；驗證機制僅採 NR-IQA 等簡易指標，可能無法完全捕捉感知品質；輔助工具集固定，未涵蓋所有退化類型；實驗缺乏詳細量化指標與統計顯著性分析，泛化至未見退化組合的穩健性尚待驗證；多輪修正可能增加推理延遲。後續研究可探索開源 MFM 替代、更完善的驗證獎勵模型與自適應工具選擇。
