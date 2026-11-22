# GitHub 專案 01：RUCAIBox/AutoMaster

- 日期：2026-11-17
- URL：https://github.com/RUCAIBox/AutoMaster
- 描述：
- Stars：26  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-22T12:31:46+00:00
- 配對論文：http://arxiv.org/abs/2611.26510v1
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
AutoMaster 是一種自主後訓練框架，透過讓同一個模型同時扮演教師與學生的角色，自行分析教師的執行軌跡、設計行為技能（Skill）並挑選具有教學價值的示範，再以這些示範對學生進行監督微調，使學生在不依賴產生的技能情況下獲得更佳的任務表現。目標使用者為研究大型語言模型後訓練、強化學習與教師－學生範式的學者與工程師，核心問題在於僅看任務成功率無法保證示範的教學品質，AutoMaster 透過塑造教師行為來改進示範內容，從而提升學生的實際能力。

## 技術
AutoMaster 以 Python 3.11+ 為主要實作語言，整合 AweAgent 框架負責代理與環境互動，使用 Qwen3.5 作為基礎語言模型，並透過 SGLang（支援 Tensor Parallelism）提供模型推論服務。技能以獨立的 SKILL.md 檔案描述，內部迴圈負責行為分析、技能設計與示範選取；外迴圈則以 Skill‑FT 進行監督微調，並在 Terminal‑Bench 2.1、BrowseComp、Doc2Repo 三個基準上評估學生表現。專案透過 Git submodule 管理第三方程式碼，採用 MIT 授權。

## 架構
AutoMaster 的架構分為內迴圈與外迴圈兩層。內迴圈負責分析教師的執行軌跡、根據觀察結果設計與測試技能（Skill），並從技能引導的教師 rollout 中挑選具教學價值的示範資料。外迴圈則將這些示範送入 Skill‑FT 進行監督微調，得到更新的學生模型，並在基準測試上評估其表現；評估分數與執行追蹤作為回饋，供內迴圈在下一輪中調整技能設計與資料選取。資料流程為：軌跡 → 行為分析 → 技能生成 → 技能導向教師 rollout → 示範選取 → Skill‑FT 微調 → 學生評估 → 回饋 → 新一輪技能設計。模組包括 Teacher 模型、Skill 設計與選取模組、Skill‑FT 訓練模組、Student 模型以及評估基準。若僅憑 README，外迴圈的具體訓練超參數與資料流細節未完整揭露，屬於推斷範圍。

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
