import os
import subprocess
import tempfile
from pathlib import Path

from config import BASE_DIR, get_secure_env


def _run_git(args: list[str]) -> tuple[int, str]:
    """執行 git 指令並回傳 (returncode, 合併輸出)。使用 subprocess 避免 shell 注入。"""
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(BASE_DIR),
    )
    return result.returncode, (result.stdout + result.stderr).strip()


def _mask(text: str, token: str) -> str:
    """將輸出中的 token 遮蔽，避免洩漏至終端/日誌"""
    if token and text:
        text = text.replace(token, "***")
    return text


def _safe_rel_files(files: list[Path]) -> list[str]:
    rel_files: list[str] = []
    base = BASE_DIR.resolve()
    for p in files:
        rp = Path(p).resolve()
        try:
            rel = rp.relative_to(base)
        except Exception as exc:
            raise ValueError(f"拒絕推送 base 外檔案: {p}") from exc
        rel_str = str(rel).replace("\\", "/")
        if rel_str.startswith(".git/") or rel_str.startswith(".system_generated/"):
            raise ValueError(f"拒絕推送受保護路徑: {rel_str}")
        if rel_str in {".env", ".env.local"} or rel_str.endswith(".env"):
            raise ValueError(f"拒絕推送敏感檔案: {rel_str}")
        rel_files.append(str(rel))
    # dedupe, preserve order
    seen = set()
    out = []
    for r in rel_files:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out


def push_to_github(files: list[Path], commit_message: str) -> bool:
    """
    將指定檔案 commit 並推送到 GitHub（僅限 BASE_DIR 內安全路徑）。

    認證策略（從最安全到備援）：
    1. 優先使用本機 Git Credential Manager 直接 git push（憑證不在程式碼中）
    2. 若失敗且系統環境變數/登錄檔有 GITHUB_TOKEN，建立暫存 credential helper 重試，
       用完立即刪除暫存檔（token 不會出現在程式碼、設定檔或指令列）
    """
    try:
        rel_files = _safe_rel_files(files)
    except Exception as exc:
        print(f"[GitPush] ❌ 路徑安全檢查失敗：{exc}")
        return False

    if not rel_files:
        print("[GitPush] ℹ️ 沒有可推送檔案。")
        return True

    # 1. 暫存指定檔案
    code, output = _run_git(["add", "--"] + rel_files)
    if code != 0:
        print(f"[GitPush] ❌ git add 失敗：\n{output}")
        return False

    # 2. 僅當指定檔案有實際變更時才提交
    code, output = _run_git(["diff", "--cached", "--name-only", "--"] + rel_files)
    if code != 0 or not output:
        print("[GitPush] ℹ️ 指定檔案沒有實際新增或變更，跳過推送。")
        return True

    # 3. 提交（僅包含暫存的指定檔案）
    code, output = _run_git(["commit", "-m", commit_message])
    if code != 0:
        print(f"[GitPush] ❌ git commit 失敗：\n{output}")
        return False

    # 4. 推送（優先使用 Git Credential Manager）
    code, output = _run_git(["push", "origin", "HEAD:main"])
    if code == 0:
        print("[GitPush] ✅ 已自動推送到 GitHub。")
        return True

    token = get_secure_env("GITHUB_TOKEN")
    if not token:
        print(f"[GitPush] ❌ 推送失敗，且未找到 GITHUB_TOKEN 可重試：\n{output}")
        return False

    # 5. 備援：使用暫存 credential helper 重試
    helper_path = Path(tempfile.gettempdir()) / "git-cred-ai-agent.cmd"
    try:
        helper_path.write_text(
            "@echo off\r\necho username=x-access-token\r\necho password={}\r\n".format(token),
            encoding="utf-8",
        )
        helper_arg = str(helper_path).replace("\\", "/")
        code, output = _run_git(
            ["-c", f"credential.helper={helper_arg}", "push", "origin", "HEAD:main"]
        )
        if code == 0:
            print("[GitPush] ✅ 已透過 GITHUB_TOKEN 自動推送到 GitHub。")
            return True
        print(f"[GitPush] ❌ 推送失敗：\n{_mask(output, token)}")
        return False
    finally:
        try:
            helper_path.unlink(missing_ok=True)
        except OSError:
            pass