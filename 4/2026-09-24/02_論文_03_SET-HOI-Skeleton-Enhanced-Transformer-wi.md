# 論文 03：SET-HOI: Skeleton-Enhanced Transformer with Parallel Fusion for HOI Detection.

- 日期：2026-09-24
- 來源層級：Tier 4（一般期刊）
- 期刊/會議/來源：Biomimetics (Basel, Switzerland)
- Venue：Biomimetics (Basel, Switzerland)
- 發布時間：2026-09-23T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42930239/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13702107/
- DOI：10.3390/biomimetics11100687
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1262（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Human-Object Interaction (HOI) detection seeks to identify the relationships between humans and objects in images that play a pivotal role in high-level vision tasks and biomimetic systems, such as biomimetic robotics, intelligent prosthetics, and embodied AI for intent understanding. However, existing approaches that rely solely on visual appearance features are susceptible to background interference, which adversely affects detection accuracy. Inspired by the biomimetic dual-stream mechanism of biological visual perception, we propose a Transformer-based HOI detection model with a dual-branch parallel fusion architecture, incorporating a skeleton topology branch alongside the standard image branch. The skeleton branch leverages a Graph Convolutional Network (GCN) to explicitly model spatial-kinematic relationships between human keypoints and objects, providing fine-grained topological priors to complement visual appearance features before joint decoding. Our approach achieves 51.6% Mean Average Precision (mAP) on the Verbs in Common Objects in Context (V-COCO) dataset, outperforming the Transformer-based HOI baseline by 2.7 mAP points, highlighting its effectiveness in enhancing perceptual robustness for biomimetic interactive applications.

## 背景與目的
人體與物件互動（HOI）偵測旨在識別影像中人與物件的關係，對生物模擬機器人、智慧義肢與具身 AI 的意圖理解至關重要。現有方法多僅依賴視覺外觀特徵，易受背景干擾導致準確度下降。本文受生物視覺雙流機制啟發，提出結合骨架拓撲分支的 Transformer 架構，透過圖卷積網路（GCN）顯式建模關鍵點與物件的空間運動關係，提供精細拓撲先驗以補充外觀特徵，期望提升感知魯棒性並推動生物模擬互動應用。

## 方法
問題設定：輸入為單張影像，輸出為人─物件配對及其互動類別與邊界框。整體架構採雙分支平行融合：影像分支使用標準 Transformer 編碼器‑解碼器提取視覺特徵；骨架分支先由姿態估計器取得人體關鍵點，再構建圖結構（節點為關鍵點與物件候選區域，邊依空間鄰近與運動學約束定義），經多層 GCN 傳遞訊息，學習空間‑運動拓撲表示。兩分支特徵在解碼器前以平行方式融合（具體融合操作如串接、注意力加權等摘錄未詳細說明），融合後的聯合特徵送入共享解碼器進行 HOI 預測。訓練目標推測為分類損失（互動類別）與邊界框回歸損失的加權和，最佳化採用常見的 AdamW 與學習率排程，但摘錄未給出具體超參數。推論流程：影像經骨干網路提取特徵 → 並行送入影像 Transformer 與骨架 GCN → 特徵融合 → 解碼器輸出 HOI 三元組。關鍵差異在於引入骨架拓撲分支並以平行融合方式注入拓撲先驗，而非單純串接或串級式融合。

## 結果
在 V‑COCO 資料集上，本方法達到 51.6% mAP，較基線 Transformer HOI 模型提升 2.7 mAP 點。摘錄未提供可驗證的其他指標（如 Recall、AP per class、推論速度）或消融實驗數據，僅能觀察到定性結論：骨架拓撲先驗能有效緩解背景干擾，提升互動偵測魯棒性。

## 限制與展望
僅在 V‑COCO 單一資料集驗證，缺乏跨資料集（如 HICO‑DET）與真實機器人場景的泛化證據；未公開消融實驗，無法量化骨架分支、融合策略、GCN 層數等組件貢獻；依賴外部姿態估計器，關鍵點誤差可能傳遞至 HOI 預測；訓練細節（損失權重、資料增強、硬體需求）未揭露，難以復現與部署評估；後續研究可探討端到端聯合學習姿態與 HOI、多模態融合機制、即時推論優化與更大規模基準比較。
