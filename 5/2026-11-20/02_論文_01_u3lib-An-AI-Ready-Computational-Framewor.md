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
u3lib 針對核結構與相關領域中 U(3)/SU(3) 表現論計算的需求，解決傳統演算法依賴超幾何函數、大階乘與交替求和導致數值不穩定的問題。該庫提供快速、準確且可重現的 Wigner 耦合係數、Racah 重耦合係數、不可約表現標籤、Casimir 不變量、張量積分解與基底轉換，並具備 AI 就緒介面，支援自然語言呼叫。

## 方法
核心機制採用 Dang et al. 2024 提出的數值零空間求解器：先從 U(3)⊃U(2)⊃U(1) 正則升算子的正交零空間獲得最高權全耦合係數，再以對應降算子傳播得到 U(3)⊃U(2) 約化耦合與重耦合係數；物理 SU(3)⊃SO(3) 係數則經由物理升算子 L+ 的零空間求得基底轉換矩陣後轉換而來。輸入為不可約表現標籤與基底選擇，輸出為耦合係數查詢表、生成元矩陣元與約化矩陣元。庫以 C++20 標頭檔實作，依賴 Eigen3、Boost、OpenMP、libwignernj 及 KraNS 迭代求解器，提供 Python pybind11 綁定與 AI 代理技能目錄，生命週期管理需顯式 initialize/finalize 並注意共享後端狀態。

## 結果
摘錄未提供可驗證數字。可見結論：u3lib 以標頭檔形式發布，支援正則 Gelfand-Tsetlin 基底與物理 SU(3)⊃SO(3) 基底、內部與外部重複度、張量積分解、生成元矩陣元、基底轉換；Python 介面完整鏡射 C++ API；附帶迴歸測試套件與 AI 代理技能目錄，展示自然語言驅動計算流程。

## 限制與展望
作為預印本，缺乏效能基準與大規模數值驗證；依賴外部庫（libwignernj、KraNS）且共享後端生命週期需謹慎管理；僅涵蓋 U(3)/SU(3) 對稱鏈，擴展至其他群組需另行開發；AI 代理整合仍處早期階段，技能目錄完整性與泛化能力有待實證。
