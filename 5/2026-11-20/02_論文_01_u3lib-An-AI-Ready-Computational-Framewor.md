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
依目前可取得資料不足，需人工查閱原文補充。

## 方法
依目前可取得資料不足，需人工查閱原文補充。

## 結果
u3lib 提供 U(3)/SU(3) 表示論計算框架，實作 2024 年 Dang 等人提出的 Wigner 耦合與 Racah 重耦合係數演算法，避免二項係數與交替求和。支援標準 Gelfand-Tsetlin 基底與物理 SU(3)⊃SO(3) 基底，含內部重數與基底轉換；提供不可約表示、維度、Casimir 不變量、共軛、張量積分解與外部重數。生成器例程回傳標準基底矩陣元與物理基底約化矩陣元。具 Python 綁定與 AI 領域技能，可從自然語言呼叫。摘錄未提供可驗證數字。

## 限制與展望
本庫目前僅實作 U(3)/SU(3) 代數與其標準基底，缺乏對更高階對稱群（如 U(4)、Sp(4)）的支援；在極大不可約表示下的效能與記憶體使用仍有優化空間，且未提供自動微分或 GPU 加速介面。未來規劃擴充更多物理基底轉換、引入並行計算與自動微分框架，並支援核結構以外的量子多體與凝態物理應用，提升通用性與計算效率。
