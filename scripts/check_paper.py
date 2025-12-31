#!/usr/bin/env python3
"""
Check a single paper note for required sections and append a Check Log entry.

Usage:
  python scripts/check_paper.py <line_number> [--jsonl PATH] [--vault PATH] [--auto-create]

Behavior:
- Reads the <line_number>-th record from the JSONL to get arxiv_id/primary.
- Resolves expected note path under the vault.
- If missing and --auto-create is given, calls scripts/read_paper.py --no-pdf to create it.
- Checks that required sections contain non-placeholder content.
- Appends a one-line entry to "# Check Log" with date and result summary (JP).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Optional

PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_JSONL = PROJECT_ROOT / "arxiv_cs_peerreview_proxy_2025_daily.jsonl"
DEFAULT_VAULT = PROJECT_ROOT / "arxiv-cs-2025"


def read_jsonl_line(filepath: Path, line_number: int) -> dict | None:
    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if i == line_number:
                return json.loads(line)
    return None


def expected_note_path(vault_root: Path, primary: str, arxiv_id: str) -> Path:
    safe_id = arxiv_id.replace("v", "_v")
    return vault_root / "01_Papers" / "2025" / primary / f"P-{safe_id}.md"


REQUIRED_SECTIONS = [
    "# TL;DR（3行）",
    "# Problem / Setting",
    "# Key Contributions",
    "# Method",
    "# Results（主要数値）",
    "# Limitations / Risks",
]


def extract_sections(content: str) -> List[Tuple[str, str]]:
    """Return list of (heading, body) for top-level headings (# ...)."""
    parts: List[Tuple[str, str]] = []
    lines = content.splitlines()
    current_h: Optional[str] = None
    buf: List[str] = []
    for ln in lines:
        if ln.startswith("# "):
            if current_h is not None:
                parts.append((current_h, "\n".join(buf).rstrip()))
            current_h = ln.strip()
            buf = []
        else:
            buf.append(ln)
    if current_h is not None:
        parts.append((current_h, "\n".join(buf).rstrip()))
    return parts


def has_meaningful_content(text: str) -> bool:
    # Consider content meaningful if it contains a non-placeholder character
    # beyond a single dash lines or empty whitespace.
    # Strip checklist dashes and whitespace-only lines.
    for raw in text.splitlines():
        ln = raw.strip()
        if not ln:
            continue
        if ln in ("-", "- [ ]"):
            continue
        # Any non-placeholder content
        return True
    return False


def ensure_check_log(content: str, line: str) -> str:
    if "# Check Log" not in content:
        if not content.endswith("\n"):
            content += "\n"
        content += "\n# Check Log\n"
    if not content.endswith("\n"):
        content += "\n"
    content += line.rstrip() + "\n"
    return content


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def run():
    ap = argparse.ArgumentParser()
    ap.add_argument("line_number", type=int)
    ap.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    ap.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    ap.add_argument("--auto-create", action="store_true", help="Create note via read_paper.py --no-pdf when missing")
    args = ap.parse_args()

    rec = read_jsonl_line(args.jsonl, args.line_number)
    if not rec:
        print(f"[check] 行 {args.line_number} が JSONL に見つかりませんでした")
        return 2

    arxiv_id = rec["arxiv_id"]
    primary = rec["primary_category"]
    note_path = expected_note_path(args.vault, primary, arxiv_id)

    created = False
    if not note_path.exists():
        if args.auto_create:
            # Create via read_paper.py --no-pdf
            cmd = [
                "python",
                str(PROJECT_ROOT / "scripts" / "read_paper.py"),
                str(args.line_number),
                "--no-pdf",
                "--jsonl",
                str(args.jsonl),
                "--vault",
                str(args.vault),
            ]
            subprocess.run(cmd, check=False)
            created = note_path.exists()
        if not note_path.exists():
            today = datetime.now().strftime("%Y-%m-%d")
            print(f"[check] ノート未作成: {note_path}")
            # Emit a lightweight stub log file to guide the next action
            stub = (
                f"---\ninfo: auto-generated check stub\n---\n\n# Check Log\n"
                f"- [{today}] ノートが存在しません。次アクション: `/read {args.line_number}` を実行してメモを作成後に再チェック。\n"
            )
            out_stub = args.vault / "00_Inbox" / f"CHECK_STUB_{arxiv_id}.md"
            write_text(out_stub, stub)
            return 1

    # Load note content
    text = note_path.read_text(encoding="utf-8")

    # Evaluate required sections
    sections = {h: b for h, b in extract_sections(text)}
    missing: List[str] = []
    for h in REQUIRED_SECTIONS:
        body = sections.get(h, "")
        if not has_meaningful_content(body):
            missing.append(h)

    today = datetime.now().strftime("%Y-%m-%d")
    if missing:
        msg = (
            f"- [{today}] 初回チェック: 必須セクション未記入 ({', '.join([m.split(' ',1)[1] if ' ' in m else m for m in missing])})。"
            f" statusはinbox維持。次アクション: 本文を埋めてから再度 `/check {args.line_number}` 実行。"
        )
    else:
        msg = (
            f"- [{today}] チェック合格: 必須セクションは埋まっています。必要なら数値検証後に status を verified へ。"
        )

    # Append to Check Log
    new_text = ensure_check_log(text, msg)
    write_text(note_path, new_text)

    # Print a concise summary to stdout
    print(json.dumps({
        "line": args.line_number,
        "arxiv_id": arxiv_id,
        "note_path": str(note_path),
        "created": created,
        "missing_sections": missing,
        "message": msg,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
