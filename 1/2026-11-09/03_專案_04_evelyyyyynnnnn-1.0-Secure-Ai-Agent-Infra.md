# GitHub 專案 04：evelyyyyynnnnn/1.0-Secure-Ai-Agent-Infrastructure

- 日期：2026-11-09
- URL：https://github.com/evelyyyyynnnnn/1.0-Secure-Ai-Agent-Infrastructure
- 描述：Research prototypes and infrastructure tools for building secure AI agent systems using large language models, blockchain technologies, and distributed architectures.
- Stars：191  |  Forks：31  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-09T23:54:34+00:00
- 配對論文：https://doi.org/10.5281/zenodo.24094759
- 品質分數：8/10 [paper_paired]

## 在做什麼
此專案提供三個可重現的研究原型，用以評估自主 AI 代理在安全決策上的可信度：Agent Verification Harness 檢查代理的事實依據是否正確；ChainTrust-Bench 評估智能合約漏洞偵測工具在不同漏洞類別上的表現；LLM Audit Agent 則實作一個四階段自我審核代理，能驗證自身發現並捨棄無法證實的項目。目標使用者為研究安全與可信 AI 系統的學者、開發者與審計人員。

## 技術
技術棧主要使用 Python 實作，涵蓋大型語言模型（如本地運行的 qwen2.5-coder:7b）、智能合約靜態分析與啟發式偵測器、基於區塊鏈的雜湊鏈式審計日誌，以及分散式資料流程。專案透過 GitHub Actions 執行測試，使用 MANIFEST.json 記錄第三方資料的 URL、SHA-256 與擷取時間，確保可重現性。每個子專案皆包含 src/（核心程式）、data/（僅存放 MANIFEST）、results/（實驗結果）與 tests/（單元與整合測試）。

## 架構
架構上，倉庫分為三個獨立但結構相同的子專案：1-agent-verification-harness、2-chaintrust-bench 與 3-llm-audit-agent。每個子專案遵循 README.md、src/、data/、results/、tests/ 與 website/ 的目錄結構。資料流程方面，Agent Verification Harness 從政府統計資料產生已知真偽的主張，經由 grounding 檢查器產出 precision/recall 指標；ChainTrust-Bench 從 SmartBugs 與 OpenZeppelin 合約集合呼叫各種漏洞偵測器，依漏洞類別計算 F1 並宏平均；LLM Audit Agent 採取「理解‑規劃‑分類‑驗證」四階段流程，每階段產出的回覆寫入以 SHA-256 串連的雜湊鏈，驗證階段重新讀取原始合約以過濾無法證實的發現，最終結果寫入 results/。所有實驗皆透過測試腳本執行，並將運行日期寫入結果檔案以符合「無數字不帶運行日誌」的規則。

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
A four-stage auditing agent — understand, plan, classify, verify — where every
stage's reply is written into a hash-chained trail with its backend, latency and
reply size. The verify stage re-reads each finding against the source and
discards what it cannot confirm.
On a real open language model (`qwen2.5-coder:7b`, served locally) the full four
stages ran end to end over one contract in **68.3 s**, confirming two real
issues and **dropping two findings it could not substantiate** — both of which
reasoned about what the contract might do if someone later changed it. On the
121-contract corpus with a deterministic backend the agent tra
```
