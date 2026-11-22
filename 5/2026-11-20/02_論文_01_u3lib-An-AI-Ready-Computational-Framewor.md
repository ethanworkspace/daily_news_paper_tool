# 論文 01：u3lib: An AI-Ready Computational Framework for U(3) Symmetry Algebra, Wigner Coupling, and Racah Recoupling Coefficients

- 日期：2026-11-20
- 來源層級：Tier 3
- 期刊/會議/來源：arXiv
- Venue：arXiv preprint
- 發布時間：2026-11-19T18:25:49+00:00
- URL：http://arxiv.org/abs/2611.26558v1
- PDF：https://arxiv.org/pdf/2611.26558v1.pdf
- DOI：
- arXiv：2611.26558
- 影響指標：N/A (preprint)
- 影響指標來源：arXiv preprint (not peer-reviewed journal/conference)
- 引用數：0
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2611.26558
- 全文字數：55401（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/Deep-SANE/u3lib
- 配對 Repo：Deep-SANE/u3lib

## 摘要
u3lib is a C++ library for U(3)/SU(3) representation-theory calculations in nuclear structure and related applications. It evaluates Wigner coupling and Racah recoupling coefficients using the procedure proposed in 2024 by Dang et al., which avoids the binomial coefficients and alternating sums used in earlier formulations. The library also provides irreducible representations (irreps), dimensions, Casimir invariants, conjugation, and tensor-product decompositions with outer multiplicities. It supports the canonical Gelfand-Tsetlin basis and the physical SU(3) $\supset$ SO(3) basis, including inner multiplicities and the transformation between the two bases. Generator routines return matrix elements in the canonical basis and reduced matrix elements in the physical basis. Python bindings mirror the C++ API. Domain skills supplied with the repository allow an AI assistant with code-execution access to call these routines from natural-language requests.

## 背景與目的
核結構與相關領域（如粒子物理、量子資訊、凝態物理、量子光學、格規理論）大量需要 U(3)/SU(3) 耦合與重耦合係數、不可約表示（irrep）、Casimir 不變量、張量積分解與基底轉換。傳統演算法（Draayer-Akiyama, 1973）依賴超幾何函數、大階乘與交替求和，易導致數值不穩定。Dang et al. (2024) 提出以群論升算子的正交零空間構建係數，避免上述問題。本文開發 u3lib，實作該演算法，提供完整的 C++ 標頭庫與 Python 綁定，並設計 AI 代理技能目錄，使自然語言可直接呼叫計算流程，目標為快速、準確、可重現且 AI 就緒的表現論計算框架。

## 方法
問題設定：輸入 U(3)/SU(3) irrep 標籤（λ, μ 或 n13,n23,n33）、角動量 L、內部多重度 κ、外部多重度 ρ，輸出 Wigner 約化耦合係數（U(3)⊃U(2) 與 SU(3)⊃SO(3)）、Racah 重耦合係數（6-U(3), 9-U(3)）、irrep 維度、Casimir、共軛、張量積分解、Gelfand-Tsetlin 標準基底與物理 SU(3)⊃SO(3) 基底、生成元矩陣元、基底轉換振幅。 整體架構：標頭式 C++ 庫（C++20），模組化為 U3irrep.h（irrep 類別）、U3gelfand.h（Gelfand 狀態）、U3basis.h（基底枚舉、內部多重度 κ、physicalvector）、U3decomposition.h（外部多重度 ρ、克羅內克級數）、U3U2xU3U2.h/U3SO3xU3SO3.h（標準/物理耦合係數查表）、U3_U6Z6Coeffs.h/U3_U9Coeffs.h（6-U(3)/9-U(3) 重耦合係數）、U3SO3_to_U3U2U1.h（物理到標準基底轉換）、U3generatorsRME.h（角動量 L 與四極矩 Q 的約化矩陣元）、Definitions.h（係數容器）、u3lib.h（初始化/終結生命週期、執行緒安全）。Python 綁定以 pybind11 一對一映射 C++ API。 核心演算法機制： 1. U(3)⊃U(2) 約化耦合/重耦合係數：從最高權 U(3)⊃U(2)⊃U(1) 完整耦合係數出發，該係數為標準升算子（E12, E23_12/22, E13_12/22）組成的矩陣之正交零空間，利用數值零空間求解器（大稀疏矩陣用迭代式 KraNS，小/塊矩陣回退密集 QR）獲得正交基；再由對應降算子傳播得到完整係數表。 2. SU(3)⊃SO(3) 物理係數：先以物理升算子 L+ 的正交零空間求得物理到標準基底的轉換矩陣（每個 κ 一組正交列），再結合標準基底係數轉換而得。 3. 張量積分解：外部多重度 ρ 由 irrep 標籤的組合規則計算，滿足 ∑_C ρ_max(C) dim C = dim A dim B。 4. 生成元矩陣元：標準基底下直接回傳 E_ij 矩陣元（含分支選擇 _12/_22）；物理基底下回傳 RME_L（角動量）與 RME_Q（四極矩），維度為 κ'_max × κ_max。 資料表示：係數容器支援多維 block 索引與扁平索引雙重存取，內部以 Eigen::MatrixXd 儲存。外部依賴：Eigen3（QR）、Boost（雜湊）、OpenMP（多執行緒）、fmt（格式化）、libwignernj（SU(2) 耦合/重耦合）、KraNS（大稀疏零空間）。 推論流程：initialize() 載入 SU(2) 快取與 U(3) 係數資料庫 → 建立 irrep、Gelfand/physical 狀態 → 查詢係數容器或呼叫轉換/生成元函數 → finalize() 釋放資源。 與既有方法關鍵差異：棄用超幾何函數與交替求和，改以數值零空間求解器構建係數，提升數值穩定性；提供標準與物理雙基底並支援內部多重度 κ 與轉換；整合 AI 代理技能目錄，自然語言可直接驅動計算。

## 結果
摘錄未提供可驗證數字（如執行時間、精度誤差、規模基準、與既有庫比較數值）。可觀察到的定性結論：u3lib 實作完整的 U(3)/SU(3) 表現論計算功能，涵蓋不可約表示、Casimir、共軛、張量積分解（含外部多重度）、標準 Gelfand-Tsetlin 基底與物理 SU(3)⊃SO(3) 基底（含內部多重度 κ）、兩基底互轉、生成元矩陣元（標準基底完整 E_ij、物理基底 RME_L/RME_Q）、Wigner 約化耦合係數（U(3)⊃U(2) 與 SU(3)⊃SO(3)）、Racah 重耦合係數（6-U(3), 9-U(3)）。庫採標頭式 C++20，提供 Python 綁定，支援多執行緒與生命週期管理。附帶 AI 代理技能目錄，實測能引導大語言模型從自然語言完成計算任務，降低整合門檻。第 V 節提及 AI 介面基準評估，但摘錄未給出具體指標。

## 限制與展望
1. 為 arXiv 預印本，未經同行審查。2. 摘錄缺乏效能基準（速度、記憶體、數值誤差）與與傳統庫（如 Draayer-Akiyama 更新版）的量化比較。3. 僅支援 U(3)/SU(3) 對稱性，擴展至其他群需重寫核心零空間構建。4. 依賴外部庫（Eigen3, Boost, libwignernj, KraNS）可能影響跨平台部署與版本相容性。5. AI 代理技能目錄的有效性僅以定性描述，缺乏系統性評估指標（任務完成率、Token 消耗、錯誤率）。6. 大量子數下的計算複雜度、記憶體增長與數值穩定性未在摘錄中討論。7. 物理基底轉換僅支援 SU(3)⊃SO(3) 一條鏈，其他子群鏈需自行實作。後續研究可著重於效能優化、擴展對稱群、完善 AI 代理評估框架、提供更豐富的教學範例與文件。
