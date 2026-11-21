"""P5 主流程：collect -> enrich/pair -> write(iAI可選) -> validate -> manifest -> push(optional)。"""
from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from collectors.news_engine import NewsEngine
from collectors.paper_engine import PaperEngine
from collectors.repo_engine import RepoEngine, link_papers_to_repos, paper_seed_map
from config import BASE_DIR, DAILY_NEWS_COUNT, DAILY_PAPER_COUNT, DAILY_REPO_COUNT
from core.logging_utils import setup_logger
from core.manifest import RunManifest
from core.models import DailyBundle, SchemaError, TechArchItem
from core.paths import ensure_day_tree
from core.security import redact_secrets
from core.timewin import end_of_day_utc, parse_datetime
from report.daily_reporter import write_bundle
from summarizer.daily_writer import DailyWriter


logger = setup_logger("pipeline")


def _target_day(value: str | date | datetime | None) -> date:
    if value is None:
        return datetime.now().date()
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    parsed = parse_datetime(value)
    if not parsed:
        raise ValueError(f"無法解析日期：{value!r}")
    return parsed.date()


def _as_dict(obj: Any) -> dict[str, Any]:
    if is_dataclass(obj):
        return asdict(obj)
    if isinstance(obj, dict):
        return dict(obj)
    return {"value": redact_secrets(obj)}


class DailyPipeline:
    def __init__(
        self,
        *,
        root: Path | str = BASE_DIR,
        writer: DailyWriter | None = None,
        news_engine: NewsEngine | None = None,
        paper_engine: PaperEngine | None = None,
        repo_engine: RepoEngine | None = None,
    ):
        self.root = Path(root)
        self.writer = writer or DailyWriter()
        self.news_engine = news_engine or NewsEngine()
        self.paper_engine = paper_engine or PaperEngine()
        self.repo_engine = repo_engine or RepoEngine()

    def run(
        self,
        *,
        target: str | date | datetime | None = None,
        news_count: int = DAILY_NEWS_COUNT,
        paper_count: int = DAILY_PAPER_COUNT,
        repo_count: int = DAILY_REPO_COUNT,
        write: bool = True,
        push: bool = False,
        use_ai: bool = True,
        force: bool = False,
    ) -> dict[str, Any]:
        day = _target_day(target)
        reference = end_of_day_utc(day)
        manifest = RunManifest(target_date=day.isoformat())
        report: dict[str, Any] = {
            "date": day.isoformat(),
            "status": "running",
            "warnings": [],
            "errors": [],
            "quotas": {},
            "files": [],
        }

        try:
            day_dir = self.root / str((day.isoweekday() % 7) + 0)  # placeholder
            # compute expected day dir via core.paths
            from core.paths import day_dir as _day_dir, digest_path as _digest_path
            out_day_dir = _day_dir(self.root, day)
            out_digest = _digest_path(self.root, day)
            existing = out_day_dir.exists() and any(out_day_dir.glob('*.md')) and out_digest.exists()
            report["existing_output"] = bool(existing)
            if existing and not force:
                report["status"] = "skipped_existing"
                report["warnings"].append("existing_output_found_use_force_to_overwrite")
                manifest.warning("existing_output_found_use_force_to_overwrite")
                manifest.finish("skipped")
                report["manifest"] = str(manifest.save())
                report["files"] = sorted([str(p) for p in out_day_dir.glob('*.md')] + ([str(out_digest)] if out_digest.exists() else []))
                return report

            with manifest.stage("collect_news"):
                news_sel = self.news_engine.collect(news_count, now=reference)
            manifest.counts["news_raw"] = int(news_sel.report.get("raw_count", 0))
            manifest.counts["news_selected"] = len(news_sel.items)
            manifest.source("news", found=manifest.counts["news_raw"], kept=len(news_sel.items))

            with manifest.stage("collect_papers"):
                paper_sel = self.paper_engine.collect(paper_count, now=reference)
            manifest.counts["papers_raw"] = int(paper_sel.report.get("raw_count", 0))
            manifest.counts["papers_selected"] = len(paper_sel.items)
            manifest.source("papers", found=manifest.counts["papers_raw"], kept=len(paper_sel.items))

            with manifest.stage("collect_repos"):
                seeds = list(paper_seed_map(paper_sel.items).values())
                repo_sel = self.repo_engine.collect(repo_count, now=reference, paper_seeds=seeds)
            manifest.counts["repos_raw"] = int(repo_sel.report.get("raw_count", 0))
            manifest.counts["repos_selected"] = len(repo_sel.items)
            manifest.counts["repo_seed_count"] = int(repo_sel.report.get("seed_count", 0))
            manifest.source("repos", found=manifest.counts["repos_raw"], kept=len(repo_sel.items))

            with manifest.stage("pairing"):
                pairing = link_papers_to_repos(paper_sel.items, repo_sel.items)
            manifest.pairing = {
                "papers_paired": int(pairing.get("papers_paired", 0)),
                "repos_paired": int(pairing.get("repos_paired", 0)),
            }
            report["pairing"] = pairing
            actual_paired = int(pairing.get("repos_paired", 0))
            seed_paired = int(pairing.get("papers_paired", 0))
            report["paired_actual"] = actual_paired
            report["paired_seed"] = seed_paired
            if actual_paired < 3:
                msg = f"paired_repos_below_target={actual_paired}/3 (seed_paired={seed_paired})"
                report["warnings"].append(msg)
                manifest.warning(msg)
            if repo_sel.report.get("seed_warning"):
                report["warnings"].append(str(repo_sel.report["seed_warning"]))
                manifest.warning(repo_sel.report["seed_warning"])

            writer = self.writer if (use_ai and self.writer.available) else None
            if use_ai and not self.writer.available:
                report["warnings"].append("IAI keys unavailable; used rule-based fallback content")
                manifest.warning("IAI keys unavailable; used rule-based fallback content")

            with manifest.stage("write_content"):
                for item in news_sel.items:
                    if writer:
                        enriched = writer.summarize_news(item)
                        item.summary = enriched.get("summary", item.summary) or item.summary
                        item.key_point = enriched.get("impact", item.key_point) or item.key_point
                    if not item.summary:
                        item.summary = (item.title or "")[:200]
                    if not item.key_point:
                        item.key_point = "（待補充影響）"

                for item in paper_sel.items:
                    if writer:
                        item.sections = writer.summarize_paper(item)
                    if not any((item.sections or {}).values()):
                        item.sections = {
                            "background": (item.abstract or item.title)[:500] or "（待補充）",
                            "method": "（待補充：需模型或人工分析）",
                            "results": "（待補充：需模型或人工分析）",
                            "limitations": "（待補充：需模型或人工分析）",
                        }

                for item in repo_sel.items:
                    if writer:
                        item.sections = writer.summarize_repo(item)
                    if not any((item.sections or {}).values()):
                        item.sections = {
                            "what": item.description or item.full_name,
                            "tech": f"Language: {item.language}; Topics: {', '.join(item.topics[:8])}",
                            "architecture": "（待補充：需模型或人工分析 README/程式結構）",
                        }

                tech_data = writer.write_tech_arch(
                    date_str=day.isoformat(), news=news_sel.items, papers=paper_sel.items, repos=repo_sel.items
                ) if writer else self._fallback_tech(news_sel.items, paper_sel.items)
                tech = TechArchItem(**tech_data)

            if writer:
                ai_report = writer.report()
                manifest.set_models(ai_report.get("model_usage", {}))
                report["ai"] = {
                    "model_usage": ai_report.get("model_usage", {}),
                    "errors": ai_report.get("ai_errors", []),
                    "fallbacks": ai_report.get("fallbacks", []),
                }
                for e in ai_report.get("ai_errors", [])[:5]:
                    manifest.warning(f"ai_error:{e}")
                if ai_report.get("fallbacks"):
                    manifest.warning(f"ai_fallbacks={len(ai_report['fallbacks'])}")

            bundle = DailyBundle(
                date=day.isoformat(),
                news=list(news_sel.items),
                papers=list(paper_sel.items),
                repos=list(repo_sel.items),
                tech=tech,
                warnings=list(report["warnings"]),
            )

            with manifest.stage("validate"):
                quotas = bundle.validate(now=reference, require_counts=True, require_sections=False, require_quotas=True)
            report["quotas"] = quotas
            manifest.quotas = quotas

            if write:
                with manifest.stage("write_files"):
                    ensure_day_tree(self.root, day)
                    out = write_bundle(bundle, root=self.root, report=report)
                report["files"] = out["files"]
                for f in out["files"]:
                    manifest.add_file(f)

            if push and report["files"]:
                with manifest.stage("git_push"):
                    from git_pusher import push_to_github

                    push_files = [Path(p) for p in report["files"] if str(p).replace('\\','/').endswith('.md')]
                    ok = push_to_github(push_files, f"docs: 每日AI匯報 {day.isoformat()} ({len(push_files)} files)")
                    report["pushed"] = bool(ok)
                    report["push_files"] = [str(p) for p in push_files]
                    if not ok:
                        report["warnings"].append("git_push_failed")
                        manifest.warning("git_push_failed")

            manifest.finish("ok")
            report["status"] = "ok"
        except Exception as exc:  # noqa: BLE001
            msg = redact_secrets(exc)
            report["status"] = "error"
            report["errors"].append(msg)
            manifest.error("pipeline", msg)
            manifest.finish("error")
            logger.exception("pipeline failed: %s", msg)
        finally:
            report["manifest"] = str(manifest.save())
            report["stages"] = dict(manifest.stages)
            report["counts"] = dict(manifest.counts)
            report["warnings"] = list(dict.fromkeys(report["warnings"] + manifest.warnings))
            try:
                (self.root / ".system_generated" / "logs").mkdir(parents=True, exist_ok=True)
                report_path = self.root / ".system_generated" / "logs" / f"pipeline_{day.isoformat()}.json"
                report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
                report["report_path"] = str(report_path)
            except Exception:
                pass

        return report

    @staticmethod
    def _fallback_tech(news: list[Any], papers: list[Any]) -> dict[str, Any]:
        refs = []
        for p in papers[:3]:
            if getattr(p, "url", ""): refs.append(p.url)
        for n in news[:2]:
            if getattr(n, "url", ""): refs.append(n.url)
        return {
            "name": "多模態 AI Agent 架構",
            "rationale": "今日新聞/論文/專案中，代理與多模態整合是共同趨勢。",
            "principle": "多模態 AI Agent 通常由感知模組、規劃/推理模組、工具呼叫模組與記憶模組組成。感知模組將文字、影像、感測資料轉為可推理表示；規劃模組分解任務；工具模組執行搜尋、程式、API 或控制指令；記憶模組保存上下文與長期狀態。關鍵在於跨模態對齊、工具可靠性與可觀測的安全邊界。",
            "applications_maritime": "海事可用於異常船舶行為偵測、港口調度協助、遙測資料摘要、事故報告生成與維修決策支援。部署時需處理低頻寬、衛星通訊延遲、惡劣海象與安全關鍵誤判風險。",
            "applications_medical": "醫療可用於影像與病歷多模態摘要、臨床決策輔助、醫療文件檢索與流程自動化。需嚴格遵守資料隱私、可追溯性、臨床驗證與人類覆核要求。",
            "applications_general": "亦可用於企業知識管理、軟體工程助理、客服自動化與工業檢測。",
            "limitations": "主要風險包括幻覺、工具誤用、資料外洩、成本過高與缺乏可解釋性；高風險場景必須有人類監督。",
            "reference_urls": refs or ["https://arxiv.org/"],
        }


def run_daily_pipeline(**kwargs: Any) -> dict[str, Any]:
    return DailyPipeline().run(**kwargs)
