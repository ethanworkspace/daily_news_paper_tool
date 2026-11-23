"""P5 主流程：collect -> enrich/pair -> write(iAI可選) -> validate -> manifest -> push(optional)。"""
from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from collectors.news_engine import NewsEngine
from collectors.paper_engine import PaperEngine
from collectors.repo_engine import RepoEngine, link_papers_to_repos, paper_seed_entries
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
        allow_stale: bool = False,
    ):
        self.root = Path(root)
        self.allow_stale = allow_stale
        self.writer = writer or DailyWriter()
        self.news_engine = news_engine or NewsEngine(allow_stale=allow_stale)
        self.paper_engine = paper_engine or PaperEngine(allow_stale=allow_stale)
        self.repo_engine = repo_engine or RepoEngine(allow_stale=allow_stale)

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
            "allow_stale": bool(self.allow_stale),
        }
        if self.allow_stale:
            report["warnings"].append("stale_backfill=true: freshness windows relaxed for backfill")
            manifest.warning("stale_backfill=true")

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
                seeds = paper_seed_entries(paper_sel.items)
                repo_sel = self.repo_engine.collect(repo_count, now=reference, paper_seeds=seeds)
            manifest.counts["repos_raw"] = int(repo_sel.report.get("raw_count", 0))
            manifest.counts["repos_selected"] = len(repo_sel.items)
            manifest.counts["repo_seed_count"] = int(repo_sel.report.get("seed_count", 0))
            manifest.source("repos", found=manifest.counts["repos_raw"], kept=len(repo_sel.items))
            from config import GITHUB_TOKEN
            report["github_token_configured"] = bool(GITHUB_TOKEN)
            report["repo_selection"] = {
                "seed_count": repo_sel.report.get("seed_count"),
                "seed_status": repo_sel.report.get("seed_status", []),
                "seed_warning": repo_sel.report.get("seed_warning"),
                "collections_excluded": repo_sel.report.get("collections_excluded"),
                "rejected_counts": repo_sel.report.get("rejected_counts", {}),
            }
            seed_status = repo_sel.report.get("seed_status", []) or []
            seed_fetch_errors = [s for s in seed_status if not s.get("fetched")]
            report["repo_seed_fetch_errors"] = len(seed_fetch_errors)
            if repo_sel.report.get("seed_warning"):
                report["warnings"].append(str(repo_sel.report["seed_warning"]))
                manifest.warning(repo_sel.report["seed_warning"])
            if seed_fetch_errors:
                msg = f"seed_repo_fetch_failed={len(seed_fetch_errors)}/{len(seed_status)}"
                report["warnings"].append(msg)
                manifest.warning(msg)
            auth_blocked = bool(repo_sel.report.get("github_auth_blocked"))
            report["github_auth_blocked"] = auth_blocked
            if auth_blocked:
                msg = f"github_auth_blocked=true seed_401_403={repo_sel.report.get('github_auth_blocked_count', 0)}"
                report["warnings"].append(msg)
                manifest.warning(msg)
            if not GITHUB_TOKEN and seed_fetch_errors:
                report["warnings"].append("github_auth_blocked: missing GITHUB_TOKEN; seed repo fetch may be rate-limited")
                manifest.warning("github_auth_blocked: missing GITHUB_TOKEN")
                report["github_auth_blocked"] = True

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
                        fallback = (item.abstract or item.title or "").strip()
                        item.sections = {
                            "background": (
                                f"本研究主題為「{item.title}」。{fallback[:700]} "
                                "依目前可取得資料，仍需查閱原文以完整確認研究問題、既有缺口與具體貢獻。"
                            ).strip(),
                            "method": (
                                "依目前可取得資料，無法可靠還原完整方法細節。需查閱原文確認問題設定與輸入輸出、整體架構、核心模組機制、"
                                "資料處理或特徵表示、訓練目標與最佳化流程，以及推論或部署流程；目前不宜臆測未經證實的技術細節。"
                            ),
                            "results": (
                                "摘錄未提供可驗證數字。依目前可取得資料，無法確認具體實驗指標、資料集規模、基線比較或消融結果；"
                                "如需結論，應以原文結果章節與附錄為準。"
                            ),
                            "limitations": (
                                "依目前可取得資料，無法完整確認限制與展望。後續應查閱原文說明資料代表性、泛化能力、計算成本、"
                                "評估公平性與實際部署風險，並以保守方式評估其適用範圍。"
                            ),
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
                    "retry_errors": ai_report.get("retry_errors", []),
                    "error_events": ai_report.get("error_events", []),
                    "fallbacks": ai_report.get("fallbacks", []),
                }
                for e in ai_report.get("ai_errors", [])[:5]:
                    manifest.warning(f"ai_error:{e}")
                retry_errors = ai_report.get("retry_errors") or []
                if retry_errors:
                    manifest.warning(f"ai_retry_errors={len(retry_errors)}")
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
                quotas = bundle.validate(now=reference, require_counts=True, require_sections=False, require_quotas=True, allow_stale=self.allow_stale)
            report["quotas"] = quotas
            manifest.quotas = quotas
            for warning in bundle.warnings:
                if warning not in report["warnings"]:
                    report["warnings"].append(warning)
                    manifest.warning(warning)

            if write:
                with manifest.stage("write_files"):
                    ensure_day_tree(self.root, day)
                    out = write_bundle(bundle, root=self.root, report=report)
                report["files"] = out["files"]
                for f in out["files"]:
                    manifest.add_file(f)

            # P8: optional architecture diagram via Pic-large (best-effort)
            if write and use_ai and self.writer.available:
                with manifest.stage("generate_image"):
                    img_path = self._generate_arch_image(bundle, day)
                    if img_path:
                        report["files"].append(img_path)
                        manifest.add_file(img_path)
                        report.setdefault("images", []).append(img_path)

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

    def _generate_arch_image(self, bundle: DailyBundle, day: date) -> str | None:
        try:
            from core.paths import assets_dir, safe_join
            prompt = (
                f"Technical architecture diagram, clean vector infographic, white background, "
                f"topic: {bundle.tech.name if bundle.tech else 'AI architecture'}. "
                "Show modules: input/perception, model/reasoning, tools/agents, memory, output, safety guardrails. "
                "Minimal labels, professional blue-gray style."
            )
            result = self.writer.client.image(prompt, size="1024x1024")
            item = result[0] if isinstance(result, list) else (result.get("data") or [{}])[0]
            if not isinstance(item, dict):
                raise ValueError(f"unexpected image item type: {type(item).__name__}")
            assets = assets_dir(self.root, day)
            assets.mkdir(parents=True, exist_ok=True)
            out = safe_join(assets, "04_architecture.png")
            self.writer.client.save_image(item, out)
            return str(out)
        except Exception as exc:
            msg = redact_secrets(exc)
            logger.warning("arch image generation failed: %s", msg)
            return None

    @staticmethod
    def _fallback_tech(news: list[Any], papers: list[Any]) -> dict[str, Any]:
        refs = []
        for p in papers[:3]:
            if getattr(p, "url", ""): refs.append(p.url)
        for n in news[:4]:
            if getattr(n, "url", ""): refs.append(n.url)
        refs = list(dict.fromkeys(refs))[:6]
        return {
            "name": "多模態 AI Agent 架構",
            "rationale": "從今日新聞、論文與專案趨勢可見，AI 正從單一問答模型走向能理解多模態輸入、調用工具並完成任務的代理架構，因此選擇此架構作為今日深度拆解主題。",
            "principle": (
                "多模態 AI Agent 架構可分為五層。1) 輸入與感知層：接收文字、影像、語音、感測器、PDF 或系統事件，先做格式轉換、OCR/語音辨識、去識別化與權限檢查，將原始資料轉成可處理的結構化表示。"
                "2) 理解與推理層：由大型語言模型或多模態模型進行意圖辨識、實體抽取、任務分解與規劃，決定要直接回答、查詢資料或呼叫工具。"
                "3) 工具與代理協作層：模型透過工具介面呼叫搜尋、資料庫、程式執行、企業 API、工單系統或機器控制介面；複雜任務可由規劃代理、執行代理、檢查代理分工，降低單一模型失誤。"
                "4) 記憶與知識層：短期記憶保存對話與任務狀態，長期記憶保存知識庫、向量索引、歷史案例與規則；檢索增強生成（RAG）可把外部證據帶入回答，降低幻覺。"
                "5) 輸出、監控與治理層：系統輸出報告、告警、草稿或操作建議，同時記錄來源、提示、工具呼叫、信心度與稽核軌跡。高風險場景必須設計人工覆核、權限邊界、失敗回退與安全策略。"
            ),
            "applications_maritime": (
                "例1：智慧港口航道異常偵測。情境是港務單位監控進港船舶是否偏航、異常停泊或有碰撞風險。輸入資料包含 AIS 軌跡、港區攝影機影像、雷達回波、氣象與潮汐資料。系統流程為感知層對齊時空資料，推理層判斷異常型態，工具層查詢港務規則與船舶檔案，最後產生告警與建議處置。效益是提早預警、降低事故；風險是感測器缺失、天候干擾或模型誤判，需由值班人員覆核。"
                "例2：船舶設備維修助理。情境是輪機人員面對引擎異常。輸入資料為感測器遙測、歷史維修工單、設備手冊與故障照片。代理檢索相似案例、比對手冊步驟，產出檢修清單與零件建議。效益是縮短排查時間；風險是文件過時或幻覺，必須以原廠手冊與工程師判斷為準。"
            ),
            "applications_medical": (
                "例1：放射科報告草稿輔助。情境是醫師需要快速整理影像觀察。輸入資料為 CT/MRI 影像、歷史影像報告與病歷摘要。系統由多模態模型對齊影像與文字，檢索院內指引後生成結構化報告草稿，並標示不確定處。效益是減少文書負擔、提升一致性；風險是誤診或遺漏，必須由醫師最終確認並符合醫療法規。"
                "例2：臨床流程與衛教代理。情境是門診後整理檢查待辦與衛教。輸入資料為病歷、檢驗值、藥囑與院內流程規範。代理檢查缺漏項目、提醒追蹤時間並產生病患可理解的衛教草稿。效益是提升流程完整性；風險涉及個資保護、存取控制與建議過度自動化，需保留臨床人員審核。"
            ),
            "applications_general": (
                "例1：企業知識庫助理。輸入內部規範、合約與客服工單，代理檢索文件後生成有來源引用的回答，協助新人快速上手。"
                "例2：軟體工程代理。輸入 issue、程式碼庫與測試紀錄，代理協助定位 bug、提出修補草稿並生成測試案例，但合併前仍需人工 code review。"
            ),
            "limitations": "主要限制包括：模型幻覺與錯誤工具呼叫、資料品質與權限治理不足、多模態對齊錯誤、即時性與成本壓力，以及高風險場景的責任歸屬不清。實務部署應採用最小權限、來源引用、人工覆核、離線評測與完整稽核紀錄。",
            "reference_urls": refs or ["https://arxiv.org/"],
        }


def run_daily_pipeline(**kwargs: Any) -> dict[str, Any]:
    allow_stale = bool(kwargs.pop("allow_stale", False))
    root = kwargs.pop("root", BASE_DIR)
    return DailyPipeline(root=root, allow_stale=allow_stale).run(**kwargs)
