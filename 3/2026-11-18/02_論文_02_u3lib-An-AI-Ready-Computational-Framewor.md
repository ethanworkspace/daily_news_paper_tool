# 論文 02：u3lib: An AI-Ready Computational Framework for U(3) Symmetry Algebra, Wigner Coupling, and Racah Recoupling Coefficients

- 日期：2026-11-18
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
u3lib 是一個 C++ 函式庫，針對核結構等應用中的 U(3)/SU(3) 表示理論計算，提供 Wigner 耦合與 Racah 重耦合係數的快速、準確、可重現評估。採用 Dang 等人 2024 年提出的數值零空間方法，避免傳統超幾何函數的數值不穩定。同時支援標準 Gelfand-Tsetlin 基底與物理 SU(3)⊃SO(3) 基底、不可約表示、Casimir 不變量、張量積分解、生成元矩陣元與基底轉換，並提供 Python 綁定與 AI 代理技能目錄，支援自然語言呼叫。

## 方法
核心機制：從最高權重 U(3)⊃U(2)⊃U(1) 完整耦合係數出發，將其作為標準升算子的正交零空間求得，再由對應降算子傳播得到 U(3)⊃U(2) 約化耦合與重耦合係數；物理 SU(3)⊃SO(3) 係數則經由物理到標準基底轉換獲得，該轉換同樣為物理升算子 L+ 的正交零空間。大型稀疏矩陣採用專用迭代零空間求解器 KraNS，小型或塊狀情況回退至稠密 QR 分解。程式庫為純標頭 C++20，依賴 Eigen3、Boost、OpenMP、fmt、libwignernj、KraNS；Python 綁定透過 pybind11 一對一映射 C++ API。提供不可約表示類別、Gelfand 態、基底枚舉、外部/內部重複度、耦合/重耦合係數查表、生成元約化矩陣元、基底轉換等功能，並具備初始化/終結生命週期管理與執行緒安全機制。

## 結果
摘錄未提供可驗證數字。論文展示了 u3lib 的完整架構與介面：涵蓋不可約表示、Casimir 不變量、Gelfand 基底與物理基底枚舉、張量積分解（外部重複度）、U(3)⊃U(2) 與 SU(3)⊃SO(3) 約化耦合係數、6-U(3) 與 9-U(3) 重耦合係數、物理到標準基底轉換、生成元 L、Q 的約化矩陣元。Python 綁定完整鏡射 C++ API，並提供 AI 代理技能目錄，使具備程式執行權限的大型語言模型能從自然語言請求呼叫例程。文中並未給出效能基準、數值精度比較或具體計算規模的實驗數據。

## 限制與展望
作為預印本，尚未經同行評審。文中未詳細討論數值穩定性極限、極大表示下的記憶體/時間複雜度、與現有 Fortran 程式庫的量化比較。依賴多個外部庫（Eigen3、Boost、libwignernj、KraNS）可能增加部署複雜度；多執行緒生命週期管理需謹慎避免共享後端衝突。未來展望包括效能基準測試、擴展至其他對稱群、更完整的驗證套件與文件範例。
