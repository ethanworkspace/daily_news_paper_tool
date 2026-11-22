# GitHub 專案 01：RUCAIBox/AutoMaster

- 日期：2026-11-19
- URL：https://github.com/RUCAIBox/AutoMaster
- 描述：
- Stars：26  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-22T12:31:46+00:00
- 配對論文：http://arxiv.org/abs/2611.26510v1
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
AutoMaster 是一種自主後訓練框架，讓同一個模型同時扮演 Teacher 與 Student 的角色。透過設計與選擇技能（Skill）來塑造 Teacher 的示範軌跡，再以這些示範資料微調 Student，目標是提升模型在終端任務、網頁搜尋與文件到倉庫三個領域的表現，適用於希望無需更強師模型即可自行改進教學行為的研究者與工程師。

## 技術
該專案主要使用 Python 3.11+，依賴 AweAgent 進行智能體操作，以 Qwen3.5 為基礎語言模型，並透過 SGLang 實現 Tensor Parallel 推論服務。核心技能設計採用 Skill‑FT 方法：先由 Teacher 在特定技能指引下產生示範軌跡，再以這些軌跡進行監督微調 (SFT) 來訓練 Student。此外提供 recipes/inference 內含評估腳本與基準配置（Terminal‑Bench 2.1、BrowseComp、Doc2Repo），支援多輪 rollout 與結果統計。

## 架構
AutoMaster 的運作分為內層迴圈與外層迴圈。內層迴圈負責分析 Teacher 的執行軌跡、設計與測試技能（Skill），然後選擇最具教學價值的示範資料作為訓練樣本；外層迴圈則以這些示範資料對 Student 進行監督微調，評估其在基準上的分數與執行痕跡，並將評估結果回饋給內層迴圈以改進後續的技能設計與資料選擒。主要模組包括：Teacher（固定模型）、Skill 生成器與選擇器、Student（待訓練模型）、評估器與資料流管線。README 未提供詳細的類別圖或訊息傳遞圖，因此架構描述僅基於所述迴圈與模組功能的推斷。

## README 摘錄（節選）
```text
## Autonomous Post-Training by Making the Same Model a Better Teacher
* Beyond task success: **autonomously shaping teacher behavior to improve what students learn**.*
Video (#how-automaster-works) · Inside AutoMaster (#inside-automaster) · Results (#results-across-three-domains) · Insights (#key-insights) · Skills (skills/README.md) · Quick start (#quick-start) · Models & data (https://huggingface.co/collections/RUC-AIBOX/automaster) · Citation (#citation)
(https://arxiv.org/pdf/2611.26510)
(https://aweai-team.github.io/AutoMaster/)
(https://huggingface.co/collections/RUC-AIBOX/automaster)
(skills/README.md)
(LICENSE)
* If you find AutoMaster useful, give us a star ⭐ to support the project.*
** AutoMaster** autonomously studies trajectories, designs skills, and selects demonstrations to make the same model a better teacher. **Skill-FT** guides Teacher rollouts with these skills and fine-tunes the Student on the resulting demonstrations. The Student is evaluated without generated skills.
This release includes nine selected skills (skills/README.md) and inference recipes (recipes/inference/README.md) for three domains, powered by AweAgent (https://github.com/AweAI-Team/AweAgent).
## How AutoMaster works
▶ Watch the overview
## Inside AutoMaster
** Inner loop · Shape the demonstrations.** Analyze behaviors, design and test skills, and select training examples. Skills can apply to overlapping task subsets, with different combinations for different tasks.
** Outer loop · Learn from the Student.** Train and evaluate the Student, then use its scores and execution traces to refine the next round of skill design and data selection.
Explore the method and behavioral examples → (docs/method.md)
## Results across three domains
## Key insights
- **Task success alone does not tell us what a demonstration teaches.** Even successful trajectories can contain unsupported assumptions, unproductive exploration, or superficial verification. Training on them can reinforce these habits alongside useful behaviors.
- **Better teaching without a stronger teacher.** Shaping how a fixed Teacher executes tasks can improve its demonstrations. AutoMaster improves mean Student performance by **1.42–8.99 percentage points** over Vanilla SFT, with the Teacher, task pool, training set size, and SFT recipe held fixed.
- **Generation and selection are complementary.** Skills shape the behaviors demonstrated; selection identifies valuable training examples. Removing either component lowers mean performance in all six evaluated settings, supporting their joint optimization.
- **Skill context helps behavioral internalization.** Keeping skill instructions during SFT improves mean performance by **2.15–4.01 percentage points** over removing them, with identical trajectories and supervised outputs—and no generated skills at evaluation. Explicit behavioral rules and their conditions of application offer a possible explanation.
- **Autonomous post-training benefits from exploration.** Rollout evidence and Student evaluation guide further skill design and data selection. Continued experimentation can uncover better candidates after limited progress; individual rounds need not improve monotonically.
## Skills in practice
Each skill is a self-contained folder with a `SKILL.md` entrypoint.
| Terminal tasks | Web search | Repository construction |
|---|---|---|
| Test a numerical claim (skills/tb2.1/execute-numeric-decision/SKILL.md) | Break out of a stalled search (skills/bc/recover-search-anchor/SKILL.md) | Exercise the public API (skills/doc2repo/run-observed-public-call/SKILL.md) |
| Compare against an independent reference and test the required bound. | Drop unsupported assumptions and follow a new identifying clue. | Call the real entry point and observe its external effects. |
Explore all nine skills and teacher instructions (skills/README.md#what-the-teacher-reads) · See how skills change a rollout (docs/method.md#behavioral-shaping-in-practice)
## Quick start
### 1.
```
