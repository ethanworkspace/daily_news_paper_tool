# 論文 01：DEEMO-R1: De-identity Multimodal Emotion Recognition and Reasoning with Reinforcement Learning.

- 日期：2026-11-28
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：IEEE transactions on pattern analysis and machine intelligence
- Venue：IEEE transactions on pattern analysis and machine intelligence
- 發布時間：2026-11-27T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43102848/
- PDF：
- DOI：10.1109/tpami.2026.3758221
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1802（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Privacy-preserving affective computing requires models to recognize and explain human emotions from de identified visual, acoustic, and textual inputs. Our prior work introduced De-identity Multimodal Emotion Recognition and Reasoning (D-MERR) and the DEEMO dataset. In this pa per, we show that Supervised Fine-Tuning (SFT) is insufficient for D-MERR: the predictions and reasoning of SFT trained Multimodal Large Language Models (MLLMs) remain weakly grounded in identity-free evidence, such as Non-Facial Body Language (NFBL). Reinforcement Learning with Verifiable Rewards (RLVR) can optimize beyond imitation, but existing reward designs remain inadequate: 1) vanilla accuracy rewards supervise only the final emotion label and can cause answer reasoning inconsistency; 2) category-level alignment rewards provide only coarse evidence supervision and can overlook event level NFBL mismatches. Therefore, we propose DEEMO-R1, a two-stage reward-driven framework that applies Group Relative Policy Optimization (GRPO) with two new verifiable rewards after an SFT cold start: 1) an answer-reasoning consistency reward that couples the polarity stated in the reasoning with the final prediction; and 2) an event-level NFBL alignment reward that matches the body-language cues cited in the reasoning to annotated NFBL events in class, count, and order. For reward driven training, we construct DEEMO-RL, a subset of 2,956 new clips annotated with emotion labels and NFBL events, extending DEEMO into DEEMO+. On DEEMO+, DEEMO-R1 improves recognition accuracy from 76.43% to 87.50% and average Clue Overlap from 6.02/10 to 6.64/10 over the SFT baseline, and reduces the answer-reasoning decoupling rate from 30.41% under a vanilla accuracy reward to 2.39%. The code and dataset will be publicly released.

## 背景與目的
隱私保護情感計算要求模型從去識別化的視覺、聲音與文本輸入中辨識並解釋人類情緒。先前工作提出去識別化多模態情緒辨識與推理（D-MERR）及 DEEMO 資料集。然而，監督微調（SFT）對 D-MERR 不足：SFT 訓練的多模態大語言模型（MLLM）其預測與推理仍弱依賴無身份證據（如非臉部身體語言 NFBL）。雖然可驗證獎勵的強化學習（RLVR）可超越模仿優化，但現有獎勵設計不足：1) 純準確率獎勵僅監督最終情緒標籤，導致答案與推理不一致；2) 類別級對齊獎勵僅提供粗略證據監督，忽略事件級 NFBL 不匹配。本文旨在提出 DEEMO-R1，一個兩階段獎勵驅動框架，在 SFT 冷啟動後應用群體相對策略優化（GRPO）並引入兩個新可驗證獎勵，以強化答案推理一致性與事件級 NFBL 對齊，提升去識別化多模態情緒辨識與推理效能。

## 方法
DEEMO-R1 採兩階段獎勵驅動框架。第一階段：對多模態大語言模型進行監督微調（SFT）冷啟動，使其具備基礎的去識別化多模態情緒辨識與推理能力。第二階段：使用群體相對策略優化（GRPO）進行強化學習，引入兩個新可驗證獎勵函數： 1. 答案推理一致性獎勵：將推理文本中陳述的情緒極性與最終預測標籤耦合，強制模型輸出的推理邏輯與最終答案在極性上保持一致，減少答案推理解耦。 2. 事件級 NFBL 對齊獎勵：將推理中引用的身體語言線索與標註的 NFBL 事件在類別、數量與順序上進行精細匹配，提供細粒度證據監督，解決類別級獎勵過於粗略的問題。 為支援獎勵驅動訓練，作者構建 DEEMO-RL 子集，包含 2,956 片新影片，標註情緒標籤與 NFBL 事件，擴充原 DEEMO 為 DEEMO+。訓練時以 GRPO 優化策略，獎勵信號來自上述兩獎勵函數的加權組合。推理階段模型輸出情緒標籤與推理文本，並隱含對 NFBL 事件的引用。關鍵差異在於：針對去識別化場景，明確建模非臉部身體語言事件級對齊，並以答案推理一致性獎勵解決傳統準確率獎勵導致的推理與預測不一致問題。

## 結果
在 DEEMO+ 上，DEEMO-R1 相較 SFT 基線將辨識準確率從 76.43% 提升至 87.50%，平均線索重疊從 6.02/10 提升至 6.64/10。使用純準確率獎勵時答案推理解耦率為 30.41%，引入兩新獎勵後降至 2.39%。摘錄未提供其他基線模型比較數字、消融實驗細節或不同情緒類別的分項表現。定性結論顯示事件級 NFBL 對齊與答案推理一致性獎勵有效改善模型對無身份證據的依賴並減少推理與預測不一致。

## 限制與展望
依目前可取得資料，無法確認模型在 DEEMO+ 以外資料集的泛化能力、NFBL 標註品質對獎勵效果的敏感度、GRPO 超參數選擇對訓練穩定性的影響、以及計算資源需求。潛在風險包含：獎勵函數設計可能過度擬合特定標註規範、事件級對齊在真實場景中噪聲較大時的魯棒性未知、以及去識別化處理可能導致關鍵情緒線索遺失。後續研究方向可探索更多樣化的無身份證據類型、跨資料集驗證、獎勵函數的自適應加權機制，以及輕量化部署策略。
