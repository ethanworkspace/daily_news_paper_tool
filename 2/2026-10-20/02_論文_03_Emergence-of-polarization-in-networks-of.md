# 論文 03：Emergence of polarization in networks of large language model agents

- 日期：2026-10-20
- 來源層級：Tier 1
- 期刊/會議/來源：Nature Communications
- Venue：Nature Communications
- 發布時間：2026-10-08T00:00:00+00:00
- URL：https://doi.org/10.1038/s41467-026-78228-y
- PDF：https://www.nature.com/articles/s41467-026-78228-y_reference.pdf
- DOI：10.1038/s41467-026-78228-y
- arXiv：2501.05171
- 影響指標：2yr_mean_citedness=20.75, h_index=799, i10_index=75898 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Communications
- 引用數：67
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2501.05171
- 全文字數：180302（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/tsinghua-fib-lab/LLM_for_Polarization
- 配對 Repo：tsinghua-fib-lab/LLM_for_Polarization

## 摘要
Rapid advances in large language models (LLMs) have empowered autonomous agents to generate social networks, communicate, and form shared and diverging opinions on political issues. However, our understanding of their collective behaviours and underlying mechanisms remains incomplete. In this paper, we simulate networked systems involving thousands of LLM agents across different backbone models (GPT-3.5, GPT-4o, ChatGLM, Llama-3, and DeepSeek-V3), in which agents interact through LLM-guided conversations and update their opinions over time, resulting in the emergence of opinion polarization. We discover that these agents spontaneously develop their own social network with properties characteristic of human social networks, such as homophilic clustering. The collective opinions of these LLM agents evolve in ways that exhibit behavioural patterns consistent with social phenomena and mechanisms widely discussed in empirical studies of human behaviour and opinion-dynamics models. This consistency suggests that LLM agents can serve as a valuable synthetic testbed for exploring hypothetical intervention strategies in networked LLM-agent systems. Using this testbed, we further examine the effects of a range of network- and individual-level interventions, such as promoting more diverse interactions and reducing confirmation bias. Overall, this work not only sheds light on subtle opinion dynamics and collective behaviour of LLM agents from a network perspective, but also demonstrates their potential for testing hypotheses about opinion dynamics and intervention strategies.

## 背景與目的
大型語言模型（LLM）賦予自主代理人生成社交網絡、溝通並形成政治觀點的能力，但其集體行為與底層機制仍不清晰，可能對人類社會產生隱性風險。現有研究多聚焦單一 LLM 與人類互動，或以預設規則限制代理人自主性，缺乏大規模、自由演化的多代理人系統實證。本文旨在構建由數千個 LLM 代理人組成的合成網絡系統，觀察觀點極化與同質聚類的自發涌現，並驗證其與人類意見動力學模型的一致性，進而作為測試干預策略的合成試驗床。

## 方法
研究構建三階段 LLM 驅動的代理人互動流程：(1) 自我表達階段，代理人依當前觀點生成支持理由；(2) 溝通階段，代理人決定與社交連結或隨機新代理人對話，並生成說服訊息；(3) 觀點更新階段，代理人根據所有連結代理人的訊息更新觀點。所有階段均由 LLM 直接生成，無預設硬性規則，提示詞作為「軟參數」調控感知與推理。初始化時，觀點採近高斯分佈（五級政治光譜：左、中左、中立、中右、右），社交網絡採 Watts–Strogatz 小世界網絡。實驗涵蓋三議題（政黨傾向、槍枝管制、墮胎禁令），使用 GPT-3.5、GPT-4o、ChatGLM、Llama-3、DeepSeek-V3 等多骨幹模型，透過 OpenAI API 及開源模型運行。另設計成對互動實驗（固定單一連結、雙方初始觀點相同）以剝離內在偏見與社會影響，並追蹤三階段的自我不一致現象（理由、溝通、更新與當前觀點不符），統計右傾代理人不一致頻率顯著較高（雙側比例 z 檢定，z=8.27, p≪.001）。干預實驗在高極化網絡中比較網絡結構修改與個體開放心態兩類策略。

## 結果
模擬顯示：中立觀點比例從 40% 驟降至 22.5%（政黨傾向）、0.4%（槍枝管制）、5.1%（墮胎禁令），代理人自發極化為左、右兩派，且呈現左傾偏態分佈（歸因於 GPT 固有左傾偏見）。成對實驗揭示非對稱觀點更新：右傾代理人偶爾轉為左傾，左傾代理人不轉右，確認偏見源於個體生成機制。自我不一致在觀點更新階段最頻繁，且右傾代理人顯著更高。網絡層面出現同質聚類（homophilic clustering），符合人類社會網絡特徵。干預結果：直接修改網絡結構對降低極化效果有限；提升個體接觸多元觀點與開放心態較有效。摘錄未提供可驗證的具體干預效果數字。

## 限制與展望
研究依賴特定 LLM（含 GPT 系列）且觀察到左傾偏見，可能限制結論普適性；自我不一致問題顯示代理人理解與整合訊息能力不足，影響動力學真實度。合成系統僅涵蓋三政治議題，未驗證其他領域；代理人無人口統計、記憶等背景，與真人社會差距大。干預實驗規模與策略有限，未量化長期效果。提示詞設計作為軟參數，敏感度與可重現性待進一步探討。倫理風險（如極化內容生成）需謹慎評估。依目前可取得資料，無法確認更大規模、多模態或真人混合環境下的表現。
