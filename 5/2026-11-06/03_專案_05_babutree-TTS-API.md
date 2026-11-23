# GitHub 專案 05：babutree/TTS-API

- 日期：2026-11-06
- URL：https://github.com/babutree/TTS-API
- 描述：Self-hosted streaming TTS gateway with Web UI + REST/WebSocket API — dual-engine local Kokoro CPU inference + Microsoft Edge neural voices, ready-to-run for AI apps, extensions, and automation. 开箱即用的自托管流式 TTS 网关，提供 Web UI + REST/WebSocket API —— 支持本地 Kokoro CPU 推理语音与 Microsoft Edge 语音，面向 AI 应用、浏览器扩展和自动化工作流。
- Stars：41  |  Forks：3  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-07T14:28:50+00:00
- 配對論文：
- 品質分數：2/10 [thin_readme]

## 在做什麼
本專案提供一個可自行部署的流式文字轉語音（TTS）網關，內建 Web UI 與 REST/WebSocket API，支援兩種引擎：本地 Kokoro CPU 推理語音與 Microsoft Edge 神經網路語音。目標使用者為需要即時語音合成的 AI 應用開發者、瀏覽器擴充功能製作者以及自動化工作流設計者，解決依賴第三方雲端 TTS 服務帶來的延遲、成本與隱私問題。

## 技術
專案主要使用 Python 實作，採用 Kokoro 本地 CPU 推理引擎進行語音合成，同時呼叫 Microsoft Edge 的神經網路 TTS 服務取得高品質語音。對外提供 RESTful 端點與 WebSocket 串流介面，並搭配簡易的 Web UI（HTML/JavaScript）供即時測試與設定。資料流程為：使用者經由 API 或 UI 傳入文字 → 選擇引擎 → 產生音訊串流 → 透過 HTTP 或 WebSocket 回傳給客戶端。

## 架構
README 摘錄未提供足夠的架構細節（如使用的 Web 框架、路由組件、併發模型或容器化方式），因此無法根據現有資訊詳細描述模組劃分、資料流或執行流程。僅可推斷存在一個伺服器負責 API 與 WebSocket 服務，以及一個前端頁面提供 UI，但此為推測，缺乏確實依據。

## README 摘錄（節選）
```text

```
