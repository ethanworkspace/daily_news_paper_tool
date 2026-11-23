# GitHub 專案 03：csml-rpi/Foam-Agent

- 日期：2026-09-13
- URL：https://github.com/csml-rpi/Foam-Agent
- 描述：Foam-Agent: A large language model-based multi-agent framework for automating computational fluid dynamics workflows. Published in Computer Methods in Applied Mechanics and Engineering (CMAME).
- Stars：372  |  Forks：80  |  Language：Python
- License：MIT
- Topics：agent, cfd, computational-fluid-dynamics, foam-agent, multi-agent-systems, openfoam, physics, simulation
- 更新時間：2026-11-19T08:45:56+00:00
- 配對論文：https://arxiv.org/abs/2509.20374
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Foam-Agent 是一個基於大型語言模型的多智慧體框架，能夠從自然語言描述或現有 OpenFOAM 案例自動完成計算流體力學工作流。其目標使用者為需要快速產生、驗證與執行 CFD 模擬的工程師、研究人員與學生，核心在於解決傳統手動建立網格、輸入檔案、執行與除錯的繁瑣且易出錯問題。透過規劃、網格與輸入檔案生成、靜態審查、本地或 Slurm 執行、錯誤修復以及可選視覺化的代理協同，Foam-Agent 實現端到端的自動化模擬流程。

## 技術
專案主要使用 Python 開發，支援 OpenFOAM Foundation v10 與 ESI/OpenCFD v2006 兩種目標。透過 FAISS 索引檢索目標特定的教程庫，實現檢索增強生成。語言模型後端可選 OpenAI、Codex、Anthropic、Bedrock、Ollama 與 DeepSeek，嵌入模型預設為 Hugging Face 的 Qwen/Qwen3-Embedding-0.6B。提供 MCP 整合，可與 Claude Code、Cursor 等客戶端互通。透過 Docker 镜像封裝 OpenFOAM、Python 依賴、教程索引與預設嵌入權重，免除主機 Conda、OpenFOAM 或 GPU 安裝。執行模式包含 careful（順序生成＋靜態審查）與 fast（並行生成），兩者皆具運行時錯誤修復機制，並支援 Slurm 作業調度。設定透過環境變數或 src/config.py 進行，涵蓋模型供應商、版本、嵌入提供者、重試上限等。

## 架構
專案結構分為數個模組：src/ 包含工作流協調、各代理服務（規劃、網格、輸入檔案、審查、執行、修復、視覺化）、模型客戶端與 MCP 伺服器；database/ 儲存目標特定的教程語料庫、FAISS 索引及其建構腳本；examples/ 提供範例提示與網格檔案；docs/ 存放使用說明與圖示；scripts/ 包含語料檢查與翻譯驗證工具；tests/ 為自動化回歸測試；docker/ 提供運行鏡像與入口腳本。執行流程為：使用者輸入自然語言提示或指定現有案例 → 規劃代理產生案例大綱 → 網格代理生成網格檔案 → 輸入檔案代理產生 OpenFOAM 輸入 → 靜態審查代理進行必要檢查並建議修正 → 執行代理在本機或 Slurm 上執行模擬 → 執行時錯誤偵測代理觸發修復代理進行迭代修正 → 視覺化代理（可選）產生結果圖表 → 工作流報告產生 HTML 檔案供檢閱。所有步驟的資料與日誌均寫入 output/ 目錄下的對應案例資料夾。

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
