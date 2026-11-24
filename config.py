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


def parse_api_keys(multi: str = "", single: str = "", numbered: list[str] | None = None) -> list[str]:
    """解析多組 API key（支援逗號分隔、單一 key、編號 key），去重並保留順序。"""
    raw: list[str] = []
    if multi:
        raw.extend(multi.split(","))
    if single:
        raw.append(single)
    if numbered:
        raw.extend(numbered)

    keys: list[str] = []
    seen: set[str] = set()
    for item in raw:
        key = (item or "").strip()
        if key and key not in seen:
            seen.add(key)
            keys.append(key)
    return keys


# API Keys 與設定 (統一由系統環境變數讀取，程式碼中不包含任何金鑰)
IAI_BASE_URL = get_secure_env("IAI_BASE_URL", "https://www.iai.nkust.edu.tw/aihub/v1").rstrip("/")

# 多模型設定（Furen-max 主力、Furen-large 輔助、Furen-coder 工程、Pic-large 生圖）
IAI_MODEL_MAX = get_secure_env("IAI_MODEL_MAX", "Furen-max")
IAI_MODEL_LARGE = get_secure_env("IAI_MODEL_LARGE", "Furen-large")
IAI_MODEL_CODER = get_secure_env("IAI_MODEL_CODER", "Furen-coder")
IAI_MODEL_IMAGE = get_secure_env("IAI_MODEL_IMAGE", "Pic-large")

# 舊版單一模型設定（保留相容）
IAI_MODEL = get_secure_env("IAI_MODEL", IAI_MODEL_LARGE)

# 金鑰池（支援 IAI_API_KEYS=a,b,c,d 或 IAI_API_KEY / IAI_API_KEY_1..4）
# 若已設定 IAI_API_KEYS，則忽略舊版單一 IAI_API_KEY，避免混入失效金鑰。
_MULTI_KEYS = parse_api_keys(get_secure_env("IAI_API_KEYS", ""))
IAI_API_KEYS = _MULTI_KEYS or parse_api_keys(
    "",
    get_secure_env("IAI_API_KEY", ""),
    [get_secure_env(f"IAI_API_KEY_{i}", "") for i in range(1, 5)],
)
# 相容舊版單一 key
IAI_API_KEY = IAI_API_KEYS[0] if IAI_API_KEYS else get_secure_env("IAI_API_KEY", "")

# 併發與重試（控制多模型同時協作）
IAI_MAX_CONCURRENCY = int(get_secure_env("IAI_MAX_CONCURRENCY", "6"))
IAI_PER_KEY_CONCURRENCY = int(get_secure_env("IAI_PER_KEY_CONCURRENCY", "2"))
IAI_TIMEOUT = int(get_secure_env("IAI_TIMEOUT", "120"))
IAI_MAX_RETRIES = int(get_secure_env("IAI_MAX_RETRIES", "3"))

# 時效窗（天）
NEWS_MAX_AGE_DAYS = int(get_secure_env("NEWS_MAX_AGE_DAYS", "14"))
PAPER_MAX_AGE_DAYS = int(get_secure_env("PAPER_MAX_AGE_DAYS", "30"))
REPO_MAX_AGE_DAYS = int(get_secure_env("REPO_MAX_AGE_DAYS", "30"))
# Backfill 模式：允許放寬時效窗（僅用於明確 backfill，manifest 會標註 stale_backfill）
ALLOW_STALE_BACKFILL = get_secure_env("ALLOW_STALE_BACKFILL", "false").lower() in {"1", "true", "yes"}
BACKFILL_MAX_AGE_DAYS = int(get_secure_env("BACKFILL_MAX_AGE_DAYS", "3650"))

# 每日產出量
DAILY_NEWS_COUNT = 10
DAILY_PAPER_COUNT = 5
DAILY_REPO_COUNT = 5
DAILY_DIGEST_FOLDER_NAME = "每日匯報"

GOOGLE_CSE_API_KEY = get_secure_env("GOOGLE_CSE_API_KEY", "")
GOOGLE_CSE_CX = get_secure_env("GOOGLE_CSE_CX", "")
GITHUB_TOKEN = get_secure_env("GITHUB_TOKEN", "")
SEMANTIC_SCHOLAR_API_KEY = get_secure_env("SEMANTIC_SCHOLAR_API_KEY", "")
MAILTO_CONTACT = "daily_agent@nkust.edu.tw"

# 每日匯報目錄名稱（新輸出結構）
DAILY_SUMMARY_FOLDER_NAME = "每日匯報"

# ===== P2：新聞蒐集設定 =====
NEWS_HTTP_TIMEOUT = int(get_secure_env("NEWS_HTTP_TIMEOUT", "20"))
NEWS_MAX_BYTES = int(get_secure_env("NEWS_MAX_BYTES", str(5 * 1024 * 1024)))
NEWS_MAX_PER_SOURCE = int(get_secure_env("NEWS_MAX_PER_SOURCE", "3"))
NEWS_MAX_PER_DOMAIN = int(get_secure_env("NEWS_MAX_PER_DOMAIN", "4"))
NEWS_ROBOTS_CHECK = get_secure_env("NEWS_ROBOTS_CHECK", "true").lower() in {"1", "true", "yes"}
NEWS_BING_ENABLED = get_secure_env("NEWS_BING_ENABLED", "true").lower() in {"1", "true", "yes"}
NEWS_USER_AGENT = get_secure_env(
    "NEWS_USER_AGENT",
    "DailyAIReportBot/2.0 (+https://github.com/ethanworkspace/daily_news_paper_tool)",
)

# 聚合搜尋查詢（Bing News RSS；遵守 robots.txt）
# 注意：Bing News RSS 不支援 OR 語法（會回傳 0 筆），因此每個概念拆成獨立查詢。
NEWS_QUERIES = [
    {"query": "人工智慧", "lang": "zh-tw", "cc": "TW", "hint": "general"},
    {"query": "大語言模型", "lang": "zh-tw", "cc": "TW", "hint": "general"},
    {"query": "生成式 AI", "lang": "zh-tw", "cc": "TW", "hint": "general"},
    {"query": "機器學習", "lang": "zh-tw", "cc": "TW", "hint": "general"},
    {"query": "海事 AI", "lang": "zh-tw", "cc": "TW", "hint": "maritime"},
    {"query": "智慧航運", "lang": "zh-tw", "cc": "TW", "hint": "maritime"},
    {"query": "船舶 AI", "lang": "zh-tw", "cc": "TW", "hint": "maritime"},
    {"query": "醫療 AI", "lang": "zh-tw", "cc": "TW", "hint": "medical"},
    {"query": "智慧醫療", "lang": "zh-tw", "cc": "TW", "hint": "medical"},
    {"query": "AI 資安", "lang": "zh-tw", "cc": "TW", "hint": "cybersecurity"},
    {"query": "資訊安全 AI", "lang": "zh-tw", "cc": "TW", "hint": "cybersecurity"},
    {"query": "具身智慧", "lang": "zh-tw", "cc": "TW", "hint": "robotics"},
    {"query": "人形機器人", "lang": "zh-tw", "cc": "TW", "hint": "robotics"},
    {"query": "AI 晶片", "lang": "zh-tw", "cc": "TW", "hint": "electronics"},
    {"query": "半導體 AI", "lang": "zh-tw", "cc": "TW", "hint": "electronics"},
    {"query": "artificial intelligence", "lang": "en-us", "cc": "US", "hint": "general"},
    {"query": "large language model", "lang": "en-us", "cc": "US", "hint": "general"},
    {"query": "maritime AI", "lang": "en-us", "cc": "US", "hint": "maritime"},
    {"query": "autonomous vessel", "lang": "en-us", "cc": "US", "hint": "maritime"},
    {"query": "shipping AI", "lang": "en-us", "cc": "US", "hint": "maritime"},
    {"query": "medical AI", "lang": "en-us", "cc": "US", "hint": "medical"},
    {"query": "healthcare AI", "lang": "en-us", "cc": "US", "hint": "medical"},
    {"query": "AI cybersecurity", "lang": "en-us", "cc": "US", "hint": "cybersecurity"},
    {"query": "AI security", "lang": "en-us", "cc": "US", "hint": "cybersecurity"},
    {"query": "humanoid robot", "lang": "en-us", "cc": "US", "hint": "robotics"},
    {"query": "embodied AI", "lang": "en-us", "cc": "US", "hint": "robotics"},
    {"query": "AI chip", "lang": "en-us", "cc": "US", "hint": "electronics"},
    {"query": "semiconductor AI", "lang": "en-us", "cc": "US", "hint": "electronics"},
]

# 直接訂閱的國內外媒體 RSS（來源可插拔；失敗不影響其他來源）
NEWS_FEEDS = [
    {"name": "TechCrunch AI", "url": "https://techcrunch.com/category/artificial-intelligence/feed/", "lang": "en", "country": "US", "hint": "general"},
    {"name": "VentureBeat AI", "url": "https://venturebeat.com/category/ai/feed/", "lang": "en", "country": "US", "hint": "general"},
    {"name": "MIT Technology Review", "url": "https://www.technologyreview.com/topic/artificial-intelligence/feed", "lang": "en", "country": "US", "hint": "general"},
    {"name": "Ars Technica", "url": "https://feeds.arstechnica.com/arstechnica/index", "lang": "en", "country": "US", "hint": "general"},
    {"name": "IEEE Spectrum AI", "url": "https://spectrum.ieee.org/feeds/topic/artificial-intelligence.rss", "lang": "en", "country": "US", "hint": "general"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "lang": "en", "country": "US", "hint": "cybersecurity"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "lang": "en", "country": "US", "hint": "cybersecurity"},
    {"name": "SecurityWeek", "url": "https://www.securityweek.com/feed/", "lang": "en", "country": "US", "hint": "cybersecurity"},
    {"name": "Healthcare IT News", "url": "https://www.healthcareitnews.com/rss.xml", "lang": "en", "country": "US", "hint": "medical"},
    {"name": "Fierce Healthcare", "url": "https://www.fiercehealthcare.com/rss/xml", "lang": "en", "country": "US", "hint": "medical"},
    {"name": "The Maritime Executive", "url": "https://www.maritime-executive.com/rss", "lang": "en", "country": "US", "hint": "maritime"},
    {"name": "gCaptain", "url": "https://gcaptain.com/feed/", "lang": "en", "country": "US", "hint": "maritime"},
    {"name": "Splash247", "url": "https://splash247.com/feed/", "lang": "en", "country": "SG", "hint": "maritime"},
    {"name": "EE Times", "url": "https://www.eetimes.com/feed/", "lang": "en", "country": "US", "hint": "electronics"},
    {"name": "The Robot Report", "url": "https://www.therobotreport.com/feed/", "lang": "en", "country": "US", "hint": "robotics"},
    {"name": "IEEE Spectrum Robotics", "url": "https://spectrum.ieee.org/feeds/topic/robotics.rss", "lang": "en", "country": "US", "hint": "robotics"},
]

# 7天主題定義 (0: 禮拜一, 1: 禮拜二, ..., 6: 禮拜日)
# keywords: 對題關鍵字（小寫），用於嚴格過濾論文/專案，確保當日資料符合主題
TOPICS = {
    0: {
        "id": 1,
        "name": "LLM、RAG、Fine tune",
        "folder": "1",
        "weekday_name": "禮拜一",
        "news_query": "LLM OR RAG OR Fine-tuning 大語言模型",
        "arxiv_query": "cat:cs.CL",
        "github_query": "LLM RAG fine-tuning in:name,description,topics stars:>100",
        "scholar_query": "LLM RAG fine-tuning large language model",
        "keywords": ["llm", "rag", "large language model", "fine-tun", "retrieval-augmented", "prompt", "language model"],
    },
    1: {
        "id": 2,
        "name": "機器學習、AI資訊安全",
        "folder": "2",
        "weekday_name": "禮拜二",
        "news_query": "\"機器學習\" OR \"Machine Learning\" OR AI資訊安全 OR 資安 OR \"AI Security\"",
        "arxiv_query": "(cat:cs.LG OR cat:cs.CR)",
        "github_query": "machine-learning security in:name,description,topics stars:>100",
        "scholar_query": "machine learning AI security intrusion detection",
        "keywords": ["machine learning", "neural", "security", "cybersecurity", "intrusion", "malware", "vulnerab", "anomaly", "adversarial", "information security", "encryption", "ai security"],
    },
    2: {
        "id": 3,
        "name": "深度學習",
        "folder": "3",
        "weekday_name": "禮拜三",
        "news_query": "深度學習 OR \"Deep Learning\" 神經網路",
        "arxiv_query": "cat:cs.CV OR cat:cs.NE",
        "github_query": "deep-learning in:name,description,topics stars:>100",
        "scholar_query": "deep learning neural network",
        "keywords": ["deep learning", "neural network", "cnn", "transformer", "vision", "reinforcement", "self-supervised", "diffusion", "语言模型", "language model"],
    },
    3: {
        "id": 4,
        "name": "ai agent",
        "folder": "4",
        "weekday_name": "禮拜四",
        "news_query": "\"AI Agent\" OR \"AI代理\" OR \"智慧代理\" OR \"autonomous agent\"",
        "arxiv_query": "cat:cs.AI AND (ti:agent OR ti:autonomous OR abs:agent)",
        "github_query": "AI-agent OR autonomous-agent in:name,description,topics stars:>100",
        "scholar_query": "AI agent autonomous multi-agent",
        "keywords": ["agent", "autonomous", "multi-agent", "tool use", "planning", "agentic"],
    },
    4: {
        "id": 5,
        "name": "智慧機器人",
        "folder": "5",
        "weekday_name": "禮拜五",
        "news_query": "智慧機器人 OR 具身智能 OR \"Embodied AI\" OR \"Robotics\"",
        "arxiv_query": "cat:cs.RO",
        "github_query": "robotics OR embodied-ai in:name,description,topics stars:>50",
        "scholar_query": "embodied AI robotics",
        "keywords": ["robot", "robotics", "embodied", "manipulation", "navigation", "drone", "autonomous", "grasp"],
    },
    5: {
        "id": 6,
        "name": "AI硬體應用、AI自動化",
        "folder": "6",
        "weekday_name": "禮拜六",
        "news_query": "\"AI晶片\" OR \"AI硬體\" OR \"AI自動化\" OR \"NPU\" OR \"GPU AI\"",
        "arxiv_query": "cat:cs.AR",
        "github_query": "AI-hardware OR edge-ai OR automation in:name,description,topics stars:>50",
        "scholar_query": "AI hardware chip NPU accelerator",
        "keywords": ["gpu", "npu", "asic", "chip", "accelerator", "edge", "quantization", "inference", "fpga", "hardware"],
    },
    6: {
        "id": 7,
        "name": "海事AI、醫療AI",
        "folder": "7",
        "weekday_name": "禮拜日",
        "news_query": "海事AI OR 智慧航運 OR \"Maritime AI\" OR \"Medical AI\" OR 醫療AI OR 智慧醫療",
        "arxiv_query": "(abs:maritime OR abs:shipping OR abs:medical OR abs:health) AND (cat:cs.AI OR cat:eess.SP OR cat:q-bio.BM OR cat:q-bio.QM)",
        "github_query": "maritime OR shipping OR medical OR healthcare OR medical-ai in:name,description,topics stars:>50",
        "scholar_query": "maritime AI medical AI healthcare",
        "keywords": ["maritime", "shipping", "vessel", "nautical", "port", "ocean", "medical", "health", "clinical", "radiology", "patient", "hospital", "diagnos", "biomed", "imaging", "海事", "醫療"],
    },
}

# ===== P3：論文蒐集設定 =====
PAPER_HTTP_TIMEOUT = int(get_secure_env("PAPER_HTTP_TIMEOUT", "25"))
PAPER_MAX_BYTES = int(get_secure_env("PAPER_MAX_BYTES", str(20 * 1024 * 1024)))
PAPER_ROBOTS_CHECK = get_secure_env("PAPER_ROBOTS_CHECK", "true").lower() in {"1", "true", "yes"}
PAPER_MAX_PER_SOURCE = int(get_secure_env("PAPER_MAX_PER_SOURCE", "3"))
PAPER_MIN_PAIRED = int(get_secure_env("PAPER_MIN_PAIRED", "3"))  # 目標值，來源不足時記錄 warning
PAPER_FULLTEXT_MAX_CHARS = int(get_secure_env("PAPER_FULLTEXT_MAX_CHARS", "300000"))  # 預設保留完整論文文字，不限頁數

# OCR / 字型解析（掃描型 PDF 補救；缺少套件時自動停用）
PAPER_OCR_ENABLED = get_secure_env("PAPER_OCR_ENABLED", "true").lower() in {"1", "true", "yes"}
PAPER_OCR_MAX_PAGES = int(get_secure_env("PAPER_OCR_MAX_PAGES", "120"))  # 0 = 不限頁數
PAPER_OCR_MAX_SECONDS = float(get_secure_env("PAPER_OCR_MAX_SECONDS", "600"))
PAPER_OCR_DPI = int(get_secure_env("PAPER_OCR_DPI", "200"))
PAPER_OCR_MIN_CHARS = int(get_secure_env("PAPER_OCR_MIN_CHARS", "40"))  # 每頁文字低於此值視為掃描頁

# 查詢詞（可擴充）；hint 對應領域偏好，實際仍以內容判斷
PAPER_QUERIES = [
    {"query": "large language model", "hint": "general"},
    {"query": "multimodal foundation model", "hint": "general"},
    {"query": "AI agent reasoning", "hint": "general"},
    {"query": "maritime AI autonomous vessel", "hint": "maritime"},
    {"query": "shipping port artificial intelligence", "hint": "maritime"},
    {"query": "medical AI clinical diagnosis", "hint": "medical"},
    {"query": "healthcare machine learning", "hint": "medical"},
    {"query": "cybersecurity machine learning intrusion detection", "hint": "cybersecurity"},
    {"query": "embodied AI humanoid robot", "hint": "robotics"},
    {"query": "edge AI semiconductor chip", "hint": "electronics"},
]

# 來源優先層級（1=頂級期刊/會議，2=重要OA/會議，3=預印本）
TIER1_VENUES = (
    "nature", "science", "cell", "lancet", "jama", "nejm",
    "neurips", "nips", "iclr", "icml", "aaai", "cvpr", "iccv", "eccv", "acl", "emnlp", "naacl",
    "siggraph", "kdd", "www", "icra", "iros", "rss", "ijcai",
    "ieee transactions", "acm transactions",
)
TIER2_VENUES = (
    "plos", "science advances", "scientific reports", "jmir", "frontiers",
    "bioinformatics", "jmlr", "pmlr", "openreview", "tmlr", "aistats", "uai", "coling",
)

# ===== P4：GitHub 專案蒐集設定 =====
REPO_HTTP_TIMEOUT = int(get_secure_env("REPO_HTTP_TIMEOUT", "25"))
REPO_MAX_BYTES = int(get_secure_env("REPO_MAX_BYTES", str(6 * 1024 * 1024)))
REPO_ROBOTS_CHECK = get_secure_env("REPO_ROBOTS_CHECK", "true").lower() in {"1", "true", "yes"}
REPO_MAX_PER_SOURCE = int(get_secure_env("REPO_MAX_PER_SOURCE", "2"))
REPO_MIN_PAIRED = int(get_secure_env("REPO_MIN_PAIRED", "3"))  # 目標值，來源不足時記錄 warning
REPO_MIN_QUALITY_SCORE = int(get_secure_env("REPO_MIN_QUALITY_SCORE", "2"))  # 0–10，低於此值視為低訊號
REPO_ENRICH_LIMIT = int(get_secure_env("REPO_ENRICH_LIMIT", "24"))  # 最多深入抓取幾個 README
REPO_EXCLUDE_COLLECTIONS = get_secure_env("REPO_EXCLUDE_COLLECTIONS", "true").lower() in {"1", "true", "yes"}

REPO_QUERIES = [
    {"query": "large language model OR llm agent", "hint": "general", "min_stars": 50},
    {"query": "multimodal AI OR vision language model", "hint": "general", "min_stars": 50},
    {"query": "maritime AI OR autonomous vessel", "hint": "maritime", "min_stars": 10},
    {"query": "medical AI OR healthcare machine learning", "hint": "medical", "min_stars": 20},
    {"query": "cybersecurity AI OR intrusion detection machine learning", "hint": "cybersecurity", "min_stars": 30},
    {"query": "embodied AI OR humanoid robot learning", "hint": "robotics", "min_stars": 30},
    {"query": "edge AI chip OR NPU inference", "hint": "electronics", "min_stars": 20},
]
