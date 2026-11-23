# GitHub 專案 03：jakobhoeg/browser-ai

- 日期：2026-11-15
- URL：https://github.com/jakobhoeg/browser-ai
- 描述：In-browser AI model providers for the Vercel AI SDK, built to make client-side AI integration simpler and more consistent across vendors.
- Stars：208  |  Forks：27  |  Language：TypeScript
- License：NOASSERTION
- Topics：ai, ai-sdk, browser, browser-ai, built-in-ai, chrome-ai, edge, inference, llm, transformer-models, transformers, transformers-js, vercel, webllm
- 更新時間：2026-11-16T05:50:25+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
此專案提供一組瀏覽器內 AI 模型提供者，專為 Vercel AI SDK 設計，讓開發者能在 Chrome/Edge、WebLLM、Transformers.js 或 wllama 等環境中直接執行大型語言模型，並在不支援時自動回落至伺服器端模型，簡化客戶端 AI 整合所需的自訂鉤子、UI 元件與狀態管理。目標使用者為前端或全棧開發者，核心問題在於減少跨供應商不相容性與重複的樣板碼。

## 技術
專案使用 TypeScript 撰寫，核心套件 @browser-ai/core 定義統一介面，而 @browser-ai/web-llm、@browser-ai/transformers-js 與 @browser-ai/wllama 分別封裝 Chrome/Edge 內建 AI（Prompt API）、WebLLM、Transformers.js 與 wllama（llama.cpp）等推論後端。透過 Vercel AI SDK 的 model 接口，實現瀏覽器端推論（依賴 WebGPU/WASM）與伺服器端 fallback。支援 AI SDK v5、v6、v7 版本。

## 架構
架構上，browser-ai 以 provider 為基本模組：core 提供抽象類別與工廠函式，各廠商套件實現具體的模型載入、權重下載與推論執行。應用層透過 Vercel AI SDK 調用 model，SDK 會呼叫對應的 browser-ai provider，provider 負責在瀏覽器中初始化模型（例如透過 Transformers.js 載入權重並使用 WebGPU 運算）並回傳產生結果；若瀏覽器環境不支援或模型載入失敗，provider 會觸發 SDK 的 fallback 機制，改為呼叫伺服器端模型。由於 README 僅列出基本使用範例與套件版本對應，未提供詳細的內部資料流圖或服務間通訊細節，故此部份架構描述僅基於可見的套件結構與使用說明進行合理推斷。

## README 摘錄（節選）
```text
# Browser AI model providers for Vercel AI SDK
(https://www.npmjs.com/package/@browser-ai/core)
(https://www.npmjs.com/package/@browser-ai/web-llm)
(https://www.npmjs.com/package/@browser-ai/transformers-js)
(https://www.npmjs.com/package/@browser-ai/wllama)
TypeScript libraries that provide access to in-browser AI model providers with seamless fallback to using server-side models.
## Documentation
For detailed documentation, browser requirements and advanced usage, refer to the official documentation site (https://browser-ai.dev/docs).
### Package Versions
| Package | AI SDK v5 | AI SDK v6 | AI SDK v7 |
| ----------------------------- | :-------: | :-------: | :---------: |
| `@browser-ai/core` | ✓ `1.0.0` | ✓ `2.x` | ✓ `≥ 3.0.0` |
| `@browser-ai/transformers-js` | ✓ `1.0.0` | ✓ `2.x` | ✓ `≥ 3.0.0` |
| `@browser-ai/web-llm` | ✓ `1.0.0` | ✓ `2.x` | ✓ `≥ 3.0.0` |
| `@browser-ai/wllama` | - | - | ✓ `≥ 3.0.0` |
[code block omitted]
### Basic Usage with Chrome/Edge AI
[code block omitted]
### Basic Usage with WebLLM
[code block omitted]
### Basic Usage with Transformers.js
[code block omitted]
### Basic Usage with wllama (llama.cpp)
[code block omitted]
## Resources
### Articles & guides
- Chrome for Developers: Use the Prompt API with the Vercel AI SDK (https://developer.chrome.com/blog/prompt-api-with-vercel-ai?hl=en)
- Chrome for Developers: Use the Vercel AI SDK UI and AI Elements with the Prompt API (https://developer.chrome.com/blog/prompt-ui-ai-elements-with-vercel-ai?hl=en)
- Hugging Face: Building a Next.js application with the AI SDK (https://huggingface.co/docs/transformers.js/tutorials/next-ai-sdk)
- Hugging Face: Transformers.js × Vercel AI SDK integration (https://huggingface.co/docs/transformers.js/integrations/vercel-ai-sdk)
### Example applications
- Huggingface Transformers.js AI SDK v5: next-vercel-ai-sdk-v5-transformers-js-example (https://github.com/huggingface/transformers.js-examples/tree/main/next-vercel-ai-sdk-v5)
- Huggingface Transformers.js AI SDK v6: next-vercel-ai-sdk-v6-transformers-js-example (https://github.com/huggingface/transformers.js-examples/blob/main/next-vercel-ai-sdk-v6-tool-calling)
## Sponsors
This project is part of the Vercel OSS Program (https://vercel.com/open-source-program), and was previously sponsored by Chrome for Developers (https://developer.chrome.com/).
## Contributing
Contributions are more than welcome! However, please make sure to check out the contribution guidelines (https://github.com/jakobhoeg/browser-ai/blob/main/CONTRIBUTING.md) before contributing.
## Why?
If you've ever built apps with local language models, you're likely familiar with the challenges: creating custom hooks, UI components and state management (lots of it), while also building complex integration layers to fall back to server-side models when compatibility is an issue.
Read more about this here (https://www.browser-ai.dev/docs/ai-sdk-v7).
## Author
2025 © Jakob Hoeg Mørk
```
