"""GitHub 專案蒐集引擎：多查詢 + 論文配對種子 → 去重 → 時效 → AI 相關性 → 品質篩選 → 配額選取。"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Iterable

from config import (
    REPO_ENRICH_LIMIT,
    REPO_EXCLUDE_COLLECTIONS,
    REPO_MAX_AGE_DAYS,
    REPO_MAX_PER_SOURCE,
    REPO_MIN_PAIRED,
    REPO_MIN_QUALITY_SCORE,
    REPO_QUERIES,
)
from collectors.news_engine import is_ai_related
from collectors.repo_parse import (
    RepoCandidate,
    build_repo_sections,
    evaluate_repo_quality,
    github_repo_full_name,
)
from collectors.repo_sources import RepoSources
from core.dedupe import Deduper, extract_arxiv_id, is_similar_title, make_keys, normalize_doi
from core.models import RepoItem, SchemaError
from core.timewin import is_within_window, now_utc, to_utc


class RepoQuotaError(RuntimeError):
    def __init__(self, message: str, report: dict):
        super().__init__(message)
        self.report = report


@dataclass
class RepoSelection:
    items: list[RepoItem]
    report: dict = field(default_factory=dict)
    rejected: list[dict] = field(default_factory=list)


def _updated_key(item: RepoItem) -> datetime:
    return item.updated_at or datetime.min.replace(tzinfo=timezone.utc)


def _is_paired(item: RepoItem) -> bool:
    return bool(item.paper_url or item.paired_paper)


def _priority_key(item: RepoItem, seed_names: set[str]) -> tuple:
    """種子／已配對優先，其次品質分數，再來才看星數，避免高星清單型專案霸榜。"""
    return (
        1 if (_is_paired(item) or item.full_name.lower() in seed_names) else 0,
        int(item.quality_score or 0),
        1 if item.language else 0,
        min(int(item.stars or 0), 200000),
        _updated_key(item),
    )


def candidate_to_item(candidate: RepoCandidate) -> RepoItem:
    sections = candidate.sections or build_repo_sections(candidate)
    paper_url = candidate.paper_url or (candidate.paper_urls[0] if candidate.paper_urls else "")
    paired_paper = candidate.paired_paper or paper_url
    return RepoItem(
        full_name=candidate.full_name,
        html_url=candidate.html_url,
        description=candidate.description or "",
        stars=int(candidate.stars or 0),
        forks=int(candidate.forks or 0),
        language=candidate.language or "",
        license_name=candidate.license_name or "",
        topics=list(candidate.topics or []),
        updated_at=candidate.updated_at,
        created_at=candidate.created_at,
        paper_url=paper_url,
        paired_paper=paired_paper,
        readme_text=candidate.readme_text or "",
        readme_excerpt=candidate.readme_excerpt or "",
        quality_score=int(candidate.quality_score or 0),
        quality_flags=list(candidate.quality_flags or []),
        sections=sections,
    )


def select_repos(
    items: Iterable[RepoItem],
    count: int,
    *,
    max_per_source: int = REPO_MAX_PER_SOURCE,
    min_paired: int = 0,
    seed_names: set[str] | None = None,
    allow_stale: bool = False,
) -> RepoSelection:
    seed_set = {str(s).lower() for s in (seed_names or set())}
    ordered = sorted(
        items,
        key=lambda item: (
            1 if item.full_name.lower() in seed_set else 0,
            1 if _is_paired(item) else 0,
            int(item.quality_score or 0),
            min(int(item.stars or 0), 200000),
            _updated_key(item),
        ),
        reverse=True,
    )
    selected: list[RepoItem] = []
    remaining = list(ordered)
    per_source: Counter[str] = Counter()
    relaxed = False

    def owner(item: RepoItem) -> str:
        return (item.full_name.split("/")[0] if "/" in item.full_name else item.full_name).lower()

    def eligible(item: RepoItem) -> bool:
        return max_per_source <= 0 or per_source[owner(item)] < max_per_source

    def take(predicate) -> bool:  # noqa: ANN001
        nonlocal relaxed
        for index, item in enumerate(remaining):
            if predicate(item) and eligible(item):
                remaining.pop(index)
                selected.append(item)
                per_source[owner(item)] += 1
                return True
        for index, item in enumerate(remaining):
            if predicate(item):
                remaining.pop(index)
                selected.append(item)
                per_source[owner(item)] += 1
                relaxed = True
                return True
        return False

    while len(selected) < count:
        paired = sum(1 for item in selected if _is_paired(item))
        seed_paired = sum(1 for item in selected if item.full_name.lower() in seed_set and _is_paired(item))
        if paired < min_paired and take(lambda i: i.full_name.lower() in seed_set and _is_paired(i)):
            continue
        if paired < min_paired and take(_is_paired):
            continue
        if take(lambda _item: True):
            continue
        break

    paired = sum(1 for item in selected if _is_paired(item))
    report = {
        "pool_size": len(ordered),
        "selected": len(selected),
        "target": count,
        "paired": paired,
        "paired_ok": paired >= min_paired,
        "per_owner": dict(per_source),
        "relaxed_caps": relaxed,
        "quality_scores": {item.full_name: int(item.quality_score or 0) for item in selected},
    }
    if len(selected) < count:
        report["quota_shortfall"] = f"repos:{len(selected)}/{count}"
        if not allow_stale:
            raise RepoQuotaError(f"GitHub 專案數量不足：{len(selected)}/{count}", report)
    return RepoSelection(items=selected, report=report)


# ===== P3 ↔ P4 雙向配對 =====

def _value(obj: Any, name: str) -> str:
    if isinstance(obj, dict):
        return str(obj.get(name) or "")
    return str(getattr(obj, name, "") or "")


def _set_value(obj: Any, name: str, value: str) -> None:
    if isinstance(obj, dict):
        obj[name] = value
    else:
        setattr(obj, name, value)


def paper_seed_entries(papers: Iterable[Any]) -> list[dict]:
    """Build seed entries for papers. Includes papers without code_url so repo search can try to pair them."""
    entries: list[dict] = []
    for paper in papers:
        repo = github_repo_full_name(_value(paper, "code_url"))
        entries.append({
            "repo": repo,
            "paper_url": _value(paper, "url"),
            "paper_title": _value(paper, "title"),
            "doi": _value(paper, "doi"),
            "arxiv_id": _value(paper, "arxiv_id"),
            "source": _value(paper, "source"),
        })
    return entries


def paper_seed_map(papers: Iterable[Any]) -> dict[str, dict]:
    """Backward-compatible: only papers with explicit GitHub code_url."""
    seeds: dict[str, dict] = {}
    for meta in paper_seed_entries(papers):
        repo = str(meta.get("repo", "")).strip()
        if not repo:
            continue
        seeds.setdefault(repo.lower(), meta)
    return seeds


def _paper_ids(paper: Any) -> tuple[set[str], set[str]]:
    dois: set[str] = set()
    arxivs: set[str] = set()
    for raw in (_value(paper, "doi"), _value(paper, "url"), _value(paper, "arxiv_id")):
        doi = normalize_doi(raw)
        if doi:
            dois.add(doi.lower())
        arxiv = extract_arxiv_id(raw)
        if arxiv:
            arxivs.add(arxiv.lower())
    return dois, arxivs


def _repo_matches_paper(repo: RepoItem, paper: Any) -> bool:
    code_repo = github_repo_full_name(_value(paper, "code_url"))
    if code_repo and code_repo.lower() == repo.full_name.lower():
        return True
    text = f"{repo.paper_url} {repo.paired_paper}".lower()
    if not text.strip():
        return False
    dois, arxivs = _paper_ids(paper)
    if any(doi in text for doi in dois):
        return True
    if any(arxiv in text for arxiv in arxivs):
        return True
    paper_url = _value(paper, "url").rstrip("/").lower()
    return bool(paper_url) and paper_url in text


def link_papers_to_repos(papers: Iterable[Any], repos: Iterable[RepoItem]) -> dict:
    """把已選論文與已選 repo 互相標記：paper.paired_repo ↔ repo.paper_url。"""
    paper_list = list(papers)
    repo_list = list(repos)
    by_name = {repo.full_name.lower(): repo for repo in repo_list}
    matched: list[dict] = []
    unpaired: list[dict] = []

    for paper in paper_list:
        code_repo = github_repo_full_name(_value(paper, "code_url"))
        repo = by_name.get(code_repo.lower()) if code_repo else None
        if repo is None:
            repo = next((candidate for candidate in repo_list if _repo_matches_paper(candidate, paper)), None)
        entry = {
            "title": _value(paper, "title"),
            "code_url": _value(paper, "code_url"),
            "paper_url": _value(paper, "url"),
        }
        if repo is None:
            unpaired.append(entry)
            continue
        _set_value(paper, "paired_repo", repo.full_name)
        if not repo.paper_url:
            repo.paper_url = _value(paper, "url")
        if not repo.paired_paper:
            repo.paired_paper = _value(paper, "url")
        matched.append({**entry, "repo": repo.full_name})

    return {
        "matched": matched,
        "unpaired": unpaired,
        "papers_paired": len(matched),
        "repos_paired": len({entry["repo"].lower() for entry in matched}),
        "paper_total": len(paper_list),
        "repo_total": len(repo_list),
    }


class RepoEngine:
    def __init__(
        self,
        *,
        sources: RepoSources | None = None,
        queries: list[dict] | None = None,
        max_per_source: int = REPO_MAX_PER_SOURCE,
        max_age_days: int = REPO_MAX_AGE_DAYS,
        min_paired: int = REPO_MIN_PAIRED,
        allow_stale: bool = False,
        min_quality_score: int = REPO_MIN_QUALITY_SCORE,
        exclude_collections: bool = REPO_EXCLUDE_COLLECTIONS,
        enrich_limit: int = REPO_ENRICH_LIMIT,
    ) -> None:
        self.sources = sources or RepoSources()
        self.queries = REPO_QUERIES if queries is None else queries
        self.max_per_source = max_per_source
        self.max_age_days = max_age_days
        self.min_paired = min_paired
        self.allow_stale = allow_stale
        self.min_quality_score = min_quality_score
        self.exclude_collections = exclude_collections
        self.enrich_limit = enrich_limit

    def collect(
        self,
        count: int = 5,
        *,
        now: datetime | None = None,
        seed_repos: list[str] | None = None,
        paper_seeds: Iterable[dict] | None = None,
    ) -> RepoSelection:
        reference = now or now_utc()
        pushed_after = (reference - timedelta(days=self.max_age_days)).date().isoformat()
        raw: list[RepoCandidate] = []
        source_stats: dict[str, dict] = {}

        seed_meta: dict[str, dict] = {}
        for meta in paper_seeds or []:
            name = github_repo_full_name(str((meta or {}).get("repo", ""))) or str((meta or {}).get("repo", "")).strip()
            if "/" not in name:
                continue
            value = dict(meta)
            value["repo"] = name
            seed_meta[name.lower()] = value

        seed_order: list[str] = []
        for name in list(seed_repos or []) + [meta["repo"] for meta in seed_meta.values()]:
            value = github_repo_full_name(name) or str(name).strip()
            if "/" in value and value.lower() not in {item.lower() for item in seed_order}:
                seed_order.append(value)

        # 1) query-based discovery
        for query in self.queries:
            q = str(query.get("query", "")).strip()
            if not q:
                continue
            min_stars = int(query.get("min_stars", 0) or 0)
            repos, st = self.sources.search_repos(q, per_page=15, pushed_after=pushed_after, min_stars=min_stars)
            raw.extend(repos)
            entry = source_stats.setdefault("github_search", {"found": 0, "fetched": 0, "errors": 0})
            entry["found"] += st.found
            entry["fetched"] += st.fetched
            entry["errors"] += st.errors
            if st.error:
                entry["error"] = st.error

        # 2) paper seeds / explicit seeds（直接抓 repo 詳情，不受搜尋排名影響）
        seed_status: list[dict] = []
        for meta in paper_seed_entries(paper_seeds or []):
            # resolve actual seed status for explicit repo, or attempt discovery for papers without code_url
            pass
        # rebuild seed handling with explicit and discovered seeds
        seed_status_by_repo: dict[str, dict] = {}
        for full_name in seed_order:
            meta = seed_meta.get(full_name.lower()) or {}
            seed_error = ""
            repo = None
            try:
                repo = self.sources.get_repo(full_name)
                if not repo:
                    seed_error = getattr(self.sources, "last_error", "") or "fetch_failed_or_not_found"
            except Exception as exc:  # noqa: BLE001
                seed_error = f"{type(exc).__name__}"
            entry = source_stats.setdefault("github_seed", {"found": 0, "fetched": 0, "errors": 0, "status_codes": []})
            status = {"repo": full_name, "paper_url": meta.get("paper_url", ""), "paper_title": meta.get("paper_title", ""), "seed_type": "explicit"}
            if repo:
                raw.append(repo)
                entry["found"] += 1
                entry["fetched"] += 1
                status["fetched"] = True
                seed_status_by_repo[full_name.lower()] = status
            else:
                entry["errors"] += 1
                status["fetched"] = False
                status["error"] = seed_error or "fetch_failed_or_not_found"
                st = getattr(self.sources, "last_status", None)
                if st is not None:
                    status["status"] = st
                    codes = entry.setdefault("status_codes", [])
                    if st not in codes:
                        codes.append(st)
                seed_status_by_repo[full_name.lower()] = status

        # 2b) discover repos for papers that have no explicit code_url
        for meta in paper_seed_entries(paper_seeds or []):
            if str(meta.get("repo", "")).strip():
                continue
            found_repo = self._discover_repo_for_paper(meta, reference=reference)
            purl = str(meta.get("paper_url", "") or "")
            if found_repo:
                raw.append(found_repo)
                status = {
                    "repo": found_repo.full_name,
                    "paper_url": purl,
                    "paper_title": meta.get("paper_title", ""),
                    "seed_type": "discovered",
                    "fetched": True,
                }
                # register in seed_meta/order so pairing/scoring recognizes it
                name_l = found_repo.full_name.lower()
                seed_meta[name_l] = {**meta, "repo": found_repo.full_name}
                if name_l not in {n.lower() for n in seed_order}:
                    seed_order.append(found_repo.full_name)
                seed_status_by_repo[name_l] = status
                entry = source_stats.setdefault("github_seed_discovered", {"found": 0, "fetched": 0, "errors": 0})
                entry["found"] += 1
                entry["fetched"] += 1
            else:
                entry = source_stats.setdefault("github_seed_discovered", {"found": 0, "fetched": 0, "errors": 0})
                entry["errors"] += 1
                seed_status_by_repo[f"paper:{purl}"] = {
                    "paper_url": purl,
                    "paper_title": meta.get("paper_title", ""),
                    "seed_type": "discovered",
                    "fetched": False,
                    "error": "no_matching_repo_found",
                }
        seed_status = list(seed_status_by_repo.values())

        # 3) 把論文 seed 資訊貼到所有候選（含搜尋結果），確保配對優先
        for cand in raw:
            meta = seed_meta.get(cand.full_name.lower())
            if not meta:
                continue
            cand.paper_url = cand.paper_url or meta.get("paper_url", "")
            cand.paired_paper = cand.paired_paper or meta.get("paper_url", "")
            cand.extra["seed_paper"] = meta
            cand.extra["is_paper_seed"] = True

        items, rejected = self._filter_and_dedupe(raw, reference)

        seed_names = {name.lower() for name in seed_order}
        ordered = sorted(items, key=lambda item: _priority_key(item, seed_names), reverse=True)

        # 4) 依優先序深入抓 README，邊抓邊做品質閘門
        qualified: list[RepoItem] = []
        enriched_count = 0
        for item in ordered:
            if enriched_count < self.enrich_limit:
                if self._enrich_item(item, rejected):
                    enriched_count += 1
                else:
                    continue

            if not self._quality_gate(item, reference, rejected):
                continue
            qualified.append(item)

        try:
            selection = select_repos(
                qualified, count, max_per_source=self.max_per_source, min_paired=self.min_paired, seed_names=seed_names, allow_stale=self.allow_stale
            )
        except RepoQuotaError as exc:
            exc.report.setdefault("sources", source_stats)
            exc.report.setdefault("raw_count", len(raw))
            exc.report.setdefault("unique_items", len(items))
            exc.report.setdefault("qualified_items", len(qualified))
            exc.report.setdefault("enriched_count", enriched_count)
            exc.report.setdefault("seed_count", len(seed_order))
            exc.report.setdefault("rejected_counts", dict(Counter(r["reason"] for r in rejected)))
            raise

        if selection.report.get("paired", 0) < self.min_paired:
            selection.report["paired_warning"] = (
                f"配對專案不足目標：{selection.report.get('paired', 0)}/{self.min_paired}"
            )

        scores = [int(item.quality_score or 0) for item in selection.items]
        selection.report["quality"] = {
            "high": sum(1 for score in scores if score >= 5),
            "mid": sum(1 for score in scores if 3 <= score < 5),
            "low": sum(1 for score in scores if score < 3),
            "average": round(sum(scores) / len(scores), 2) if scores else 0,
        }
        selection.rejected = rejected
        missing_seed_repos = [s for s in seed_status if not s.get("fetched")]
        auth_blocked = [s for s in missing_seed_repos if s.get("status") in {401, 403} or "http_401" in str(s.get("error","")) or "http_403" in str(s.get("error",""))]
        if missing_seed_repos and selection.report.get("paired", 0) < self.min_paired:
            reason = "GitHub auth/rate limit、repo 不存在或名稱變更"
            if auth_blocked and len(auth_blocked) == len(missing_seed_repos):
                reason = "GitHub token 無效/SSO 未授權或 rate limit（已嘗試匿名 fallback）"
            selection.report["seed_warning"] = (
                f"論文種子 repo 未完整抓取：{len(missing_seed_repos)}/{len(seed_status)}；{reason}"
            )
        if auth_blocked:
            selection.report["github_auth_blocked"] = True
            selection.report["github_auth_blocked_count"] = len(auth_blocked)
        if source_stats.get("github_seed", {}).get("error") == "auth_fallback:200":
            selection.report["github_auth_fallback"] = True

        selection.report["sources"] = source_stats
        selection.report["raw_count"] = len(raw)
        selection.report["unique_items"] = len(items)
        selection.report["qualified_items"] = len(qualified)
        selection.report["enriched_count"] = enriched_count
        selection.report["seed_count"] = len(seed_order)
        selection.report["seed_status"] = seed_status
        selection.report["collections_excluded"] = sum(
            1 for entry in rejected if entry.get("reason") == "collection_repo"
        )
        selection.report["rejected_counts"] = dict(Counter(r["reason"] for r in rejected))
        return selection

    def _discover_repo_for_paper(self, meta: dict, *, reference: datetime) -> RepoCandidate | None:
        """Best-effort repo discovery for papers without code_url. Only returns repos with traceable paper link."""
        arxiv_id = str(meta.get("arxiv_id", "") or "").strip()
        doi = str(meta.get("doi", "") or "").strip()
        title = str(meta.get("paper_title", "") or "").strip()
        paper_url = str(meta.get("paper_url", "") or "").strip()
        queries: list[str] = []
        if arxiv_id:
            queries.append(arxiv_id)
        if doi:
            queries.append(doi)
        if title:
            # use a compact title query; keep it simple to avoid GitHub query syntax issues
            words = [w for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9\-]{2,}", title)[:8]]
            if words:
                queries.append(" ".join(words))
        seen: set[str] = set()
        for q in queries:
            try:
                repos, _st = self.sources.search_repos(q, per_page=5, pushed_after="", min_stars=0, sort="stars", order="desc")
            except Exception:
                continue
            for repo in repos:
                key = repo.full_name.lower()
                if key in seen:
                    continue
                seen.add(key)
                try:
                    enriched = self.sources.enrich_repo(repo)
                except Exception:
                    continue
                item = candidate_to_item(enriched)
                text = f"{item.paper_url} {item.paired_paper} {item.readme_text} {item.readme_excerpt}".lower()
                matched = False
                if arxiv_id and arxiv_id.lower() in text:
                    matched = True
                if doi and doi.lower() in text:
                    matched = True
                if paper_url and paper_url.lower() in text:
                    matched = True
                if not matched:
                    continue
                # attach seed metadata
                item.paper_url = item.paper_url or paper_url
                item.paired_paper = item.paired_paper or paper_url
                item.extra["seed_paper"] = meta
                item.extra["is_paper_seed"] = True
                item.extra["discovered_by_paper"] = True
                # return as candidate-like object for downstream flow
                return RepoCandidate(
                    full_name=item.full_name,
                    html_url=item.html_url,
                    description=item.description,
                    stars=item.stars,
                    forks=item.forks,
                    language=item.language,
                    license_name=item.license_name,
                    topics=list(item.topics),
                    updated_at=item.updated_at.isoformat() if item.updated_at else "",
                    created_at=item.created_at.isoformat() if item.created_at else "",
                    readme_text=item.readme_text,
                    readme_excerpt=item.readme_excerpt,
                    paper_url=item.paper_url,
                    paper_urls=[item.paper_url] if item.paper_url else [],
                    paired_paper=item.paired_paper,
                    quality_score=item.quality_score,
                    quality_flags=list(item.quality_flags),
                    sections=dict(item.sections),
                    extra=dict(item.extra),
                )
        return None

    def _enrich_item(self, item: RepoItem, rejected: list[dict]) -> bool:
        try:
            cand = RepoCandidate(
                full_name=item.full_name,
                html_url=item.html_url,
                description=item.description,
                stars=item.stars,
                forks=item.forks,
                language=item.language,
                license_name=item.license_name,
                topics=list(item.topics),
                updated_at=item.updated_at,
                created_at=item.created_at,
                readme_text=item.readme_text,
                readme_excerpt=item.readme_excerpt,
                paper_url=item.paper_url,
                paired_paper=item.paired_paper,
                quality_score=item.quality_score,
                quality_flags=list(item.quality_flags),
                sections=dict(item.sections),
            )
            enriched = self.sources.enrich_repo(cand)
            new_item = candidate_to_item(enriched).validate()
            item.description = new_item.description
            item.stars = new_item.stars
            item.forks = new_item.forks
            item.language = new_item.language
            item.license_name = new_item.license_name
            item.topics = new_item.topics
            item.updated_at = new_item.updated_at or item.updated_at
            item.created_at = new_item.created_at or item.created_at
            item.paper_url = new_item.paper_url or item.paper_url
            item.paired_paper = new_item.paired_paper or item.paired_paper
            item.readme_text = new_item.readme_text or item.readme_text
            item.readme_excerpt = new_item.readme_excerpt or item.readme_excerpt
            item.sections = new_item.sections or item.sections
            return True
        except Exception as exc:  # noqa: BLE001
            rejected.append({
                "title": item.full_name,
                "reason": f"enrich_error:{type(exc).__name__}",
                "source": "github",
            })
            return False

    def _quality_gate(self, item: RepoItem, reference: datetime, rejected: list[dict]) -> bool:
        if not item.readme_excerpt and not item.description:
            rejected.append({"title": item.full_name, "reason": "no_content", "source": "github"})
            return False

        quality = evaluate_repo_quality(
            item.full_name,
            item.description,
            item.topics,
            item.readme_excerpt,
            item.language,
            item.stars,
            paired=_is_paired(item),
        )
        item.quality_score = quality.score
        item.quality_flags = quality.flags

        if item.updated_at and not is_within_window(item.updated_at, self.max_age_days, now=reference):
            # stale seed: keep only when paired to a paper for P3↔P4 traceability
            if _is_paired(item):
                item.quality_flags = list(dict.fromkeys((item.quality_flags or []) + ["stale_seed"]))
            else:
                rejected.append({"title": item.full_name, "reason": "stale_after_enrich", "source": "github"})
                return False

        extra = item.extra if isinstance(getattr(item, "extra", None), dict) else {}
        is_seed = bool(extra.get("is_paper_seed") or extra.get("seed_paper") or _is_paired(item))
        if self.exclude_collections and quality.collection:
            if is_seed:
                item.quality_flags = list(dict.fromkeys((item.quality_flags or []) + ["collection_paired_override"]))
            else:
                rejected.append({
                    "title": item.full_name,
                    "reason": "collection_repo",
                    "source": "github",
                    "flags": quality.flags,
                })
                return False
        if quality.score < self.min_quality_score:
            if is_seed:
                item.quality_flags = list(dict.fromkeys((item.quality_flags or []) + [f"low_quality_override:{quality.score}"]))
            else:
                rejected.append({
                    "title": item.full_name,
                    "reason": f"low_quality:{quality.score}",
                    "source": "github",
                    "flags": quality.flags,
                })
                return False

        if not item.sections.get("what") or not item.sections.get("tech") or not item.sections.get("architecture"):
            item.sections = build_repo_sections(
                RepoCandidate(
                    full_name=item.full_name,
                    html_url=item.html_url,
                    description=item.description,
                    stars=item.stars,
                    forks=item.forks,
                    language=item.language,
                    license_name=item.license_name,
                    topics=item.topics,
                    updated_at=item.updated_at,
                    readme_excerpt=item.readme_excerpt,
                    paper_urls=[item.paper_url] if item.paper_url else [],
                    paper_url=item.paper_url,
                    paired_paper=item.paired_paper,
                )
            )
        return True

    def _filter_and_dedupe(self, candidates: list[RepoCandidate], reference: datetime) -> tuple[list[RepoItem], list[dict]]:
        deduper = Deduper()
        kept: list[RepoItem] = []
        rejected: list[dict] = []

        for cand in candidates:
            if not cand.full_name or not cand.html_url:
                rejected.append({"title": cand.full_name[:160], "reason": "missing_name_or_url", "source": "github"})
                continue
            if (cand.extra or {}).get("archived"):
                rejected.append({"title": cand.full_name, "reason": "archived", "source": "github"})
                continue
            updated = cand.updated_at or cand.pushed_at
            if updated is None:
                rejected.append({"title": cand.full_name, "reason": "no_date", "source": "github"})
                continue
            updated = to_utc(updated)
            cand.updated_at = updated
            is_seed = bool((cand.extra or {}).get("is_paper_seed"))
            if not self.allow_stale and not is_within_window(updated, self.max_age_days, now=reference):
                if is_seed:
                    cand.extra["stale_seed"] = True
                else:
                    rejected.append({"title": cand.full_name, "reason": "stale", "source": "github"})
                    continue
            elif self.allow_stale and not is_within_window(updated, self.max_age_days, now=reference):
                cand.extra["stale_backfill"] = True

            text = f"{cand.full_name} {cand.description} {' '.join(cand.topics)} {cand.readme_excerpt[:500]}"
            seed = (cand.extra or {}).get("seed_paper") or {}
            seed_text = f"{seed.get('paper_title','')} {seed.get('paper_url','')}".strip()
            ai_related = is_ai_related(text) or (bool(seed_text) and is_ai_related(seed_text))
            if not ai_related:
                if bool(seed_text):
                    cand.extra["seed_ai_override"] = True
                else:
                    rejected.append({"title": cand.full_name, "reason": "not_ai", "source": "github"})
                    continue

            quality = evaluate_repo_quality(
                cand.full_name,
                cand.description,
                cand.topics,
                cand.readme_excerpt or cand.readme_text,
                cand.language,
                cand.stars,
                paired=bool(cand.paper_url or cand.paired_paper),
            )
            cand.quality_score = quality.score
            cand.quality_flags = quality.flags
            if self.exclude_collections and quality.collection:
                if is_seed and bool(cand.paper_url or cand.paired_paper):
                    cand.extra["collection_paired_override"] = True
                    cand.quality_flags = list(dict.fromkeys((quality.flags or []) + ["collection_paired_override"]))
                else:
                    rejected.append({
                        "title": cand.full_name,
                        "reason": "collection_repo",
                        "source": "github",
                        "flags": quality.flags,
                    })
                    continue

            try:
                item = candidate_to_item(cand)
                item.validate()
            except SchemaError as exc:
                rejected.append({"title": cand.full_name, "reason": f"invalid:{exc}", "source": "github"})
                continue

            keys = make_keys(repo=item.full_name, url=item.html_url, title=item.full_name)
            if not deduper.add(*keys):
                rejected.append({"title": cand.full_name, "reason": "duplicate", "source": "github"})
                continue
            if any(is_similar_title(item.full_name, other.full_name) for other in kept):
                rejected.append({"title": cand.full_name, "reason": "similar_name", "source": "github"})
                continue
            kept.append(item)

        return kept, rejected


def collect_daily_repos(
    count: int = 5,
    *,
    now: datetime | None = None,
    seed_repos: list[str] | None = None,
    paper_seeds: Iterable[dict] | None = None,
) -> RepoSelection:
    return RepoEngine().collect(count, now=now, seed_repos=seed_repos, paper_seeds=paper_seeds)
