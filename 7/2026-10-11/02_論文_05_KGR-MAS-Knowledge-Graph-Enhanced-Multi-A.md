# 論文 05：KGR-MAS: Knowledge Graph-Enhanced Multi-Agent LLM Framework for Evidence-Based Medical Diagnosis and Clinical Decision Support.

- 日期：2026-10-11
- 來源層級：Tier 2
- 期刊/會議/來源：IEEE journal of biomedical and health informatics
- Venue：IEEE journal of biomedical and health informatics
- 發布時間：2026-10-08T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42848569/
- PDF：
- DOI：10.1109/jbhi.2026.3740738
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1354（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Large Language Models (LLMs) demonstrate significant potential in healthcare applications, yet they exhibit reasoning bias, information bottlenecks, and limited adaptability in complex clinical settings. To address these limitations, we propose KGR-MAS, which introduces an integrated control loop that couples (1) KG-derived diagnostic paths for executable subtask decomposition and dynamic agent allocation, while using these KG reasoning paths to initialize shared short-term memory; (2) a language-level LSTM-inspired gating mechanism with Transformer-XL short-term memory to regulate cross-agent information flow and maintain global coherence; and (3) a KG-guided RAG-STM process that triggers evidence retrieval at diagnostic checkpoints and writes the retrieved evidence back into STM for subsequent reasoning. We constructed a large-scale medical knowledge graph achieving the best embedding performance (Hits@1:32.8%, MRR:0.498). Experimental results on MedQA and MedMCQA show that KGR-MAS achieves 87.2% accuracy on MedQA($\uparrow$14.4%), and 77.4% average accuracy across four open-domain datasets ($\uparrow$29.0%), outperforming larger models like GPT-o1(72.0%). KGR-MAS provides interpretable, accurate, and clinically grounded diagnostic reasoning, highlighting its potential as a next-generation AI assistant for medical decision-making.

## 背景與目的
大型語言模型在醫療應用展現潛力，但存在推理偏誤、資訊瓶頸與複雜臨床情境適應性不足等問題。現有方法多缺乏知識圖譜驅動的診斷路徑、動態多代理分配與跨代理記憶調控機制，導致推理不可解釋且難以落地。本文提出 KGR-MAS，透過整合控制迴路，耦合知識圖譜衍生的診斷路徑進行子任務分解與代理動態分配、以 LSTM 風格閘控機制結合 Transformer‑XL 短期記憶調節跨代理資訊流、並在診斷檢查點觸發 KG 引導的 RAG‑STM 檢索與寫回，旨在提供可解釋、準確且臨床落地的診斷推理。

## 方法
問題設定為給定臨床病例描述，輸出診斷決策。KGR-MAS 採用多代理架構，核心包含三大模組與一體化控制迴路：(1) 知識圖譜衍生診斷路徑模組：利用大規模醫學知識圖譜（嵌入表現 Hits@1 32.8%、MRR 0.498）產生可執行的診斷路徑，據此將病例分解為子任務並動態分配專責代理，同時將路徑資訊初始化共享短期記憶 (STM)。(2) 語言層級 LSTM 風格閘控機制與 Transformer‑XL STM：在代理間引入閘控單元，控制資訊寫入、遺忘與輸出，配合 Transformer‑XL 的循環記憶保持長距離上下文連貫，確保全域推理一致性。(3) KG 引導的 RAG‑STM 流程：於關鍵診斷檢查點觸發知識圖譜導向的檢索增強生成，將檢索到的證據寫回 STM 供後續推理使用。訓練階段著重於知識圖譜嵌入優化與代理協作的損失函數（摘錄未詳細列出），推理時依序經過路徑生成、子任務分配、閘控記憶交互、檢查點檢索與最終診斷輸出。與既有方法相比，關鍵差異在於將 KG 推理路徑直接作為代理分配與記憶初始化依據，並以語言層級閘控實現跨代理資訊流的精細調控。

## 結果
實驗顯示 KGR-MAS 在 MedQA 達 87.2% 準確率（較基線提升 14.4%），在四個開放領域資料集平均準確率 77.4%（提升 29.0%），超越 GPT‑o1 的 72.0%。知識圖譜嵌入達到最佳 Hits@1 32.8%、MRR 0.498。對 MedMCQA 的具體數字摘錄未提供可驗證數字。定性上，系統展現可解釋、準確且具臨床依據的診斷推理能力。

## 限制與展望
研究限制包括：(1) 僅在 MedQA、MedMCQA 及四開放資料集驗證，缺乏真實臨床病歷與前瞻性試驗；(2) 知識圖譜建構與嵌入品質對整體表現影響大，擴展性與更新機制未詳述；(3) 多代理協作與閘控機制的計算成本、延遲未量化，部署可行性待證；(4) 摘錄未提供消融實驗細節，難以判斷各模組貢獻；(5) 潛在幻覺與錯誤傳播風險仍需進一步安全性評估。後續可朝臨床實證、知識圖譜動態更新、效率優化與完整消融研究方向推進。
