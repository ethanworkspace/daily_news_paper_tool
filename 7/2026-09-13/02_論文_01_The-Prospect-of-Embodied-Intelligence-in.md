# 論文 01：The Prospect of Embodied Intelligence in Dentistry.

- 日期：2026-09-13
- 來源層級：Tier 2
- 期刊/會議/來源：International dental journal
- Venue：International dental journal
- 發布時間：2026-09-10T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42721686/
- PDF：
- DOI：10.1016/j.identj.2026.111133
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2147（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Conventional artificial intelligence in dentistry is limited by a 'diagnostic-executive disconnect', functioning primarily as static 'bystander intelligence'. This review aims to delineate the technical architecture of Embodied Artificial Intelligence (EAI) in dentistry and analyze its potential to bridge this gap through a clinician-supervised closed-loop framework. We synthesized current literature from medical and engineering databases (PubMed, IEEE Xplore, Scopus) regarding the integration of multimodal perception, memory and knowledge integration, embodied reasoning and planning, and precision execution within dental systems. The review focused on literature demonstrating the transition from static diagnostic AI to active therapeutic intervention. The proposed dental EAI architecture integrates four core modules: multimodal perception, memory and knowledge integration, embodied reasoning and planning, and precision execution. Analysis reveals its clinical potential in robot-assisted implant navigation, precision endodontic microsurgery, and dynamic orthodontic monitoring. Digital twin technology is identified as a key 'decision sandbox' for prospective outcome prediction. Furthermore, the review evaluates systemic barriers such as data scarcity and algorithmic opacity, discussing Dental Foundation Models and Explainable AI (XAI) as potential approaches. However, much of the current evidence remains at the engineering, preclinical, or early clinical stage. EAI provides an emerging framework for shifting from 'bystander intelligence' to active clinician-agent partnership. By establishing a closed-loop framework of perception, planning, and execution, EAI addresses the limitations of current digital workflows. Current systems should be regarded as task-specific, clinician-supervised co-pilots rather than autonomous replacements for dental professionals, and further clinical validation is required before broader implementation. By bridging the diagnostic-executive disconnect, Embodied AI may provide a clinician-supervised framework to support more integrated dental workflows across diverse dental specialties.

## 背景與目的
傳統牙醫 AI 受限於「診斷-執行斷層」，多為靜態旁觀智能，無法直接介入治療流程。現有方法缺乏感知、規劃與執行的閉環整合，導致數位工作流程斷裂。作者從 PubMed、IEEE Xplore、Scopus 等醫學與工程資料庫綜述多模態感知、記憶知識整合、具身推理規劃與精準執行的整合文獻，聚焦從靜態診斷 AI 向主動治療介入的轉型。本文旨在勾畫具身人工智慧（EAI）在牙醫領域的技術架構，提出臨床醫師監督的閉環框架，以彌補診斷與執行之間的鴻溝，推動從旁觀智能轉向醫師-代理人協作。

## 方法
本文提出的牙醫 EAI 架構包含四大核心模組，形成感知‑規劃‑執行的閉環： 1. 多模態感知：整合影像（CBCT、口內掃描）、力覺、聲音與病歷文字等異構資料，透過多模態融合網路產生統一的環境表徵。 2. 記憶與知識整合：建立長期記憶庫（病例庫、指南、文獻）與短期工作記憶，引入牙醫基礎模型進行知識蒸餾與檢索增強生成，支援情境感知推理。 3. 具身推理與規劃：採用層級式規劃器，高層以任務圖描述治療步驟，低層以模型預測控制（MPC）或強化學習產生機器人運動軌跡，並引入數位雙生技術作為「決策沙箱」，在虛擬環境預演多種方案並評估預後風險。 4. 精準執行：結合導航機器人、微創手術器械與即時感知回授，實現亞毫米級定位與力控制，支援植體導航、根尖微手術與動態矯正監測等場景。 訓練目標方面，文獻指出採用監督式損失（分割、關鍵點回歸）、對比學習對齊多模態表徵、以及基於模擬環境的強化學習獎勵函數（安全性、精度、時間），並以可解釋 AI（XAI）模組輸出注意力熱力圖與決策理由供醫師審核。推論流程為：感知模組輸出環境狀態 → 記憶模組檢索相關知識 → 推理規劃模組生成候選方案 → 數位雙生模擬評分 → 醫師確認後下發控制指令 → 執行模組驅動機器人並持續回授感知更新。與既有靜態診斷 AI 不同，EAI 強調閉環互動、實體執行與醫師在環監督，屬任務特定的協作副駕駛而非全自主系統。

## 結果
摘錄未提供可驗證數字。定性結論顯示：EAI 架構在機器人輔助植體導航、精密根管微手術、動態牙齒矯正監測三大應用展現臨床潛力；數位雙生被視為關鍵決策沙箱，可預測預後；系統性障礙包含資料稀缺與演算法不透明，牙醫基礎模型與 XAI 被提出為潛在解決路徑；目前證據多停留在工程驗證、臨床前或早期臨床階段，建議視為醫師監督的任務專用副駕駛，尚需進一步臨床驗證才能廣泛推廣。

## 限制與展望
綜述僅基於文獻綜合，缺乏原始實驗數據與大規模臨床試驗支撐；資料稀缺、異質性高、標註成本大，限制基礎模型訓練與泛化；演算法不透明與安全性驗證機制尚未成熟，XAI 解釋品質仍待量化；數位雙生建模精度依賴高保真生物力學參數，獲取困難；法規、倫理與責任歸屬在醫師-代理人協作模式下尚無明確標準；未來研究需著重多中心前瞻性臨床研究、標準化資料集建構、實時安全監控機制與法規適應性評估。
