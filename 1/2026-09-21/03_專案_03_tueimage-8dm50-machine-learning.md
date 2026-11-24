# GitHub 專案 03：tueimage/8dm50-machine-learning

- 日期：2026-09-21
- URL：https://github.com/tueimage/8dm50-machine-learning
- 描述：TU/e 8DM50 Machine Learning in Medical Imaging and Biology course materials.
- Stars：42  |  Forks：101  |  Language：TeX
- License：MIT
- Topics：
- 更新時間：2026-09-15T08:53:50+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案提供荷蘭埃因霍芬理工大學 8DM50 課程《Medical Imaging and Biology 中的機器學習》的完整教學資源，包括講義投影片、實作 Jupyter Notebook、環境設置指南與 Python 自評測驗，目標使用者為修讀該課程的研究生與對醫學影像及計算生物學機器學習感興趣的自學者，核心在於統一公開內容與課程溝通平台，減少設定障礙並促進實作練習。

## 技術
教材主要以 TeX 撰寫講義並匯出為 PDF，實作部分使用 Python 3、Jupyter Notebook 與 Google Colab（第五次實作），環境設置說明於 software.md，課程參考書目包括《Deep Learning》、《Elements of Statistical Learning》與《Probabilistic Machine Learning》，此外利用 GitHub 托管內容、Canvas 進行通訊、作業提交與討論區，以及提供 Markdown 形式的提問指南。

## 架構
資料流程始於學生從 GitHub 下載 repo，依照 software.md 建立 Python 虛擬環境；接著依週次開啟對應的講義 PDF（TeX 編譯）與實作 Notebook，在 guided self-study 時段進行 coding，完成後將作業上傳至 Canvas Assignments；問題則張貼在 Canvas Discussion 或遵照 how_to_ask_questions.md；若使用大型語言模型，需繳交一頁反思報告。整體架構可視為三層：內容層（TeX/Notebook）、環境層（Python setup）、互動層（Canvas + GitHub）。README 未詳細說明 TeX 編譯流程與自動化測試，因此架構描述僅基於可見檔案與說明推斷。

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
