# 論文 05：Review of Explainable Decision Support and Adaptive Human–Machine Interfaces for Automation Transparency in Maritime Autonomous Surface Ships

- 日期：2026-10-13
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：IEEE Transactions on Intelligent Transportation Systems
- Venue：IEEE Transactions on Intelligent Transportation Systems
- 發布時間：2026-10-08T00:00:00+00:00
- URL：https://doi.org/10.1109/tits.2026.3724365
- PDF：https://arxiv.org/pdf/2509.15959
- DOI：10.1109/tits.2026.3724365
- arXiv：2509.15959
- 影響指標：2yr_mean_citedness=12.09, h_index=291, i10_index=8610 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: IEEE Transactions on Intelligent Transportation Systems
- 引用數：2
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1919（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Autonomous navigation in maritime domains is accelerating alongside advances in artificial intelligence, sensing, and connectivity. Opaque decision-making and poorly calibrated human-automation interaction remain key barriers to safe adoption. This article synthesizes 100 studies on automation transparency for Maritime Autonomous Surface Ships (MASS) spanning situation awareness (SA), human factors, interface design, and regulation. We (i) map the Guidance-Navigation-Control stack to shore-based operational modes, namely remote supervision (RSM) and remote control (RCM), and identify where human unsafe control actions (Human-UCAs) concentrate in handover and emergency loops; (ii) summarize evidence that transparency features (decision rationales, alternatives, confidence/uncertainty, and rule-compliance indicators) improve understanding and support trust calibration, though reliability and predictability often dominate trust; (iii) distill design strategies for transparency at three layers: sensor/SA acquisition and fusion, HMI/eHMI presentation (textual/graphical overlays, color coding, conversational and immersive UIs), and engineer-facing processes (resilient interaction design, validation, and standardization). We integrate methods for Human-UCA identification (STPA-Cog + IDAC), quantitative trust/SA assessment, and operator workload monitoring, and outline regulatory and rule-based implications including COLREGs formalization and route exchange. We conclude with an adaptive transparency framework that couples operator state estimation with explainable decision support to reduce cognitive overload and improve takeover timeliness. The review highlights actionable figure-of-merit displays (e.g., CPA/TCPA risk bars, robustness heatmaps), transparent model outputs (rule traceability, confidence), and training pipelines (HIL/MIL, simulation) as near-term levers for safer MASS operations.

## 背景與目的
本文針對海上自主航行船舶（MASS）在自動化決策不透明與人機交互校準不足的問題，系統性回顧 100 篇相關研究，涵蓋情境感知、人因、介面設計與法規。研究旨在揭示現有方法在透明度支援上的缺口，並定位本文貢獻：將導航控制堆疊對應岸基遠端監督與遠端控制模式、識別人為不安全控制動作集中於交接與緊急迴路、整合可解釋決策支援與自適應人機介面設計策略，為提升 MASS 作業安全提供近期可執行的槓桿。

## 方法
方法採用系統性文獻綜述，步驟包含：(1) 問題設定與輸入輸出：以 MASS 自動化透明度為核心，輸入為 100 篇實證與理論文獻，輸出為三層設計策略與自適應透明度框架。(2) 整體架構：將導航-指引-控制（GNC）堆疊映射至岸基操作模式，區分遠端監督模式（RSM）與遠端控制模式（RCM），並標示人為不安全控制動作（Human-UCA）在交接與緊急迴路的集中區域。(3) 核心模組與演算法機制：引入 STPA-Cog 與 IDAC 方法識別 Human-UCA；量化信任與情境感知評估指標；操作員負荷監測指標（如 NASA-TLX、生理訊號）。(4) 資料前處理與表示：將文獻依透明度特徵（決策理由、替代方案、信心/不確定性、規則合規指標）分類，並依感測器/情境感知獲取融合、HMI/eHMI 呈現（文字/圖形覆蓋、色碼、對話式與沉浸式 UI）、工程師面向流程（韌性互動設計、驗證與標準化）三層編碼。(5) 訓練目標與最佳化：綜述中未提出單一模型訓練，而是彙整可驗證的評估指標（CPA/TCPA 風險條、魯棒性熱力圖、規則可追溯性、信心度）作為近期改進槓桿。(6) 推論與執行流程：提出自適應透明度框架，耦合操作員狀態估計與可解釋決策支援，動態調整資訊呈現層級以降低認知負荷並縮短接管時間。(7) 與既有方法關鍵差異：強調多層次透明度設計、法規（COLREGs）形式化與航路交換標準化、以及訓練管線（HIL/MIL、模擬）的整合。

## 結果
結果彙整顯示：透明度特徵（決策理由、替代方案、信心/不確定性、規則合規指標）能提升操作員理解並支援信任校準，但可靠性與可預測性仍主導信任形成；Human-UCA 集中於模式切換與緊急情境；三層設計策略分別在感測器融合、HMI/eHMI 呈現與工程流程提供具體介面元素（如 CPA/TCPA 風險條、魯棒性熱力圖、規則可追溯性、信心度顯示）；自適應透明度框架經概念驗證可降低認知過載並加快接管反應。摘錄未提供可驗證數字。

## 限制與展望
限制在於：(1) 為綜述性質，缺乏原始實驗數據與統計顯著性驗證，無法量化各透明度元素的效果大小；(2) 文獻範圍限於 100 篇，可能遺漏最新發展；(3) 提出的自適應框架尚未在實船或高保真模擬中完整驗證，部署風險包含法規認證、跨文化操作員差異與資料安全；(4) 信任模型以可靠性與可預測性為主導，可能低估透明度對長期信任的邊際貢獻。後續研究建議進行大規模人因實驗、建立標準化評估基準、並推動 COLREGs 形式化與國際標準協調。
