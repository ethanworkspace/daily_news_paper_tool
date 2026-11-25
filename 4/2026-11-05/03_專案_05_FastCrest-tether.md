# GitHub 專案 05：FastCrest/tether

- 日期：2026-11-05
- URL：https://github.com/FastCrest/tether
- 描述：FastCrest Tether: the OSS edge-to-cloud AI deploy CLI. Optimize, verify, deploy across Jetson, RTX, Apple Silicon, AMD. Hybrid edge-cloud inference with parity certs.
- Stars：86  |  Forks：20  |  Language：Python
- License：NOASSERTION
- Topics：cli, deployment, edge-ai, edge-cloud, fastcrest, groot, inference, jetson, onnx, pi0, python, robot-learning, robotics, smolvla, tensorrt, tether, vision-language-action, vla
- 更新時間：2026-11-01T01:06:22+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
FastCrest Tether 是一個開源的邊緣到雲端 AI 部署命令列工具，專門針對視覺‑語言‑動作（VLA）機器人策略提供優化、驗證與跨平台部署。它支援 Jetson、NVIDIA RTX、Apple Silicon 與 AMD 硬體，可在邊緣設備或雲端執行推論，並透過雙向邊緣‑雲端推論與 parity 證書確保模型在不同硬體上行為一致。主要使用者是機器人學研究者、邊緣 AI 工程師以及需要將 VLA 模型安全落地的開發者，核心問題在於如何證明導出的 ONNX 模型與原始 PyTorch 策略在數值上完全等價（cos = 1.000000），並且能在目標硬體上可靠執行而不產生安全風險。

## 技術
Tether 以 Python 3.10+ 為基礎，透過 CLI 提供 install、serve、connect、go、chat 等子命令。核心技術包括將 VLA PyTorch 模型匯出為單一 ONNX 檔案（支援外部權重資料 .onnx_data），使用 ONNX Runtime 搭配 TensorRT 執行提供者（CUDAExecutionProvider 為後備），並可選擇啟用 Triton Fast Kernels 或 ZMQ 傳輸以降低延遲。此外，專案引用 safetensors 直接載入權重以減少記憶體開支，支援 transformers 5.x DynamicCache，並提供 ROS2 適配器起始套件（Aloha、UR3）以連接真實機器人。支援的硬體平台涵蓋 Jetson Orin、NVIDIA GPU（CUDA 12/13）、Apple Silicon 與 AMD CPU/GPU，並透過安裝腳本自動偵測平台選擇適當的相依性。

## 架構
Tether 的架構分為四層：第一層為 CLI 介面，負責解析子命令（install、serve、connect、go、chat）並呼叫對應功能；第二層為模型匯出層，包含各 VLA 的 exporter（pi0、pi05、smolvla、gr00t）負責將 PyTorch 模型轉換為單一 ONNX 檔案，並處理外部權重資料；第三層為推論執行層，透過 ONNX Runtime 建立 Session，依使用者選擇啟用 TensorRT Execution Provider 或 CUDA Execution Provider，並可選擇啟用 Triton Fast Kernels 或 ZMQ 傳輸以降低延遲；第四層為驗證與證照層，載入 parity inputs、計算輸出與參考模型的 cosine similarity 與 max_abs 差異，並透過 Doctor 工具探測硬體與庫的可用性，最終將結果透過 HTTP 或 ZMQ 傳輸回呼叫端。若 README 未明確說明某些內部細節，則標示推斷依據不足。

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
