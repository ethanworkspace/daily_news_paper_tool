$ErrorActionPreference = "Stop"

$base = Split-Path -Parent $MyInvocation.MyCommand.Path
$bat = Join-Path $base "run_daily.bat"

if (-not (Test-Path -LiteralPath $bat)) {
    Write-Host "[失敗] 找不到 run_daily.bat：$bat" -ForegroundColor Red
    exit 1
}

# 執行動作：呼叫 run_daily.bat（其內建「每日僅執行一次」護衛，重複觸發會直接跳過）
$action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$bat`"" -WorkingDirectory $base

# 觸發條件：每天 08:30 + 每次登入時檢查
$triggers = @(
    (New-ScheduledTaskTrigger -Daily -At "08:30"),
    (New-ScheduledTaskTrigger -AtLogOn)
)

# 設定：開機/喚醒後錯過時間立即補跑
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2)

try {
    Register-ScheduledTask `
        -TaskName "DailyAINewsAgent" `
        -Description "每日 AI 新聞匯報 Agent（08:30 自動生成並推送 GitHub）" `
        -Action $action `
        -Trigger $triggers `
        -Settings $settings `
        -Force | Out-Null

    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "  [成功] 已註冊排程任務 DailyAINewsAgent" -ForegroundColor Green
    Write-Host "  - 每天 08:30 自動執行" -ForegroundColor Green
    Write-Host "  - 每次登入亦會檢查（今日已執行則自動跳過）" -ForegroundColor Green
    Write-Host "  - 電腦睡著錯過時間時，喚醒後自動補跑" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green

    Start-ScheduledTask -TaskName "DailyAINewsAgent"
    Write-Host "  [測試] 已立即呼叫一次執行驗證（若今日未執行會開始生成）。" -ForegroundColor Cyan
} catch {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host "  [失敗] 註冊排程任務失敗：" -ForegroundColor Red
    Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "  請對 setup_scheduler.bat 按右鍵，選擇「以系統管理員身分執行」。" -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Red
}