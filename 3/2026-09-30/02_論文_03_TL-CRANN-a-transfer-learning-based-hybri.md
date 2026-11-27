# 論文 03：TL-CRANN: a transfer-learning-based hybrid CNN-RNN model with attention mechanism for cross-domain IoT attack detection.

- 日期：2026-09-30
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Frontiers in artificial intelligence
- Venue：Frontiers in artificial intelligence
- 發布時間：2026-01-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42870898/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13657973/
- DOI：10.3389/frai.2026.1934604
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1589（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
INTRODUCTION: The rapid and pervasive growth of Internet of Things (IoT) devices has significantly expanded the attack surface of current network environments, making them vulnerable to advanced and evolving cyber threats. However, current intrusion detection systems (IDS) usually suffer from weak cross-domain generalization, high false positive rates, and poor performance against novel attacks. METHODS: To overcome these issues, this paper proposes TL-CRANN, a transfer-learning-based hybrid deep learning framework utilizing a convolutional neural network (CNN), bidirectional long short-term memory (Bi-LSTM), and a multi-head self-attention mechanism for cross-domain IoT attack detection. Transfer learning is leveraged to transfer knowledge acquired from source-domain traffic and achieve rapid adaptation to heterogeneous target IoT environments with scarce labeled data. The proposed model is evaluated using three benchmark datasets: CICIDS2017, TON_IoT, and Bot-IoT. RESULTS: Experimental results show that TL-CRANN achieved detection accuracies of 98.37%, 96.21%, and 97.14%, respectively, on the three datasets, and significantly outperformed existing state-of-the-art machine learning and deep learning baselines. DISCUSSION: The results show that transfer learning improves the cross-domain detection performance and training cost. Moreover, the ablation analysis shows that CNN, Bi-LSTM and attention mechanisms-based modules are contribution to effectiveness of proposed framework which also confirms the applicability of TL-CRANN for cross-domain IoT attack detection.

## 背景與目的
物聯網設備快速普及大幅擴大攻擊面，現有入侵偵測系統在跨域泛化能力弱、誤報率高、對新型攻擊偵測差等問題上表現不足。本文旨在解決跨域 IoT 攻擊偵測的泛化與標註資料稀缺難題，提出基於遷移學習的混合 CNN‑BiLSTM‑多頭自注意力框架 TL‑CRANN，期望以預訓練知識快速適應異質目標環境，提升偵測準確度並降低訓練成本。

## 方法
問題設定為跨域 IoT 流量分類，輸入為網路封包/流量特徵向量，輸出為攻擊類別標籤。整體架構包含三階段：(1) 來源域預訓練，使用大規模標註資料（如 CICIDS2017）訓練混合網絡；(2) 遷移微調，將預訓練權重凍結部分層，並在目標域（TON_IoT、Bot‑IoT）少量標註資料上微調；(3) 推理階段，依序通過 CNN 提取局部空間特徵、雙向 LSTM 捕捉時序依賴、多頭自注意力機制對時序特徵加權融合，最後經全連接層輸出類別機率。核心模組：CNN 以多尺度卷積核擷取封包級模式；Bi‑LSTM 雙向建模前後文資訊；多頭注意力並行計算多組注意力權重並拼接，增強關鍵時序段落表達。資料前處理包含流量特徵標準化、類別平衡採樣。訓練目標採用交叉熵損失，優化器為 Adam，學習率衰減策略；遷移學習透過參數共享實現知識遷移，減少目標域標註需求。關鍵差異在於將遷移學習與 CNN‑BiLSTM‑注意力混合架構結合，專門針對異質 IoT 環境的跨域適應。

## 結果
實驗於 CICIDS2017、TON_IoT、Bot‑IoT 三資料集分別達 98.37%、96.21%、97.14% 準確率，顯著優於現有機器學習與深度學習基線。消融實驗證實 CNN、Bi‑LSTM、注意力三模組皆對性能有正向貢獻，遷移學習亦降低訓練成本並提升跨域偵測效果。

## 限制與展望
僅在三個公開基準集驗證，缺乏真實部署與即時推論延遲評估；遷移學習假設源域與目標域分佈相似度較高，若差異過大效果未知；標註資料極少情況下的微調穩定性未深入探討；未報告偽陽性率、F1 等綜合指標，且計算資源消耗細節缺失。後續研究可擴展至更多異質 IoT 場景、引入域適應損失、探索輕量化架構以滿足邊緣部署需求。
