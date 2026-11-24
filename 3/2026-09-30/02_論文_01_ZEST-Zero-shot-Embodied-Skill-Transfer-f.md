# 論文 01：ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control

- 日期：2026-09-30
- 來源層級：Tier 1
- 期刊/會議/來源：Science robotics
- Venue：Science robotics
- 發布時間：2026-01-30T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/5882a4d872551a31775bad801a239bac08e99b1d
- PDF：
- DOI：10.48550/arxiv.2602.00401
- arXiv：2602.00401
- 影響指標：N/A
- 影響指標來源：
- 引用數：35
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2602.00401
- 全文字數：132932（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Achieving robust, humanlike whole-body control on humanoid robots for agile, contact-rich behaviors remains a central challenge, demanding heavy per-skill engineering and a brittle process of tuning controllers. We introduce ZEST (zero-shot embodied skill transfer), a streamlined motion-imitation framework that trains policies via reinforcement learning from diverse sources-high-fidelity motion capture, noisy monocular video, and non-physics-constrained animation-and deploys them to hardware zero-shot. ZEST generalizes across behaviors and platforms without relying on contact labels, reference or observation windows, state estimators, or extensive reward shaping. Its training pipeline combines adaptive sampling, which focuses training on difficult motion segments, and an automatic curriculum using a model-based assistive wrench, together enabling dynamic, long-horizon maneuvers. We further provide a procedure for selecting joint-level gains from approximate analytical armature values for closed-chain actuators, along with a refined model of actuators. Trained entirely in simulation with moderate domain randomization, ZEST demonstrated broad generality. On Boston Dynamics' Atlas humanoid, ZEST learned dynamic, multicontact skills (army crawl and breakdancing) from motion capture. It transferred expressive dance and scene-interaction skills, such as box climbing, directly from videos to Atlas and the Unitree G1. Furthermore, it extended across morphologies to the Spot quadruped, enabling acrobatics, such as a continuous backflip, through animation. Together, these results demonstrate robust zero-shot deployment across heterogeneous data sources and embodiments, establishing ZEST as a scalable interface between biological movements and their robotic counterparts.

## 背景與目的
本研究旨在解決人形機器人進行敏捷、多接觸全身控制時，需大量逐技能工程與脆弱控制器調參的問題。現有基於模型的離線軌跡優化與線上追蹤方法，對環境建模、狀態估計與參考軌跡保真度要求高，難以應對高不確定性與複雜接觸；純強化學習雖具敏捷性但樣本效率低、極依賴獎勵設計；模仿學習雖引入動作先驗，仍常需接觸標籤、多階段訓練、歷史觀測或狀態估計器等手工組件。ZEST 提出統一、極簡的單階段動作模仿框架，從動作捕捉、單目影片、關鍵幀動畫等異構資料來源學習策略，並零樣本部署至實體機器人，建立生物動作與機器人對應的可擴展介面。

## 方法
方法核心為單階段強化學習動作模仿管線。問題設定：輸入為下一步參考動作（關節位置/速度）與當前本體感測（關節位置、速度、投影重力、基座角速度），僅保留前一動作作為歷史；輸出為殘差關節目標，加上參考後送入關節級 PD 控制器。架構採用簡單前饋神經網路，無循環或注意力模組。核心模組包含：(1) 自適應採樣：將長軌跡切分為固定時長區塊，以指數移動平均（EMA）追蹤各區塊失敗分數估計難度，類別採樣器偏向高難度區塊，避免災難性遺忘並支援長時程多技能學習。(2) 模型輔助扭矩課程：以模型計算作用於機器人基座的虛擬輔助扭矩，大小依區塊難度自適應調整並隨追蹤改善衰減至零，免除手工課程設計。(3) 關節增益選取：利用解析性電樞近似值處理閉鏈致動器（膝、踝）動力學，推導有效 PD 增益；Spot 另加入更精確的電源與致動器模型。訓練目標為單一模仿獎勵（關節位置/速度追蹤、基座姿態、足端接觸一致性），無額外塑形項、接觸標籤、參考視窗或狀態估計器。最佳化採用 PPO，領域隨機化包含衝擊推力、感測噪聲、摩擦係數與質量變化。推論時直接以當前觀測與下一步參考輸入網路，輸出殘差目標實時控制。關鍵差異在於統一處理 MoCap、ViCap、動畫三類資料，移除接觸標籤、歷史觀測、狀態估計、多階段訓練等複雜組件，單一超參數集即可跨機器人平台部署。

## 結果
實驗結果顯示：在 Boston Dynamics Atlas（約 1.8 m、100 kg）上，從 MoCap 學得動態多接觸技能（軍隊爬行、霹靂舞）；從單目影片（ViCap）直接轉移富表現力舞蹈與場景互動技能（箱子攀爬）至 Atlas 與 Unitree G1；並擴展至 Spot 四足機器人，透過關鍵幀動畫實現連續後空翻等特技動作。所有策略均在模擬器中訓練並以中度領域隨機化零樣本部署至實體，展現跨異構資料來源與本體型態的強健性。摘錄未提供可驗證的具體數值指標（如追蹤誤差、成功率、樣本數），僅能觀察到定性結論：ZEST 實現首個全尺寸人形機器人動態多接觸行為、首個影片到行為的敏捷接觸豐富技能轉移，以及跨形態的特技泛化。

## 限制與展望
限制方面：(1) 評估僅涵蓋三款機器人與有限技能集，未量化跨任務泛化極限；(2) 缺乏詳細消融實驗數據，無法確認自適應採樣、輔助扭矩課程、增益選取程序各自貢獻；(3) 領域隨機化範圍屬中度，極端模型誤差或未建模動力學（如柔性關節、磨損）下的魯棒性未驗證；(4) 影片來源動作經 ViCap 處理後品質與物理一致性依賴上游姿態估計，噪聲大時可能影響策略品質；(5) 部署仍需精確 PD 增益與致動器模型，若硬體差異大可能需重新校準。後續研究可擴大機器人與技能多樣性、量化各模組效益、探索更強領域隨機化與實時適應機制。
