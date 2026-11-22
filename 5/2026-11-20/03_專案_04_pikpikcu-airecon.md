# GitHub 專案 04：pikpikcu/airecon

- 日期：2026-11-20
- URL：https://github.com/pikpikcu/airecon
- 描述：AIRecon is an autonomous cybersecurity agent that combines a self-hosted Large Language Model (Ollama) with a Kali Linux Docker sandbox and a Textual TUI. It is designed to automate security assessments, penetration testing, and bug bounty reconnaissance — without any API keys or cloud dependency.
- Stars：1098  |  Forks：176  |  Language：Python
- License：MIT
- Topics：ai-agents, automation, bugbounty, cli, ollama, penetration-testing, python, reconnaissance
- 更新時間：2026-11-21T09:36:34+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
AIRecon is an autonomous cybersecurity agent that combines a self-hosted Large Language Model (Ollama) with a Kali Linux Docker sandbox and a Textual TUI. It is designed to automate security assessments, penetration testing, and bug bounty reconnaissance — without any API keys or cloud dependency.
AIRecon is an autonomous cybersecurity agent that combines a self-hosted Large Language Model (Ollama) with a Kali Linux Docker sandbox and a Textual TUI. It is designed to automate security assessments, penetration testing, and bug bounty reconnaissance — without any API keys or cloud dependency.

主要語言：Python；Topics：ai-agents, automation, bugbounty, cli, ollama, penetration-testing, python, reconnaissance；Stars：1098；License：MIT

## 技術
實作語言以 Python 為主。
從 topics 可見技術方向：ai-agents, automation, bugbounty, cli, ollama, penetration-testing, python, reconnaissance。
專案描述：AIRecon is an autonomous cybersecurity agent that combines a self-hosted Large Language Model (Ollama) with a Kali Linux Docker sandbox and a Textual TUI. It is designed to automate security assessments, penetration testing, and bug bounty reconnaissance — without any API keys or cloud dependency.

## 架構
README 未明確提供架構章節；依描述推斷此專案聚焦於：AIRecon is an autonomous cybersecurity agent that combines a self-hosted Large Language Model (Ollama) with a Kali Linux Docker sandbox and a Textual TUI. It is designed to automate security assessments, penetration testing, and bug bounty reconnaissance — without any API keys or cloud dependency.

## README 摘錄（節選）
```text
AI-Powered Autonomous Penetration Testing Agent
AIRecon is an autonomous penetration testing agent that drives any **OpenAI-compatible LLM gateway** (LiteLLM / vLLM / a hosted endpoint — or a local gateway proxying a local Ollama) with a **Kali Linux Docker sandbox**, native **Caido proxy integration**, a structured **RECON → ANALYSIS → EXPLOIT → REPORT pipeline**, and a real-time **Textual TUI**.
> **Backend-agnostic by design.** Point AIRecon at a **local** gateway (LiteLLM / vLLM, or a gateway proxying a local Ollama) for **fully offline / private** operation, or at a **hosted** OpenAI/Anthropic/Gemini-compatible endpoint for maximum reasoning quality. Reasoning support is **auto-detected at runtime** — no per-model hardcoding.
--- 
## Sponsor
### Swiftproxy – Reliable Residential Proxies for AI-Powered Web Research
Swiftproxy (https://www.swiftproxy.net/?ref=pikpikcu) provides **90M+ clean residential IPs across 220+ locations**, supporting HTTP(S)/SOCKS5, IP rotation, Sticky Sessions, and precise geo-targeting. It helps AI-powered research and reconnaissance workflows access websites reliably from different locations, making it suitable for web research, data collection, scraping, and location-based access.
** Free testing is available, with 10% off using code `PROXY90`.**
--- 
## Why AIRecon?
AIRecon talks to **one OpenAI-compatible gateway**, so you choose the trade-off — run a **local** model for privacy and zero API cost, or a **hosted** model for top reasoning quality. The same agent, pipeline, sandbox, and tooling work either way.
| Feature | AIRecon |
|---------|---------|
| Backend | Any OpenAI-compatible gateway (LiteLLM / vLLM / hosted) |
| Fully offline / no API keys | **Yes** — when using a local gateway (vLLM, or a gateway → local Ollama) |
| Reasoning detection | **Automatic** at runtime (no model-name hardcoding) |
| Caido integration | **Native** |
| Scope guard + audit log | **Yes** — refuse out-of-scope targets, log every command |
| Verified-only learning | **Yes** — the brain compounds proven findings, not noise |
| Session resume (chat + tool calls) | **Yes** |
| Local knowledge base | **~1.09M records** (optional) |
- **Privacy when you want it** — with a local gateway, target intelligence, tool output, and reports never leave your machine.
- **Caido Native** — built-in tools: list, replay, automate (`§FUZZ§`), findings, scope, sitemap, intercept.
- **Full Stack** — Kali sandbox + browser automation + custom fuzzer + Schemathesis API fuzzing + Semgrep SAST.
- **Skills Knowledge Base** — 57 built-in skill files, 289 keyword → skill auto-mappings. Extended by **airecon-skills (https://github.com/pikpikcu/airecon-skills)** — a community skill library with 57 additional CLI-based playbooks for CTF, bug bounty, and pentesting.
- **Local Security Knowledge Base** — Optional **airecon-dataset (https://github.com/pikpikcu/airecon-dataset)** indexes ~1.09M security records (CVEs, red team techniques, CTF writeups, nuclei templates, bug bounty payloads) into local SQLite FTS5. The LLM calls `dataset_search` autonomously before attempting unfamiliar techniques — grounding its decisions in real indexed data.
--- 
## Pipeline
[code block omitted]
Each phase has specific objectives, recommended tools, and automatic transition criteria. Phase enforcement is **soft** — the agent is guided but never blocked. Checkpoints run every 5 (phase eval), 10 (self-eval), and 15 (context compression) iterations.
--- 
## Memory & Learning (What It Actually Does)
AIRecon does **not** fine-tune the LLM. Its "learning" is local, structured telemetry that guides tool choice and avoids repeating failed paths.
** Local persistence (all on disk, no cloud):**
- SQLite memory DB at `~/.airecon/memory/airecon.db` storing sessions, findings, patterns, target intel, tool usage, model performance, skill usage, and attack-chain discoveries.
- Adaptive learning state at `~/.airecon/learning/global_learning.json` (tool performance stats, strate
```
