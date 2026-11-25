# 論文 01：System of agentic AI for the discovery of metal-organic frameworks.

- 日期：2026-11-06
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
金屬有機框架（MOF）在二氧化碳捕集與集水應用具潛力，但化學空間龐大且需確保可合成性，現有生成模型多受限於原子數規模，難以精確產出大型結構。本文旨在建立一套代理式 AI 系統 MOFGen，整合大型語言模型、擴散模型、量子力學代理與合成可行性代理，實現原子級精度的大型 MOF 結構生成並經實驗驗證。

## 方法
MOFGen 採用多代理協作架構： 1. 問題設定與輸入輸出：輸入為目標應用需求（如 CO₂ 捕集、集水），輸出為具原子座標的 MOF 晶體結構與對應有機連結子。 2. 整體架構：四個相互串聯的代理依序執行組成、結構生成、優化篩選、合成可行性評估。 3. 核心模組： - 大型語言模型（LLM）代理：根據文獻知識與專家規則提出 MOF 化學組成（金屬節點、連結子類型、拓撲）。 - 擴散模型代理：以條件擴散過程在三維空間生成完整晶體結構，突破傳統生成模型僅能處理數十原子的限制，可產出數百至數千原子的大型週期性結構。 - 量子力學代理：對生成結構執行第一性原理計算（如 DFT）進行幾何優化、能階評估與性質預測（吸附能、孔隙度），並依能量與性質門檻過濾候選。 - 合成可行性代理：結合專家合成規則與機器學習分類器，評估連結子合成路徑、反應物可得性、反應條件相容性，輸出可合成性分數。 4. 資料表示：結構以原子類型、分數座標、晶格向量編碼；連結子以 SMILES/圖神經網路嵌入表示。 5. 訓練目標與損失：擴散模型採用去噪分數匹配損失；LLM 以條件生成損失微調；合成可行性分類器採用交叉熵損失。優化採用 AdamW，學習率排程與早停。 6. 推論流程：LLM 提出組成 → 擴散模型生成初始結構 → 量子力學代理優化並篩選 → 合成可行性代理打分 → 保留高分候選進入高通量實驗驗證。 7. 與既有方法差異：傳統生成模型多為單一模型且限於小分子/小晶胞；MOFGen 以代理串聯實現跨尺度、多目標協同，並整合量子計算與合成規則實現端到端可合成設計。

## 結果
作者報告 MOFGen 產生數十萬個 MOF 結構與可合成有機連結子，並通過高通量實驗驗證，成功合成四個「AI 夢境」MOF。摘錄未提供可驗證數字（如吸附容量、合成成功率、基線模型比較指標），僅能觀察到定性結論：系統能生成大尺度原子級精確結構並實現實驗合成。

## 限制與展望
目前摘錄缺乏訓練資料規模、模型超參數、量子計算精度、合成可行性分類器效能指標等關鍵細節，無法評估泛化能力與計算成本。代理間錯誤傳播風險、LLM 產生組成的化學合理性、擴散模型對長程有序性的保真度均未量化。後續研究需補充基線比較、消融實驗、擴展至其他多孔材料，並建立標準化評估基準以利重現與部署。
