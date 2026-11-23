# 論文 01：u3lib: An AI-Ready Computational Framework for U(3) Symmetry Algebra, Wigner Coupling, and Racah Recoupling Coefficients

- 日期：2026-11-15
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
u3lib 是針對核結構與相關應用中 U(3)/SU(3) 表徵理論計算而開發的 C++ 函式庫。現有演算法長期依賴含大階乘與交替和的超幾何函數，數值穩定性不足。Dang 等人 (2024) 提出以群論升算子的正交零空間構建耦合係數，避免二項式係數與交替和，提升精度與速度。本文旨在提供完整、可重現、AI 就緒的計算框架，包含 Wigner 耦合、Racah 重耦合係數、不可約表徵、Casimir 不變量、張量積分解、Gelfand-Tsetlin 標準基與物理 SU(3)⊃SO(3) 基底、生成元矩陣元、基底變換，並提供 Python 綁定與 AI 代理技能目錄，支援自然語言呼叫。

## 方法
u3lib 採用 header-only C++20 設計，依賴 Eigen3 (QR 零空間求解)、Boost (雜湊表)、OpenMP (多執行緒)、fmt (格式化)、libwignernj (SU(2) 耦合/重耦合係數) 及 KraNS (大型稀疏矩陣迭代零空間求解器，小矩陣回退密集 QR)。核心演算法分兩條群鏈： 1. U(3)⊃U(2)⊃U(1) 標準鏈：最高權態的完整耦合係數由標準升算子的正交零空間獲得，再以對應降算子傳播得到所有態；據此構建 U(3)⊃U(2) 約化耦合係數與 6-U(3)、9-U(3) 重耦合係數。 2. SU(3)⊃SO(3) 物理鏈：物理升算子 L+ 的正交零空間給出物理到標準基底的變換矩陣，進而導出物理約化耦合係數。 庫提供類別：su3::irrep / u3::irrep (不可約表徵、維度、Casimir、共軛)、u3::gelfand (Gelfand 標準態、生成元矩陣元)、u3::physicalvector (物理態、內重數 κ)、基底枚舉 (gelfandBasis, physicalBasis)、張量積分解 (Rho, decomposition)、係數資料庫 (wigU3U2db, wigU3SO3db, u3u6db, u3z6db, u3u9db)、基底變換 (phys_to_cano) 及生成元約化矩陣元 (RME_L, RME_Q)。生命週期管理採 initialize/finalize、執行緒局部初始化、快取清除。係數容器支援多維區塊索引與扁平索引雙重存取。Python 綁定透過 pybind11 一對一映射 C++ API。AI 代理技能目錄 (agents/) 規範群論符號、相位慣例、記憶體生命週期與執行緒安全，輔助自然語言驅動計算。

## 結果
摘錄未提供可驗證數字。定性結論顯示 u3lib 整合了 U(3)/SU(3) 表徵論所需的完整代數工具：不可約表徵與 Casimir、標準與物理雙基底、內/外重數、張量積分解、Wigner 耦合與 Racah 重耦合係數 (6-U(3)、9-U(3))、生成元矩陣元、基底變換。採用 header-only 架構、Python 綁定與 AI 代理技能，降低使用門檻。程式碼開源 (MIT)、文件完備、含回歸測試套件。作者宣稱在 AI 就緒介面與基準評估 (Sec. V) 中驗證了代理技能對任務完成度與資源需求的改善，但摘錄未給出具體指標。

## 限制與展望
摘錄未揭露效能基準、數值精度比較、大規模矩陣收斂性測試，亦未說明 AI 代理技能的量化評估結果。共享 libwignernj 後端需謹慎管理初始化/終結順序，否則導致執行時錯誤。KraNS 迭代求解器對極大稀疏矩陣的收斂性與預處理策略未詳述。Header-only 設計可能增加編譯時間。依賴 Eigen3、Boost、OpenMP、KraNS 等外部庫，移植性需驗證。僅支援 U(3)/SU(3) 對稱，擴展至其他群需重構。AI 代理技能僅針對本庫，通用性有限。預印本未經同行評審，API 可能變動。
