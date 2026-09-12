@echo off
chcp 65001 > nul
cd /d "c:\my project\daily_news_paper_tool"
echo [%date% %time%] 每日 AI 新聞匯報開始執行... >> run.log
"C:\Python314\python.exe" main.py >> run.log 2>&1
echo [%date% %time%] 每日 AI 新聞匯報執行完成 >> run.log
