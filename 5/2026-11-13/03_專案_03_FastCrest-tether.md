# GitHub 專案 03：FastCrest/tether

- 日期：2026-11-13
- URL：https://github.com/FastCrest/tether
- 描述：FastCrest Tether: the OSS edge-to-cloud AI deploy CLI. Optimize, verify, deploy across Jetson, RTX, Apple Silicon, AMD. Hybrid edge-cloud inference with parity certs.
- Stars：86  |  Forks：21  |  Language：Python
- License：NOASSERTION
- Topics：cli, deployment, edge-ai, edge-cloud, fastcrest, groot, inference, jetson, onnx, pi0, python, robot-learning, robotics, smolvla, tensorrt, tether, vision-language-action, vla
- 更新時間：2026-11-01T01:06:22+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
FastCrest Tether 是一個開源的邊緣到雲端 AI 部署命令列工具，專注於視覺‑語言‑動作（VLA）機器人策略。它提供部署信心，驗證匯出的 ONNX 模型與原始 PyTorch 政策在機器精度下的逐步相等性，支援 Jetson、RTX、Apple Silicon、AMD 等平台的優化、驗證與混合邊緣‑雲端推理，幫助機器學習與機器人工程師安全地將 VLA 政策從開發環境推向生產。

## 技術
Tether 以 Python 實作，核心功能包括使用 ONNX 匯出單體模型、搭配 ONNX Runtime 的 TensorRT 執行提供者（預設）或 CUDA 後備、可選的 Triton 快速核心（需 fast‑kernels extra）以及 ZMQ 傳輸（serve‑extra）。它支援 safetensors 直接載入、transformers 5.x DynamicCache 相容性、ROS2 機器人適配器起始套件，並透過 install.sh 依據硬體自動選擇對應的 CUDA/JetPack 依賴。CLI 提供 tether serve、tether connect、tether go 等子命令進行模型服務、狀態查詢與端到端驗證。

## 架構
Tether 的架構圍繞 CLI 入口與數個內部模組：exporters 負責將各種 VLA（SmolVLA、pi0、pi0.5、GR00T）的 PyTorch 政策匯出為單體 ONNX（含外部資料檔案）；model 包裝 BaseVLA 脊柱與各組件槽位；serve 模組啟動 ONNX Runtime 會話，依據提供者選項（TensorRT、CUDA、Triton）進行推理，並可透過 ZMQ 或 HTTP 進行低延遲機器人通訊；connect 模組提供狀態查詢與健康檢查；go 模組整合匯出、服務與驗證流程；doctor 與 version 檢查模組處理快取失效與平台相容性。資料流程為：使用者透過 CLI 指令觸發匯出 → 產生 ONNX + 權重資料 → serve 載入模型（外部權重選項、Tokenizer 載入） → 接收圖像/文字輸入 → 經過 ONNX 推理產出動作 → 透過 ZMQ 或 HTTP 回傳給機器人或客戶端。若 README 未明確說明的內部細節（例如具體的錯誤處理或排程），則標示為推斷依據不足。

## README 摘錄（節選）
```text
# Tether
> by FastCrest (https://fastcrest.com) — deployment infrastructure for vision-language-action models.
(https://pypi.org/project/fastcrest-tether/)
(https://pypi.org/project/fastcrest-tether/)
(https://github.com/FastCrest/tether/blob/main/LICENSE)
(https://pypi.org/project/fastcrest-tether/)
** Deployment confidence for VLA robot policies** — Tether answers one production question: can this policy safely move forward?
** Verified parity across ALL four major open VLAs.** Tether's monolithic ONNX export matches the reference PyTorch policy to **cos = +1.000000** end-to-end on SmolVLA, pi0, pi0.5 (canonical 10-step flow-matching unrolled) and GR00T N1.6 (canonical 4-step DDIM loop external to the ONNX). Per-model first-action max_abs: SmolVLA 5.96e-07, pi0 2.09e-07, pi0.5 2.38e-07, GR00T 8.34e-07 — all at machine precision, shared seeded inputs. Full claim ledger in reflex_context/measured_numbers.md (reflex_context/measured_numbers.md).
The public workflow is intentionally small:
[code block omitted]
Everything else in the CLI feeds evidence into that answer.
## Install
** Recommended** — runs hardware + Python checks first, picks the right install extras for your machine:
[code block omitted]
The bootstrap installer detects your platform (Mac / Jetson Orin / NVIDIA GPU / CPU) and chooses the right extras automatically. It also bails early with a useful message on unsupported hardware (e.g. original 4 GB Jetson Nano — Maxwell GPU + JetPack 4.6 / Python 3.6, too old for VLAs).
** Manual install** if you know what you want:
[code block omitted]
`serve` installs the HTTP stack; choose `onnx` or `gpu` for the inference
runtime. Keep model export in its own virtual environment with `[monolithic]`
when its PyTorch/CUDA requirements differ from serving. The default GPU extra
selects one bounded CUDA 12 dependency family. Jetson uses its JetPack vendor
stack through the installer instead of these x86 GPU wheels. A manually managed
CUDA 13 serving environment must provide matching ORT, TensorRT and CUDA
libraries; mixing CUDA families is not an automatic repair path.
Requires Python ≥ 3.10.
For a smaller existing monolithic export, use the opt-in
validated mixed-FP16 conversion (docs/precision-conversion.md). It preserves the
FP32 source and requires supplied parity inputs and explicit tolerances. Target
memory fit and TensorRT remain separate qualification checks.
The standalone RTSM SigLIP encoder export (docs/rtsm-siglip-export.md) records its
checkpoint, applied preprocessing and CPU parity; policy integration needs a
separate adapter contract.
### What's new in v0.11.2 (2026-05-29)
- **`tether connect` works on a clean install** — `requests` is now a core dependency, so `tether connect status` no longer raises `ModuleNotFoundError` on `pip install fastcrest-tether` without extras (it had been an undeclared import that only resolved transitively).
- **`--fast-kernels` cleared the formal N=100/task L3 LIBERO parity gate** — on Pi0.5 LIBERO-10 tasks 0-2 (600 episodes), Triton fast kernels scored 91.3% (274/300) vs native ORT 85.3% (256/300) — 6.0pp *ahead* of native, so kill-trigger 3 stays clear and the opt-in Triton runtime stays on.
- **Hardened monolithic serve/bench path, with external-data ONNX** — dedicated ORT provider-options + tokenizer-loading modules are extracted from the request hot path; ONNX models with external weight data (`.onnx` + `.onnx_data`, required once a graph exceeds the 2 GB protobuf limit) now load in both serve and the weight-fusion export pass.
- **Cleaner streams** — integration-command errors route to stderr, so `--json` consumers and shell pipelines get a clean stdout.
### What's new in v0.11.1 (2026-05-27)
- **Triton fast kernels** — 2.5x PyTorch, ~12x ORT on A100. Opt in with `tether serve --fast-kernels` (requires the `[fast-kernels]` extra). Falls back to ORT silently when Triton is unavailable.
- **ZMQ transport** — `tether serve --transport zmq` for low-latency robot communication. JPEG
```
