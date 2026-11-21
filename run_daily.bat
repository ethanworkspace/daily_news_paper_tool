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
set "PYEXE=python"
if exist "C:\Python314\python.exe" set "PYEXE=C:\Python314\python.exe"

set "EXTRA_ARGS="
if /I "%DAILY_PUSH%"=="1" set "EXTRA_ARGS=--push"
if /I "%DAILY_NO_AI%"=="1" set "EXTRA_ARGS=%EXTRA_ARGS% --no-ai"

"%PYEXE%" main.py %EXTRA_ARGS% >> run.log 2>&1
set "RC=%ERRORLEVEL%"

if not "%RC%"=="0" goto :failed

if not exist ".system_generated" mkdir ".system_generated"
echo %TODAY%> "%MARKER%"

>> run.log echo [%date% %time%] Daily AI News Agent finished.
echo [%date% %time%] Daily AI News Agent finished.
exit /b 0

:failed
>> run.log echo [%date% %time%] Daily AI News Agent FAILED rc=%RC%.
echo [%date% %time%] Daily AI News Agent FAILED rc=%RC%.
exit /b %RC%

:already_ran
echo [%date% %time%] Already ran today. Skipping.
>> run.log echo [%date% %time%] Already ran today. Skipping.
exit /b 0