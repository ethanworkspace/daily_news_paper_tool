# GitHub 專案 01：csml-rpi/Foam-Agent

- 日期：2026-11-21
- URL：https://github.com/csml-rpi/Foam-Agent
- 描述：Foam-Agent: A large language model-based multi-agent framework for automating computational fluid dynamics workflows. Published in Computer Methods in Applied Mechanics and Engineering (CMAME).
- Stars：372  |  Forks：81  |  Language：Python
- License：MIT
- Topics：agent, cfd, computational-fluid-dynamics, foam-agent, multi-agent-systems, openfoam, physics, simulation
- 更新時間：2026-11-19T08:45:56+00:00
- 配對論文：https://arxiv.org/abs/2509.20374
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Foam-Agent 是一個基於大型語言模型的多智能體框架，旨在自動化 OpenFOAM 計算流體動力學（CFD）工作流程。使用者只需提供自然語言需求或現有案例，系統的規劃、網格、輸入檔案、審查、執行、錯誤修復與可視化等智能體會依序協作，完成從案例概念到模擬結果的全程自動化。目標使用者為 CFD 工程師、研究人員及學生，他們希望減少手動設定網格與邊界條件的重複勞動，提高案例可重現性與實驗效率。核心問題在於傳統 OpenFOAM 工作流程需要專家逐步編寫網格與求解器設定檔，耗時且易出錯；Foam-Agent 透過 LLM 驅動的規劃與靜態審查，將這些步驟自動化，同時支援本地或 Slurm 叢集執行，並提供錯誤修復機制與工作流程報告。

## 技術
Foam-Agent 以 Python 實作，支援多種 LLM 後端，包括 OpenAI、Codex 訂閱、Anthropic、Bedrock、Ollama 與 DeepSeek，透過環境變數選擇模型與提供者。檢索教程採用 FAISS 索引，嵌入模型預設為 Hugging Face 的 Qwen/Qwen3-Embedding-0.6B，可選擇本地快取。框架隨 Docker 镜像捆綁 Foundation OpenFOAM v10（預設）與可選的 ESI/OpenCFD v2006 原生目標，提供 MCP 整合以供 Claude Code、Cursor 等客戶端呼叫工具。核心服務分別位於 src/ 中的工作流程、模型客戶端與 MCP 伺服器，教程語料與索引存放於 database/，範例案例放於 examples/，設定透過 src/config.py 與環境變數調整，支援 careful（靜態審查）與 fast（平行生成）兩種執行模式，並內建運行時錯誤迴圈與可選的結果視覺化步驟。

## 架構
Foam-Agent 的架構由多個專責智能體組成：規劃智能體根據自然語言或現有案例產生案例大綱；網格智能體呼叫 OpenFOAM 網格工具（如 snappyHexMesh）生成或修改 mesh 檔案；輸入檔案智能體產生 boundary、controlDict、transportProperties 等求解器所需設定；靜態審查智能體利用 LLM 對上述檔案進行必要的修正建議，最多執行十次重試；執行智能體在本機或透過 Slurm 叢集啟動 OpenFOAM 求解器；運行時檢測智能體捕捉求解器錯誤並觸發修復智能體進行迴圈修正，最多設定的運行時迴圈次數；可視化智能體於成功執行後產生後處理圖表或工作流程報告 HTML。資料流為：使用者提示 → 規劃 → 網格 → 輸入檔案 → 靜態審查 → 執行 → （若失敗）運行時檢測 → 修復 → 重複執行 → 成功後可視化與報告。在 careful 模式下，各階段依序依賴生成並進行靜態審查；fast 模式則允許平行產生檔案，但仍保留運行時錯誤修復。所有設定與重試上限均可透過環境變數或 src/config.py 調整。README 未提供詳細的類別圖或序列圖，因此上述流程說明基於文件中描述的智能體職責與執行模式推斷。

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
