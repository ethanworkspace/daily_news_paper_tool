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
from config import BASE_DIR

SCHEDULE_HOUR = 8
SCHEDULE_MINUTE = 30
RUN_LOG = BASE_DIR / "run.log"


def _log(message: str):
    """附時間戳記寫入 run.log (供 pythonw 無視窗模式排錯用)"""
    try:
        with open(RUN_LOG, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
    except Exception:
        pass


def _today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _already_ran_today() -> bool:
    """檢查今日是否已執行過（與 run_daily.bat 共用 .system_generated/last_run_date.txt 護衛）"""
    marker = BASE_DIR / ".system_generated" / "last_run_date.txt"
    try:
        if marker.exists():
            return marker.read_text(encoding="utf-8").strip() == _today_str()
    except Exception:
        pass
    return False


def _mark_ran_today():
    marker_file = BASE_DIR / ".system_generated" / "last_run_date.txt"
    try:
        marker_file.parent.mkdir(parents=True, exist_ok=True)
        marker_file.write_text(_today_str(), encoding="utf-8")
    except Exception as e:
        print(f"[錯誤] 無法寫入執行護衛檔: {e}")


def run_scheduler():
    """常駐 Python 排程器。若已過 08:30 且今日未執行，啟動時立即補跑一次。"""
    print("=" * 60)
    print("⏰ 每日新聞匯報 Python 排程守護程序已啟動")
    print(f"🎯 目標執行時間：每天 {SCHEDULE_HOUR:02d}:{SCHEDULE_MINUTE:02d}")
    print("💡 已支援「錯過時間自動補跑」：若開機晚於排程時間，會立即執行今日匯報")
    print("=" * 60)

    while True:
        now = datetime.now()
        now_minutes = now.hour * 60 + now.minute
        schedule_minutes = SCHEDULE_HOUR * 60 + SCHEDULE_MINUTE

        # 已達排程時間、今日尚未執行、且沒有被 run_daily.bat 執行過 → 執行
        if now_minutes >= schedule_minutes and not _already_ran_today():
            print(f"\n[{now.strftime('%Y-%m-%d %H:%M:%S')}] ⏰ 排程/補跑時間到達，開始執行今日匯報...")
            _log("排程時間到達，開始執行今日匯報")
            try:
                run_agent()
                _mark_ran_today()
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ 今日匯報完成，進入等待明日排程...")
                _log("今日匯報完成")
            except Exception as e:
                print(f"[錯誤] 今日匯報執行發生例外: {e}")
                _log(f"今日匯報執行發生例外: {e}")

        # 每 30 秒檢查一次
        time.sleep(30)


if __name__ == "__main__":
    run_scheduler()