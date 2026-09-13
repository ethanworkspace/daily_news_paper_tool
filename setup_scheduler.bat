@echo off
rem Register Windows Scheduled Task: DailyAINewsAgent
rem Run this file AS ADMINISTRATOR to install the schedule.
setlocal
chcp 65001 >nul
echo ============================================================
echo   Registering Windows Scheduled Task: DailyAINewsAgent
echo ============================================================
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup_scheduler.ps1"
echo.
pause