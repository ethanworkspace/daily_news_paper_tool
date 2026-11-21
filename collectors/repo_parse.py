"""GitHub 專案內容解析：README 萃取、論文連結偵測、技術/架構段落啟發式整理。"""
from __future__ import annotations

import base64
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from collectors.news_parse import strip_html
from collectors.paper_parse import extract_doi, extract_github_urls, first_github_url
from core.dedupe import extract_arxiv_id, normalize_doi
from core.timewin import parse_datetime

ARXIV_ABS_RE = re.compile(
    r"https?://arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?|[a-z\-]+(?:\.[A-Z]{2})?/\d{7}(?:v\d+)?)",
    re.IGNORECASE,
)
DOI_URL_RE = re.compile(r"https?://(?:dx\.)?doi\.org/(10\.\d{4,9}/[-._;()/:A-Z0-9]+)", re.IGNORECASE)
BARE_ARXIV_RE = re.compile(r"\b(?:arxiv\s*[:=]?\s*)?([0-9]{4}\.[0-9]{4,5})(?:v\d+)?\b", re.IGNORECASE)
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")
CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


@dataclass
class RepoCandidate:
    full_name: str
    html_url: str
    description: str = ""
    stars: int = 0
    forks: int = 0
    language: str = ""
    license_name: str = ""
    topics: list[str] = field(default_factory=list)
    updated_at: datetime | None = None
    created_at: datetime | None = None
    pushed_at: datetime | None = None
    homepage: str = ""
    default_branch: str = ""
    readme_text: str = ""
    readme_excerpt: str = ""
    paper_urls: list[str] = field(default_factory=list)
    paper_url: str = ""
    paired_paper: str = ""
    quality_score: int = 0
    quality_flags: list[str] = field(default_factory=list)
    sections: dict[str, str] = field(default_factory=dict)
    extra: dict[str, Any] = field(default_factory=dict)


def clean_readme(text: object, max_length: int = 20000) -> str:
    if not text:
        return ""
    raw = str(text).replace("\r\n", "\n").replace("\r", "\n")
    raw = CODE_FENCE_RE.sub("\n[code block omitted]\n", raw)
    raw = MD_IMAGE_RE.sub(" ", raw)
    raw = MD_LINK_RE.sub(r"\1 (\2)", raw)
    raw = HTML_TAG_RE.sub(" ", raw)
    raw = CONTROL_CHARS.sub(" ", raw)
    # keep headings/lists readable
    lines = []
    for line in raw.split("\n"):
        line = re.sub(r"[ \t]+", " ", line).strip()
        line = re.sub(r"^\s*[#>*\-+]+\s*", lambda m: m.group(0).strip() + " ", line)
        if line:
            lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text[:max_length]


def extract_paper_urls(text: object) -> list[str]:
    if not text:
        return []
    raw = str(text)
    urls: list[str] = []
    seen: set[str] = set()

    for m in ARXIV_ABS_RE.finditer(raw):
        arxiv_id = extract_arxiv_id(m.group(1))
        if not arxiv_id:
            continue
        url = f"https://arxiv.org/abs/{arxiv_id}"
        if url not in seen:
            seen.add(url)
            urls.append(url)
    for m in BARE_ARXIV_RE.finditer(raw):
        arxiv_id = extract_arxiv_id(m.group(1))
        if not arxiv_id:
            continue
        url = f"https://arxiv.org/abs/{arxiv_id}"
        if url not in seen:
            seen.add(url)
            urls.append(url)

    for m in DOI_URL_RE.finditer(raw):
        doi = normalize_doi(m.group(1))
        if not doi:
            continue
        url = f"https://doi.org/{doi}"
        key = url.lower()
        if key not in seen:
            seen.add(key)
            urls.append(url)

    # bare DOI
    for m in re.finditer(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", raw, re.IGNORECASE):
        doi = normalize_doi(m.group(0))
        if not doi:
            continue
        url = f"https://doi.org/{doi}"
        key = url.lower()
        if key not in seen:
            seen.add(key)
            urls.append(url)

    return urls[:20]


def _first_paragraph(text: str, max_len: int = 500) -> str:
    for block in re.split(r"\n{2,}", text):
        block = block.strip()
        if len(block) < 30:
            continue
        if block.lower().startswith(("[code block omitted]", "http")):
            continue
        return block[:max_len]
    return text[:max_len].strip()


def _section_extract(text: str, keywords: tuple[str, ...], max_len: int = 1200) -> str:
    lines = text.splitlines()
    capture = False
    buf: list[str] = []
    for line in lines:
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            title = heading.group(2).strip().lower()
            if capture:
                break
            if any(k in title for k in keywords):
                capture = True
                continue
        elif capture:
            # stop on obvious separator-like short all-caps markers
            if line.strip().startswith("# "):
                break
        if capture and line.strip():
            buf.append(line.strip())
            if sum(len(x) for x in buf) >= max_len:
                break
    if not buf:
        # fallback: pick lines containing keywords
        for line in lines:
            low = line.lower()
            if any(k in low for k in keywords):
                buf.append(line.strip())
                if sum(len(x) for x in buf) >= max_len:
                    break
    return "\n".join(buf)[:max_len].strip()


def build_repo_sections(candidate: RepoCandidate) -> dict[str, str]:
    text = candidate.readme_excerpt or clean_readme(candidate.readme_text)
    desc = (candidate.description or "").strip()
    topics = ", ".join(candidate.topics[:8])
    meta = []
    if candidate.language:
        meta.append(f"主要語言：{candidate.language}")
    if topics:
        meta.append(f"Topics：{topics}")
    if candidate.stars:
        meta.append(f"Stars：{candidate.stars}")
    if candidate.license_name:
        meta.append(f"License：{candidate.license_name}")
    meta_line = "；".join(meta)

    overview = _section_extract(text, ("overview", "introduction", "about", "what is", "summary", "簡介", "介紹", "專案"), 900)
    if not overview:
        overview = _first_paragraph(text, 700) or desc
    what = f"{desc}\n{overview}".strip()
    if meta_line:
        what = f"{what}\n\n{meta_line}".strip()

    tech = _section_extract(
        text,
        ("tech", "stack", "feature", "features", "installation", "usage", "quickstart", "getting started", "model", "method", "api", "技術", "功能", "安裝", "使用"),
        1200,
    )
    if not tech:
        hints = []
        if candidate.language:
            hints.append(f"實作語言以 {candidate.language} 為主。")
        if topics:
            hints.append(f"從 topics 可見技術方向：{topics}。")
        if desc:
            hints.append(f"專案描述：{desc}")
        tech = "\n".join(hints)

    arch = _section_extract(
        text,
        ("architecture", "design", "structure", "pipeline", "workflow", "module", "components", "system", "架構", "設計", "流程", "模組"),
        1200,
    )
    if not arch:
        # heuristic from headings
        headings = [m.group(1).strip() for m in re.finditer(r"^#{1,3}\s+(.*)$", text, re.MULTILINE)]
        if headings:
            arch = "README 主要結構：" + " → ".join(headings[:12])
        elif desc:
            arch = f"README 未明確提供架構章節；依描述推斷此專案聚焦於：{desc}"
        else:
            arch = "README 未明確提供架構章節，需後續由 LLM 根據程式與文件補充。"

    if candidate.paper_urls:
        arch = arch + "\n\n相關論文/文件：" + "\n".join(candidate.paper_urls[:5])

    return {
        "what": what[:4000].strip(),
        "tech": tech[:4000].strip(),
        "architecture": arch[:4000].strip(),
    }


# ===== 專案品質訊號：排除 Awesome／survey／paper list 等清單型專案 =====

_COLLECTION_NAME_TOKENS = {
    "awesome", "survey", "surveys", "papers", "paperlist", "curated",
    "collection", "collections", "roadmap", "cheatsheet", "cheatsheets",
    "tutorial", "tutorials", "course", "courses", "book", "books",
    "interview", "interviews",
}
_COLLECTION_PHRASES = (
    "awesome ",
    "curated list",
    "a list of",
    "list of ",
    "collection of",
    "reading list",
    "paper list",
    "papers list",
    "survey of",
    "survey on",
    "resources for",
    "learning path",
    "cheat sheet",
    "cheatsheet",
)
_IMPL_TOKENS = (
    "pip install",
    "pip3 install",
    "conda install",
    "npm install",
    "yarn add",
    "docker run",
    "docker compose",
    "python -m",
    "from ",
    "import ",
    "requirements.txt",
    "pyproject.toml",
    "setup.py",
    "package.json",
    "quickstart",
    "getting started",
    "installation",
    "install",
    "usage",
    "checkpoint",
    "inference",
    "training",
    "fine-tune",
    "fine tune",
    "src/",
    "pytorch",
    "tensorflow",
    "jax",
    "onnx",
    "cuda",
    "huggingface",
)
_CODE_TOPICS = {
    "pytorch", "tensorflow", "jax", "onnx", "cuda", "deep-learning",
    "machine-learning", "llm", "implementation", "library", "framework",
    "toolkit", "inference", "training", "computer-vision", "nlp",
}
_GITHUB_URL_RE = re.compile(
    r"https?://(?:www\.)?github\.com/([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+)",
    re.IGNORECASE,
)


@dataclass
class RepoQuality:
    score: int = 0
    collection: bool = False
    flags: list[str] = field(default_factory=list)
    impl_hits: list[str] = field(default_factory=list)
    readme_chars: int = 0


def _tokens(text: object) -> list[str]:
    return [part for part in re.split(r"[^a-z0-9]+", str(text or "").lower()) if part]


def github_repo_full_name(value: object) -> str:
    """從 GitHub URL 取出 owner/name；支援 /tree/... 與 .git 後綴。"""
    match = _GITHUB_URL_RE.search(str(value or ""))
    if not match:
        return ""
    owner, name = match.group(1), match.group(2)
    if name.lower().endswith(".git"):
        name = name[:-4]
    if name.lower() in {"tree", "blob", "issues", "pulls", "releases"}:
        return ""
    return f"{owner}/{name}"


def is_collection_repo_name(full_name: object) -> bool:
    """以專案名稱判斷是否為 Awesome／survey／paper list 等清單型專案。"""
    name = str(full_name or "").split("/")[-1].lower()
    tokens = set(_tokens(name))
    if not tokens:
        return False
    if tokens & _COLLECTION_NAME_TOKENS:
        return True
    if "list" in tokens and tokens & {
        "reading", "paper", "papers", "resource", "resources", "awesome", "curated", "collection",
    }:
        return True
    if tokens & {"resource", "resources"} and tokens & {
        "ai", "ml", "llm", "deep", "learning", "machine", "data",
    }:
        return True
    return bool(re.search(r"(?:^|[-_])paper[-_]?list(?:$|[-_])", name))


def evaluate_repo_quality(
    full_name: object,
    description: object = "",
    topics: list[str] | tuple[str, ...] | None = None,
    readme: object = "",
    language: object = "",
    stars: int = 0,
    *,
    paired: bool = False,
) -> RepoQuality:
    """以名稱／描述／topics／README 訊號評估專案實作含量（0–10）。"""
    topic_list = [str(t) for t in (topics or []) if str(t).strip()]
    readme_text = str(readme or "")
    readme_chars = len(" ".join(readme_text.split()))
    text = " ".join(
        [str(full_name or ""), str(description or ""), " ".join(topic_list), readme_text[:6000]]
    ).lower()
    impl_hits = [token for token in _IMPL_TOKENS if token in text]

    name_collection = is_collection_repo_name(full_name)
    head = f"{description or ''}\n{readme_text[:700]}".lower()
    phrase_collection = any(phrase in head for phrase in _COLLECTION_PHRASES)
    collection = name_collection or (phrase_collection and len(impl_hits) <= 1)

    lang = str(language or "").strip().lower()
    has_language = bool(lang) and lang not in {"unknown", "none"}
    topic_tokens: set[str] = set()
    for topic in topic_list:
        topic_tokens.update(_tokens(topic))
    code_topic = bool(topic_tokens & _CODE_TOPICS)

    score = 0
    if has_language:
        score += 2
    if code_topic:
        score += 1
    if len(impl_hits) >= 1:
        score += 1
    if len(impl_hits) >= 3:
        score += 1
    if len(impl_hits) >= 5:
        score += 1
    if readme_chars >= 400:
        score += 1
    if readme_chars >= 1200:
        score += 1
    if int(stars or 0) >= 100:
        score += 1
    if int(stars or 0) >= 1000:
        score += 1
    if paired:
        score += 2
    if collection:
        score -= 5
        if paired and len(impl_hits) >= 2 and readme_chars >= 400:
            # 論文配對且有實作訊號的 repo 即使名稱像 collection，也不應被過度懲罰到 0
            score = max(score, 3)
    if not has_language and not impl_hits:
        score -= 2
    if readme_chars < 150:
        score -= 1
    score = max(0, min(10, score))

    flags: list[str] = []
    if collection:
        flags.append("collection")
    if name_collection:
        flags.append("collection_name")
    if not has_language:
        flags.append("no_language")
    if readme_chars < 150:
        flags.append("thin_readme")
    if paired:
        flags.append("paper_paired")
    if len(impl_hits) >= 3:
        flags.append("implementation_signals")

    return RepoQuality(
        score=score,
        collection=collection,
        flags=flags,
        impl_hits=impl_hits[:12],
        readme_chars=readme_chars,
    )


def parse_github_repo_json(data: dict) -> RepoCandidate | None:
    if not isinstance(data, dict):
        return None
    full_name = str(data.get("full_name") or "").strip()
    html_url = str(data.get("html_url") or "").strip()
    if not full_name or not html_url:
        return None
    owner = data.get("owner") or {}
    license_obj = data.get("license") or {}
    topics = data.get("topics") or []
    if not isinstance(topics, list):
        topics = []
    return RepoCandidate(
        full_name=full_name,
        html_url=html_url,
        description=str(data.get("description") or "").strip(),
        stars=int(data.get("stargazers_count") or 0),
        forks=int(data.get("forks_count") or 0),
        language=str(data.get("language") or "").strip(),
        license_name=str((license_obj or {}).get("spdx_id") or (license_obj or {}).get("name") or "").strip(),
        topics=[str(t).strip() for t in topics if str(t).strip()][:20],
        updated_at=parse_datetime(data.get("updated_at") or data.get("pushed_at")),
        created_at=parse_datetime(data.get("created_at")),
        pushed_at=parse_datetime(data.get("pushed_at")),
        homepage=str(data.get("homepage") or "").strip(),
        default_branch=str(data.get("default_branch") or "main").strip(),
        extra={"owner": owner.get("login", ""), "archived": bool(data.get("archived", False))},
    )


def decode_readme_content(data: dict) -> str:
    if not isinstance(data, dict):
        return ""
    content = data.get("content") or ""
    encoding = (data.get("encoding") or "").lower()
    if not content:
        return ""
    if encoding == "base64":
        try:
            raw = base64.b64decode(content, validate=False)
            return raw.decode("utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            return ""
    return str(content)
