# 論文 04：SET-HOI: Skeleton-Enhanced Transformer with Parallel Fusion for HOI Detection.

- 日期：2026-09-24
- 來源層級：Tier 2
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
人體與物件互動（HOI）偵測旨在識別影像中人與物件之間的關係，這對高層視覺任務與仿生系統（如仿生機器人、智慧義肢、具身 AI 意圖理解）至關重要。現有方法多仰賴視覺外觀特徵，易受背景干擾導致偵測精度下降。本文受生物視覺雙流機制啟發，提出基於 Transformer 的 HOI 偵測模型，採用雙分支並行融合架構，引入骨架拓撲分支以補充視覺特徵，期望提升感知魯棒性並推動仿生互動應用。

## 方法
本文提出的 SET-HOI 採用雙分支並行融合架構，包含標準影像分支與骨架拓撲分支。影像分支以 Transformer 為骨幹，提取全域視覺外觀特徵；骨架拓撲分支則利用圖卷積網路（GCN）對人體關鍵點與物件之間的空間運動關係進行顯式建模，產生精細的拓撲先驗。兩分支特徵在聯合解碼前進行融合，使模型能同時利用外觀與運動拓撲資訊進行 HOI 三元組（人、動詞、物件）預測。輸入為影像與對應的人體關鍵點座標，輸出為偵測到的互動類別與邊界框。摘錄未提供具體損失函數、訓練目標、最佳化策略、資料增強或推論流程細節，故無法進一步描述訓練與推論的具體機制。關鍵差異在於引入 GCN 建模骨架拓撲，並以並行融合方式在解碼前注入拓撲先驗，區別於單純依賴視覺特徵的既有 Transformer 基線。

## 結果
在 V-COCO 資料集上，SET-HOI 達到 51.6% mAP，較 Transformer 基線提升 2.7 mAP 點，顯示骨架拓撲分支能有效改善偵測性能。摘錄未提供可驗證的其他數字（如各動詞類別 AP、消融實驗數值、推論速度等），僅能觀察到定性結論：雙分支融合架構在該基準上優於單一視覺分支基線。

## 限制與展望
僅在 V-COCO 單一資料集驗證，缺乏跨資料集（如 HICO-DET）泛化證據；未公開消融實驗，無法量化骨架分支、融合策略、GCN 深度等組件貢獻；依賴準確的人體關鍵點偵測，關鍵點誤差可能傳遞至 HOI 預測；計算成本與模型參數量未揭露，部署於即時仿生系統的可行性不明；程式碼連結缺失，難以重現與擴展。後續研究可探討多資料集評估、關鍵點不確定性建模、輕量化融合模組與端到端訓練目標設計。
