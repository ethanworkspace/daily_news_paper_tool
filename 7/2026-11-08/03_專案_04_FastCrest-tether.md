# GitHub 專案 04：FastCrest/tether

- 日期：2026-11-08
- URL：https://github.com/FastCrest/tether
- 描述：FastCrest Tether: the OSS edge-to-cloud AI deploy CLI. Optimize, verify, deploy across Jetson, RTX, Apple Silicon, AMD. Hybrid edge-cloud inference with parity certs.
- Stars：86  |  Forks：20  |  Language：Python
- License：NOASSERTION
- Topics：cli, deployment, edge-ai, edge-cloud, fastcrest, groot, inference, jetson, onnx, pi0, python, robot-learning, robotics, smolvla, tensorrt, tether, vision-language-action, vla
- 更新時間：2026-11-01T01:06:22+00:00
- 論文層級：未對應論文
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
FastCrest Tether 是一個開源的邊緣‑到‑雲端 AI 部署命令列工具，專注於視覺‑語言‑動作（VLA）機器人政策的驗證與推論。它提供跨 Jetson、RTX、Apple Silicon 與 AMD 平台的一致 ONNX 匯出、混合邊緣‑雲端推論以及 parity 證書，讓使用者能確認政策在實際硬體上是否安全前進。

## 技術
Tether 以 Python 3.10+ 為基礎，使用 ONNX 作為模型中介格式，並依賴 ONNX Runtime 包含 CUDAExecutionProvider 與 TensorRTExecutionProvider（透過 fastcrest‑tensor[serve,gpu] extra），可選擇 Triton fast kernels（[fast‑kernels] extra）或 ZMQ 傳輸（[serve] extra）進行低延遲機器人通訊。模型匯出階段支援 monolithic ONNX、外部權重資料（.onnx + .onnx_data）、safetensors 直接載入以及動態快取相容的 transformers 5.x。CLI 包含 install、serve、connect、go、chat 等子命令，並透過 Doctor 進行硬體與庫路徑偵測。

## 架構
Tether 的架構圍繞 CLI 入口與模型匯出、驗證、服務三層。首先，使用者透過 `tether install` 依硬體自動選擇對應的 extra（onnx、gpu、serve 等）完成環境與依賴安裝。接著，`tether go`（或 `tether serve`）呼叫對應的 VLA 匯出器（pi0、smolvla、gr00t）將 PyTorch policy 轉換為 monolithic ONNX，必要時附加外部權重資料並執行 parity 檢查（cos = 1.000000、max_abs 殘差）。匯出後，模型可經由 `tether serve` 以 HTTP 或 ZMQ 方式啟動推論服務，後端使用 ONNX Runtime，依 extra 選擇 CUDA、TensorRT 或 Triton 執行提供者；`tether connect` 提供狀態查詢與證書產生，`tether chat` 則封裝 CLI 為互動式對話。整個流程中，Doctor 模組負責偵測庫路徑、執行提供者載入與版本相容性，確保部署前的硬體適配與效能基準。

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
