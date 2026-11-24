# 論文 04：SET-HOI: Skeleton-Enhanced Transformer with Parallel Fusion for HOI Detection.

- 日期：2026-09-29
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
人體-物件互動（HOI）偵測旨在識別影像中人與物件之間的關係，對高階視覺任務與仿生系統（如仿生機器人、智慧義肢、具身 AI 意圖理解）至關重要。現有方法多仰賴視覺外觀特徵，易受背景干擾導致偵測精度下降。本文受生物視覺雙流機制啟發，提出基於 Transformer 的 HOI 偵測模型，採用雙分支平行融合架構，引入骨架拓撲分支以補充視覺特徵，期望提升感知魯棒性並推動仿生互動應用。

## 方法
問題設定：輸入單張影像，輸出人-物件-動作三元組。整體架構包含兩條平行分支：(1) 影像分支，採用標準 Transformer 編碼器提取視覺外觀特徵；(2) 骨架拓撲分支，先由姿態估計器取得人體關鍵點，再構建圖結構，利用圖卷積網路（GCN）對關鍵點與物件節點進行空間-運動關係建模，產生精細拓撲先驗。兩分支特徵在聯合解碼前以平行融合方式合併，隨後送入 Transformer 解碼器進行 HOI 預測。資料表示上，影像分支使用區域特徵與位置編碼；骨架分支以關鍵點座標與物件邊界框為節點特徵，邊緣依人體骨架連接與人-物空間關係定義。訓練目標與損失函數於摘錄未詳細說明，依目前可取得資料，無法確認具體損失形式與最佳化策略。推論流程為：影像經骨干網路提取特徵 → 並行送入影像 Transformer 編碼器與 GCN 骨架編碼器 → 特徵融合 → Transformer 解碼器輸出 HOI 三元組。關鍵差異在於引入 GCN 骨架分支並採平行融合，提供明確空間-運動先驗，區別於單純視覺 Transformer 基線。

## 結果
在 V-COCO 資料集上，本方法達到 51.6% mAP，較 Transformer 基線提升 2.7 mAP 點，顯示骨架拓撲先驗能有效改善背景干擾下的偵測表現。摘錄未提供其他資料集、消融實驗或各動作類別的詳細數字，故無法進一步驗證各組件貢獻。

## 限制與展望
僅在 V-COCO 單一資料集驗證，泛化能力未經多基準測試；缺乏消融實驗以量化骨架分支、融合策略與 GCN 深度的具體影響；依賴姿態估計器準確度，若關鍵點偵測失誤可能傳遞錯誤先驗；未報告計算量、參數量與推理延遲，部署於即時仿生系統的可行性尚待評估；後續研究可擴展至更大規模 HOI 基準（如 HICO-DET）、探討端到端聯合訓練姿態與 HOI、以及輕量化融合模組以滿足邊緣裝置需求。
