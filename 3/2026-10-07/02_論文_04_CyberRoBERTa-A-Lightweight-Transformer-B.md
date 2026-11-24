# 論文 04：CyberRoBERTa: A Lightweight Transformer-Based Language Model for IoT Intrusion Detection.

- 日期：2026-10-07
- 來源層級：Tier 2
- 期刊/會議/來源：Sensors (Basel, Switzerland)
- Venue：Sensors (Basel, Switzerland)
- 發布時間：2026-10-07T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42884526/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13667479/
- DOI：10.3390/s26196326
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1559（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
With the accelerated proliferation of the Internet of Things (IoT) and its widespread use in sensitive areas such as healthcare, homes, and factories, security has become an increasingly critical concern. IoT remains one of the most challenging domains to secure, lacking the manageable scale, well-maintained software, and homogeneous environments of easily secured systems. Large language models (LLMs) have recently been applied to improve IoT security; however, most applications treat LLMs as "off-the-shelf" tools, creating a domain mismatch because model representations, tokenizers, and data collators are designed for natural language rather than network traffic. In this work, we present CyberRoBERTa, built specifically to test whether departing from off-the-shelf LLM components, through a domain-specific Unigram tokenizer and an IoT-specialized data collator, yields a genuine advantage for IoT intrusion detection. We instantiate this framework as a compact, 10.2-million-parameter model designed for fully self-contained, on-device operation. Using CICIoT2023, TON_IoT, and Edge-IIoTset, the model achieves a binary classification F1-score of 96% and a multiclass F1-score of 89.54%. We further validate these results in three ways: a comparison against a classical machine learning baseline shows comparable accuracy; isolating the tokenizer's contribution from pretraining scale shows its benefit holds under matched pretraining conditions; and evaluating class-imbalance interventions shows improved detection on the most data-scarce class.

## 背景與目的
物聯網設備廣泛應用於醫療、家庭與工廠等敏感領域，但其異質性、缺乏統一管理與軟體更新，使安全防護極具挑戰。近年大型語言模型被嘗試用於入侵偵測，但多數直接套用現成模型，導致 tokenizer、資料整理器與表示層為自然語言設計，與網路流量特徵不匹配。本研究旨在驗證是否透過領域專用的 Unigram tokenizer 與 IoT 專用 data collator，脫離現成 LLM 元件，能為 IoT 入侵偵測帶來實質優勢，並構建可在裝置端獨立運行的輕量模型。

## 方法
問題設定：輸入為原始網路流量封包或流統計特徵，輸出為二元（正常/攻擊）與多類別攻擊類型標籤。模型架構：採用 RoBERTa 風格的 Transformer 編碼器，參數量約 1,020 萬，設計為輕量化以支援 on-device 推論。核心模組：(1) 領域專用 Unigram tokenizer，將流量位元組序列切分為適合網路協定語彙的子詞單元，取代標準 BPE/WordPiece；(2) IoT 專用 data collator，負責將 tokenizer 輸出轉換為模型所需的張量格式，並處理封包長度不一、欄位對齊等網路特有問題。資料表示：流量經 tokenizer 編碼為 token ID 序列，再由 collator 進行 padding/truncation 與 batch 組裝。訓練目標與損失：摘錄未明確說明預訓練任務（如 MLM）或微調損失函數，僅指出模型在三個公開資料集上進行監督式分類訓練。最佳化策略：未提供學習率、排程器或硬體細節。推論流程：原始流量 → tokenizer → collator → CyberRoBERTa 編碼器 → 分類頭 → 預測標籤。關鍵差異：與直接微調現成 LLM 不同，本文自行設計 tokenizer 與 collator，並縮小模型規模以適應邊緣部署，強調領域適配而非單純參數遷移。

## 結果
在 CICIoT2023、TON_IoT 與 Edge-IIoTset 三資料集上，CyberRoBERTa 達到二元分類 F1 96% 與多類別分類 F1 89.54%。作者進一步以三種方式驗證：(1) 與傳統機器學習基線比較，準確度相當；(2) 在控制預訓練規模條件下隔離 tokenizer 貢獻，證明其優勢持續存在；(3) 測試類別不平衡處理策略，發現對最稀少類別的偵測有所提升。摘錄未提供可驗證數字（如基線具體 F1、消融實驗數值、不平衡處理前後差異），僅能觀察到定性結論為正向。

## 限制與展望
資料層面僅使用三個公開資料集，未涵蓋真實部署環境的流量分佈變化與零日攻擊。方法層面缺乏預訓練任務、損失函數、超參數與訓練計算資源的詳細描述，難以復現或評估訓練效率。評估層面未報告混淆矩陣、每類別 F1、推論延遲與記憶體佔用等關鍵指標，亦未與最新深度學習基線（如 CNN、LSTM、Graph-based 模型）直接比較。部署層面雖宣稱 on-device 可行，但未提供實際嵌入式平台測試結果。後續研究可擴展至更多異質 IoT 場景、引入自監督預訓練、量化與剪枝優化，並建立標準化基線以利公平比較。
