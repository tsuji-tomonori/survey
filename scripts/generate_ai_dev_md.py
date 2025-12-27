import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]
JSONL_PATH = PROJECT_ROOT / "arxiv_cs_peerreview_proxy_2025_daily.jsonl"
OUT_DIR = PROJECT_ROOT / "codex" / "ai-dev-2025"


KEYWORDS = [
    # Software engineering & coding
    "software", "engineer", "engineering", "developer", "ide", "devops", "llmops",
    "code", "coding", "program", "programming", "program synthesis", "synthesis",
    "compiler", "static analysis", "type inference", "verification", "formal", "refactor",
    "bug", "debug", "repair", "mutation", "trace", "profiling", "performance",
    "test", "testing", "fuzz", "coverage", "symbolic", "unit test", "integration test",
    # LLMs & agents for dev
    "llm", "large language model", "code llm", "code generation", "tool use", "toolformer",
    "agent", "multi-agent", "automation", "copilot", "retrieval", "rag", "memory",
    "prompt", "system prompt", "instruction", "alignment", "guardrail", "safety",
    # MLOps / productivity / eval
    "evaluation", "benchmark", "reliability", "hallucination", "grounding", "planning",
    "workflow", "pipeline", "api", "framework", "library", "dataset"
]

# Category boosts (arXiv primary_category)
CATEGORY_BOOSTS = {
    "cs.SE": 6.0,  # Software Engineering
    "cs.PL": 4.0,  # Programming Languages
    "cs.AI": 3.0,  # AI
    "cs.CL": 3.0,  # Computation and Language (LLMs)
    "cs.LG": 2.5,  # Machine Learning
    "cs.DC": 1.5,  # Distributed/Systems
    "cs.CR": 1.5,  # Security
    "cs.DB": 1.5,  # Databases (RAG infra)
    "cs.IR": 1.5,  # Information Retrieval (RAG)
}


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\-\s_]+", "", text)
    text = text.strip().replace(" ", "-")
    text = re.sub(r"-+", "-", text)
    return text[:120]


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    items = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                items.append(obj)
            except json.JSONDecodeError:
                continue
    return items


def score_item(it: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
    title = (it.get("title") or "").lower()
    cats = it.get("categories") or []
    primary = (it.get("primary_category") or "").strip()

    # Keyword matches in title
    kw_score = 0.0
    matched: List[str] = []
    for kw in KEYWORDS:
        if kw in title:
            kw_score += 1.0
            matched.append(kw)

    # Category boost
    cat_score = 0.0
    if primary in CATEGORY_BOOSTS:
        cat_score += CATEGORY_BOOSTS[primary]
    for c in cats:
        if c in CATEGORY_BOOSTS and c != primary:
            cat_score += 0.5 * CATEGORY_BOOSTS[c]

    # Recency bonus
    recency = 0.0
    try:
        pub = it.get("published") or it.get("day")
        if pub:
            # handle both ISO and YYYY-MM-DD
            if "T" in pub:
                dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
            else:
                dt = datetime.fromisoformat(pub + "T00:00:00+00:00")
            # Simple linear recency: newer gets small boost
            base = datetime(2025, 1, 1, tzinfo=dt.tzinfo)
            delta_days = (dt - base).days
            recency = max(0.0, min(2.0, delta_days / 30.0))
    except Exception:
        pass

    total = kw_score + cat_score + recency
    it["_matched_keywords"] = matched
    it["_kw_score"] = kw_score
    it["_cat_score"] = cat_score
    it["_recency"] = recency
    it["_total_score"] = total
    return total, it


def reason_bullets(it: Dict[str, Any]) -> List[str]:
    title = it.get("title", "")
    primary = it.get("primary_category", "")
    cats = it.get("categories") or []
    kws = it.get("_matched_keywords") or []

    bullets = []
    # Map some common keywords to rationale phrasing
    rationale_map = {
        "code": "コード生成や補完の品質向上に直結する知見",
        "program": "プログラム理解・合成・検証に関する基礎と応用",
        "programming": "開発実務へのAI適用を促進する設計指針",
        "program synthesis": "仕様からの自動コード生成に関する最新動向",
        "compiler": "コンパイラ・最適化観点からの性能/安全性の向上",
        "static analysis": "静的解析による品質保証・自動修復の可能性",
        "type inference": "型推論・制約解決を用いた堅牢化",
        "verification": "形式手法・検証による信頼性向上",
        "refactor": "自動リファクタリング/保守性向上のベストプラクティス",
        "bug": "バグ検出・原因推定・自動修復の実践",
        "debug": "デバッグ支援・可観測性の強化",
        "repair": "コード自動修復/提案の評価・限界",
        "test": "テスト生成・カバレッジ・回帰抑止の自動化",
        "fuzz": "ファジング/探索で堅牢性を高める手法",
        "coverage": "テスト網羅性や不足検出の改善",
        "symbolic": "シンボリック実行/SMTでの厳密検証",
        "llm": "LLMの能力・限界・安全性に関する最新知見",
        "large language model": "LLMの能力・限界・安全性に関する最新知見",
        "code generation": "プロダクション品質のコード生成に向けた工夫",
        "tool use": "ツール呼び出し/関数呼び出しの信頼化",
        "agent": "エージェント/マルチエージェントの設計・評価",
        "multi-agent": "マルチエージェント協調による開発自動化",
        "retrieval": "RAG/知識接地での幻覚抑制・正確性向上",
        "rag": "RAG/知識接地での幻覚抑制・正確性向上",
        "prompt": "プロンプト設計・評価・堅牢化の実践",
        "alignment": "アラインメント/安全性・ガードレールの適用",
        "guardrail": "ガードレール/ポリシーでの誤用防止",
        "evaluation": "ベンチマーク/評価法での実力測定",
        "benchmark": "ベンチマーク/評価法での実力測定",
        "workflow": "ワークフロー/パイプライン設計の実装知見",
        "framework": "フレームワーク/ライブラリの利用設計",
        "dataset": "データセット品質/拡張がモデル性能へ与える影響",
    }

    added = set()
    for kw in kws:
        if kw in rationale_map and rationale_map[kw] not in added:
            bullets.append(rationale_map[kw])
            added.add(rationale_map[kw])

    # Category-based generic reasons
    if primary == "cs.SE" and "ソフトウェア工学の実務に直結する評価・設計指針" not in added:
        bullets.append("ソフトウェア工学の実務に直結する評価・設計指針")
        added.add("ソフトウェア工学の実務に直結する評価・設計指針")
    if primary == "cs.PL" and "言語仕様/型/検証による品質担保の基礎" not in added:
        bullets.append("言語仕様/型/検証による品質担保の基礎")
        added.add("言語仕様/型/検証による品質担保の基礎")
    if primary in ("cs.CL", "cs.AI") and "LLM適用における限界・設計パターンの理解" not in added:
        bullets.append("LLM適用における限界・設計パターンの理解")
        added.add("LLM適用における限界・設計パターンの理解")

    # Fallback reason if none detected
    if not bullets:
        bullets.append("AI駆動開発の実践に有用な示唆が得られる可能性")

    return bullets[:6]


def one_liner_reason(it: Dict[str, Any]) -> str:
    bullets = reason_bullets(it)
    return bullets[0] if bullets else "AI駆動開発に有用"


def main():
    items = load_jsonl(JSONL_PATH)
    scored: List[Tuple[float, Dict[str, Any]]] = [score_item(it) for it in items]
    # Keep only items with non-trivial score
    filtered = [it for s, it in scored if s >= 2.0]
    # Sort by score desc, then by published desc
    def sort_key(it: Dict[str, Any]):
        pub = it.get("published") or it.get("day") or ""
        # Convert to sortable string YYYYMMDDHHMMSS where possible
        try:
            if "T" in pub:
                dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
            else:
                dt = datetime.fromisoformat(pub + "T00:00:00+00:00")
            pub_key = dt.strftime("%Y%m%d%H%M%S")
        except Exception:
            pub_key = "00000000000000"
        return (-it.get("_total_score", 0.0), -int(pub_key))

    filtered.sort(key=sort_key)

    # Deduplicate by arXiv ID
    seen = set()
    selected: List[Dict[str, Any]] = []
    for it in filtered:
        aid = it.get("arxiv_id")
        if aid and aid not in seen:
            seen.add(aid)
            selected.append(it)
        if len(selected) >= 100:
            break

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Index file
    index_lines: List[str] = []
    index_lines.append("# AI駆動開発に役立つ論文100（2025, arXivベース）")
    index_lines.append("")
    index_lines.append("注意: タイトル/カテゴリから自動抽出した候補です。詳細は各論文の要旨・本文をご確認ください。")
    index_lines.append("")
    index_lines.append("一覧:")
    index_lines.append("")

    for i, it in enumerate(selected, start=1):
        title = it.get("title", "")
        aid = it.get("arxiv_id", "")
        abs_url = it.get("abs_url", f"https://arxiv.org/abs/{aid}")
        pub = it.get("published") or it.get("day") or ""
        cats = ", ".join(it.get("categories") or [])
        slug = slugify(title)
        filename = f"{i:03d}_{aid}_{slug}.md"
        reason = one_liner_reason(it)
        index_lines.append(f"- [{i:03d}. {title}]({filename}) — {reason}")

        # Build per-paper content
        bullets = reason_bullets(it)
        content: List[str] = []
        content.append(f"# {title}")
        content.append("")
        content.append(f"- arXiv: `{aid}`")
        content.append(f"- Link: {abs_url}")
        if pub:
            content.append(f"- Published: {pub}")
        if cats:
            content.append(f"- Categories: {cats}")
        content.append("")
        content.append("## 読むべき理由")
        for b in bullets:
            content.append(f"- {b}")
        content.append("")
        content.append("## ソフトウェアエンジニア向けの示唆")
        content.append("- 実サービス/プロダクトへの適用を想定し、再現可能性と評価指標に注目する")
        content.append("- ツール呼び出し・RAG・ガードレール等の設計を既存ワークフローに統合する")
        content.append("- 評価の落とし穴（データリーク/過学習/指標の偏り）をチェックする")
        content.append("- コスト・レイテンシ・信頼性のトレードオフを意識して設計する")
        content.append("")
        content.append("---")
        content.append("注意: 本ファイルはタイトル/カテゴリから自動生成された要点です。正確な理解には原著の要旨・本文をご確認ください。")

        (OUT_DIR / filename).write_text("\n".join(content), encoding="utf-8")

    # Write index
    (OUT_DIR / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(selected)} markdown files to {OUT_DIR}")


if __name__ == "__main__":
    main()

