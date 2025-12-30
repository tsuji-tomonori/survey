#!/usr/bin/env python3
"""
Check a paper note for completeness and append a Check Log entry.

Usage:
  python scripts/check_paper.py <line_number> [--jsonl PATH] [--vault PATH]

Behavior:
- Loads the paper metadata from the JSONL (1-based line index).
- Locates or creates the Obsidian note for the paper under the vault.
- Checks required sections for placeholder-only content.
- Appends a Check Log entry with actionable next steps.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Defaults aligned with repo layout
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSONL = PROJECT_ROOT / "arxiv_cs_peerreview_proxy_2025_daily.jsonl"
DEFAULT_VAULT = PROJECT_ROOT / "arxiv-cs-2025"


def read_jsonl_line(filepath: Path, line_number: int) -> Dict | None:
    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if i == line_number:
                try:
                    return json.loads(line.strip())
                except Exception:
                    return None
    return None


def note_path_for(paper: Dict, vault: Path) -> Path:
    arxiv_id: str = paper["arxiv_id"]
    primary: str = paper.get("primary_category", "uncategorized") or "uncategorized"
    return (
        vault
        / "01_Papers"
        / "2025"
        / primary
        / f"P-{arxiv_id.replace('v', '_v')}.md"
    )


def ensure_note_exists(paper: Dict, note_path: Path) -> bool:
    """Ensure a paper note exists. Returns True if created in this call."""
    if note_path.exists():
        return False

    # Minimal template content (aligned with scripts/read_paper.py output)
    note_path.parent.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    authors_yaml = json.dumps(paper.get("authors", []), ensure_ascii=False)
    categories_yaml = json.dumps(paper.get("categories", []), ensure_ascii=False)
    content = f"""---
type: paper
arxiv_id: "{paper.get('arxiv_id','')}"
title: "{paper.get('title','')}"
year: 2025
primary: "{paper.get('primary_category','')}"
categories: {categories_yaml}
authors: {authors_yaml}
published: "{paper.get('published','')}"
updated: "{paper.get('updated','')}"
doi: "{paper.get('doi','') or ''}"
journal_ref: "{paper.get('journal_ref','') or ''}"
abs_url: "{paper.get('abs_url','')}"
pdf: ""
status: inbox
ai_summary_level: brief
score: 0
signals: []
methods: []
tasks: []
datasets: []
claims: []
risks: []
created: "{today}"
---

# TL;DR（3行）
-

# Problem / Setting
-

# Key Contributions
-
-
-

# Method
-

# Experiments
- Dataset / Benchmark:
- Metrics:
- Baselines:
- Setup:

# Results（主要数値）
-

# Ablations / Analysis
-

# Limitations / Risks
-

# Relation to Prior Work
-

# My Notes（解釈・疑問・使い道）
-

# Links
- Topics:
- Methods:
- Datasets:
- Related Papers:

# Action Items
- [ ]

# Check Log
"""
    note_path.write_text(content, encoding="utf-8")
    return True


Section = Tuple[str, str]


def parse_sections(md_text: str) -> Dict[str, str]:
    sections: Dict[str, str] = {}
    lines = md_text.splitlines()
    current: Optional[str] = None
    buf: List[str] = []
    for line in lines:
        if line.startswith("# "):
            # flush previous
            if current is not None:
                sections[current] = "\n".join(buf).rstrip()
            current = line[2:].strip()
            buf = []
        else:
            if current is not None:
                buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).rstrip()
    return sections


def get_yaml_field(md_text: str, key: str) -> Optional[str]:
    if not md_text.startswith("---\n"):
        return None
    try:
        front, _rest = md_text.split("\n---\n", 1)
    except ValueError:
        return None
    for ln in front.splitlines()[1:]:
        if not ln.strip():
            continue
        if ":" in ln:
            k, v = ln.split(":", 1)
            if k.strip() == key:
                return v.strip().strip('"')
    return None


def is_placeholder_block(text: str) -> bool:
    # Empty or only hyphen placeholders
    for ln in text.strip().splitlines():
        s = ln.strip()
        if not s:
            continue
        if s != "-" and not s.startswith("- [ ]"):
            return False
    return True


def required_sections() -> List[str]:
    return [
        "TL;DR（3行）",
        "Problem / Setting",
        "Key Contributions",
        "Method",
        "Results（主要数値）",
        "Limitations / Risks",
    ]


def build_check_entry(idx: int, status: str, missing: List[str], pdf_missing: bool, initial: bool) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    header = (
        f"- {today} 初回チェック: テンプレート作成のみ（status: {status or 'unknown'}）。"
        if initial
        else f"- {today} 再チェック: status={status or 'unknown'}"
    )

    details: List[str] = []
    if pdf_missing:
        details.append("PDF未取得（ネットワーク制限）。")
    if missing:
        if initial:
            details.append("以下を記入後に再度 `/check {}` を実行:".format(idx))
        else:
            details.append("不足セクションを補完後に再度 `/check {}` を実行:".format(idx))
        # Guidance for each required section
        guidance_map = {
            "TL;DR（3行）": "TL;DRを3行で（何を/どうやって/どうなった）",
            "Problem / Setting": "入力・出力・目的・評価指標・制約・比較対象を具体化",
            "Key Contributions": "差分と根拠（表・図・実験）を紐付けて箇条書き",
            "Method": "推論手順まで含めて最小再現単位で整理（前処理/学習/推論）",
            "Results（主要数値）": "絶対値＋差分＋条件（同規模/同データ/同設定）をセットで記載",
            "Limitations / Risks": "再現性・外的妥当性・計算コスト・評価の穴を明記",
        }
        for sec in missing:
            tip = guidance_map.get(sec, "内容を記入")
            details.append(f"  - {tip}")
    else:
        details.append("必須セクションは記入済み。`status: summarized` または `verified` を検討。")

    entry = header + "\n" + "\n".join(details)
    return entry


def append_check_log(note_path: Path, entry: str) -> None:
    text = note_path.read_text(encoding="utf-8")
    if "# Check Log" in text:
        new_text = text.rstrip() + "\n" + entry + "\n"
    else:
        # Append a header if missing
        new_text = text.rstrip() + "\n\n# Check Log\n" + entry + "\n"
    note_path.write_text(new_text, encoding="utf-8")


def check_note(md_text: str) -> Tuple[List[str], bool]:
    secs = parse_sections(md_text)
    missing: List[str] = []
    for sec in required_sections():
        blk = secs.get(sec, "")
        if is_placeholder_block(blk):
            missing.append(sec)
    pdf_missing = True
    pdf_field = get_yaml_field(md_text, "pdf")
    if pdf_field:
        pdf_missing = (pdf_field.strip() == "" )
    return missing, pdf_missing


def main() -> None:
    ap = argparse.ArgumentParser(description="Check arXiv paper note completeness and log results")
    ap.add_argument("line_number", type=int, help="Line number in JSONL (1-based)")
    ap.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    ap.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    args = ap.parse_args()

    paper = read_jsonl_line(args.jsonl, args.line_number)
    if not paper:
        print(f"Error: Line {args.line_number} not found or invalid JSON", file=sys.stderr)
        sys.exit(1)

    note_path = note_path_for(paper, args.vault)
    created = ensure_note_exists(paper, note_path)

    md_text = note_path.read_text(encoding="utf-8")
    status = get_yaml_field(md_text, "status") or ""
    missing, pdf_missing = check_note(md_text)

    entry = build_check_entry(
        idx=args.line_number,
        status=status,
        missing=missing,
        pdf_missing=pdf_missing,
        initial=created or status == "inbox",
    )
    append_check_log(note_path, entry)

    result = {
        "index": args.line_number,
        "arxiv_id": paper.get("arxiv_id"),
        "title": paper.get("title"),
        "note_path": str(note_path),
        "created": created,
        "status": status,
        "missing_sections": missing,
        "pdf_missing": pdf_missing,
        "log_entry_appended": True,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

