# 論文 05：Mathematical discovery and exploration can be done at scale.

- 日期：2026-10-07
- 來源層級：Tier 2
- 期刊/會議/來源：Proceedings of the National Academy of Sciences of the United States of America
- Venue：Proceedings of the National Academy of Sciences of the United States of America
- 發布時間：2026-10-06T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42814542/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13643321/
- DOI：10.1073/pnas.2536158123
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1757（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
AlphaEvolve, introduced in A. Novikov et al. ["AlphaEvolve: A coding agent for scientific and algorithmic discovery" (Tech. Rep., Google DeepMind, 2025).], is a generic evolutionary coding agent that combines large language models (LLMs) with automated evaluation in a loop that proposes, tests, and refines algorithmic solutions. Here we showcase AlphaEvolve as a tool for autonomously discovering novel mathematical constructions and making progress on long-standing open problems. On 67 problems spanning mathematical analysis, combinatorics, geometry, and number theory, the system rediscovered the best known solutions in most cases and improved on them in several. In some instances, it also generalized results for finitely many input values into a formula valid for all inputs. Furthermore, we combine this methodology with Deep Think [Google DeepMind, Advanced Version of Gemini with Deep Think Officially Achieves Gold-Medal Standard at the International Mathematical Olympiad (Google DeepMind Blog, 2025).] and AlphaProof [Google DeepMind, AI Achieves Silver-Medal Standard Solving International Mathematical Olympiad Problems (Google DeepMind Blog, 2024).] in a broader framework where the additional proof assistants and reasoning systems provide automated proof generation and further mathematical insights. These results demonstrate that LLM-guided evolutionary search can autonomously discover mathematical constructions that complement human intuition, at times matching or improving the best known results, and point to new modes of interaction between mathematicians and AI systems. AlphaEvolve explores vast search spaces to solve complex optimization problems at scale, often with significantly reduced preparation and computation time.

## 背景與目的
本研究旨在解決數學發現與探索的規模化問題。現有方法主要依賴人類直覺與手工證明，難以在龐大搜尋空間中高效發現新構造。AlphaEvolve 作為一個通用演化編碼代理，結合大型語言模型（LLM）與自動化評估，形成「提出-測試-優化」迴路，能自主發現數學構造並推進長期開放問題。本文目標在展示該系統在數學分析、組合、幾何、數論等 67 道問題上的表現，並結合 Deep Think 與 AlphaProof 引入自動證明生成，確立 LLM 引導演化搜尋作為輔助數學家的新範式。

## 方法
問題設定：輸入為數學問題描述（涵蓋分析、組合、幾何、數論），輸出為算法解決方案、構造或通用公式。整體架構採用演化迴路：LLM 作為提案生成器，根據當前種群與問題描述產生候選程式碼；自動化評估模組對候選方案執行測試、驗證或目標函數計算；依評估結果進行選擇、變異與交叉，迭代優化。核心機制包含：(1) LLM 引導的程式碼生成與修改，(2) 執行環境與自動化評估器（單元測試、屬性驗證、最佳化目標），(3) 演化策略（種群管理、適應度排序、多樣性維持）。資料表示方面，問題被編碼為可執行的程式碼框架與規格，LLM 操作程式碼而非自然語言。訓練目標與損失函數：摘錄未提及離線訓練，屬於推論階段的演化搜尋，最佳化目標由問題定義的評估指標決定。推理流程：初始化種群 → LLM 提案 → 自動評估 → 選擇與變異 → 迭代至收斂或資源耗盡。關鍵差異：結合 LLM 的程式碼理解與演化搜尋的全域探索，並整合 Deep Think 與 AlphaProof 提供自動證明生成，實現「發現-驗證-證明」一體化，大幅減少前置準備與計算時間。

## 結果
在 67 個跨領域問題上，AlphaEvolve 在大多數情況下重現了目前最佳已知解，並在若干問題上取得改進；部分案例中將有限輸入值的結果推廣為適用於所有輸入的通用公式。結合 Deep Think 與 AlphaProof 後，系統能自動生成證明並提供進一步數學洞見。定性結論顯示 LLM 引導演化搜尋可自主發現補足人類直覺的數學構造，有時達到或超越現有最佳結果。摘錄未提供可驗證的具體數值指標（如成功率、改進幅度、計算時間）。

## 限制與展望
依目前可取得資料，無法確認系統在更大規模、更多樣數學領域的泛化能力；演化搜尋的計算成本、超參數敏感度、LLM 產生幻覺對解決方案正確性的影響未詳細說明；自動證明生成的完整性與可信度仍需進一步驗證；評估僅限 67 道問題，缺乏與人類專家或其他 AI 系統的系統性比較。潛在風險包含錯誤證明被接受、過度依賴特定 LLM 能力。後續研究方向可朝擴大問題集、改進演化策略、強化證明助手整合、建立人機協作介面等方向發展。
