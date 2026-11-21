"""P5：新格式每日報告輸出（1-7/<date>/ + 每日匯報/）。"""
from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any

from core.models import DailyBundle
from core.paths import (
    assets_dir,
    atomic_write_text,
    digest_path,
    ensure_day_tree,
    news_path,
    paper_path,
    repo_path,
    slugify,
    tech_path,
)
from core.security import redact_secrets


def _dt(value: datetime | None) -> str:
    return value.isoformat() if value else ""


def _md_escape(text: object) -> str:
    return str(text or "").replace("\r", "").strip()


def _link(url: object) -> str:
    u = str(url or "").strip()
    return u if u.startswith("http://") or u.startswith("https://") else ""


def render_news_markdown(bundle: DailyBundle) -> str:
    lines = [f"# 每日 AI 新聞（10篇） - {bundle.date}", "", "> 來源以實際抓取內容為準；每則含摘要與影響。", ""]
    for i, item in enumerate(bundle.news, 1):
        lines += [
            f"## {i}. {item.title}",
            f"- 來源：{item.source or '未知'}",
            f"- 發布時間：{_dt(item.published_at)}",
            f"- URL：{_link(item.url)}",
            f"- 領域：{', '.join(item.domains)}{'（海事）' if item.is_maritime else ''}",
            f"- AI 焦點：{item.ai_focus or 'AI'}",
            "",
            "### 重點摘要",
            _md_escape(item.summary) or "（無摘要）",
            "",
            "### 影響",
            _md_escape(item.key_point) or "（待補充影響）",
            "",
        ]
    return "\n".join(lines).strip() + "\n"


def render_paper_markdown(item: Any, index: int, bundle_date: str) -> str:
    s = item.sections or {}
    return "\n".join([
        f"# 論文 {index:02d}：{item.title}",
        "",
        f"- 日期：{bundle_date}",
        f"- 來源層級：Tier {item.source_tier}",
        f"- 期刊/會議/來源：{item.journal or item.venue or item.source_name}",
        f"- Venue：{item.venue or item.journal or item.source_name}",
        f"- 發布時間：{_dt(item.published_at)}",
        f"- URL：{_link(item.url)}",
        f"- PDF：{_link(item.pdf_url)}",
        f"- DOI：{item.doi}",
        f"- arXiv：{item.arxiv_id}",
        f"- 影響指標：{item.impact_factor}",
        f"- 影響指標來源：{item.impact_factor_source}",
        f"- 引用數：{item.cited_by_count}",
        f"- 解析程度：{item.parse_level} / {item.fulltext_kind}",
        f"- 全文來源：{_link(item.fulltext_source)}",
        f"- 全文字數：{len(item.fulltext_excerpt or '')}（pages={item.fulltext_pages}, ocr_pages={item.ocr_pages}）",
        f"- GitHub/Code：{_link(item.code_url)}",
        f"- 配對 Repo：{item.paired_repo}",
        "",
        "## 摘要",
        _md_escape(item.abstract) or "（無摘要）",
        "",
        "## 背景與目的",
        _md_escape(s.get("background", "")) or "（待補充）",
        "",
        "## 方法",
        _md_escape(s.get("method", "")) or "（待補充）",
        "",
        "## 結果",
        _md_escape(s.get("results", "")) or "（待補充）",
        "",
        "## 限制與展望",
        _md_escape(s.get("limitations", "")) or "（待補充）",
        "",
    ]).strip() + "\n"


def render_repo_markdown(item: Any, index: int, bundle_date: str) -> str:
    s = item.sections or {}
    return "\n".join([
        f"# GitHub 專案 {index:02d}：{item.full_name}",
        "",
        f"- 日期：{bundle_date}",
        f"- URL：{_link(item.html_url)}",
        f"- 描述：{_md_escape(item.description)}",
        f"- Stars：{item.stars}  |  Forks：{item.forks}  |  Language：{item.language or 'unknown'}",
        f"- License：{item.license_name}",
        f"- Topics：{', '.join(item.topics)}",
        f"- 更新時間：{_dt(item.updated_at)}",
        f"- 配對論文：{_link(item.paper_url) or item.paired_paper}",
        f"- 品質分數：{item.quality_score}/10 {'[' + ', '.join(item.quality_flags) + ']' if item.quality_flags else ''}",
        "",
        "## 在做什麼",
        _md_escape(s.get("what", "")) or "（待補充）",
        "",
        "## 技術",
        _md_escape(s.get("tech", "")) or "（待補充）",
        "",
        "## 架構",
        _md_escape(s.get("architecture", "")) or "（待補充）",
        "",
        "## README 摘錄（節選）",
        "```text",
        _md_escape((item.readme_excerpt or "")[:4000]),
        "```",
        "",
    ]).strip() + "\n"


def render_tech_markdown(tech: Any, bundle: DailyBundle) -> str:
    return "\n".join([
        f"# AI 技術架構深度拆解：{tech.name}",
        "",
        f"- 日期：{bundle.date}",
        f"- 選題理由：{_md_escape(tech.rationale)}",
        "",
        "## 原理",
        _md_escape(tech.principle),
        "",
        "## 應用（海事）",
        _md_escape(tech.applications_maritime),
        "",
        "## 應用（醫療）",
        _md_escape(tech.applications_medical),
        "",
        "## 應用（其他產業）",
        _md_escape(tech.applications_general) or "（待補充）",
        "",
        "## 限制與風險",
        _md_escape(tech.limitations) or "（待補充）",
        "",
        "## 參考來源",
        *[f"- {_link(u)}" for u in (tech.reference_urls or []) if _link(u)],
        "",
    ]).strip() + "\n"


def render_digest_markdown(bundle: DailyBundle, report: dict[str, Any]) -> str:
    lines = [f"# 每日 AI 匯報 - {bundle.date}", ""]
    lines.append("## 新聞（10）")
    for i, n in enumerate(bundle.news, 1):
        lines.append(f"- {i}. {n.title}｜{n.source}｜{_link(n.url)}")
    lines.append("")
    lines.append("## 論文（5）")
    for i, p in enumerate(bundle.papers, 1):
        venue = p.journal or p.venue or p.source_name
        lines.append(f"- {i}. {p.title}｜{venue}｜IF/Impact: {p.impact_factor}｜{_link(p.url)}")
    lines.append("")
    lines.append("## GitHub 專案（5）")
    for i, r in enumerate(bundle.repos, 1):
        pair = f"｜paper: {r.paper_url}" if r.paper_url else ""
        lines.append(f"- {i}. {r.full_name}（★{r.stars}, {r.language or 'unknown'}）{pair}｜{_link(r.html_url)}")
    lines.append("")
    lines.append("## AI 架構深度拆解（1）")
    if bundle.tech:
        lines.append(f"- {bundle.tech.name}｜{_link(bundle.tech.reference_urls[0]) if bundle.tech.reference_urls else ''}")
    lines.append("")
    lines.append("## 驗收摘要")
    q = report.get('quotas', {})
    lines.append(f"- 跨域新聞：{q.get('cross_domain', 0)}（需 >=3）")
    lines.append(f"- 海事新聞：{q.get('maritime', 0)}（需 >=1）")
    lines.append(f"- 實際配對論文：{q.get('paired_papers', 0)}（目標 >=3）；seed/code_url配對：{q.get('paired_papers_seed', 0)}")
    lines.append(f"- 實際配對repo：{q.get('paired_repos', 0)}；seed配對：{q.get('paired_repos_seed', 0)}")
    if q.get("stale_backfill") or report.get("allow_stale"):
        lines.append("- stale_backfill：true（回補模式，已放寬時效窗；需人工/後續補驗證）")
    if report.get("warnings"):
        lines.append(f"- warnings：{len(report['warnings'])}")
    return "\n".join(lines).strip() + "\n"


def write_bundle(bundle: DailyBundle, *, root: Path | str, report: dict[str, Any] | None = None) -> dict[str, Any]:
    report = report or {}
    day = datetime.strptime(bundle.date, "%Y-%m-%d").date()
    ensure_day_tree(root, day)
    files: list[Path] = []

    p_news = news_path(root, day)
    atomic_write_text(p_news, render_news_markdown(bundle))
    files.append(p_news)

    for i, paper in enumerate(bundle.papers, 1):
        path = paper_path(root, day, i, paper.title)
        atomic_write_text(path, render_paper_markdown(paper, i, bundle.date))
        files.append(path)

    for i, repo in enumerate(bundle.repos, 1):
        path = repo_path(root, day, i, repo.full_name.replace("/", "-"))
        atomic_write_text(path, render_repo_markdown(repo, i, bundle.date))
        files.append(path)

    if bundle.tech:
        p_tech = tech_path(root, day)
        atomic_write_text(p_tech, render_tech_markdown(bundle.tech, bundle))
        files.append(p_tech)

    p_digest = digest_path(root, day)
    atomic_write_text(p_digest, render_digest_markdown(bundle, report))
    files.append(p_digest)

    assets = assets_dir(root, day)
    assets.mkdir(parents=True, exist_ok=True)

    return {
        "files": [str(p) for p in files],
        "day_dir": str(p_news.parent),
        "digest": str(p_digest),
    }
