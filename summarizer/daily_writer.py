"""P5/P6：以 iAI 產出新格式每日報告內容（結構化、可驗收）。

設計原則：
- 預設使用 IAIClient：主寫 Furen-max，輔助/摘要 Furen-large，repo/git 類任務可用 Furen-coder。
- 任何模型輸出都經過欄位/長度/URL 安全檢查後才落檔。
- 模型失敗時降級為可稽核的規則式內容（不編造來源/連結）。
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict
from typing import Any

from config import IAI_API_KEYS
from core.security import redact_secrets
from iai_client import IAIClient, IAIClientError


def _clip(text: object, limit: int) -> str:
    value = re.sub(r"\s+", " ", str(text or "")).strip()
    return value[:limit]


def _bullets(items: list[str], limit: int = 5) -> str:
    cleaned = [f"- {_clip(item, 220)}" for item in items if str(item or "").strip()]
    return "\n".join(cleaned[:limit]) or "- （無資料）"


class DailyWriter:
    def __init__(self, client: IAIClient | None = None):
        self.client = client or IAIClient()
        self.last_errors: list[str] = []
        self.fallbacks: list[str] = []

    @property
    def available(self) -> bool:
        return self.client.has_keys

    def _chat(self, prompt: str, *, model: str = "max", max_tokens: int = 1800, temperature: float = 0.2) -> str:
        if not self.available:
            self.fallbacks.append(f"chat:{model}:no_keys")
            return ""
        try:
            if model == "coder":
                return self.client.chat_coder(prompt, max_tokens=max_tokens, temperature=temperature)
            if model == "large":
                return self.client.chat_large(prompt, max_tokens=max_tokens, temperature=temperature)
            return self.client.chat_max(prompt, max_tokens=max_tokens, temperature=temperature)
        except IAIClientError as exc:
            msg = redact_secrets(exc)
            self.last_errors.append(f"{model}:{msg}")
            return ""
        except Exception as exc:  # noqa: BLE001
            msg = redact_secrets(exc)
            self.last_errors.append(f"{model}:{msg}")
            return ""

    def _json(self, prompt: str, *, model: str = "max", schema_hint: str = "", max_tokens: int = 1800) -> dict[str, Any]:
        if not self.available:
            self.fallbacks.append(f"json:{model}:no_keys")
            return {}
        attempts = [(model, max_tokens), (model, max(max_tokens, 3200))]
        # if still failing, switch to max as stronger fallback for structure
        if model != "max":
            attempts.append(("max", max(max_tokens, 3200)))
        last_exc = None
        for mdl, mt in attempts:
            try:
                data = self.client.chat_json(prompt, model=mdl, schema_hint=schema_hint, max_tokens=mt)
                if isinstance(data, dict) and data:
                    return data
                self.fallbacks.append(f"json:{mdl}:non_dict")
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
                self.last_errors.append(f"{mdl}:{redact_secrets(exc)}")
                self.fallbacks.append(f"json:{mdl}:error")
        if last_exc:
            return {}
        return {}

    def report(self) -> dict[str, Any]:
        usage = {}
        try:
            usage = self.client.usage() if hasattr(self.client, "usage") else {}
        except Exception:
            usage = {}
        return {
            "available": self.available,
            "model_usage": usage,
            "ai_errors": self.last_errors[-20:],
            "fallbacks": self.fallbacks[-50:],
        }

    # ---------- 新聞 ----------
    def summarize_news(self, item: Any) -> dict[str, str]:
        title = _clip(getattr(item, "title", ""), 300)
        url = _clip(getattr(item, "url", ""), 500)
        source = _clip(getattr(item, "source", ""), 120)
        published = getattr(item, "published_at", None)
        date_str = published.isoformat() if published else ""
        content = _clip(getattr(item, "content", "") or getattr(item, "summary", ""), 3500)
        domains = ", ".join(getattr(item, "domains", []) or [])
        prompt = f"""你是 AI 科技日報編輯。請用繁體中文，根據提供的新聞內容撰寫摘要，不可編造未出現的事實或數字。
輸出 JSON，鍵：summary(150-300字，說明事件與AI重點), impact(80-180字，產業/技術影響), key_point(一句話重點,40字內)。
新聞標題：{title}
來源：{source}
日期：{date_str}
領域：{domains}
URL：{url}
內容：
{content}
"""
        data = self._json(prompt, model="large", schema_hint='{"summary":"","impact":"","key_point":""}', max_tokens=1400)
        summary = _clip(data.get("summary", ""), 1200)
        impact = _clip(data.get("impact", ""), 800)
        key_point = _clip(data.get("key_point", ""), 120)
        if not summary or not impact:
            # field-level salvage prompt
            salvage = self._json(
                f"請根據新聞內容輸出JSON：summary(100-180字), impact(60-120字)。不可編造。標題:{title}\n內容:{_clip(content,1800)}",
                model="max", schema_hint='{"summary":"","impact":""}', max_tokens=900)
            summary = summary or _clip(salvage.get("summary", ""), 1200)
            impact = impact or _clip(salvage.get("impact", ""), 800)
        if not summary:
            summary = _clip(content, 320) or "（無可用摘要）"
        if not impact:
            impact = f"此新聞與 {domains or 'AI'} 相關，可能影響相關產業的技術採用與風險管理；細節需以原文為準。"
        if not key_point:
            key_point = _clip(title, 60)
        return {"summary": summary, "impact": impact, "key_point": key_point}

    # ---------- 論文 ----------
    def summarize_paper(self, item: Any) -> dict[str, str]:
        title = _clip(getattr(item, "title", ""), 500)
        abstract = _clip(getattr(item, "abstract", ""), 3000)
        fulltext = _clip(getattr(item, "fulltext_excerpt", ""), 12000)
        venue = _clip(getattr(item, "venue", "") or getattr(item, "journal", ""), 300)
        impact = _clip(getattr(item, "impact_factor", ""), 120)
        code_url = _clip(getattr(item, "code_url", ""), 500)
        prompt = f"""你是 AI 論文分析師。請用繁體中文，僅根據提供的論文摘要/全文摘錄分析，不可編造實驗數字。
輸出 JSON，鍵：
background(背景與目的,120-260字),
method(方法,150-320字),
results(結果,120-280字；若摘錄無明確數字請說明依摘錄可見的結果),
limitations(限制與展望,100-220字)。
論文：{title}
期刊/會議：{venue}
影響指標：{impact}
程式碼：{code_url}
摘要：
{abstract}
全文摘錄：
{fulltext}
"""
        data = self._json(prompt, model="max", schema_hint='{"background":"","method":"","results":"","limitations":""}', max_tokens=2400)
        out = {
            "background": _clip(data.get("background", ""), 1500),
            "method": _clip(data.get("method", ""), 1800),
            "results": _clip(data.get("results", ""), 1500),
            "limitations": _clip(data.get("limitations", ""), 1200),
        }
        placeholders = {"（模型未產出，待補充）", "（待補充）"}
        for key, ask, mt in [
            ("background", f"用繁體中文寫論文背景與目的，120-220字。JSON {{\"background\":\"...\"}}。標題:{title}\n摘要:{_clip(abstract,2000)}", 900),
            ("method", f"用繁體中文寫論文方法，150-260字。JSON {{\"method\":\"...\"}}。標題:{title}\n摘要:{_clip(abstract,1500)}\n全文摘錄:{_clip(fulltext,2500)}", 1000),
            ("results", f"用繁體中文寫論文結果；若無明確數字請說明依摘錄可見結果。120-220字。JSON {{\"results\":\"...\"}}。標題:{title}\n摘要:{_clip(abstract,1500)}\n全文摘錄:{_clip(fulltext,2500)}", 1000),
            ("limitations", f"用繁體中文寫限制與展望，100-180字。JSON {{\"limitations\":\"...\"}}。標題:{title}\n摘要:{_clip(abstract,1500)}", 800),
        ]:
            if (not _clip(out.get(key, ""), 10)) or out.get(key) in placeholders:
                s = self._json(ask, model="max", schema_hint='{"'+key+'":""}', max_tokens=mt)
                val = _clip(s.get(key, ""), 1800)
                if val:
                    out[key] = val
        if not any(v and v not in placeholders for v in out.values()):
            fallback = _clip(abstract or fulltext, 900)
            out["background"] = f"本研究主題為「{title}」。{fallback[:300]}"
            out["method"] = "需依論文全文進一步確認方法細節；目前依摘要/摘錄判斷其屬於 AI 相關研究。"
            out["results"] = "摘要/摘錄未提供足夠可驗證的完整實驗數字，需查閱原文結果章節。"
            out["limitations"] = "需確認資料集、基線、泛化範圍與實際部署限制。"
        for k, v in out.items():
            if not v or v in placeholders:
                out[k] = "資訊不足，待人工補充。"
        return out

    # ---------- Repo ----------
    def summarize_repo(self, item: Any) -> dict[str, str]:
        name = _clip(getattr(item, "full_name", ""), 200)
        desc = _clip(getattr(item, "description", ""), 1000)
        readme = _clip(getattr(item, "readme_excerpt", ""), 9000)
        topics = ", ".join(getattr(item, "topics", []) or [])
        lang = _clip(getattr(item, "language", ""), 64)
        stars = getattr(item, "stars", 0)
        paper = _clip(getattr(item, "paper_url", "") or getattr(item, "paired_paper", ""), 500)
        prompt = f"""你是資深軟體/AI 架構師。請用繁體中文，僅根據 README 摘錄與專案資訊分析，不可編造不存在的功能。
輸出 JSON，鍵：
what(這個專案在做什麼,120-260字),
tech(技術重點,120-260字),
architecture(架構與流程,150-320字；可依README結構推斷但要標明依據不足處)。
Repo：{name}
語言：{lang}  Stars：{stars}
Topics：{topics}
描述：{desc}
配對論文：{paper}
README 摘錄：
{readme}
"""
        data = self._json(prompt, model="coder", schema_hint='{"what":"","tech":"","architecture":""}', max_tokens=1800)
        out = {
            "what": _clip(data.get("what", ""), 1500),
            "tech": _clip(data.get("tech", ""), 1500),
            "architecture": _clip(data.get("architecture", ""), 1800),
        }
        if not any(out.values()):
            out["what"] = desc or f"{name} 是一個與 AI 相關的開源專案。"
            out["tech"] = f"主要語言：{lang or '未知'}；Topics：{topics or '未標註'}。"
            out["architecture"] = "README 未提供完整架構章節，需進一步檢視原始碼目錄與模組邊界。"
        for k, v in out.items():
            if not v:
                out[k] = "（模型未產出，待補充）"
        return out

    # ---------- 架構深拆 ----------
    def write_tech_arch(self, *, date_str: str, news: list[Any], papers: list[Any], repos: list[Any]) -> dict[str, Any]:
        news_ctx = "\n".join(f"- {getattr(n,'title','')}" for n in news[:10])
        paper_ctx = "\n".join(f"- {getattr(p,'title','')} ({getattr(p,'venue','') or getattr(p,'journal','')})" for p in papers[:5])
        repo_ctx = "\n".join(f"- {getattr(r,'full_name','')}: {getattr(r,'description','')[:120]}" for r in repos[:5])
        prompt = f"""你是 AI 架構研究員。請從今日素材中挑選一個最具代表性的「最新 AI 技術架構」做深度拆解。
必須輸出 JSON，鍵：
name(架構名稱),
rationale(為何今日選它,80-180字),
principle(原理與核心機制,250-500字),
applications_maritime(海事應用,180-350字，具體場景),
applications_medical(醫療應用,180-350字，具體場景),
applications_general(其他產業應用,120-260字),
limitations(限制與風險,100-220字),
reference_urls(陣列,1-5個https URL,優先使用今日素材中的真實URL)。

日期：{date_str}
今日新聞：
{news_ctx}
今日論文：
{paper_ctx}
今日專案：
{repo_ctx}
"""
        data = self._json(prompt, model="max", schema_hint='{"name":"","rationale":"","principle":"","applications_maritime":"","applications_medical":"","applications_general":"","limitations":"","reference_urls":[]}', max_tokens=2600)
        refs = [str(u).strip() for u in (data.get("reference_urls") or []) if str(u).strip().startswith("http")]
        if not refs:
            for pp in papers[:2]:
                u = getattr(pp, "url", "")
                if u: refs.append(u)
            for n in news[:2]:
                u = getattr(n, "url", "")
                if u: refs.append(u)
        refs = list(dict.fromkeys(refs))[:5]
        name = _clip(data.get("name", ""), 200) or "多模態 AI Agent 架構"
        # field salvage for common truncation
        for key, ask, mt in [
            ("principle", f"用繁體中文說明{name}的原理與核心機制，200-350字，JSON {{\"principle\":\"...\"}}", 900),
            ("applications_maritime", f"用繁體中文說明{name}在海事領域的2個具體應用場景與部署考量，150-260字，JSON {{\"applications_maritime\":\"...\"}}", 700),
            ("applications_medical", f"用繁體中文說明{name}在醫療領域的2個具體應用場景與合規考量，150-260字，JSON {{\"applications_medical\":\"...\"}}", 700),
        ]:
            if not _clip(data.get(key, ""), 10):
                s = self._json(ask, model="max", schema_hint='{ "'+key+'":"" }', max_tokens=mt)
                if s.get(key):
                    data[key] = s[key]
        return {
            "name": name,
            "rationale": _clip(data.get("rationale", ""), 800) or "依今日素材中模型/代理/多模態趨勢選定。",
            "principle": _clip(data.get("principle", ""), 2500) or "（待補充原理）",
            "applications_maritime": _clip(data.get("applications_maritime", ""), 2000) or "可用於船舶感知、航線異常偵測、港口調度與海事文件理解；部署需考慮低頻寬、惡劣氣候與安全驗證。",
            "applications_medical": _clip(data.get("applications_medical", ""), 2000) or "可用於多模態病歷理解、影像輔助判讀與臨床流程代理；需符合隱私、可追溯與醫療法規要求。",
            "applications_general": _clip(data.get("applications_general", ""), 1500) or "可擴展至企業知識助理、自動化客服與軟體工程代理。",
            "limitations": _clip(data.get("limitations", ""), 1200) or "需關注幻覺、資料外洩、成本與可解釋性。",
            "reference_urls": refs or ["https://arxiv.org/"],
        }
