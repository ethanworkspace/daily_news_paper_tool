# 論文 01：u3lib: An AI-Ready Computational Framework for U(3) Symmetry Algebra, Wigner Coupling, and Racah Recoupling Coefficients

- 日期：2026-11-19
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
u3lib 是一個針對核結構及相關應用中 U(3)/SU(3) 表現理論計算的 C++ 函式庫。它採用 Dang 等人 2024 年提出的方法，避免早期公式中的二項式係數與交替求和，計算 Wigner 耦合係數與 Racah 重耦合係數。庫提供不可約表現、維度、Casimir 不變量、共軛、張量積分解與外部重複度，支援標準 Gelfand-Tsetlin 基底與物理 SU(3)⊃SO(3) 基底，含內部重複度與基底轉換，並提供產生器矩陣元、Python 綁定及 AI 可呼叫的領域技能。

## 方法
核心機制利用數值零空間求解器 (KraNS) 從群的升算子作用建構係數，避免超幾何函數與大階乘的數值不穩定。U(3)⊃U(2) 歸約耦合與重耦合係數由最高權 U(3)⊃U(2)⊃U(1) 完整耦合係數經正交零空間獲得，再由降算子傳播；物理 SU(3)⊃SO(3) 係數則經由物理到標準基底轉換 (L+ 零空間) 得到。庫為純標頭 C++20，依賴 Eigen3、Boost、OpenMP、fmt、libwignernj、KraNS，並以 pybind11 提供 Python 介面，支援多執行緒與生命週期管理。

## 結果
摘錄未提供可驗證數字。可見結論為：u3lib 整合了 U(3)/SU(3) 代數所需的完整計算組件，包含不可約表現、耦合/重耦合係數、基底枚舉、產生器矩陣元與基底轉換，並提供一對一映射的 Python 綁定。其 AI 就緒介面透過領域技能目錄讓大型語言模型能從自然語言呼叫例程，屬於 DeepSANE 生態系統一部分，旨在降低整合複雜度並提升任務完成率。

## 限制與展望
作為預印本尚未經同行評審，效能基準與數值精度驗證細節未在摘錄中呈現。庫專注於 U(3)/SU(3) 對稱，擴展至其他群論需另行開發。AI 代理技能目錄的實際易用性與泛化能力仍待更大規模驗證。外部依賴 (Eigen3、KraNS 等) 可能增加部署複雜度，且共享後端生命週期管理需謹慎處理以免運行時錯誤。
