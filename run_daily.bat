@echo off
setlocal
cd /d "%~dp0"

rem ============ Compute today as YYYY-MM-DD (locale independent) ============
for /f "usebackq tokens=1" %%i in (`powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"`) do set "TODAY=%%i"

rem ============ Guard: run at most once per day ============
set "MARKER=.system_generated\last_run_date.txt"
if exist "%MARKER%" findstr /x /c:"%TODAY%" "%MARKER%" >nul 2>&1
if not errorlevel 1 goto :already_ran

echo [%date% %time%] Daily AI News Agent started.
>> run.log echo [%date% %time%] Daily AI News Agent started.

rem ============ Run generator ============
if exist "C:\Python314\python.exe" (
    "C:\Python314\python.exe" main.py >> run.log 2>&1
) else (
    python main.py >> run.log 2>&1
)

if not exist ".system_generated" mkdir ".system_generated"
echo %TODAY%> "%MARKER%"

>> run.log echo [%date% %time%] Daily AI News Agent finished.
echo [%date% %time%] Daily AI News Agent finished.
exit /b 0

:already_ran
echo [%date% %time%] Already ran today. Skipping.
>> run.log echo [%date% %time%] Already ran today. Skipping.
exit /b 0