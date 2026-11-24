# 論文 02：The Prospect of Embodied Intelligence in Dentistry.

- 日期：2026-09-14
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
傳統牙醫 AI 受限於「診斷-執行斷層」，多為靜態「旁觀者智能」，無法將診斷結果直接轉化為治療動作。本文旨在梳理具身人工智慧（EAI）在牙醫領域的技術架構，提出以醫師監督的閉環框架，整合多模態感知、記憶與知識融合、具身推理規劃及精準執行四大核心模組，期望彌補現有數位工作流程的缺口，推動從輔助診斷邁向主動治療介入的醫師-智能體協作新模式。

## 方法
方法上，論文構想的牙醫 EAI 系統包含四大模組與一個決策沙箱： 1. 多模態感知：融合口內影像（CBCT、光學掃描）、力覺/觸覺傳感器、語音與病歷文字，透過編碼器將異構資料映射至共同潛在空間，支援即時環境建模。 2. 記憶與知識整合：引入長期記憶庫儲存患者歷程、術前規劃與文獻指引，並結合牙醫基礎模型進行知識檢索與推理增強，實現跨任務知識遷移。 3. 具身推理與規劃：採用層級規劃器，高層以語言模型生成治療策略，低層轉換為機器人運動軌跡；引入數位雙生技術作為「決策沙箱」，在虛擬環境預演多種手術方案並評估預測結果，再回傳最優策略。 4. 精準執行：由導航機器人或微創手術器械依規劃軌跡執行，並以閉環力覺回授修正偏差。 訓練目標方面，文中未給出具體損失函數，僅指出需以醫師監督的強化學習或模仿學習優化策略，並以可解釋 AI（XAI）模組輸出決策依據。推論流程為感知→知識檢索→規劃→模擬驗證→執行→回授，形成醫師可介入的閉環。與現有靜態診斷 AI 不同，關鍵差異在於具備物理執行能力、即時環境適應與可解釋決策沙箱。

## 結果
結果部分為綜述性質，摘錄未提供可驗證數字。作者指出 EAI 在機器人輔助植體導航、精密根管微創手術、動態牙齒矯正監測三大場景具臨床潛力；數位雙生技術可作為決策沙箱進行預測性結果模擬；並提出牙醫基礎模型與可解釋 AI 為解決資料稀缺與演算法不透明的潛在路徑。但強調現有證據多停留在工程驗證、臨床前或早期臨床階段，系統應視為醫師監督的任務專用副駕駛，而非自主替代。

## 限制與展望
限制與展望：目前多數研究仍處於工程原型或小規模臨床前驗證，缺乏大規模隨機對照試驗支撐；資料稀缺、異質性高導致模型泛化能力未經充分驗證；演算法不透明與安全性風險（如力覺回授失效）需以 XAI 與嚴格法規審查緩解；數位雙生建模精度受限於影像解析度與組織力學參數；未來需推進多中心資料聯盟、標準化評估指標與長期臨床追蹤，才能向廣泛臨床部署邁進。
