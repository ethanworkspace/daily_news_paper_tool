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
        content = _clip(getattr(item, "content", "") or getattr(item, "summary", ""), 4000)
        domains = ", ".join(getattr(item, "domains", []) or [])
        prompt = f"""你是 AI 科技日報編輯。請使用繁體中文，根據提供的新聞內容撰寫摘要，不可編造未出現的事實、數字或引述。
輸出 JSON，鍵：
summary(180-350字，清楚說明發生什麼事、AI/技術重點、關鍵角色)；
impact(120-220字，對產業、技術路線、風險或政策的具體影響；若內容不足請明確標示「依目前公開資訊」)；
key_point(一句話重點，35字內，繁體中文)。
新聞標題：{title}
來源：{source}
日期：{date_str}
領域：{domains}
URL：{url}
內容：
{content}
"""
        data = self._json(prompt, model="large", schema_hint='{"summary":"","impact":"","key_point":""}', max_tokens=1600)
        summary = _clip(data.get("summary", ""), 1400)
        impact = _clip(data.get("impact", ""), 1000)
        key_point = _clip(data.get("key_point", ""), 120)
        if not summary or not impact:
            salvage = self._json(
                f"請用繁體中文根據新聞內容輸出JSON：summary(120-220字), impact(80-150字), key_point(30字內)。不可編造。標題:{title}\n內容:{_clip(content,2200)}",
                model="max", schema_hint='{"summary":"","impact":"","key_point":""}', max_tokens=900)
            summary = summary or _clip(salvage.get("summary", ""), 1400)
            impact = impact or _clip(salvage.get("impact", ""), 1000)
            key_point = key_point or _clip(salvage.get("key_point", ""), 120)
        if not summary:
            summary = _clip(content, 360) or "（無可用摘要，建議查閱原文）"
        if not impact:
            impact = f"依目前公開資訊，此新聞與 {domains or 'AI'} 相關，可能影響相關產業的技術採用、風險控管或投資決策；實際影響仍需以原文與後續發展為準。"
        if not key_point:
            key_point = _clip(title, 35)
        return {"summary": summary, "impact": impact, "key_point": key_point}

    # ---------- 論文 ----------
    def summarize_paper(self, item: Any) -> dict[str, str]:
        title = _clip(getattr(item, "title", ""), 500)
        abstract = _clip(getattr(item, "abstract", ""), 4500)
        fulltext = _clip(getattr(item, "fulltext_excerpt", ""), 18000)
        venue = _clip(getattr(item, "venue", "") or getattr(item, "journal", ""), 300)
        impact = _clip(getattr(item, "impact_factor", ""), 120)
        code_url = _clip(getattr(item, "code_url", ""), 500)
        prompt = f"""你是 AI 論文深度分析師。請使用繁體中文，僅根據提供的論文摘要/全文摘錄分析，不可編造未出現的實驗數字、資料集規模、基線名稱或比較結果；若資料不足，必須明確標示「依目前可取得資料，無法確認」。
輸出 JSON，鍵：
background(背景與目的，220-420字)：說明研究問題、現有方法缺口、為何重要、本文目標與貢獻定位。
method(方法，500-900字，這是最重要欄位)：必須深度解說方法。請盡量涵蓋：問題設定/輸入輸出；模型或系統整體架構；核心模組或演算法機制；資料前處理/特徵/表示方式；訓練目標、損失函數或最佳化策略（若摘錄有）；推論或執行流程；與既有方法的關鍵差異（僅限摘錄可支持）。用清楚的技術語言分層說明，不要只寫一句泛泛描述。
results(結果，220-420字)：說明作者報告的主要實驗結果、比較結論、消融或案例發現；若摘錄無明確數字，必須明確寫「摘錄未提供可驗證數字」，並描述可觀察到的定性結論。
limitations(限制與展望，180-320字)：說明資料/方法/評估/部署限制、潛在風險與後續研究方向；不確定處要保守表述。
論文：{title}
期刊/會議：{venue}
影響指標：{impact}
程式碼：{code_url}
摘要：
{abstract}
全文摘錄：
{fulltext}
"""
        data = self._json(prompt, model="max", schema_hint='{"background":"","method":"","results":"","limitations":""}', max_tokens=3600)
        out = {
            "background": _clip(data.get("background", ""), 3200),
            "method": _clip(data.get("method", ""), 5200),
            "results": _clip(data.get("results", ""), 3200),
            "limitations": _clip(data.get("limitations", ""), 2600),
        }
        placeholders = {
            "資訊不足，待人工補充。", "（待補充）", "（待補充：需模型或人工分析）",
            "依目前可取得資料不足，需人工查閱原文補充。"
        }
        for key, ask, mt, min_len in [
            (
                "background",
                f"用繁體中文詳細撰寫論文背景與目的，220-420字。需包含：研究問題、既有缺口、本文目標與貢獻。不可編造。JSON {{\"background\":\"...\"}}。標題:{title}\n摘要:{_clip(abstract,2600)}\n全文摘錄:{_clip(fulltext,2500)}",
                1200,
                120,
            ),
            (
                "method",
                f"用繁體中文深度解說論文方法，500-900字，這是最重要欄位。必須盡量涵蓋：問題設定與輸入輸出；整體架構；核心模組/演算法機制；資料處理或表示；訓練目標/損失/最佳化（若可確認）；推論流程；關鍵設計理由。僅根據提供內容，不可編造。JSON {{\"method\":\"...\"}}。標題:{title}\n摘要:{_clip(abstract,2200)}\n全文摘錄:{_clip(fulltext,9000)}",
                2200,
                260,
            ),
            (
                "results",
                f"用繁體中文詳細撰寫論文結果，220-420字。若無明確數字必須寫「摘錄未提供可驗證數字」，並描述可見的定性結論、比較或消融觀察。不可編造數字。JSON {{\"results\":\"...\"}}。標題:{title}\n摘要:{_clip(abstract,2200)}\n全文摘錄:{_clip(fulltext,7000)}",
                1400,
                120,
            ),
            (
                "limitations",
                f"用繁體中文撰寫論文限制與展望，180-320字。需包含方法/資料/評估/部署面向的限制與後續方向，不確定處保守表述。JSON {{\"limitations\":\"...\"}}。標題:{title}\n摘要:{_clip(abstract,2200)}\n全文摘錄:{_clip(fulltext,3500)}",
                1100,
                100,
            ),
        ]:
            cur = _clip(out.get(key, ""), 5200)
            if (not cur) or cur in placeholders or len(cur) < min_len or "模型未產出" in cur:
                s = self._json(ask, model="max", schema_hint='{"'+key+'":""}', max_tokens=mt)
                val = _clip(s.get(key, ""), 5200)
                if val and len(val) >= max(60, min_len // 2):
                    out[key] = val
        if not any(v and v not in placeholders for v in out.values()):
            fallback = _clip(abstract or fulltext, 1600)
            out["background"] = f"本研究主題為「{title}」。{fallback[:520]} 依目前可取得資料，本文的具體問題設定與貢獻細節仍需查閱原文引言與方法章節進一步確認。"
            out["method"] = (
                "依目前可取得的摘要/全文摘錄，尚不足以完整還原方法細節。從可見資訊可初步判斷此研究與 "
                f"{title} 相關，但模型架構、輸入輸出定義、核心模組機制、訓練目標與損失函數、最佳化流程、推論步驟及關鍵超參數等關鍵技術內容，"
                "仍需查閱原文方法章節、架構圖與實驗設定後才能可靠補齊；目前不宜臆測具體實作細節。"
            )
            out["results"] = "摘錄未提供可驗證數字。依目前可取得資料，只能確認作者提出了相關方法方向與初步結論，但缺乏可核對的實驗指標、資料集規模、基線比較與消融結果，因此無法可靠總結量化成效。"
            out["limitations"] = "依目前可取得資料，無法完整評估此研究的外部效度與部署成本。潛在限制可能包括資料代表性、基線比較公平性、計算資源需求、泛化能力與實際應用風險；後續需查閱原文實驗、附錄與限制說明確認。"
        for k in ("background","method","results","limitations"):
            v = _clip(out.get(k, ""), 5200)
            if not v or v in placeholders or "模型未產出" in str(v):
                if k == "background":
                    out[k] = f"本研究主題為「{title}」。依目前可取得資料，僅能確認其研究方向與問題意識，詳細背景與貢獻需查閱原文補充。"
                elif k == "method":
                    out[k] = "依目前可取得資料，無法可靠還原完整方法。需查閱原文確認問題設定、模型架構、核心模組、訓練目標與推論流程等技術細節，目前不宜臆測。"
                elif k == "results":
                    out[k] = "摘錄未提供可驗證數字。依目前可取得資料，無法確認具體實驗成效，需查閱原文結果表格與消融分析。"
                else:
                    out[k] = "依目前可取得資料，無法完整確認限制與展望；需查閱原文討論資料代表性、泛化能力、計算成本與部署風險。"
            else:
                out[k] = v
        return out

    # ---------- Repo ----------
    def summarize_repo(self, item: Any) -> dict[str, str]:
        name = _clip(getattr(item, "full_name", ""), 200)
        desc = _clip(getattr(item, "description", ""), 1200)
        readme = _clip(getattr(item, "readme_excerpt", ""), 10000)
        topics = ", ".join(getattr(item, "topics", []) or [])
        lang = _clip(getattr(item, "language", ""), 64)
        stars = getattr(item, "stars", 0)
        paper = _clip(getattr(item, "paper_url", "") or getattr(item, "paired_paper", ""), 500)
        prompt = f"""你是資深軟體/AI 架構師。請使用繁體中文，僅根據 README 摘錄與專案資訊分析，不可編造不存在的功能、效能數字或部署能力。
輸出 JSON，鍵：
what(這個專案在做什麼,150-300字，說明目標使用者與核心問題),
tech(技術重點,150-320字，說明語言/框架/模型/推論或資料流程等可見技術),
architecture(架構與流程,180-360字，說明模組、資料流或執行流程；若README不足請明確標示推斷依據不足)。
Repo：{name}
語言：{lang}  Stars：{stars}
Topics：{topics}
描述：{desc}
配對論文：{paper}
README 摘錄：
{readme}
"""
        data = self._json(prompt, model="coder", schema_hint='{"what":"","tech":"","architecture":""}', max_tokens=2200)
        out = {
            "what": _clip(data.get("what", ""), 1800),
            "tech": _clip(data.get("tech", ""), 1800),
            "architecture": _clip(data.get("architecture", ""), 2200),
        }
        placeholders = {"資訊不足，待人工補充。", "（待補充：需模型或人工分析 README/程式結構）", "README 未提供完整架構章節，需進一步檢視原始碼目錄與模組邊界。"}
        for key, ask, mt in [
            ("what", f"用繁體中文說明這個 GitHub 專案在做什麼、解決什麼問題，150-260字。JSON {{\"what\":\"...\"}}。Repo:{name}\n描述:{desc}\nREADME:{_clip(readme,2200)}", 900),
            ("tech", f"用繁體中文說明這個專案的技術重點，150-260字。JSON {{\"tech\":\"...\"}}。Repo:{name}\n語言:{lang}\nTopics:{topics}\nREADME:{_clip(readme,2600)}", 900),
            ("architecture", f"用繁體中文說明這個專案的架構與流程，180-300字；若依據不足請明確標示。JSON {{\"architecture\":\"...\"}}。Repo:{name}\nREADME:{_clip(readme,3200)}", 1100),
        ]:
            if (not _clip(out.get(key, ""), 10)) or out.get(key) in placeholders:
                s = self._json(ask, model="max", schema_hint='{"'+key+'":""}', max_tokens=mt)
                val = _clip(s.get(key, ""), 2200)
                if val:
                    out[key] = val
        if not any(v and v not in placeholders for v in out.values()):
            out["what"] = desc or f"{name} 是一個與 AI 相關的開源專案，需進一步檢視 README 與程式碼確認其完整目標。"
            out["tech"] = f"主要語言為 {lang or '未標註'}；Topics：{topics or '未標註'}。依目前 README 摘錄可見與 AI/軟體工程相關實作，但技術細節需進一步確認。"
            out["architecture"] = "README 摘錄未提供完整架構章節；目前無法可靠還原模組邊界與資料流，建議後續檢視原始碼目錄、入口點與設定檔。"
        for k in ("what","tech","architecture"):
            v = out.get(k, "")
            if not v or v in placeholders or "模型未產出" in str(v):
                if k == "what":
                    out[k] = desc or f"{name} 是一個與 AI 相關的開源專案。"
                elif k == "tech":
                    out[k] = f"主要語言：{lang or '未標註'}；Topics：{topics or '未標註'}。"
                else:
                    out[k] = "README 摘錄不足以完整還原架構，需人工檢視原始碼模組與執行流程。"
        return out

    # ---------- 架構深拆 ----------
    def write_tech_arch(self, *, date_str: str, news: list[Any], papers: list[Any], repos: list[Any]) -> dict[str, Any]:
        news_ctx = "\n".join(f"- {getattr(n,'title','')} | {getattr(n,'url','')}" for n in news[:10])
        paper_ctx = "\n".join(f"- {getattr(p,'title','')} ({getattr(p,'venue','') or getattr(p,'journal','')}) | {getattr(p,'url','')}" for p in papers[:5])
        repo_ctx = "\n".join(f"- {getattr(r,'full_name','')}: {getattr(r,'description','')[:160]} | {getattr(r,'html_url','')}" for r in repos[:5])
        prompt = f"""你是 AI 架構研究員。請從今日素材中挑選一個最具代表性的「最新 AI 技術架構」做深度拆解。
請使用繁體中文，避免空泛口號；必須清楚說明架構元件、資料流、控制流與部署考量。不可編造不存在的產品能力或實驗數字。
輸出 JSON，鍵：
name(架構名稱),
rationale(為何今日選它,120-220字),
principle(原理與核心機制,450-900字，至少說明輸入/感知、模型推理、工具或代理協作、記憶/資料層、輸出與監控),
applications_maritime(海事應用,260-450字，至少2個具體例子：情境、輸入資料、系統如何運作、價值與風險),
applications_medical(醫療應用,260-450字，至少2個具體例子：情境、輸入資料、系統如何運作、價值與合規風險),
applications_general(其他產業應用,180-320字，至少2個具體例子),
limitations(限制與風險,180-320字),
reference_urls(陣列,1-6個https URL,優先使用今日素材中的真實URL)。

日期：{date_str}
今日新聞：
{news_ctx}
今日論文：
{paper_ctx}
今日專案：
{repo_ctx}
"""
        data = self._json(prompt, model="max", schema_hint='{"name":"","rationale":"","principle":"","applications_maritime":"","applications_medical":"","applications_general":"","limitations":"","reference_urls":[]}', max_tokens=3600)
        refs = [str(u).strip() for u in (data.get("reference_urls") or []) if str(u).strip().startswith("http")]
        if not refs:
            for pp in papers[:3]:
                u = getattr(pp, "url", "")
                if u: refs.append(u)
            for n in news[:2]:
                u = getattr(n, "url", "")
                if u: refs.append(u)
            for r in repos[:1]:
                u = getattr(r, "html_url", "")
                if u: refs.append(u)
        refs = list(dict.fromkeys(refs))[:6]
        name = _clip(data.get("name", ""), 200) or "多模態 AI Agent 架構"

        for key, ask, mt in [
            ("rationale", f"用繁體中文說明為何今日選擇{name}，120-200字。JSON {{\"rationale\":\"...\"}}。新聞:{_clip(news_ctx,1200)}\n論文:{_clip(paper_ctx,900)}", 700),
            ("principle", f"用繁體中文深度說明{name}的原理與架構，350-500字。必須包含：輸入/感知層、核心模型/推理層、工具或代理協作層、記憶與資料層、輸出與監控治理層。避免冗長。JSON {{\"principle\":\"...\"}}", 1400),
            ("applications_maritime", f"用繁體中文說明{name}在海事領域的2個具體應用例子，每個例子包含情境、輸入資料、系統流程、效益與風險，合計260-420字。JSON {{\"applications_maritime\":\"...\"}}", 1200),
            ("applications_medical", f"用繁體中文說明{name}在醫療領域的2個具體應用例子，每個例子包含情境、輸入資料、系統流程、效益與合規風險，合計260-420字。JSON {{\"applications_medical\":\"...\"}}", 1200),
            ("applications_general", f"用繁體中文說明{name}在其他產業的2個具體應用例子，合計180-300字。JSON {{\"applications_general\":\"...\"}}", 900),
            ("limitations", f"用繁體中文說明{name}的限制與風險，180-300字，包含技術、資料、成本、治理。JSON {{\"limitations\":\"...\"}}", 900),
        ]:
            if len(_clip(data.get(key, ""), 2000)) < 80:
                s = self._json(ask, model="max", schema_hint='{ "'+key+'":"" }', max_tokens=mt)
                if _clip(s.get(key, ""), 2000):
                    data[key] = s[key]

        principle = _clip(data.get("principle", ""), 4500)
        if len(principle) < 220:
            principle = (
                f"{name} 通常可拆解為五個層次。第一，輸入與感知層負責接收文字、影像、感測器、文件或 API 事件，並進行清理、標準化與權限檢查。"
                "第二，核心模型與推理層使用大型模型或多模態模型理解任務、抽取實體、生成假設並規劃步驟。"
                "第三，工具與代理協作層讓模型呼叫搜尋、資料庫、程式執行、企業系統或外部 API，並由規則或子代理完成分工。"
                "第四，記憶與資料層保存短期對話上下文、長期知識、任務狀態與稽核紀錄，常搭配向量檢索與結構化資料庫。"
                "第五，輸出與監控治理層將結果轉為報告、告警或操作建議，同時記錄來源、信心度與人工覆核點，確保可追溯與安全。"
            )
        maritime = _clip(data.get("applications_maritime", ""), 2600)
        if len(maritime) < 120:
            maritime = (
                "例1：港口航道異常偵測。輸入 AIS 船舶軌跡、雷達/港區攝影機影像與氣象資料，系統先由感知層對齊時空資料，推理層判斷偏航、異常停泊或碰撞風險，工具層呼叫港務規則引擎與告警系統通知值班人員。效益是提早發現風險；風險是感測缺失或惡劣天候造成誤判。"
                "例2：船舶維修決策輔助。輸入引擎感測資料、維修手冊與歷史工單，代理檢索相似故障並產出檢修建議。效益是縮短排查時間；風險是模型幻覺或資料不完整，必須保留工程師覆核。"
            )
        medical = _clip(data.get("applications_medical", ""), 2600)
        if len(medical) < 120:
            medical = (
                "例1：放射科影像輔助摘要。輸入 CT/MRI 影像與既有報告文字，模型先做影像特徵與病歷文字對齊，再生成結構化草稿供醫師確認。效益是減少文書時間；風險是誤判與責任歸屬，必須有人類醫師最終簽核。"
                "例2：臨床流程代理。輸入病歷、檢驗結果與院內指引，代理協助整理待辦、提醒檢查缺漏並草擬衛教說明。效益是提升流程效率；風險涉及病患隱私、存取控制與法規遵循。"
            )

        return {
            "name": name,
            "rationale": _clip(data.get("rationale", ""), 1200) or "依今日新聞、論文與 GitHub 專案的共同趨勢，選擇此架構作為代表性技術。",
            "principle": principle,
            "applications_maritime": maritime,
            "applications_medical": medical,
            "applications_general": _clip(data.get("applications_general", ""), 1800) or "例1：企業知識助理，輸入內部文件與工單，代理檢索並生成可追溯答案。例2：軟體工程代理，輸入 issue 與程式碼庫，協助定位 bug、產生修補草稿與測試建議，但需人工審查。",
            "limitations": _clip(data.get("limitations", ""), 1600) or "限制包括模型幻覺、資料品質不穩、跨系統整合成本高、即時性不足與權限治理複雜。高風險場景必須保留人工覆核、完整稽核紀錄與明確責任邊界。",
            "reference_urls": refs or ["https://arxiv.org/"],
        }
