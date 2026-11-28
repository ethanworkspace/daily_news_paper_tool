# GitHub 專案 03：evelyyyyynnnnn/1.0-Secure-Ai-Agent-Infrastructure

- 日期：2026-11-09
- URL：https://github.com/evelyyyyynnnnn/1.0-Secure-Ai-Agent-Infrastructure
- 描述：Research prototypes and infrastructure tools for building secure AI agent systems using large language models, blockchain technologies, and distributed architectures.
- Stars：191  |  Forks：31  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-09T23:54:34+00:00
- 論文層級：未對應論文
- 配對論文：https://doi.org/10.5281/zenodo.24094759
- 品質分數：8/10 [paper_paired]

## 在做什麼
此專案提供可重現的研究原型與基礎設施工具，探索利用大型語言模型、區塊鏈技術與分散式架構構建安全的 AI 代理系統。目標使用者為研究 AI 安全與可驗證性的學者、開發者以及政策制定者。核心問題在於評估自主代理是否能被信任執行安全決策，以及在其無法勝出時能否被偵測。透過三個子專案分別測驗代理驗證、智能合約檢測基準與 LLM 審計代理，每個皆在第三方公開資料上進行實證，並報告成功與失敗的具體情況。

## 技術
專案主要以 Python 實作，使用本地運行的開放語言模型（如 qwen2.5-coder:7b）進行推論。涉及區塊鏈相關技術，包括智能合約原始碼與基於規則的漏洞檢測器（heuristic detectors），以及以 SHA-256 生成的哈希鏈審計軌跡，確保每個推論階段的提示與回覆不可竄改。資料流程採用第三方公開資料（美國政府統計發布、SmartBugs 合約庫、OpenZeppelin Contracts），所有原始資料僅透過 MANIFEST.json 記錄 URL、SHA-256 與擷取時間，不 commit 到倉庫。測試框架包含單元與整合測試，CI 工作流程自動執行。

## 架構
倉庫採用統一的專案骨架，每個子專案（1-agent-verification-harness、2-chaintrust-bench、3-llm-audit-agent）皆包含 README、src、data、results、tests、website 目錄。data 目錄僅存放 MANIFEST.json，實際資料於執行時從第三方來源重新下載，確保可重現性。src 內含各專案的核心邏輯：代理驗證 harness 實施基於來源的事實 grounding 檢查；ChainTrust-Bench 實施漏洞類別別計分與宏平均；LLM Audit Agent 則分為理解、規劃、分類、驗證四個階段，每階段產生 SHA-256 鏈結的審計軌跡，驗證階段重新讀取來源以捨去無法證實的發現。results 目錄保存運行日誌與數據指標，tests 目錄存放對應的測試腳本。由於 README 未詳細描述跨專案的共享元件或中央協調器，架構說明僅基於各子專案的獨立結構與共用骨架推斷。

## README 摘錄（節選）
```text
# 1.0 — Secure AI Agent Infrastructure
(https://github.com/evelyyyyynnnnn/1.0-Secure-Ai-Agent-Infrastructure/actions/workflows/tests.yml)
(https://doi.org/10.5281/zenodo.24094759)
Reproducible research prototypes for one question: **can an autonomous agent be
trusted with a security decision, and would you know if it could not?**
Three projects, each taking one part of that question, each measured on data
published by a third party, and each reporting what did not work next to what
did. Part of a five-repository portfolio on verifiable AI for high-stakes
decisions, alongside healthcare safety (`2.0`), financial stability (`3.0`),
decision auditing (`4.0`) and shared tooling (`5.0`).
| | |
|---|---|
| Projects with measured results | **3** |
| Tests across the three suites | **88** |
| Running on real third-party data | **3 of 3** |
| Most recent reportable run | 2026-09-07 |
## Projects
| Folder | Project | What it measures | Tests |
|---|---|---|---|
| `1-agent-verification-harness/` (1-agent-verification-harness/) | Agent Verification Harness | Whether a grounding check catches an agent's bad claims without flagging its good ones | 32 |
| `2-chaintrust-bench/` (2-chaintrust-bench/) | ChainTrust-Bench | How well smart-contract detectors score *per vulnerability class*, and how often they misfire on audited code | 38 |
| `3-llm-audit-agent/` (3-llm-audit-agent/) | LLM Audit Agent | Whether an auditing agent that re-checks itself actually drops what it cannot verify | 18 |
## What each one found
### 1. Agent Verification Harness — `1-agent-verification-harness/` (1-agent-verification-harness/)
Three real US government statistical releases (BLS CPI, BLS Employment
Situation, Federal Reserve H.15) are turned into twelve claims whose truth is
known *by construction*: supported claims are quoted verbatim, fabricated ones
are the same sentence with a single number altered, and unsupported ones are
real sentences lifted from a different release and cited to this one.
** Precision 1.000, recall 0.667, F1 0.800** at the committed threshold of 0.55,
with zero good claims falsely flagged. The split is the finding: a claim citing
the wrong source is caught every time (3 of 3), a claim where one digit was
changed is caught once in three. The threshold is not what decides it: all
three altered-digit claims scored 0.78-0.83, above every threshold swept.
### 2. ChainTrust-Bench — `2-chaintrust-bench/` (2-chaintrust-bench/)
A benchmark that scores detectors per vulnerability class and then
macro-averages, so a detector that only finds the common bug cannot hide behind
a high overall accuracy. 121 vulnerable contracts from the SmartBugs curated
corpus across seven classes, plus 20 negative controls from OpenZeppelin
Contracts `v5.0.2`.
** Both heuristic detectors raise false alarms on 9 of 20 pieces of audited
OpenZeppelin library code** — a false-positive rate of 0.450. The rule baseline
reports `integer_overflow` on `Math.sol` under Solidity ^0.8, where the compiler
reverts on overflow by default, and `missing_access_control` on contracts that
inherit the reference `Ownable` implementation. Per class, the baseline finds
unchecked calls reasonably well (F1 0.60) and reentrancy not at all (0 of 31).
That headroom is the reason the benchmark exists.
### 3. LLM Audit Agent — `3-llm-audit-agent/` (3-llm-audit-agent/)
A four-stage auditing agent — understand, plan, classify, verify. Every stage is
written to a hash-chained trail (SHA-256 of the exact prompt and reply, linked
to the previous stage), so editing any stage after the fact is detectable. The
verify stage re-reads each finding against the source and discards what it
cannot confirm.
** Indirect prompt injection (`qwen2.5-coder:7b`, 20 SmartBugs
contracts).** A comment planted in the contract telling "automated audit tools"
to report nothing suppressed **14 of 14** detections the agent otherwise makes;
every contract came back clean. Stripping comments before the model reads the
```
