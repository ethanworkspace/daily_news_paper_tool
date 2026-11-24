# 論文 05：The Prospect of Embodied Intelligence in Dentistry.

- 日期：2026-09-22
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
傳統牙醫 AI 受限於「診斷-執行斷層」，多為靜態「旁觀者智能」，無法直接介入治療。本文旨在梳理具身人工智慧（EAI）在牙醫領域的技術架構，並分析其透過醫師監督的閉環框架，彌補診斷與執行之間的鴻溝。研究綜合醫學與工程資料庫（PubMed、IEEE Xplore、Scopus）文獻，聚焦從靜態診斷 AI 向主動治療干預的轉型，提出四大核心模組整合的 EAI 架構，定位為臨床醫師-代理人協作的新範式。

## 方法
本文提出的牙醫 EAI 架構包含四大核心模組，形成感知‑規劃‑執行的閉環。1) 多模態感知：整合口內影像、CBCT、光學掃描、力覺/觸覺訊號等異構資料，經由特徵融合網路產生統一的環境表徵。2) 記憶與知識整合：引入長期記憶庫與牙醫知識圖譜，結合病例歷史、指南與文獻嵌入，支援情境感知的推理。3) 體現推理與規劃：採用層級化任務規劃器，結合符號推理與深度強化學習，在數位雙生體（Digital Twin）中模擬手術路徑、力量控制與風險評估，作為「決策沙箱」進行前瞻性結果預測。4) 精密執行：透過機械臂或微創手持機器人，配合實時視覺伺服與力控制迴路，實現亞毫米級植體導航、根尖微創手術與動態矯正力調節。訓練目標採用多任務損失，包含感知分割、軌跡預測、力控制誤差與安全約束；優化採用階段式預訓練（牙醫基礎模型）再微調。推論流程為：感知→知識檢索→規劃模擬→執行指令下發→感測回授→線上修正。與既有靜態診斷 AI 不同，EAI 強調感知‑行動耦合、醫師在環監督與數位雙生體驗證。

## 結果
作者報告 EAI 在機器人輔助植體導航、精密根管微創手術、動態齒列監測三大場景展現臨床潛力；數位雙生體被視為關鍵「決策沙箱」可進行前瞻性結果預測。系統性障礙包括資料稀缺與演算法不透明，提出牙醫基礎模型與可解釋 AI（XAI）作為潛在對策。然而，現有證據多停留在工程驗證、臨床前或早期臨床階段，摘錄未提供可驗證數字。定性結論顯示 EAI 能將「旁觀者智能」轉為醫師監督下的任務專用副駕駛，而非自主替代。

## 限制與展望
主要限制在於：1) 高品質多模態牙醫資料集稀缺，難以支撐大規模基礎模型訓練；2) 演算法決策過程不透明，臨床信任度受限；3) 現階段驗證多為實驗室或小樣本臨床，缺乏大規模隨機對照證據；4) 系統僅能作為醫師監督的特定任務副駕駛，無法實現完全自主；5) 法規、倫理與責任歸屬尚未明確。後續研究需著重資料聯盟建構、可解釋機制、長期臨床驗證與標準化評估框架。
