# GitHub 專案 02：FastCrest/tether

- 日期：2026-11-03
- URL：https://github.com/FastCrest/tether
- 描述：FastCrest Tether: the OSS edge-to-cloud AI deploy CLI. Optimize, verify, deploy across Jetson, RTX, Apple Silicon, AMD. Hybrid edge-cloud inference with parity certs.
- Stars：86  |  Forks：21  |  Language：Python
- License：NOASSERTION
- Topics：cli, deployment, edge-ai, edge-cloud, fastcrest, groot, inference, jetson, onnx, pi0, python, robot-learning, robotics, smolvla, tensorrt, tether, vision-language-action, vla
- 更新時間：2026-11-01T01:06:22+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
FastCrest Tether 是一個開源的邊緣到雲端 AI 部署 CLI，專注於驗證與最佳化視覺‑語言‑動作（VLA）機器人政策，提供跨 Jetson、RTX、Apple Silicon、AMD 平台的一致性檢查與混合邊緣‑雲端推理，確保政策在實際執行前能安全前進。

## 技術
該專案以 Python 實作 CLI，核心功能包括將 VLA Policy 匯出為單一 ONNX 模型、使用 ONNX Runtime（可選 TensorRT、CUDA 或 Triton 執行提供者）進行推理、支援 safetensors 直接載入權重、提供 ZMQ 低延遲傳輸、以及透過 BaseVLA 脊柱將不同 VLA 家族組合為約 100 行的組合類別。

## 架構
Tether 的主要模組包括：CLI 入口（tether connect、tether serve、tether go、tether bench）、模型匯出器（exporters）負責 PyTorch → ONNX 的單一模型與外部資料處理、VLA 模型庫（models/vlas）實作 BaseVLA 脊柱的組合類別、推理服務（serve）載入 ONNX 並根據選擇的執行提供者執行前向傳播、基準測試（bench）測量延遲與精度、以及傳輸層（ZMQ）用於機器人即時通訊。資料流程為：使用者透過 CLI 指令觸發模型匯出或服務啟動 → 載入 ONNX 權重（可外部 .onnx_data） → 建立 ONNX Runtime Session（選擇 EP） → 接收輸入（影像、文字等） → 執行推理 → 輸出動作向量，若使用 ZMQ 則透過 msgpack 序列化傳輸。由於 README 未詳細說明內部模組間的依賴圖與錯誤處理，以上架構描述僅基於可見的 CLI 指令與說明。

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
