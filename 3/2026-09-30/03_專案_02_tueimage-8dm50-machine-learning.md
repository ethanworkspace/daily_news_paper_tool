# GitHub 專案 02：tueimage/8dm50-machine-learning

- 日期：2026-09-30
- URL：https://github.com/tueimage/8dm50-machine-learning
- 描述：TU/e 8DM50 Machine Learning in Medical Imaging and Biology course materials.
- Stars：42  |  Forks：101  |  Language：TeX
- License：MIT
- Topics：
- 更新時間：2026-09-15T08:53:50+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案提供荷蘭埃因霍芬理工大學 8DM50 課程的教學資源，包括講義幻燈片、Python 實作練習（Jupyter Notebook）與環境設定指南，旨在幫助醫學影像與計算生物學領域的學生學習機器學習基礎與深度學習方法，並完成小組實作。

## 技術
課程內容以 Python 為主要程式語言，實作練習採用 Jupyter Notebook，其中一項作業在 Google Colab 上完成；講義採用 TeX（Beamer）編寫並輸出為 PDF；環境設定透過 software.md 說明，可選擇使用 Git 管理程式碼；課程資訊與作業提交透過 Canvas LMS 進行，討論區供問題詢問。

## 架構
學生首先依照 software.md 設定 Python 開發環境（可選擇安裝 Git），接著從 GitHub 下載或 clone 本倉庫取得講義（TeX 編譯的 PDF）與實作練習（Jupyter Notebook）。在導師指導的自習時段，學生依序完成每週的 Notebook 練習，其中第五週的作業需在 Google Colab 環境中執行。完成練習後，學小組將作業上傳至 Canvas 的 Assignments 區域，並在 Canvas Discussion 區提問或回覆。講義與投影片則由教師在課堂上使用，課程評分依據實作練習（25%）、閱讀報告（10%）與期末考試（65%）計算。若 README 未明確說明底層深度學習框架，則此部分為基於可見內容的合理推斷。

## README 摘錄（節選）
```text
# Machine Learning in Medical Imaging and Biology (8DM50)
The course covers a number of machine learning methods and concepts, including state-of-the-art deep learning methods, with example applications in the medical imaging and computational biology domains.
## Use of Canvas
This GitHub page contains all the general information about the course and the study materials. The Canvas page of the course (https://canvas.tue.nl/courses/31358) will be used only for sharing of course information that cannot be made public (e.g. Microsoft Teams links), submission of the practical work and posting questions to the instructors and teaching assistants (in the Discussion section). The students are highly encouraged to use the Discussion section in Canvas. All general questions (e.g. issues with setting up the programming environment, error messages etc., general methodology questions) should be posted in the Discussion section. **Such questions asked by email will not be answered.**
** TLDR**: GitHub is for content, Canvas for communication and submission of assignments. Do not ask questions by email unless absolutely necessary.
## Schedule
The course schedule is as follows:
* **Lectures**, *time*: Wednesdays 08:45 - 10:45, *location*: Neuron -1.354 (always check your timetable for changes).
* **Guided self-study**, *time*: Wednesdays 10.45 - 12.45, *location*: Atlas 4.215 (always check your timetable for changes).
## Practical work
The practical work will be done in groups. The groups will be formed in Canvas and you will also submit all your work there (check the Assignments section for the deadlines). Your are expected to do this work independently with the help of the teaching assistants during the guided self-study sessions (*begeleide zelfstudie*). You can also post your questions in the Discussion section in Canvas at any time (i.e. not just during the practical sessions).
** IMPORTANT: Please read this guide (how_to_ask_questions.md) on effectively asking questions during the practical sessions.**
### Use of ChatGPT and other large language models
The use of ChatGPT and other large language models for the practical work is allowed, provided that:
1) You use ChatGPT and other large language models only as aid in your work and **NOT** as primary sources of information (e.g. to do literature search), and primary mode of writing and coding (e.g. asking for answers to entire assignment questions is not allowed, however, improving the writing or coding of answers to questions is allowed).
2) You write a one-page reflection report on the use of such tools answering the following questions:
* What were the up- and down-sides of using ChatGPT (or similar tools) in your work?
* In your view, are such tools helpful or harmful when used in education?
* Did it make you more or less productive?
* How did you specifically use these tools (give examples)?
* Were these tools accurate in their answers?
Note that the report is **mandatory** if you used ChatGPT (or similar tools) in any way for the course and it does NOT have any negative consequence (e.g. lead to lower grades). If you do not submit the report we will assume that you did not use such tools but if this is detected during the grading it will be considered cheating.
# Materials
## Books
The lectures are mainly based on the selected chapters from the following two books that are freely available online:
* Deep Learning (https://www.deeplearningbook.org/), Ian Goodfellow and Yoshua Bengio and Aaron Courville
* Elements of Statistical Learning (https://web.stanford.edu/~hastie/ElemStatLearn/), Trevor Hastie, Robert Tibshirani, Jerome Friedman
The follwing book is optional but highly recommended:
* Probabilistic Machine Learning: An Introduction (https://probml.github.io/pml-book/book1.html), Kevin Patrick Murphy.
Additional reading materials such as journal articles are listed within the lecture slides.
## Software
** IMPORTANT: It is essential that you correctly set up the Python working
```
