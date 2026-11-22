# GitHub 專案 02：RUCAIBox/AutoMaster

- 日期：2026-11-20
- URL：https://github.com/RUCAIBox/AutoMaster
- 描述：
- Stars：25  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-22T11:19:18+00:00
- 配對論文：http://arxiv.org/abs/2611.26510v1
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
AutoMaster 是一種自主後訓練框架，透過讓同一個模型同時擔任教師與學生，自行設計技能（Skill）並篩選示範軌跡，以提升教師的示範品質，進而強化學生的表現。其目標使用者為研究 LLM 教學與微調的學者與工作者，核心問題在於僅看任務成功率無法判斷示範是否真的傳遞有用行為，AutoMaster 透過行為塑造與示範選擇解決此問題。

## 技術
專案主要使用 Python 3.11+，依賴 AweAgent 實現代理行為，基礎模型採用 Qwen3.5，透過 SGLang 服務檢查點（支援張量平行）。核心技能（Skill）以獨立資料夾組織，每個含 SKILL.md 入口，並搭配 Skill‑FT 進行教師導向的推演與學生微調。內部流程包含內部迴圈（行為分析、技能設計與示範選擇）與外部迴圈（學生訓練、評估與回饋），所有程式碼採用 MIT 授權，AweAgent 為 Apache-2.0。

## 架構
AutoMaster 的架構分為兩個主要迴圈：內部迴圈負責分析教師軌跡、設計並測試技能、選擇有價值的示範；外部迴圈則以這些示範微調學生模型，評估學生表現後將其分數與執行痕跡回饋給內部迴圈以改進後續技能設計與資料選擇。具體流程為：教師模型產生軌跡 → 行為分析模塊產生技能候選 → 技能測試與示範選擇 → 以技能引導教師產生新示範 → 使用 Skill‑FT 對學生進行監督微調 → 在基準（Terminal‑Bench 2.1、BrowseComp、Doc2Repo）上評估學生 → 依評估結果更新技能與示範選擇策略，週期性重複。此設計依賴 AweAgent 實現代理的探索與決策，若 README 未明確說明某些細節，則僅根據上述描述進行推斷。

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
