' 每日 AI 新聞匯報排程器 - 開機自動啟動 (隱藏視窗, 每天 08:30 / 錯過自動補跑)
' 複製本檔至「啟動資料夾」即可於每次登入時自動執行
PROJECT_PATH = "C:\my project\daily_news_paper_tool"
Scheduler_Py = PROJECT_PATH & "\scheduler.py"
PythonW = "C:\Python314\pythonw.exe"

Set ws = CreateObject("WScript.Shell")
ws.CurrentDirectory = PROJECT_PATH
ws.Run Chr(34) & PythonW & Chr(34) & " " & Chr(34) & Scheduler_Py & Chr(34), 0, False