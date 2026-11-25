# GitHub 專案 01：csml-rpi/Foam-Agent

- 日期：2026-11-19
- URL：https://github.com/csml-rpi/Foam-Agent
- 描述：Foam-Agent: A large language model-based multi-agent framework for automating computational fluid dynamics workflows. Published in Computer Methods in Applied Mechanics and Engineering (CMAME).
- Stars：372  |  Forks：80  |  Language：Python
- License：MIT
- Topics：agent, cfd, computational-fluid-dynamics, foam-agent, multi-agent-systems, openfoam, physics, simulation
- 更新時間：2026-11-19T08:45:56+00:00
- 配對論文：https://arxiv.org/abs/2509.20374
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Foam-Agent 是一個基於大型語言模型的多智慧體框架，旨在自動化 OpenFOAM 計算流體動力學（CFD）工作流程。使用者僅需提供自然語言需求或現有案例，系統即可由規劃智慧體生成案例描述、網格與輸入檔案，經過靜態審查後在本機或 Slurm 叢集執行模擬，遇到錯誤時自動嘗試修復，並可選擇性地產出可視化結果與工作流程報告。目標使用者為需要快速原型或重複執行 CFD 模擬的研究者、工程師與教學人員，核心問題在於減少手動案例準備、參數調試與錯誤追蹤的重複勞動。

## 技術
技術上，Foam-Agent 以 Python 為主要實作語言，透過模組化的 LLM 客戶端支援多種後端，包括 OpenAI、Codex 訂閱、Anthropic、Bedrock、Ollama 與 DeepSeek。檢索增強生成（RAG）採用 FAISS 索引，對應選定的 OpenFOAM 教程庫（Foundation v10 或 ESI/OpenCFD v2006），嵌入模型預設為 Hugging Face 的 Qwen/Qwen3-Embedding-0.6B，亦可指定本地複製。工作流程由規劃、網格生成、輸入檔案撰寫、靜態審查、執行與錯誤修復等服務組成，透過環境變數（FOAMAGENT_MODEL_PROVIDER、FOAMAGENT_EMBEDDING_PROVIDER 等）切換後端與目標。Docker 镜像內建 Foundation OpenFOAM v10、Python 依賴、教程索引與預設嵌入權重，免除主機 Conda、OpenFOAM 或 GPU 需求。此外，透過 Model Context Protocol（MCP）提供給 Claude Code、Cursor 等客戶端的工具，使得語言模型能直接呼叫 Foam-Agent 的案例產生與執行功能。

## 架構
架構方面，專案採用模組化目錄結構：src/ 包含工作流程協調器、各類服務（案例規劃、網格準備、輸入檔案生成、靜態與運行審查、錯誤修復）、LLM 客戶端封裝以及 MCP 伺服器實作；database/ 儲存針對不同 OpenFOAM 目標的教程語料庫、對應的 FAISS 索引及其建構腳本；examples/ 提供範例需求檔案與網格，用於快速驗證；docs/ 存放使用手冊、MCP 指南與圖解；scripts/ 包含語料檢查與翻譯驗證工具；tests/ 放置自動化回歸測試；docker/ 則提供基礎映像與入腳本，支援本機 Docker 或自行建置的 ESI/OpenCFD v2006 目標。執行流程從使用者輸入（自然語言或現有案例）開始，經過規劃智慧體產出案例描述，接著網格與輸入檔案智慧體並行（依據執行模式）產生相應檔案，隨後靜態審查智慧體以 LLM 檢查並提出必要修正，經過修正後送至執行智慧體在本機或 Slurm 執行 OpenFOAM solver，運行失敗時觸發錯誤修復智慧體基於日誌嘗試修正，重複直至達到最大重試次數或成功，最後可選擇地產出可視化與工作流程報告（HTML）。整個過程受環境變數與設定檔（src/config.py）控制，支援 careful（預設，sequential 依賴順序＋靜態審查）與 fast（平行生成）兩種執行模式。

## README 摘錄（節選）
```text
# Foam-Agent
Foam-Agent automates OpenFOAM simulations from a natural language prompt or an existing case. Its agents plan the case, prepare meshes and input files, review them before execution, run locally or through Slurm, repair errors, and optionally visualize results.
- **OpenFOAM targets:** Foundation v10 by default, with a separate native ESI/OpenCFD v2006 target.
- **Tutorial retrieval:** FAISS indices provide references from the selected target's tutorials.
- **Model choice:** OpenAI, Codex subscription, Anthropic, Bedrock, Ollama, and DeepSeek backends.
- **MCP integration:** Tools for Claude Code, Cursor, and other MCP clients.
## Quick Start (Recommended: Docker)
Docker bundles Foundation OpenFOAM v10, Python dependencies, tutorial indices,
and the default Qwen 0.6B embedding weights. No host Conda, OpenFOAM, or GPU is
needed. Configure an API-key provider or a Codex subscription using the
authentication guide (docs/usage.md#authentication). For Ollama, follow the
local setup (docs/usage.md#ollama): it requires optional Python packages and
a running Ollama service, which the default images do not include.
| Your environment | Installation |
|---|---|
| A host with Docker | Use the Docker steps below |
| An existing container or OpenFOAM installation | Local Python installation (docs/usage.md#local-installation) |
| Native ESI/OpenCFD v2006 | Build its matching image (docs/usage.md#docker-builds) |
Build the current source on Linux amd64 (or an amd64 Docker VM):
[code block omitted]
Edit `.env` with your provider, model and API key. Then check the installation
and run the bundled example, keeping results on the host:
[code block omitted]
The diagnostic checks LLM access with a small request; the example uses the existing
`user_requirement.txt`. Files and logs are saved to `output/quickstart/`.
Use a fresh output directory for another run. See authentication (docs/usage.md#authentication)
for a Codex subscription or another provider.
Open `.foamagent/workflow_report.html` in the generated case directory to explore
the execution steps, decisions and repairs. See workflow reports (docs/usage.md#workflow-report).
Locally built images run their bundled code and assets without startup updates.
See Docker builds (docs/usage.md#docker-builds) for native targets and older image
compatibility.
To use your own prompt, mount its directory read-only and pass the container path:
[code block omitted]
An existing directory or ZIP (docs/usage.md#existing-cases) is also supported with
`--case_path`. Foam-Agent keeps an `original/` copy and runs in `work/`.
## Configuration
| Environment variable | Purpose | Default |
|---|---|---|
| `FOAMAGENT_MODEL_PROVIDER` | LLM backend | `openai-codex` |
| `FOAMAGENT_MODEL_VERSION` | Model identifier for that backend | `gpt-5.3-codex` |
| `FOAMAGENT_EMBEDDING_PROVIDER` | Tutorial embedding backend | `huggingface` |
| `FOAMAGENT_EMBEDDING_MODEL` | Model identity matching the FAISS indices | `Qwen/Qwen3-Embedding-0.6B` |
| `FOAMAGENT_EMBEDDING_MODEL_PATH` | Optional local copy of that Hugging Face model | Unset |
| `FOAMAGENT_OPENFOAM_TARGET` | Native target: `foundation-v10` or `esi-v2006` | Unset; Foundation v10 |
The default LLM uses a Codex OAuth cache. An API key requires selecting its provider and model explicitly, as in Quick Start. Docker builds bundle the default embedding weights. Local Python installations may download them on first use; prebuilt tutorial indices come through Git LFS and must match the embedding model. See installation checks and offline setup (docs/usage.md#installation-checks-and-offline-use).
Choose an execution mode with `--execution_mode` (or `Config.execution_mode`):
| Mode | File generation | Before each stage's first execution |
|---|---|---|
| `careful` (default) | Sequential in planned dependency order | Mesh/solver LLM static review |
| `fast` | Independent parallel generation | Run directly |
Both modes repair runtime errors. Static review requests only defin
```
