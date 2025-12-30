#!/usr/bin/env python3
"""
Lightweight check command for arXiv notes.

Usage:
  python scripts/check_paper.py <line_number>

Behavior:
  - Reads the given 1-based line from arxiv_cs_peerreview_proxy_2025_daily.jsonl
  - Locates the note at arxiv-cs-2025/01_Papers/2025/{primary}/P-{arxiv_id.replace('v','_v')}.md
  - If missing, creates a minimal skeleton (no PDF path) similar to read_paper.py
  - Scans key sections to see if content exists beyond placeholders
  - Optionally bumps status from inbox -> summarized if some content exists
  - Appends a timestamped entry under a "# Check Log" section
  - Prints a short JSON summary to stdout
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


PROJECT_ROOT = Path(__file__).resolve().parents[1]
JSONL_PATH = PROJECT_ROOT / "arxiv_cs_peerreview_proxy_2025_daily.jsonl"
VAULT_ROOT = PROJECT_ROOT / "arxiv-cs-2025"


@dataclass
class Paper:
    arxiv_id: str
    title: str
    primary_category: str
    categories: list[str]
    authors: list[str]
    published: str
    updated: str
    doi: str | None
    journal_ref: str | None
    abs_url: str


def read_jsonl_line(filepath: Path, line_number: int) -> dict | None:
    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if i == line_number:
                try:
                    return json.loads(line.strip())
                except json.JSONDecodeError:
                    return None
    return None


def ensure_note(paper: Paper) -> Path:
    note_dir = VAULT_ROOT / "01_Papers" / "2025" / paper.primary_category
    note_dir.mkdir(parents=True, exist_ok=True)
    filename = f"P-{paper.arxiv_id.replace('v', '_v')}.md"
    note_path = note_dir / filename

    if note_path.exists():
        return note_path

    # Create minimal skeleton (no PDF path)
    today = datetime.now().strftime("%Y-%m-%d")
    categories_yaml = json.dumps(paper.categories, ensure_ascii=False)
    authors_yaml = json.dumps(paper.authors, ensure_ascii=False)

    content = f"""---
type: paper
arxiv_id: "{paper.arxiv_id}"
title: "{paper.title}"
year: 2025
primary: "{paper.primary_category}"
categories: {categories_yaml}
authors: {authors_yaml}
published: "{paper.published}"
updated: "{paper.updated}"
doi: "{paper.doi or ''}"
journal_ref: "{paper.journal_ref or ''}"
abs_url: "{paper.abs_url}"
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
"""

    note_path.write_text(content, encoding="utf-8")
    return note_path


SECTION_HEADERS = [
    "# TL;DR（3行）",
    "# Problem / Setting",
    "# Key Contributions",
    "# Method",
    "# Experiments",
    "# Results（主要数値）",
    "# Ablations / Analysis",
    "# Limitations / Risks",
]


def extract_section_content(md: str, header: str) -> str:
    # Capture content following header until next H1/H2 header or EOF
    pattern = rf"(?m)^{re.escape(header)}\n(.*?)(?=^# |\Z)"
    m = re.search(pattern, md, flags=re.DOTALL)
    return m.group(1).strip() if m else ""


def has_meaningful_content(section_text: str) -> bool:
    # Consider content meaningful if any non-placeholder token exists
    for line in section_text.splitlines():
        if line.strip() and line.strip() not in {"-", "- [ ]"}:
            return True
    return False


def update_status(md: str, new_status: str) -> str:
    # Replace status: ... inside frontmatter block
    def repl(m: re.Match[str]) -> str:
        fm = m.group(0)
        fm = re.sub(r"(?m)^status:\s*.*$", f"status: {new_status}", fm)
        return fm

    return re.sub(r"(?s)^---\n.*?\n---", repl, md, count=1)


def append_check_log(md: str, log_line: str) -> str:
    if re.search(r"(?m)^# Check Log\s*$", md):
        return md.rstrip() + f"\n- {log_line}\n"
    else:
        return md.rstrip() + f"\n\n# Check Log\n- {log_line}\n"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/check_paper.py <line_number>", file=sys.stderr)
        return 2
    try:
        line_number = int(sys.argv[1])
    except ValueError:
        print("Line number must be an integer", file=sys.stderr)
        return 2

    rec = read_jsonl_line(JSONL_PATH, line_number)
    if not rec:
        print(f"Error: Line {line_number} not found in {JSONL_PATH}", file=sys.stderr)
        return 1

    paper = Paper(
        arxiv_id=rec.get("arxiv_id", ""),
        title=rec.get("title", ""),
        primary_category=rec.get("primary_category", ""),
        categories=rec.get("categories", []) or [],
        authors=rec.get("authors", []) or [],
        published=rec.get("published", rec.get("day", "")) or "",
        updated=rec.get("updated", "") or "",
        doi=rec.get("doi") or None,
        journal_ref=rec.get("journal_ref") or None,
        abs_url=rec.get("abs_url", ""),
    )

    note_path = ensure_note(paper)
    md = note_path.read_text(encoding="utf-8")

    filled_sections = 0
    for h in SECTION_HEADERS:
        if has_meaningful_content(extract_section_content(md, h)):
            filled_sections += 1

    old_status_match = re.search(r"(?m)^status:\s*(\w+)\s*$", md)
    old_status = old_status_match.group(1) if old_status_match else ""

    action = "checked"
    new_status: Optional[str] = None
    if filled_sections == 0:
        action = "initialized" if "# TL;DR（3行）" in md and old_status == "inbox" else "checked"
        log_msg = (
            f"{datetime.now():%Y-%m-%d} Initialized via /check {line_number}: "
            f"memo skeleton created (no TL;DR or sections filled). Status remains `inbox`. "
            f"Please summarize the paper, then re-run `/check {line_number}` for verification and skill/topic updates."
        )
    else:
        if old_status == "inbox":
            new_status = "summarized"
            md = update_status(md, new_status)
            action = "updated-status"
        log_msg = (
            f"{datetime.now():%Y-%m-%d} /check {line_number}: found {filled_sections} key sections with content. "
            + ("Status updated to `summarized`." if new_status else "Status unchanged.")
        )

    md = append_check_log(md, log_msg)
    note_path.write_text(md, encoding="utf-8")

    # Structured summary for tooling
    out = {
        "line_number": line_number,
        "arxiv_id": paper.arxiv_id,
        "note_path": str(note_path),
        "action": action,
        "old_status": old_status,
        "new_status": new_status or old_status,
        "filled_sections": filled_sections,
    }
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

