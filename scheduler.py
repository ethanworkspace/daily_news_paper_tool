import sys
import time
from datetime import datetime

# UTF-8 編碼確保
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from main import run_agent

SCHEDULE_HOUR = 8
SCHEDULE_MINUTE = 30


def run_scheduler():
    """常駐 Python 排程器，每天 08:30 自動觸發 run_agent()"""
    print("=" * 60)
    print("⏰ 每日新聞匯報 Python 排程守護程序已啟動")
    print(f"🎯 目標執行時間：每天 {SCHEDULE_HOUR:02d}:{SCHEDULE_MINUTE:02d}")
    print("💡 保持此視窗開啟即可每日自動運行（或執行 setup_scheduler.bat 設定 Windows 工作排程器）")
    print("=" * 60)

    last_run_date = None

    while True:
        now = datetime.now()
        today_str = now.strftime("%Y-%m-%d")

        # 檢查是否到達 08:30 且今天尚未執行過
        if (
            now.hour == SCHEDULE_HOUR
            and now.minute >= SCHEDULE_MINUTE
            and last_run_date != today_str
        ):
            print(f"\n[{now.strftime('%Y-%m-%d %H:%M:%S')}] ⏰ 排程時間到達，開始執行今日匯報...")
            try:
                run_agent()
                last_run_date = today_str
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ 今日匯報完成，進入等待明日排程...")
            except Exception as e:
                print(f"[錯誤] 今日匯報執行發生例外: {e}")

        # 每 30 秒檢查一次
        time.sleep(30)


if __name__ == "__main__":
    run_scheduler()
