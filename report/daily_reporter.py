"""P5：新格式每日報告輸出（1-7/<date>/ + 每日匯報/）。"""
from __future__ import annotations

import os
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any

from config import TIER_LABELS
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


def _tier_label(tier: object) -> str:
    try:
        value = int(tier or 0)
    except (TypeError, ValueError):
        value = 0
    return f"Tier {value}（{TIER_LABELS.get(value, '未分類')}）"


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
        f"- 來源層級：{_tier_label(item.source_tier)}" + ("（海事）" if getattr(item, "is_maritime", False) else ""),
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
        f"- 論文層級：{_tier_label(getattr(item, 'paper_tier', 0)) if getattr(item, 'paper_tier', 0) else '未對應論文'}"
        f"{'（海事）' if getattr(item, 'is_maritime', False) else ''}",
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
        "## 一、架構原理與核心機制",
        _md_escape(tech.principle),
        "",
        "## 二、海事領域應用（含實際例子）",
        _md_escape(tech.applications_maritime),
        "",
        "## 三、醫療領域應用（含實際例子）",
        _md_escape(tech.applications_medical),
        "",
        "## 四、其他產業應用（含實際例子）",
        _md_escape(tech.applications_general) or "（待補充）",
        "",
        "## 五、限制、風險與治理建議",
        _md_escape(tech.limitations) or "（待補充）",
        "",
        "## 參考來源",
        *[f"- {_link(u)}" for u in (tech.reference_urls or []) if _link(u)],
        "",
    ]).strip() + "\n"


def _short(text: object, limit: int = 140) -> str:
    t = " ".join(str(text or "").replace("\n", " ").split()).strip()
    if len(t) <= limit:
        return t
    return t[: limit - 1].rstrip() + "…"


def render_digest_markdown(bundle: DailyBundle, report: dict[str, Any]) -> str:
    lines = [f"# 每日 AI 匯報 - {bundle.date}", "", "> 本頁為每日總覽：每則項目含簡短摘要與連結。", ""]

    lines.append(f"## 新聞（{len(bundle.news)}）")
    for i, n in enumerate(bundle.news, 1):
        lines.append(f"### {i}. {n.title}")
        lines.append(f"- 來源/時間：{n.source or '未知'}｜{_dt(n.published_at)}")
        lines.append(f"- 領域：{', '.join(n.domains)}{'（海事）' if n.is_maritime else ''}")
        lines.append(f"- 摘要：{_short(n.summary, 180)}")
        lines.append(f"- 影響：{_short(n.key_point or n.summary, 120)}")
        lines.append(f"- 連結：{_link(n.url)}")
        lines.append("")

    lines.append(f"## 論文（{len(bundle.papers)}）")
    for i, p in enumerate(bundle.papers, 1):
        s = p.sections or {}
        venue = p.journal or p.venue or p.source_name
        lines.append(f"### {i}. {p.title}")
        lines.append(
            f"- 來源/發表：{venue}（{_tier_label(p.source_tier)}"
            f"{'／海事' if getattr(p, 'is_maritime', False) else ''}）"
            f"｜{_dt(p.published_at)}｜IF/Impact: {p.impact_factor}"
        )
        lines.append(f"- 摘要：{_short(s.get('background') or p.abstract, 220)}")
        lines.append(f"- 方法重點：{_short(s.get('method'), 180)}")
        lines.append(f"- 結果重點：{_short(s.get('results'), 140)}")
        lines.append(f"- 連結：{_link(p.url)}")
        if p.code_url:
            lines.append(f"- 程式碼：{_link(p.code_url)}")
        lines.append("")

    lines.append(f"## GitHub 專案（{len(bundle.repos)}）")
    for i, r in enumerate(bundle.repos, 1):
        s = r.sections or {}
        lines.append(f"### {i}. {r.full_name}")
        tier_text = _tier_label(getattr(r, "paper_tier", 0))
        if not getattr(r, "paper_tier", 0):
            tier_text = "未對應論文"
        lines.append(
            f"- 資訊：★{r.stars}｜{r.language or 'unknown'}｜論文層級：{tier_text}"
            f"{'／海事' if getattr(r, 'is_maritime', False) else ''}｜更新 {_dt(r.updated_at)}"
        )
        lines.append(f"- 在做什麼：{_short(s.get('what') or r.description, 160)}")
        lines.append(f"- 技術/架構：{_short(s.get('tech'), 90)} / {_short(s.get('architecture'), 90)}")
        lines.append(f"- 連結：{_link(r.html_url)}")
        if r.paper_url or r.paired_paper:
            lines.append(f"- 配對論文：{_link(r.paper_url) or r.paired_paper}")
        lines.append("")

    lines.append("## AI 架構深度拆解（1）")
    if bundle.tech:
        t = bundle.tech
        lines.append(f"### {t.name}")
        lines.append(f"- 選題理由：{_short(t.rationale, 160)}")
        lines.append(f"- 原理摘要：{_short(t.principle, 220)}")
        lines.append(f"- 海事應用：{_short(t.applications_maritime, 140)}")
        lines.append(f"- 醫療應用：{_short(t.applications_medical, 140)}")
        lines.append(f"- 其他應用：{_short(t.applications_general, 120)}")
        lines.append(f"- 限制風險：{_short(t.limitations, 120)}")
        if t.reference_urls:
            lines.append("- 參考來源：" + "；".join(_link(u) for u in t.reference_urls[:3] if _link(u)))
    lines.append("")

    lines.append("## 驗收摘要")
    q = report.get("quotas", {})
    lines.append(f"- 跨域新聞：{q.get('cross_domain', 0)}（需 >=3）")
    lines.append(f"- 海事新聞：{q.get('maritime', 0)}（需 >=1）")
    lines.append(f"- 海事論文：{q.get('maritime_papers', 0)}（需 >=2）")
    lines.append(f"- 海事 GitHub 專案：{q.get('maritime_repos', 0)}（需 >=2）")
    lines.append(f"- 實際配對論文：{q.get('paired_papers', 0)}（加分項）；seed/code_url配對：{q.get('paired_papers_seed', 0)}")
    lines.append(f"- 實際配對repo：{q.get('paired_repos', 0)}；seed配對：{q.get('paired_repos_seed', 0)}")
    if q.get("stale_backfill") or report.get("allow_stale"):
        lines.append("- stale_backfill：true（回補模式，已放寬時效窗；需人工/後續補驗證）")
    warnings = report.get("warnings") or []
    if warnings:
        lines.append(f"- warnings：{len(warnings)}")
        for w in warnings[:8]:
            lines.append(f"  - {redact_secrets(w)}")
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


def embed_tech_image(root: Path | str, date_value: str, image_path: str | Path) -> bool:
    """把 Pic-large 產生的架構圖嵌入深度拆解 md（使用相對於 md 的路徑）。"""
    if not image_path:
        return False
    day = datetime.strptime(date_value, "%Y-%m-%d").date()
    target = tech_path(root, day)
    if not target.exists():
        return False
    text = target.read_text(encoding="utf-8")
    if "![" in text or "<img" in text:
        return False
    rel = os.path.relpath(Path(image_path), target.parent).replace("\\", "/")
    block = f"![AI 技術架構示意圖]({rel})\n\n"
    marker = "## 一、架構原理與核心機制"
    if marker in text:
        text = text.replace(marker, block + marker, 1)
    else:
        text = text.rstrip() + "\n\n" + block.rstrip() + "\n"
    atomic_write_text(target, text)
    return True
