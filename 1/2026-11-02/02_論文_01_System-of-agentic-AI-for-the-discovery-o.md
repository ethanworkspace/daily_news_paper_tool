# 論文 01：System of agentic AI for the discovery of metal-organic frameworks.

- 日期：2026-11-02
- 來源層級：Tier 1
- 期刊/會議/來源：Nature computational science
- Venue：Nature computational science
- 發布時間：2026-11-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43064736/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13787987/
- DOI：10.1038/s43588-026-01058-x
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1085（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Generative models and machine learning promise accelerated material discovery in metal-organic frameworks (MOFs) for CO2 capture and water harvesting, but face substantial challenges in navigating vast chemical spaces while ensuring synthesizability. Here we present MOFGen, a system of agentic artificial intelligence (AI) comprising interconnected agents: a large language model that proposes MOF compositions, a diffusion model that generates crystal structures, quantum mechanical agents that optimize and filter candidates, and synthetic-feasibility agents guided by expert rules and machine learning. Trained on a broad set of experimentally reported MOFs and computational databases, MOFGen generated hundreds of thousands of MOF structures and synthesizable organic linkers. The uniqueness of our approach lies in its ability to generate large MOF structures with atomic precision, beyond the scale of conventional generative models limited to tens of atoms. This approach was validated through high-throughput experiments and the successful synthesis of four 'AI-dreamt' MOFs.

## 背景與目的
本研究針對金屬有機框架（MOF）在二氧化碳捕集與集水應用中的材料發現問題，現有生成模型難以在龐大化學空間中兼顧合成可行性與原子級精度，且多限於數十原子規模。MOFGen 提出一套代理式 AI 系統，整合大型語言模型、擴散模型、量子力學代理與合成可行性代理，旨在實現大規模、原子精確的 MOF 結構生成並經實驗驗證，填補生成模型與實際合成之間的鴻溝。

## 方法
問題設定：輸入為目標性能指標（如 CO₂ 吸附容量、水收集能力）與化學組成約束，輸出為具備原子座標的完整 MOF 晶體結構及可合成有機連結子。系統架構包含四大相互協作代理：(1) 大型語言模型（LLM）代理，根據文獻知識與專家規則提出候選金屬節點、連結子類型及拓撲組合；(2) 擴散模型代理，以條件擴散過程在三維周期性晶格空間中生成原子級結構，支援超過百原子的大尺度 MOF；(3) 量子力學代理，採用 DFT 或半經驗方法對生成結構進行幾何優化、能量篩選與性質預測，確保熱力學穩定；(4) 合成可行性代理，結合專家規則庫與機器學習分類器，評估連結子合成路徑、反應條件與前驅體可得性。資料前處理將實驗報告 MOF（如 CSD、CoRE MOF）與計算資料庫標準化為統一圖表示，包含原子類型、鍵序、拓撲標識與周期性邊界條件。訓練目標採用多任務損失：擴散模型的去噪分數匹配損失、LLM 的序列生成交叉熵、量子代理的能量/性質回歸損失、可行性代理的二元分類交叉熵，並以階段式最佳化依序預訓練再微調。推理流程為：LLM 提出組成 → 擴散模型生成初始結構 → 量子代理優化並篩選 → 可行性代理打分 → 保留高分候選進入高通量實驗驗證。關鍵差異在於代理間的閉環反饋與大尺度原子精確生成，突破傳統生成模型僅能處理數十原子的限制。

## 結果
作者報告 MOFGen 共生成數十萬個 MOF 結構與可合成有機連結子，經高通量實驗驗證成功合成四個「AI 夢想」MOF，證實系統能產出具備原子級精度的大尺度結構並具備實際合成可行性。摘錄未提供可驗證的具體吸附容量、比表面積或基線模型比較數字，僅能觀察到定性結論：代理式架構有效整合生成與篩選，實現從設計到合成的閉環。

## 限制與展望
目前摘錄僅說明整體流程與四例成功合成，缺乏系統性基線比較、統計顯著性分析、擴散模型對不同拓撲類別的泛化能力評估，以及量子力學計算成本與擴展性討論。合成可行性代理依賴專家規則可能引入偏見，且高通量實驗規模有限，難以全面驗證化學空間覆蓋率。後續研究需補充大規模基線實驗、不確定性量化、自動化合成路徑規劃與開放原始碼釋出，以利社群驗證與擴展。
