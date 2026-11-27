# 論文 03：Emergence of polarization in networks of large language model agents

- 日期：2026-10-13
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature Communications
- Venue：Nature Communications
- 發布時間：2026-10-08T00:00:00+00:00
- URL：https://doi.org/10.1038/s41467-026-78228-y
- PDF：https://www.nature.com/articles/s41467-026-78228-y_reference.pdf
- DOI：10.1038/s41467-026-78228-y
- arXiv：2501.05171
- 影響指標：2yr_mean_citedness=20.66, h_index=791, i10_index=75837 (OpenAlex)
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
研究問題：LLM agents 在大規模網絡中自發形成意見極化，但其集體行為機制尚不清楚。現有方法多為規則代理或小規模、重腳手架模擬，缺乏自主社交能力與大規模涌現現象觀察。本文旨在建立千級 LLM agents 自由互動的合成系統，觀察極化涌現、同質聚類等社會網絡特性，並驗證其與人類意見動力學模型的一致性，提供干預策略測試平台。

## 方法
問題設定：輸入為政治議題（如黨派立場、槍枝管制、墮胎禁令）與初始近高斯分佈的五級意見（左、中左、中立、中右、右），以及 Watts–Strogatz 小世界網絡初始化社會關係。輸出為隨輪次演化的意見分佈與自組織網絡結構。整體架構採三階段迭代循環，完全由 LLM 提示驅動，無硬編碼規則：(1) 自我表達階段，agent 依歷史互動生成支持當前意見的理由；(2) 溝通階段，agent 決定與現有鄰居或隨機新節點互動，並依雙方意見與理由生成說服訊息；(3) 意見更新階段，agent 綜合所有鄰居訊息更新自身意見。提示詞作為「軟參數」編碼異質心理行為模式。實驗使用 OpenAI ChatGPT (GPT-3.5/GPT-4o) 為主，並測試 ChatGLM、Llama-3、DeepSeek-V3 等開源模型，結果可比。為釐清內在偏誤，設計成對互動實驗：固定雙方意見相同、僅單輪交換，觀察意見轉移概率的非對稱性。另追蹤三階段中的自我不一致現象（理由、溝通、更新與當前意見不符），統計右傾 agents 顯著更高（雙側比例 z 檢定，z=8.27, p≪.001）。所有代理無預設人口屬性、記憶或詳細思維，均由提示即時生成。

## 結果
模擬顯示，中立意見比例從 40% 在少於 10 輪內分別降至 22.5%（黨派）、0.4%（槍枝）、5.1%（墮胎），agents 自發極化為左、右兩派，且呈現左偏分佈（與 OpenAI 模型固有左傾偏誤一致）。成對實驗揭示右傾 agents 在單輪同質互動後偶爾轉為左傾，左傾則不轉右，證明偏誤源於個體意見形成而非網絡影響。自我不一致在意見更新階段最頻繁，且右傾 agents 顯著更高（z=8.27, p≪.001）。自組織網絡展現同質聚類特性，集體意見動態與論點累積模型一致。干預實驗發現，在高度極化且近結晶化的網絡中，直接修改網絡結構效果有限，個體層面鼓勵接觸多元意見與開放心態較有效。摘錄未提供完整消融數值與統計顯著性細節。

## 限制與展望
研究僅以三個美國政治議題為例，且主要依賴 OpenAI 閉源模型，開源模型驗證僅在補充資料中簡述，泛化性有待進一步確認。模擬規模雖達千級，但與真實社群規模仍有數量級差距，且缺乏長期演化與外部事件衝擊的考量。提示詞作為軟參數難以精確控制心理構念，自我不一致問題顯示 LLM 理解與推理仍有缺口，可能影響極化機制的解讀。干預策略僅在合成系統測試，真實部署風險（如操縱輿論、加劇極化）需謹慎評估。後續研究可擴展議題多樣性、引入異質人口屬性、改進一致性機制，並探討人機混合環境下的動態互動。
