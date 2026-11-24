# 論文 02：HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration

- 日期：2026-10-25
- 來源層級：Tier 3
- 期刊/會議/來源：arXiv (Cornell University)
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
真實世界影像常同時受雜訊、模糊、大氣效應等多重退化影響，傳統單一退化修復與全能模型多假設單一退化類型，難以處理耦合退化。近期代理式修復將任務視為串聯任務特定模型的工具鏈，但此範式存在三大缺口：退化無法乾淨解耦、規劃過程丟失細粒度資訊、任務特定工具泛化能力弱，且多在合成基準評估。本文提出 HarnessIR，旨在利用多模態基礎模型（MFM）作為單一執行器，透過感知診斷、按需輔助工具、提示組合、單次執行與驗證驅動迭代，將代理動作從工具排程轉為對 MFM 的引導，實現通用真實世界影像修復。

## 方法
HarnessIR 採五階段流程： 1. 感知與診斷：凍結的視覺語言模型（VLM）作為診斷器 𝒱_d，輸入低品質影像 x 與使用者請求 r，輸出內容與退化描述 d，並規劃需調用的輔助工具集 π ⊆ 𝒯_aux（OCR、人臉偵測、深度估計、語意分割）。 2. 按需工具調用：依診斷結果動態呼叫輔助工具，取得影像特定證據 e（辨識文字與框、人臉框、稠密深度圖、分割標籤），證據不直接送入執行器。 3. 提示組合：另一凍結 VLM 作為組合器 𝒱_c，將 (x, r, d, e) 綜合解讀，依領域知識（如去雨不移除濕路面、未要求亮度增強則保持亮度）將證據融入單一自然語言提示 p，明確指明需處理的退化、需保留的內容及空間範圍。 4. 執行：固定的 MFM 執行器 ℰ（如 Nano Banana 2、GPT-Image-2.5-Sunburst）接收原始 x 與提示 p，單次生成修復結果 ŷ^(k)=ℰ(x, p^(k))。 5. 驗證驅動迭代：驗證器 𝒱_v 以無參考品質指標、亮度/色彩統計、與 x 的 SSIM 等測量為輔助證據，結合請求 r 與修復需求判斷結果是否接受；若失敗則重新組合提示並從原始 x 重新執行，而非從上一輪輸出延續，避免錯誤內容累積。 關鍵差異：不使用任務特定修復模型作為工具鏈，執行器固定、僅變化提示；輔助工具僅提供證據；驗證器依任務需求而非指令內容判斷；每輪皆從原始影像開始。

## 結果
在廣泛使用的 MiO100 合成混合退化基準上，HarnessIR 超越現有全能與代理式修復方法，幾乎在所有指標上取得最佳表現（摘錄未提供可驗證數字）。在具挑戰性的真實世界單一與混合退化影像上，先前代理系統常失效，HarnessIR 以顯著優勢優於 Nano Banana 2、GPT-Image-2.5 等基線及既有方法。消融實驗指出性能提升主要源於引導框架而非執行器本身。視覺結果顯示能還原細節且不改變文字與內容；雷達圖顯示在真實測試集多項指標均優於比較對象。

## 限制與展望
系統高度依賴強大的專有 MFM（Nano Banana 2、GPT-Image-2.5），部署需 API 存取且延遲較高；驗證機制僅採 NR-IQA 及簡單統計，可能無法完整捕捉感知品質；輔助工具僅限 OCR、人臉、深度、分割，若退化涉及其他語意（如水印、光暈）可能證據不足；多輪迭代增加計算成本；真實世界退化類型極其多樣，泛化能力仍需更大規模、多樣化資料驗證；消融與定量分析於摘錄中缺乏具體數字，後續研究需補充完整實驗報告。
