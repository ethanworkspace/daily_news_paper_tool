# 論文 03：Emergence of polarization in networks of large language model agents

- 日期：2026-10-19
- 來源層級：Tier 1
- 期刊/會議/來源：Nature Communications
- Venue：Nature Communications
- 發布時間：2026-10-08T00:00:00+00:00
- URL：https://doi.org/10.1038/s41467-026-78228-y
- PDF：https://www.nature.com/articles/s41467-026-78228-y_reference.pdf
- DOI：10.1038/s41467-026-78228-y
- arXiv：2501.05171
- 影響指標：2yr_mean_citedness=20.68, h_index=800, i10_index=75885 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Communications
- 引用數：68
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2501.05171
- 全文字數：180302（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/tsinghua-fib-lab/LLM_for_Polarization
- 配對 Repo：tsinghua-fib-lab/LLM_for_Polarization

## 摘要
Rapid advances in large language models (LLMs) have empowered autonomous agents to generate social networks, communicate, and form shared and diverging opinions on political issues. However, our understanding of their collective behaviours and underlying mechanisms remains incomplete. In this paper, we simulate networked systems involving thousands of LLM agents across different backbone models (GPT-3.5, GPT-4o, ChatGLM, Llama-3, and DeepSeek-V3), in which agents interact through LLM-guided conversations and update their opinions over time, resulting in the emergence of opinion polarization. We discover that these agents spontaneously develop their own social network with properties characteristic of human social networks, such as homophilic clustering. The collective opinions of these LLM agents evolve in ways that exhibit behavioural patterns consistent with social phenomena and mechanisms widely discussed in empirical studies of human behaviour and opinion-dynamics models. This consistency suggests that LLM agents can serve as a valuable synthetic testbed for exploring hypothetical intervention strategies in networked LLM-agent systems. Using this testbed, we further examine the effects of a range of network- and individual-level interventions, such as promoting more diverse interactions and reducing confirmation bias. Overall, this work not only sheds light on subtle opinion dynamics and collective behaviour of LLM agents from a network perspective, but also demonstrates their potential for testing hypotheses about opinion dynamics and intervention strategies.

## 背景與目的
大型語言模型（LLM）近年快速發展，使自主代理能生成社交網絡、溝通並形成政治議題觀點，但其集體行為與底層機制仍不清晰，構成潛在社會風險。現有研究多聚焦單一 LLM 與人類互動，或以預設規則操控代理，缺乏大規模、自主演化的網絡化觀點。本文旨在透過模擬數千個 LLM 代理（GPT-3.5、GPT-4o、ChatGLM、Llama-3、DeepSeek-V3），觀察其自發建立社交關係、交換意見並產生極化現象，驗證代理行為是否符合人類意見動力學模型，並探討干預策略，提供合成測試平台以研究假設性干預。

## 方法
研究構建三階段純 LLM 驅動的代理互動流程：(1) 自我表達階段，代理依當前觀點生成支持理由；(2) 溝通階段，代理決定與社交連結或隨機新代理對話，並生成說服訊息；(3) 觀點更新階段，代理根據所有連結代理的訊息修正觀點。系統不預設硬參數，提示詞作為「軟參數」塑造感知、推理與互動，可模擬異質人群。初始化時，觀點以近高斯分佈隨機分配（左、中左、中立、中右、右五級），社交網絡採 Watts–Strogatz 小世界網絡。模擬針對黨派立場、槍枝管制、墮胎禁令三議題，代理自由互動數輪（<10 輪即出現極化）。為釐清左傾偏誤來源，設計成對互動實驗：每對代理僅單輪對話且初始觀點相同，觀察觀點轉移概率；並追蹤三階段的自我不一致頻率，統計檢定（雙側比例 z 檢定，z=8.27，p≪.001）顯示右傾代理不一致顯著較高。另進行網絡層級（調整連結結構）與個體層級（鼓勵開放心態、減少確認偏誤）干預實驗，比較極化緩解效果。

## 結果
模擬顯示中立觀點比例從 40% 下降至 22.5%（黨派）、0.4%（槍枝）、5.1%（墮胎），代理自發極化為左、右兩派，且呈現左傾偏態分佈。代理自發形成同質聚類網絡，符合人類社會網絡同質性特徵。成對實驗揭示右傾代理在單輪互動後易轉向左傾，左傾代理則不轉向右傾，證明左傾模式源於個體層面偏誤。自我不一致在觀點更新階段最頻繁，右傾代理顯著更高。干預實驗發現，在高度極化且近乎固化的網絡中，直接修改網絡結構效果有限；個體層面提升多元接觸與開放心態較有效降低極化。整體行為模式與既有意見動力學模型（論點累積機制）一致。

## 限制與展望
研究依賴特定 LLM（以 GPT 系列為主），觀察到的左傾偏誤可能源於模型微調，限制跨模型泛化。模擬僅涵蓋三政治議題，未涉更廣泛社會議題。代理缺乏人口統計、記憶等背景設定，可能簡化真實人類異質性。自我不一致問題顯示 LLM 理解與轉化訊息能力有限，影響觀點更新可靠性。干預實驗僅在合成環境驗證，尚未在真實人類社交平台測試。後續研究可擴展代理規模、引入更豐富異質屬性、探討長期演化與真實世界驗證。
