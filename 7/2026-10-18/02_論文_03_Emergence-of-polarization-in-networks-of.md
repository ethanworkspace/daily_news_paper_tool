# 論文 03：Emergence of polarization in networks of large language model agents

- 日期：2026-10-18
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature Communications
- Venue：Nature Communications
- 發布時間：2026-10-08T00:00:00+00:00
- URL：https://doi.org/10.1038/s41467-026-78228-y
- PDF：https://www.nature.com/articles/s41467-026-78228-y_reference.pdf
- DOI：10.1038/s41467-026-78228-y
- arXiv：2501.05171
- 影響指標：2yr_mean_citedness=20.66, h_index=791, i10_index=75883 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Communications
- 引用數：69
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2501.05171
- 全文字數：180302（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/tsinghua-fib-lab/LLM_for_Polarization
- 配對 Repo：tsinghua-fib-lab/LLM_for_Polarization

## 摘要
Rapid advances in large language models (LLMs) have empowered autonomous agents to generate social networks, communicate, and form shared and diverging opinions on political issues. However, our understanding of their collective behaviours and underlying mechanisms remains incomplete. In this paper, we simulate networked systems involving thousands of LLM agents across different backbone models (GPT-3.5, GPT-4o, ChatGLM, Llama-3, and DeepSeek-V3), in which agents interact through LLM-guided conversations and update their opinions over time, resulting in the emergence of opinion polarization. We discover that these agents spontaneously develop their own social network with properties characteristic of human social networks, such as homophilic clustering. The collective opinions of these LLM agents evolve in ways that exhibit behavioural patterns consistent with social phenomena and mechanisms widely discussed in empirical studies of human behaviour and opinion-dynamics models. This consistency suggests that LLM agents can serve as a valuable synthetic testbed for exploring hypothetical intervention strategies in networked LLM-agent systems. Using this testbed, we further examine the effects of a range of network- and individual-level interventions, such as promoting more diverse interactions and reducing confirmation bias. Overall, this work not only sheds light on subtle opinion dynamics and collective behaviour of LLM agents from a network perspective, but also demonstrates their potential for testing hypotheses about opinion dynamics and intervention strategies.

## 背景與目的
大型語言模型（LLM）賦予自主代理生成社交網絡、溝通並形成政治觀點的能力，但其集體行為與底層機制仍不清晰，帶來潛在社會風險。現有研究多聚焦單一 LLM 與人類互動，或受限於代理規模與預設規則，難以捕捉大規模自主互動產生的涌現極化現象。本文旨在構建千級 LLM 代理系統，觀察其自發形成社交網絡與觀點極化過程，驗證與人類社會現象的一致性，並測試干預策略，為網絡化 LLM 代理系統提供合成測試床。

## 方法
研究構建三階段 LLM 驅動代理：自我表達階段，代理生成支持當前觀點的理由；溝通階段，代理決定與社交連結或隨機新代理互動，並生成說服性訊息；觀點更新階段，代理根據接收訊息更新觀點。全程無預設硬規則，提示詞作為軟參數塑造感知與推理。模擬針對黨派立場、槍枝管制、墮胎禁令三議題，採五級政治光譜（左、溫和左、中立、溫和右、右），初始觀點近高斯分佈，社交網絡為 Watts–Strogatz 小世界網絡。代理骨幹模型涵蓋 GPT-3.5、GPT-4o、ChatGLM、Llama-3、DeepSeek-V3。另設計成對互動實驗剝離固有偏見：固定雙代理同觀點、單輪互動，測量觀點轉移概率。並追蹤三階段自我不一致頻率，統計檢驗右傾代理不一致顯著更高（z=8.27, p≪.001）。干預實驗比較網絡結構修改與個體開放心態對極化緩解效果。

## 結果
模擬顯示中立比例從 40% 下降至 22.5%、0.4%、5.1%（三議題），觀點自發極化為左右兩派，且呈現左傾偏斜，符合 OpenAI 模型固有偏見。成對實驗揭示非對稱觀點更新：右傾代理偶爾轉為左傾，反之則無。自我不一致在觀點更新階段最頻繁，右傾代理顯著更高。干預實驗發現：高極化網絡中直接修改網絡結構效果有限，鼓勵個體接觸多元觀點與開放心態更有效。多骨幹模型結果一致。摘錄未提供可驗證的完整消融實驗數字。

## 限制與展望
研究依賴特定提示詞設計，可能無法涵蓋所有人類心理異質性；初始化為近高斯分佈與小世界網絡，現實社會結構更複雜；骨幹模型偏見（如左傾）影響極化分佈，難以完全剝離模型內在偏好與社會影響；干預實驗僅在合成環境驗證，推廣至真人-LLM 混合系統需謹慎；未探討長期演化穩定性、惡意代理攻擊或隱私風險。後續可擴展多模態互動、動態網絡重構、跨文化議題及真實部署評估。
