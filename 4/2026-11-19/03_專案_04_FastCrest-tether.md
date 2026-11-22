# GitHub 專案 04：FastCrest/tether

- 日期：2026-11-19
- URL：https://github.com/FastCrest/tether
- 描述：FastCrest Tether: the OSS edge-to-cloud AI deploy CLI. Optimize, verify, deploy across Jetson, RTX, Apple Silicon, AMD. Hybrid edge-cloud inference with parity certs.
- Stars：86  |  Forks：21  |  Language：Python
- License：NOASSERTION
- Topics：cli, deployment, edge-ai, edge-cloud, fastcrest, groot, inference, jetson, onnx, pi0, python, robot-learning, robotics, smolvla, tensorrt, tether, vision-language-action, vla
- 更新時間：2026-11-01T01:06:22+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
FastCrest Tether 是一個開源的邊緣‑到‑雲端 AI 部署命令列工具，專門用於視覺‑語言‑動作 VLA 機器人政策的安全驗證與跨平台部署。它支援 Jetson、RTX、Apple Silicon 與 AMD 硬體，提供單體 ONNX 匯出與參考 PyTorch 政策的逐位元 parity 檢查，並透過混合邊緣‑雲端推論與憑證機制，讓開發者能確認政策在真實硬體上是否可安全執行。

## 技術
Tether 以 Python 3.10+ 為基礎，透過 CLI 安裝腳本自動偵測平台並選擇對應的安裝 extra（serve、gpu、onnx、fast‑kernels、zmq 等）。核心依賴包括 ONNX Runtime、TensorRT 執行提供者、Triton 快核、safetensors 直接載入、msgpack 與 pyzmq（ZMQ 傳輸），以及 FastCrest 自行實作的 BaseVLA spine 架構，將各 VLA 家族抽象為約 100 行的組合類別。模型匯出階段採用單體 ONNX 匯出，支援超過 2GB 的外部權重資料（.onnx + .onnx_data），並提供選擇性混合 FP16 轉換與 TensorRT 引擎建置。推論階段可選擇 CUDAExecutionProvider、TensorrtExecutionProvider 或 Triton 後端，並透過 HTTP 或 ZMQ 進行低延遲機器人通訊。

## 架構
Tether 的架構圍繞三個主要模組：安裝與平台偵測（installer）、模型匯出與驗證（exporter / parity checker）以及推論服務（serve）。安裝腳本會先執行硬體與 Python 檢查，依據偵測到的作業系統與晶片（Jetson Orin、NVIDIA GPU、Apple Silicon、AMD）自動選擇對應的依賴套件。匯出模組將參考 PyTorch VLA 政策轉換為單體 ONNX，在過程中執行逐位元 parity 比對（cos = +1.000000）並產生 measured_numbers.md 證明。服務模組載入產生的 ONNX（可含外部權重），透過 ONNX Runtime 選擇 TensorRT、CUDA 或 Triton 執行提供者，並依據使用者選擇啟用 HTTP 或 ZMQ 傳輸層；ZMQ 路徑使用 msgpack 序列化 JPEG 圖像以實現低延遲機器人圖傳。CLI 提供 tether go（一鍵啟動服務與客戶端對話）、tether connect（查詢服務狀態）以及 chat（透過 subprocess 包裝真實 CLI 進行互動）等指令，所有資料流均經由標準輸出/錯誤流分離，以便 JSON 消費者與管線處理。若 README 未明確說明某些內部細節，則以上描述僅基於可見的安裝、匯出與服務說明進行合理推斷。

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
