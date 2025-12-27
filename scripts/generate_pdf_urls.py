from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "codex" / "ai-dev-2025"
OUT_PATH = MD_DIR / "urls.txt"


def main() -> None:
    if not MD_DIR.exists():
        raise SystemExit(f"Not found: {MD_DIR}")

    entries = []
    for p in MD_DIR.glob("*.md"):
        if p.name == "README.md":
            continue
        # Expect filenames like 001_<arxiv_id>_<slug>.md
        m = re.match(r"^(\d{3})_([^_]+)_", p.name)
        if not m:
            continue
        idx = int(m.group(1))
        arxiv_id = m.group(2)
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        entries.append((idx, pdf_url))

    # Sort by index to match README order
    entries.sort(key=lambda x: x[0])

    lines = [url for _, url in entries]
    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} URLs to {OUT_PATH}")


if __name__ == "__main__":
    main()

