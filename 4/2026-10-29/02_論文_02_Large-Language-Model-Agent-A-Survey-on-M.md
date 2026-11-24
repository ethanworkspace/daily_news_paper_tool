# 論文 02：Large Language Model Agent: A Survey on Methodology, Applications and Challenges

- 日期：2026-10-29
- 來源層級：Tier 3
- 期刊/會議/來源：ArXiv
- Venue：ArXiv
- 發布時間：2025-03-27T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/56fc00881e8d854f3cdecb2d072c369ac818c3ef
- PDF：
- DOI：10.48550/arxiv.2503.21460
- arXiv：2503.21460
- 影響指標：N/A (preprint)
- 影響指標來源：preprint (not peer-reviewed journal/conference)
- 引用數：259
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2503.21460
- 全文字數：176237（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/luo-junyu/Awesome-Agent-Papers
- 配對 Repo：luo-junyu/Awesome-Agent-Papers

## 摘要
The era of intelligent agents is upon us, driven by revolutionary advancements in large language models. Large Language Model (LLM) agents, with goal-driven behaviors and dynamic adaptation capabilities, potentially represent a critical pathway toward artificial general intelligence. This survey systematically deconstructs LLM agent systems through a methodology-centered taxonomy, linking architectural foundations, collaboration mechanisms, and evolutionary pathways. We unify fragmented research threads by revealing fundamental connections between agent design principles and their emergent behaviors in complex environments. Our work provides a unified architectural perspective, examining how agents are constructed, how they collaborate, and how they evolve over time, while also addressing evaluation methodologies, tool applications, practical challenges, and diverse application domains. By surveying the latest developments in this rapidly evolving field, we offer researchers a structured taxonomy for understanding LLM agents and identify promising directions for future research. The collection is available at https://github.com/luo-junyu/Awesome-Agent-Papers.

## 背景與目的
大型語言模型（LLM）代理被視為通往通用人工智慧的關鍵路徑，具備目標導向行為與動態適應能力。現有研究碎片化，缺乏統一的方法論分類，難以系統理解代理架構、協作機制與演化路徑間的根本聯繫。本文旨在建立以方法論為中心的分類體系，解構代理建構、協作與演化三大維度，並整合評估、工具、現實挑戰與應用領域，提供研究者結構化的認知框架，推動領域發展。

## 方法
本調查提出三維度方法論框架： 1. 代理建構：包含四大支柱——(a) 角色定義：靜態人工策展（如 Camel、AutoGen、MetaGPT）與動態批次生成（參數化初始化、DSPy 優化）兩種範式；(b) 記憶機制：短期記憶保留對話歷史與環境回饋（ReAct、ChatDev、Graph of Thoughts、AFlow），長期記憶將推理軌跡轉化為可復用資產，分為技能庫、經驗庫、工具合成三類（Voyager、GITM、ExpeL、Reflexion、TPTU、OpenAgents、Lego-Prover、MemGPT）；知識檢索作為外部記憶擴展，採靜態語料/知識圖譜、互動式檢索、推理整合檢索（RAG、GraphRAG、Chain of Agents、IRCoT、Llatrieval、KG-RAR、DeepRAG）。(c) 規劃能力：任務分解與回饋驅動調整（摘錄未完整）。(d) 行動執行：工具調用與環境互動。 2. 協作機制：集中式控制、去中心化合作、混合架構，強調多代理通訊協定與角色協調。 3. 演化機制：自主優化、多代理共同演化、外部資源整合，支援代理隨時間自我改進。 輔以評估基準、開發工具、安全隱私倫理議題、多元應用領域四大實務維度，形成完整生命週期視角。

## 結果
摘錄未提供可驗證數字。本文為綜述論文，主要結論為質性：提出統一的建構-協作-演化分類法，揭示代理設計原則與涌現行為的根本聯繫；整理現有框架（如 Camel、AutoGen、MetaGPT、Voyager、MemGPT 等）並歸類至分類體系；指出評估方法、工具生態、安全隱私與應用落地仍為關鍵挑戰；識別未來研究方向包含標準化評估、跨域泛化、長期記憶優化、多代理協作協定與負責任部署。

## 限制與展望
依目前可取得資料，無法確認完整實驗數據與基線比較。限制包括：(1) 文獻截止至 2025 年 3 月，可能遺漏最新進展；(2) 分類法基於作者主觀整理，缺乏實證驗證其完備性；(3) 評估基準與指標尚未統一，難以量化比較各架構優劣；(4) 安全、隱私、倫理等現實議題僅質性討論，缺乏具體緩解方案實證；(5) 部署層面的延遲、成本、可擴展性分析不足。後續研究可朝標準化評估框架、長期記憶機制實證、多代理協作協定形式化、負責任 AI 治理等方向深入。
