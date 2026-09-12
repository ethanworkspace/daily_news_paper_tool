@echo off
chcp 65001 > nul
echo ============================================================
echo   正在註冊 Windows 工作排程器：每日 08:30 執行 AI 新聞 Agent
echo ============================================================

set "TASK_NAME=DailyAINewsAgent"
set "ACTION_PATH=c:\my project\daily_news_paper_tool\run_daily.bat"

schtasks /create /tn "%TASK_NAME%" /tr "\"%ACTION_PATH%\"" /sc daily /st 08:30 /f

if %ERRORLEVEL% equ 0 (
    echo.
    echo [成功] 已成功註冊排程任務「%TASK_NAME%」！
    echo 每天 08:30 將自動啟動爬蟲，抓取當日主題新聞、論文、GitHub專案並以 AI 生成日報。
    echo 執行日誌將自動寫入 run.log。
    echo.
) else (
    echo.
    echo [注意] 建立排程任務失敗，可能需要系統管理員權限。
    echo 請對此檔案按右鍵，選擇「以系統管理員身分執行」。
    echo.
)

pause
