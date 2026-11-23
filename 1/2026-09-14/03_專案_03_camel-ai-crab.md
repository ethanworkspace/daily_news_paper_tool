# GitHub 專案 03：camel-ai/crab

- 日期：2026-09-14
- URL：https://github.com/camel-ai/crab
- 描述：🦀️ CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents. https://crab.camel-ai.org/
- Stars：435  |  Forks：65  |  Language：Python
- License：
- Topics：gui-automation, language-model-agent, large-language-models, multi-agent-systems, visual-language-models
- 更新時間：2026-11-18T00:47:10+00:00
- 配對論文：https://arxiv.org/abs/2407.01511
- 品質分數：8/10 [paper_paired, stale_seed]

## 在做什麼
CRAB 是一個以 Python 為核心的框架，用於構建多模語言模型（LLM）代理的跨平台基準環境。它讓研究者能夠在記憶體內、Docker、虛擬機或實體機等多種部署方式下，透過統一的 Python 介面同時操控多個環境，從而評估代理在不同情境下的感知、規劃與執行能力。目標使用者包括從事多模態代理、視覺語言模型以及多代理系統研究的學者與工程師，他們需要一種可重複、可擴展且易於配置的基準來比較不同模型或算法在真實或模擬任務中的表現。

## 技術
CRAB 使用 Python 3.10+ 作為主要語言，核心透過 @action 裝飾器將任意 Python 函式註冊為可供代理呼叫的動作；環境由多個動作組合而成，支援記憶體內、Docker、VM 或分佈式實體機器的執行，只要能透過 Python 函式存取即可。框架提供統一介面讓代理同時存取所有環境，並內建圖形評估器（graph evaluator）以細粒度方式衡量任務完成度。此外，CRAB 可與各種語言模型（如 OpenAI GPT、多模態視覺語言模型）透過 API 結合，進行基準測試。

## 架構
CRAB 的架構分為四層：(1) 動作層，使用 @action 註冊函式並管理參數與回傳值；(2) 環境層，將多個動作組合成可供代理互動的環境實例，支援不同後端（本地、Docker、VM）透過統一的 Python 介面存取；(3) 任務與評估層，使用者以 Python 定義任務目標與對應的評估函式，評估層引入圖形評估器來產生節點與邊的細粒度指標；(4) 執行層，負責載入代理（可為任何 LLM API 包裝），在環境中執行動作序列，收集軌跡並交給評估層計算分數。資料流程為：使用者定義動作 → 建立環境 → 代理透過統一介面發出動作請求 → 環境執行對應後端函式回傳狀態 → 評估器根據軌跡與任務圖計算指標 → 結果輸出供比較與分析。若 README 未明確說明後端實作細節，則上述說明以文件所述的跨平台、統一介面與 @action 裝飾器為推斷依據。

## README 摘錄（節選）
```text
# 🦀 CRAB: Cross-platform Agent Benchmark for Multimodal Embodied Language Model Agents
[![arXiv][arxiv-image]][arxiv-url]
[![Slack][slack-image]][slack-url]
[![Discord][discord-image]][discord-url]
[![Wechat][wechat-image]][wechat-url]
[![Twitter][twitter-image]][twitter-url]
Documentation |
Website & Demos |
Blog |
Chinese Blog |
CAMEL-AI
## Overview
CRAB is a framework for building LLM agent benchmark environments in a Python-centric way.
#### Key Features
🌐 Cross-platform and Multi-environment
* Create build agent environments that support various deployment options including in-memory, Docker-hosted, virtual machines, or distributed physical machines, provided they are accessible via Python functions.
* Let the agent access all the environments in the same time through a unified interface.
⚙ ️Easy-to-use Configuration
* Add a new action by simply adding a `@action` decorator on a Python function.
* Define the environment by integrating several actions together.
📐 Novel Benchmarking Suite
* Define tasks and the corresponding evaluators in an intuitive Python-native way.
* Introduce a novel graph evaluator method providing fine-grained metrics.
## Installation
#### Prerequisites
- Python 3.10 or newer
[code block omitted]
## Experiment on CRAB-Benchmark-v0
All datasets and experiment code are in crab-benchmark-v0 (./crab-benchmark-v0/) directory. Please carefully read the benchmark tutorial (./crab-benchmark-v0/README.md) before using our benchmark.
## Examples
#### Run template environment with openai agent
[code block omitted]
## Demo Video
(https://www.youtube.com/watch?v=PNqrHNQlU6I&ab_channel=CamelAI)
## Cite
Please cite our paper (https://arxiv.org/abs/2407.01511) if you use anything related in your work:
[code block omitted]
## Community
Join us (*Discord* (https://discord.camel-ai.org/) or *WeChat* (https://ghli.org/camel/wechat.png)) in pushing the boundaries of finding the scaling laws of agents.
- **WeChat Community:** Scan the QR code below to join our WeChat community.
[slack-url]: https://join.slack.com/t/camel-kwr1314/shared_invite/zt-1vy8u9lbo-ZQmhIAyWSEfSwLCl2r2eKA
[slack-image]: https://img.shields.io/badge/Slack-CAMEL--AI-blueviolet?logo=slack
[discord-url]: https://discord.gg/CNcNpquyDc
[discord-image]: https://img.shields.io/badge/Discord-CAMEL--AI-7289da?logo=discord&logoColor=white&color=7289da
[wechat-url]: https://ghli.org/camel/wechat.png
[wechat-image]: https://img.shields.io/badge/WeChat-CamelAIOrg-brightgreen?logo=wechat&logoColor=white
[twitter-url]: https://twitter.com/CamelAIOrg
[twitter-image]: https://img.shields.io/twitter/follow/CamelAIOrg?style=social&color=brightgreen&logo=twitter
[arxiv-image]: https://img.shields.io/badge/arXiv-2407.01511-b31b1b.svg
[arxiv-url]: https://arxiv.org/abs/2407.01511
```
