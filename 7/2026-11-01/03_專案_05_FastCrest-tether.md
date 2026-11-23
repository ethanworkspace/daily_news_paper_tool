# GitHub 專案 05：FastCrest/tether

- 日期：2026-11-01
- URL：https://github.com/FastCrest/tether
- 描述：FastCrest Tether: the OSS edge-to-cloud AI deploy CLI. Optimize, verify, deploy across Jetson, RTX, Apple Silicon, AMD. Hybrid edge-cloud inference with parity certs.
- Stars：86  |  Forks：21  |  Language：Python
- License：NOASSERTION
- Topics：cli, deployment, edge-ai, edge-cloud, fastcrest, groot, inference, jetson, onnx, pi0, python, robot-learning, robotics, smolvla, tensorrt, tether, vision-language-action, vla
- 更新時間：2026-11-01T01:06:22+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
FastCrest Tether 是一個開源的邊緣到雲端 AI 部署命令列工具，專門針對視覺‑語言‑動作（VLA）模型提供驗證、優化與跨平台部署功能。它支援 Jetson、RTX、Apple Silicon、AMD 等硬體，並提供混合邊緣‑雲端推論以及 parity 證書，幫助機器人與邊緣 AI 開發者確認策略是否安全可執行，解決 VLAs 在不同框架與硬體上的一致性與可靠性問題。

## 技術
Tether 以 Python 實作 CLI，核心功能包括將 PyTorch VLA 政策匯出為單體 ONNX 模型（支援外部權重資料）、使用 ONNX Runtime 配合 TensorRT 執行提供者（可選 Triton 快速核心與 ZMQ 傳輸），並透過 safetensors 直接載入權重以減少記憶體開銷。專案採用 BaseVLA 脊椎架構，將視覺、語言、投影等組件組合為可組合類別，並提供 ROS2 適配器起始套件。依賴項涵盖 fastcrest-tether[serve,gpu]、[fast-kernels]、[onnx] 等額外套件，需 Python ≥3.10。

## 架構
Tether 的架構围绕四個主要指令：install（自動偵測平台並安裝適當的硬體相依套件）、export（將 VLA 政策轉換為單體 ONNX，必要時附帶外部權重檔案並執行 parity 驗證）、serve（啟動 ONNX Runtime 推論服務，可選擇 TensorRT、Triton 快速核心或 ZMQ 傳輸，並載入 tokenizer 與外部資料模組）、bench/connect（基於服務進行效能基準測試或狀態查詢）。資料流程為：使用者透過 CLI 指定模型與硬體，export 階段產生 ONNX 模型並產生 parity 證書；serve 階段載入該模型、建立執行階段提供者、處理輸入（圖像經 JPEG‑msgpack 序列化）並產生動作輸出；connect 與 bench 則是對同一服務發出查詢或基準請求以取得延遲、成功率等指標。若 README 未詳細說明內部模組劃分，則以上說明基於可觀察的指令行為與檔案結構推斷。

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
