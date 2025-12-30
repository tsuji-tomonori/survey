#!/usr/bin/env python3
"""
arXiv論文読み込みスクリプト
JSONLから論文情報を取得し、PDFダウンロード・Obsidianメモ作成を行う
"""
import json
import sys
import os
from pathlib import Path
from datetime import datetime
import argparse
"""
Note: requests is imported lazily inside download_pdf to allow
running with --no-pdf in environments without network or the
requests package installed.
"""

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent
JSONL_PATH = PROJECT_ROOT / "arxiv_cs_peerreview_proxy_2025_daily.jsonl"
VAULT_ROOT = PROJECT_ROOT / "arxiv-cs-2025"


def read_jsonl_line(filepath: Path, line_number: int) -> dict | None:
    """JSONLファイルから指定行（1ベース）を読み込む"""
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if i == line_number:
                return json.loads(line.strip())
    return None


def download_pdf(arxiv_id: str, output_dir: Path) -> Path | None:
    """arXiv PDFをダウンロード"""
    # Lazy import so that --no-pdf works without requests installed
    try:
        import requests  # type: ignore
    except Exception as e:
        print(f"requests not available, skipping PDF download: {e}", file=sys.stderr)
        return None
    # バージョン番号を除去してPDF URLを構築
    base_id = arxiv_id.split('v')[0] if 'v' in arxiv_id else arxiv_id
    pdf_url = f"https://arxiv.org/pdf/{base_id}.pdf"
    pdf_path = output_dir / f"{arxiv_id.replace('v', '_v')}.pdf"

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading PDF: {pdf_url}", file=sys.stderr)
    try:
        response = requests.get(pdf_url, timeout=60)
        response.raise_for_status()

        with open(pdf_path, 'wb') as f:
            f.write(response.content)

        print(f"Saved: {pdf_path}", file=sys.stderr)
        return pdf_path
    except Exception as e:
        print(f"Error downloading PDF: {e}", file=sys.stderr)
        return None


def create_paper_note(paper: dict, pdf_path: Path | None, output_dir: Path) -> Path:
    """Obsidian用の論文メモを作成"""
    arxiv_id = paper['arxiv_id']
    primary = paper['primary_category']

    # 出力ディレクトリ
    note_dir = output_dir / "01_Papers" / "2025" / primary
    note_dir.mkdir(parents=True, exist_ok=True)

    note_path = note_dir / f"P-{arxiv_id.replace('v', '_v')}.md"

    # 相対PDFパス
    pdf_relative = f"90_Attachments/pdf/2025/{arxiv_id.replace('v', '_v')}.pdf" if pdf_path else ""

    # 著者リスト
    authors_yaml = json.dumps(paper['authors'], ensure_ascii=False)
    categories_yaml = json.dumps(paper['categories'], ensure_ascii=False)

    today = datetime.now().strftime("%Y-%m-%d")

    content = f'''---
type: paper
arxiv_id: "{arxiv_id}"
title: "{paper['title']}"
year: 2025
primary: "{primary}"
categories: {categories_yaml}
authors: {authors_yaml}
published: "{paper['published']}"
updated: "{paper['updated']}"
doi: "{paper.get('doi', '')}"
journal_ref: "{paper.get('journal_ref', '') or ''}"
abs_url: "{paper['abs_url']}"
pdf: "{pdf_relative}"
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
'''

    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return note_path


def main():
    parser = argparse.ArgumentParser(description='arXiv論文読み込み')
    parser.add_argument('line_number', type=int, help='JSONLの行番号（1ベース）')
    parser.add_argument('--no-pdf', action='store_true', help='PDFダウンロードをスキップ')
    parser.add_argument('--jsonl', type=Path, default=JSONL_PATH, help='JSONLファイルパス')
    parser.add_argument('--vault', type=Path, default=VAULT_ROOT, help='Obsidian Vaultパス')
    args = parser.parse_args()

    # 論文情報を読み込む
    paper = read_jsonl_line(args.jsonl, args.line_number)
    if not paper:
        print(f"Error: Line {args.line_number} not found in JSONL", file=sys.stderr)
        sys.exit(1)

    print(f"Found: {paper['title']}", file=sys.stderr)
    print(f"arXiv ID: {paper['arxiv_id']}", file=sys.stderr)
    print(f"Category: {paper['primary_category']}", file=sys.stderr)

    # PDFダウンロード
    pdf_path = None
    if not args.no_pdf:
        pdf_dir = args.vault / "90_Attachments" / "pdf" / "2025"
        pdf_path = download_pdf(paper['arxiv_id'], pdf_dir)

    # メモ作成
    note_path = create_paper_note(paper, pdf_path, args.vault)
    print(f"Note created: {note_path}", file=sys.stderr)

    # 結果をJSON出力（Claude Codeが利用可能）
    result = {
        "arxiv_id": paper['arxiv_id'],
        "title": paper['title'],
        "primary_category": paper['primary_category'],
        "authors": paper['authors'],
        "note_path": str(note_path),
        "pdf_path": str(pdf_path) if pdf_path else None,
        "abs_url": paper['abs_url']
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
