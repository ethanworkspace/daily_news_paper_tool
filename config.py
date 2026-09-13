import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# 專案根目錄
BASE_DIR = Path(__file__).resolve().parent

# 嘗試載入 .env (若有)
load_dotenv(BASE_DIR / ".env")


def get_secure_env(key: str, default: str = "") -> str:
    """
    安全獲取環境變數：
    1. 優先從 os.environ 讀取
    2. 若未設定且在 Windows 系統，直接讀取使用者登錄檔 (避免金鑰出現在任何檔案中)
    """
    val = os.getenv(key)
    if val:
        return val

    if sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as reg_key:
                reg_val, _ = winreg.QueryValueEx(reg_key, key)
                if reg_val:
                    return str(reg_val)
        except Exception:
            pass

    return default


# API Keys 與設定 (統一由系統環境變數讀取，程式碼中不包含任何金鑰)
IAI_API_KEY = get_secure_env("IAI_API_KEY", "")
IAI_BASE_URL = get_secure_env("IAI_BASE_URL", "https://www.iai.nkust.edu.tw/aihub/v1").rstrip("/")
IAI_MODEL = get_secure_env("IAI_MODEL", "Furen-large")

GOOGLE_CSE_API_KEY = get_secure_env("GOOGLE_CSE_API_KEY", "")
GOOGLE_CSE_CX = get_secure_env("GOOGLE_CSE_CX", "")
GITHUB_TOKEN = get_secure_env("GITHUB_TOKEN", "")
SEMANTIC_SCHOLAR_API_KEY = get_secure_env("SEMANTIC_SCHOLAR_API_KEY", "")
MAILTO_CONTACT = "daily_agent@nkust.edu.tw"

# 每日新聞總結目錄名稱
DAILY_SUMMARY_FOLDER_NAME = "8.每日新聞總結"

# 7天主題定義 (0: 禮拜一, 1: 禮拜二, ..., 6: 禮拜日)
TOPICS = {
    0: {
        "id": 1,
        "name": "LLM、RAG、Fine tune",
        "folder": "1.LLM、RAG、Fine tune",
        "weekday_name": "禮拜一",
        "news_query": "LLM OR RAG OR Fine-tuning 大語言模型",
        "arxiv_query": "cat:cs.CL",
        "github_query": "LLM RAG fine-tuning in:name,description,topics stars:>100",
        "scholar_query": "LLM RAG fine-tuning large language model",
    },
    1: {
        "id": 2,
        "name": "機器學習",
        "folder": "2.機器學習",
        "weekday_name": "禮拜二",
        "news_query": "機器學習 OR \"Machine Learning\" AI 演算法",
        "arxiv_query": "cat:cs.LG",
        "github_query": "machine-learning in:name,description,topics stars:>100",
        "scholar_query": "machine learning algorithm",
    },
    2: {
        "id": 3,
        "name": "深度學習",
        "folder": "3.深度學習",
        "weekday_name": "禮拜三",
        "news_query": "深度學習 OR \"Deep Learning\" 神經網路",
        "arxiv_query": "cat:cs.CV OR cat:cs.NE",
        "github_query": "deep-learning in:name,description,topics stars:>100",
        "scholar_query": "deep learning neural network",
    },
    3: {
        "id": 4,
        "name": "ai agent",
        "folder": "4.ai agent",
        "weekday_name": "禮拜四",
        "news_query": "\"AI Agent\" OR \"AI代理\" OR \"智慧代理\" OR \"autonomous agent\"",
        "arxiv_query": "cat:cs.AI AND (ti:agent OR ti:autonomous OR abs:agent)",
        "github_query": "AI-agent OR autonomous-agent in:name,description,topics stars:>100",
        "scholar_query": "AI agent autonomous multi-agent",
    },
    4: {
        "id": 5,
        "name": "智慧機器人",
        "folder": "5.智慧機器人",
        "weekday_name": "禮拜五",
        "news_query": "智慧機器人 OR 具身智能 OR \"Embodied AI\" OR \"Robotics\"",
        "arxiv_query": "cat:cs.RO",
        "github_query": "robotics OR embodied-ai in:name,description,topics stars:>50",
        "scholar_query": "embodied AI robotics",
    },
    5: {
        "id": 6,
        "name": "AI硬體應用、AI自動化",
        "folder": "6.AI硬體應用、AI自動化",
        "weekday_name": "禮拜六",
        "news_query": "\"AI晶片\" OR \"AI硬體\" OR \"AI自動化\" OR \"NPU\" OR \"GPU AI\"",
        "arxiv_query": "cat:cs.AR",
        "github_query": "AI-hardware OR edge-ai OR automation in:name,description,topics stars:>50",
        "scholar_query": "AI hardware chip NPU accelerator",
    },
    6: {
        "id": 7,
        "name": "海事AI、醫療AI",
        "folder": "7.海事AI、醫療AI",
        "weekday_name": "禮拜日",
        "news_query": "海事AI OR 智慧航運 OR \"Maritime AI\" OR \"Medical AI\" OR 醫療AI OR 智慧醫療",
        "arxiv_query": "(abs:maritime OR abs:shipping OR abs:medical OR abs:health) AND (cat:cs.AI OR cat:eess.SP OR cat:q-bio.BM OR cat:q-bio.QM)",
        "github_query": "maritime OR shipping OR medical OR healthcare OR medical-ai in:name,description,topics stars:>50",
        "scholar_query": "maritime AI medical AI healthcare",
    },
}
