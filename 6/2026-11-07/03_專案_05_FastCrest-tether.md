# GitHub 專案 05：FastCrest/tether

- 日期：2026-11-07
- URL：https://github.com/FastCrest/tether
- 描述：FastCrest Tether: the OSS edge-to-cloud AI deploy CLI. Optimize, verify, deploy across Jetson, RTX, Apple Silicon, AMD. Hybrid edge-cloud inference with parity certs.
- Stars：86  |  Forks：20  |  Language：Python
- License：NOASSERTION
- Topics：cli, deployment, edge-ai, edge-cloud, fastcrest, groot, inference, jetson, onnx, pi0, python, robot-learning, robotics, smolvla, tensorrt, tether, vision-language-action, vla
- 更新時間：2026-11-01T01:06:22+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
FastCrest Tether 是一個開源的邊緣‑雲端 AI 部署命令列工具，專門針對視覺‑語言‑動作（VLA）機器人策略提供安全驗證與一致性認證。它支援在 Jetson、RTX、Apple Silicon 與 AMD 平台上最佳化、驗證並部署單體 ONNX 模型，並提供混合邊緣‑雲端推論路徑，讓使用者能確認策略在真實硬體上是否可以安全前進。目標使用者為機器學習工程師、機器人系統開發者以及需要在資源受限設備上執行高精度 VLA 模型的研究團隊。核心問題在於如何將參考 PyTorch VLA 政策無損轉換為可在異構硬體上運行的 ONNX 形式，同時保證數值奇偶校驗（cos = 1.000000）與效能，從而解決部署信心與跨平台一致性的挑戰。

## 技術
Tether 以 Python 3.10+ 為主要實作語言，透過 CLI（install、serve、go、connect、bench、chat）提供功能。它依賴 ONNX 進行模型匯出與推論，支援 ONNX Runtime 的 CUDA、TensorRT EP 以及可選的 Triton Fast Kernels（需額外安裝 fast‑kernels extra），在 Jetson 設備則使用 JetPack 提供的 TensorRT 庫。模型匯出階段採用單體 ONNX（含外部權重資料 .onnx_data）與權重融合 pass，並提供 safetensors 直接載入以減少記憶體開銷。Tokenizer 與前處理被抽離為獨立模組，以減少熱路徑開銷。此外，Tether 內建 ZMQ 傳輸（需 pyzmq、msgpack）用於低延遲機器人通訊，並提供 ROS2 適配器起始套件（Aloha、UR3）供真實硬體整合。其餘依賴包括 transformers（支援 5.x DynamicCache）、msgpack、requests 等。

## 架構
典型使用流程始於安裝階段，執行 `tether install`（或使用一鍵腳本）會偵測硬體與 Python 版本，自動選擇對應的 extra（例如 Jetson、GPU、serve、onnx 等）。安裝完成後，使用者可透過 `tether export`（或對應的 monolithic ONNX 匯出腳本）將參考 PyTorch VLA 政策轉換為單體 ONNX 模型，此步驟會驗證匯出後的輸出與原始 PyTorch 在相同種子輸入下的餘弦相似度達到 1.000000，並記錄最大絕對誤差。接著，`tether serve` 啟動推論服務，使用者可指定執行提供者（ORT‑CUDA、TensorRT EP、Triton Fast Kernels）以及傳輸方式（預設 HTTP 或 ZMQ）。服務接受圖像與語言輸入，經過內建的前處理（SigLIP 編碼器或其他視覺 backbone）後送入 ONNX 模型，得到動作向量，再經過後處理（如動作縮放、離散化）後透過所選傳輸回傳給客戶端。`tether connect` 提供狀態查詢與健康檢查，`tether bench` 則用於測量延遲與吞吐，`tether go` 與 `tether chat` 是包裝腳本，分別用於快速啟動服務與互動式查詢。整個資料流程因此為：輸入 → 前處理 → ONNX 推論（依硬體選擇的 EP） → 後處理 → 傳輸 → 消費者（機器人控制器或使用者）。若採用混合邊緣‑雲端模式，邊緣端僅運行輕量視覺編碼器，將特徵傳送至雲端端完成語言與動作解碼，雙端皆透過相同的 ONNX 權重與 parity 證明確保數值一致。

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
