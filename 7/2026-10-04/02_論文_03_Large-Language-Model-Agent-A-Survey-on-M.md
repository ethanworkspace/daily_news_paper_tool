# 論文 03：Large Language Model Agent: A Survey on Methodology, Applications and Challenges

- 日期：2026-10-04
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
大型語言模型（LLM）代理被視為通往通用人工智慧的關鍵路徑，但現有研究碎片化，缺乏系統性的方法論分類。本文旨在透過方法論為中心的分類法，整合代理建構、協作與演化三大維度，並連結評估、工具、現實挑戰與應用領域，提供統一的架構視角，釐清設計原則與涌現行為的關聯，為後續研究建立結構化分類基礎。

## 方法
本調查提出以「建構—協作—演化」為核心的三維方法論分類法（圖 2）。建構層包含四大支柱：① 角色定義，分為人工靜態配置（如 Camel、AutoGen、MetaGPT 等預設對話角色）與批次動態生成（透過參數化模板或潛在空間採樣產生異質群體）；② 記憶機制，分短期記憶（對話歷史、環境回饋，受上下文窗口限制，需壓縮）與長期記憶（技能庫、經驗庫、工具合成框架，如 Voyager、ExpeL、TPTU），並引入知識檢索作為外部記憶（RAG、GraphRAG、互動式檢索、推理整合檢索如 IRCoT、DeepRAG）；③ 規劃能力，著重任務分解與回饋驅動的迭代修正；④ 行動執行，涵蓋工具調用與環境互動。協作層依控制模式分為集中式、去中心化與混合式架構。演化層包含自主優化、多代理共同演化與外部資源整合。調查並梳理評估基準、開發工具、安全隱私倫理議題及多元應用場域，形成完整生命週期視角。

## 結果
本文為綜述論文，摘錄未提供可驗證數字。主要定性結論包括：建立了統一的 LLM 代理方法論分類法，揭示建構、協作、演化三維度的內在聯繫；整理了主流框架的角色、記憶、規劃、行動設計模式；彙整評估基準、開發工具與安全隱私挑戰；指出未來研究方向朝向更自主的演化機制、跨領域工具合成與可信賴部署。

## 限制與展望
作為文獻綜述，本文僅涵蓋至 2025 年 3 月的公開論文，可能遺漏最新進展；分類法基於作者人工歸納，未經實證驗證其完整性與互斥性；未提供實驗基準比較，無法量化各架構優劣；後續研究需補充實證評估、擴展至多模態代理、並深入探討大規模部署的安全治理與標準化問題。
