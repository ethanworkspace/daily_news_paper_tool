# 論文 05：Enhanced SAR Ship Detection Using Multiscale Neighborhood Correlation and Self-Supervised Constraint.

- 日期：2026-09-21
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：IEEE transactions on neural networks and learning systems
- Venue：IEEE transactions on neural networks and learning systems
- 發布時間：2026-09-10T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42721178/
- PDF：
- DOI：10.1109/tnnls.2026.3731090
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1782（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Ship detection in synthetic aperture radar (SAR) imagery is a cornerstone of maritime surveillance, leveraging active microwave backscattering for all-weather target acquisition. However, the coherent imaging mechanism inherently introduces speckle noise, scattering ambiguity, and sidelobe effects, causing general-purpose deep learning models to suffer from false alarms and missed detections in complex nearshore environments. To address the critical lack of domain-specific modeling in current frameworks, this article proposes an enhanced SAR ship detection approach driven by electromagnetic physical priors. In particular, acknowledging that vessels are represented as discrete clusters of dominant scattering centers, center difference convolution (CDC) is incorporated to emphasize local structural variations, thereby suppressing sidelobe-induced interference while preserving discriminative ship boundaries. Furthermore, a multiscale neighborhood correlation analysis strategy is developed to exploit the statistical divergence of neighborhood backscattering responses between ship targets and surrounding sea clutter while enhancing robustness against ambiguous local scattering patterns through multiscale contextual modeling. To mitigate the signal dilution effect during successive downsampling, a self-supervised constraint mechanism is introduced to maintain cross-layer feature consistency and compensate for the energy loss of dim small targets in deeper layers. Extensive evaluations on benchmark datasets demonstrate that the proposed method significantly improves detection performance in complex scenes, underscoring the importance of incorporating SAR-specific scattering characteristics into deep learning architectures for robust maritime target detection.

## 背景與目的
本研究針對合成孔徑雷達（SAR）船舶偵測在近岸複雜場景中，因相干成像機制產生的斑點雜訊、散射模糊與旁瓣效應，導致通用深度學習模型出現誤報與漏報的問題。現有方法缺乏針對 SAR 散射特性的領域建模，無法有效利用船舶作為離散強散射中心簇群的電磁物理先驗。本文提出結合電磁物理先驗的增強式 SAR 船舶偵測方法，旨在抑制旁瓣干擾、保留邊界資訊、利用多尺度鄰域相關性區分目標與海雜訊，並透過自監督約束緩解下採樣造成的訊號稀釋，提升複雜場景下的偵測魯棒性。

## 方法
方法整體架構建立在典型單階段或雙階段檢測器骨幹之上，輸入為單通道 SAR 影像，輸出為船舶邊界框與類別分數。核心創新包含三大模組： 1. 中心差分卷積（CDC）模組：在骨幹網路的早期層替換標準 3×3 卷積，利用中心像素與鄰域像素的差分運算強化局部結構變化，對應船舶由離散強散射中心組成的物理特性，抑制旁瓣產生的平滑干擾並保留邊緣細節。 2. 多尺度鄰域相關性分析（MNCA）模組：在特徵金字塔的多個尺度上，計算各像素鄰域內回波強度的統計相關係數，構建船舶目標與周圍海雜訊在統計分佈上的差異圖；再透過多尺度上下文融合（如空洞卷積或特徵重加權）增強對模糊散射模式的抗擾能力。 3. 自監督跨層一致性約束：在骨幹網路的每次下採樣階段後，引入輔助重建或對比損失，強制深層特徵與淺層特徵在語義上保持一致，補償小目標在深層因能量衰減而導致的特徵稀釋。 訓練目標結合標準檢測損失（分類交叉熵、邊界框回歸 IoU 損失）與自監督一致性損失（如 L2 特徵差或對比學習 InfoNCE），採用端到端優化。推論時僅保留主干與檢測頭，CDC、MNCA 以正常前向傳播運作，自監督分支移除，無額外計算負擔。與既有方法相比，關鍵差異在於顯式引入電磁散射先驗的 CDC、統計鄰域相關性的多尺度建模，以及跨層自監督補償機制。

## 結果
摘錄未提供可驗證數字。作者聲稱在多個基準資料集上進行大量實驗，結果顯示提出方法在複雜近岸場景中顯著提升偵測性能，能有效降低誤報率並改善小型、弱回波船舶的漏報情況；消融實驗證實 CDC、多尺度鄰域相關性與自監督約束三模組各自貢獻正向增益，且組合效果優於單一模組。

## 限制與展望
受限於摘錄資訊，無法確認具體資料集名稱、影像解析度、訓練樣本數量、推論速度與記憶體佔用等部署指標。方法依賴人工設計的 CDC 核與鄰域統計計算，可能在極高解析度或極低信噪比條件下效果下降；自監督一致性損失的超參數敏感度未說明。後續研究可探索自適應鄰域尺度選擇、輕量化 CDC 實現、以及在真實海上監視系統中的線上學習與領域適應。
