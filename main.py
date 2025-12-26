from __future__ import annotations

import time
import json
from dataclasses import dataclass, asdict
from datetime import date, timedelta
from typing import Iterator, Optional, List, Dict
import xml.etree.ElementTree as ET

import requests


ARXIV_API_ENDPOINT = "http://export.arxiv.org/api/query"

# arXiv API の Atom 名前空間（ユーザーマニュアルより）:contentReference[oaicite:5]{index=5}
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}


@dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: List[str]
    published: str
    updated: str
    primary_category: str
    categories: List[str]
    doi: Optional[str]
    journal_ref: Optional[str]
    abs_url: str


def daterange(d0: date, d1: date) -> Iterator[date]:
    d = d0
    while d <= d1:
        yield d
        d += timedelta(days=1)


def parse_feed(xml_text: str) -> List[Paper]:
    root = ET.fromstring(xml_text)
    papers: List[Paper] = []

    for entry in root.findall("atom:entry", NS):
        abs_url = (entry.findtext("atom:id", default="", namespaces=NS) or "").strip()
        title = (entry.findtext("atom:title", default="", namespaces=NS) or "").strip()
        published = (
            entry.findtext("atom:published", default="", namespaces=NS) or ""
        ).strip()
        updated = (
            entry.findtext("atom:updated", default="", namespaces=NS) or ""
        ).strip()

        authors = []
        for a in entry.findall("atom:author", NS):
            nm = (a.findtext("atom:name", default="", namespaces=NS) or "").strip()
            if nm:
                authors.append(nm)

        # arXiv ID は <id> の末尾が /abs/{id} なのでそこから抽出
        # 例: http://arxiv.org/abs/2501.01234v1
        arxiv_id = abs_url.rsplit("/", 1)[-1]

        # categories
        cat_terms = []
        for c in entry.findall("atom:category", NS):
            term = c.attrib.get("term", "").strip()
            if term:
                cat_terms.append(term)
        primary_category = (
            entry.find("arxiv:primary_category", NS).attrib.get("term", "").strip()
            if entry.find("arxiv:primary_category", NS) is not None
            else ""
        )

        doi = (
            entry.findtext("arxiv:doi", default="", namespaces=NS) or ""
        ).strip() or None
        journal_ref = (
            entry.findtext("arxiv:journal_ref", default="", namespaces=NS) or ""
        ).strip() or None

        papers.append(
            Paper(
                arxiv_id=arxiv_id,
                title=title,
                authors=authors,
                published=published,
                updated=updated,
                primary_category=primary_category,
                categories=cat_terms,
                doi=doi,
                journal_ref=journal_ref,
                abs_url=abs_url,
            )
        )
    return papers


def arxiv_query_day_cs_submitted(day: date, start: int, max_results: int) -> str:
    # submittedDate のレンジクエリは arXiv API 利用者の間で広く使われる形
    # 例: submittedDate:[YYYYMMDD0000 TO YYYYMMDD2359]
    ymd = day.strftime("%Y%m%d")
    date_range = f"submittedDate:[{ymd}0000 TO {ymd}2359]"

    # CS 全体は cat:cs.* で取得（サブカテゴリ横断）
    # もし cat:cs.* が環境で合わない場合は、必要な cs.XX を OR で列挙してください。
    search_query = f"cat:cs.* AND {date_range}"

    params = {
        "search_query": search_query,
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",  # sortBy は submittedDate をサポート :contentReference[oaicite:6]{index=6}
        "sortOrder": "ascending",
    }
    # requests が URL エンコードしてくれるのでそのまま渡す
    return params


def fetch_day(
    day: date, session: requests.Session, page_size: int = 2000
) -> List[Paper]:
    results: List[Paper] = []
    start = 0

    while True:
        params = arxiv_query_day_cs_submitted(day, start=start, max_results=page_size)
        r = session.get(ARXIV_API_ENDPOINT, params=params, timeout=60)
        r.raise_for_status()

        batch = parse_feed(r.text)
        if not batch:
            break

        results.extend(batch)

        # レート制限（3秒に1回）:contentReference[oaicite:7]{index=7}
        time.sleep(5.0)

        # 2000件ずつ前進
        if len(batch) < page_size:
            break
        start += page_size

    return results


def is_peer_reviewed_proxy(p: Paper) -> bool:
    # “査読付き”の近似: journal_ref または doi がある
    return (p.journal_ref is not None) or (p.doi is not None)


def main(
    start_date: date = date(2025, 1, 1),
    end_date: date = date.today(),
    out_jsonl_path: str = "arxiv_cs_peerreview_proxy_2025_daily.jsonl",
) -> None:
    headers = {
        # ToU/運用上、User-Agent は識別可能な文字列にするのが推奨です
        "User-Agent": "my-arxiv-harvester/0.1 (contact: you@example.com)"
    }

    with requests.Session() as session:
        session.headers.update(headers)

        with open(out_jsonl_path, "w", encoding="utf-8") as f:
            for d in daterange(start_date, end_date):
                papers = fetch_day(d, session=session)
                filtered = [p for p in papers if is_peer_reviewed_proxy(p)]

                for p in filtered:
                    rec = asdict(p)
                    rec["day"] = d.isoformat()
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

                print(f"{d.isoformat()} total={len(papers)} peer_proxy={len(filtered)}")

    print(f"Saved: {out_jsonl_path}")


if __name__ == "__main__":
    main()
