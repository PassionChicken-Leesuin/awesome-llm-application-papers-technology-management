#!/usr/bin/env python3
"""Monthly candidate sweep for the awesome list.

Queries OpenAlex and Semantic Scholar for recent papers matching
TIM x LLM/agent keyword combinations, drops anything already in
data/papers.tsv (matched by normalized title or DOI/arXiv id), and prints
the survivors as a markdown checklist (used as the body of the review issue).

No API keys required; both APIs are public. Recall-oriented by design —
expect false positives, humans triage.

Usage:
    python scripts/sweep_candidates.py [--months 2] [--per-query 25]
"""

import argparse
import csv
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "papers.tsv"

MAILTO = "openalex@example.org"  # polite-pool contact for OpenAlex; replace with maintainer email

# Each query pairs an LLM/agent term with a TIM task term.
QUERIES = [
    '"large language model" patent',
    '"LLM" "patent classification"',
    '"LLM agent" patent',
    '"multi-agent" patent analysis',
    '"large language model" "technology forecasting"',
    '"large language model" "technology opportunity"',
    '"LLM" scientometrics',
    '"large language model" bibliometric',
    '"LLM" "systematic review" screening',
    '"large language model" "idea generation" innovation',
    '"generative AI" "new product development"',
    '"LLM agents" "market simulation"',
    '"large language model" "innovation management"',
    '"large language model" "technology roadmap"',
    '"LLM" "competitive intelligence"',
    '"large language model" "technology transfer" OR "IP licensing"',
    '"LLM" "R&D portfolio" OR "R&D project management"',
    '"large language model" standards OR regulation "technology management"',
    '"LLM" commercialization OR "startup scouting"',
    '"generative AI" "digital prototyping"',
]


def norm_title(t):
    t = unicodedata.normalize("NFKD", t or "").lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


FAILED_FETCHES = []  # sweep is only complete if this stays empty


def get_json(url, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": f"awesome-tm-sweep (mailto:{MAILTO})"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 — best-effort sweep
            if i == tries - 1:
                print(f"WARN: giving up on {url}: {e}", file=sys.stderr)
                FAILED_FETCHES.append(url)
                return None
            time.sleep(2 * (i + 1))


def known_keys():
    keys = set()
    with TSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            keys.add(norm_title(row["title"]))
            m = re.search(r"(?:doi\.org/|arxiv\.org/abs/)(.+)$", row["url"])
            if m:
                keys.add(m.group(1).lower())
    return keys


def openalex(query, since, per_query):
    url = ("https://api.openalex.org/works?"
           + urllib.parse.urlencode({
               "search": query,
               "filter": f"from_publication_date:{since},type:article|preprint",
               "sort": "publication_date:desc",
               "per-page": per_query,
               "mailto": MAILTO,
           }))
    data = get_json(url) or {}
    for w in data.get("results", []):
        doi = (w.get("doi") or "").replace("https://doi.org/", "")
        yield {
            "title": w.get("display_name") or "",
            "year": w.get("publication_year"),
            "url": w.get("doi") or (w.get("primary_location") or {}).get("landing_page_url") or w.get("id"),
            "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
            "id": doi.lower(),
            "src": "OpenAlex",
            "query": query,
        }


def semantic_scholar(query, since_year, per_query):
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?"
           + urllib.parse.urlencode({
               "query": query.replace('"', ""),
               "year": f"{since_year}-",
               "limit": per_query,
               "fields": "title,year,venue,externalIds,url",
           }))
    data = get_json(url) or {}
    for p in data.get("data", []):
        ext = p.get("externalIds") or {}
        pid = (ext.get("DOI") or ext.get("ArXiv") or "").lower()
        yield {
            "title": p.get("title") or "",
            "year": p.get("year"),
            "url": ("https://doi.org/" + ext["DOI"]) if ext.get("DOI")
                   else ("https://arxiv.org/abs/" + ext["ArXiv"]) if ext.get("ArXiv")
                   else p.get("url"),
            "venue": p.get("venue") or "",
            "id": pid,
            "src": "SemanticScholar",
            "query": query,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--months", type=int, default=2, help="look-back window in months")
    ap.add_argument("--per-query", type=int, default=25)
    args = ap.parse_args()

    today = date.today()
    total = today.year * 12 + (today.month - 1) - args.months
    y, m0 = divmod(total, 12)
    since = date(y, m0 + 1, 1).isoformat()

    known = known_keys()
    seen, candidates = set(), []
    for q in QUERIES:
        rows = list(openalex(q, since, args.per_query))
        rows += list(semantic_scholar(q, y, args.per_query))
        time.sleep(1)  # be nice to both APIs
        for r in rows:
            key = norm_title(r["title"])
            if not key or key in known or key in seen or (r["id"] and r["id"] in known):
                continue
            seen.add(key)
            candidates.append(r)

    candidates.sort(key=lambda r: (-(r["year"] or 0), r["title"]))
    print(f"## Candidate sweep {today.isoformat()}\n")
    print(f"{len(candidates)} candidates since {since} "
          f"(deduplicated against {len(known) // 2}+ listed papers). "
          "Triage per [CONTRIBUTING.md](../CONTRIBUTING.md): check inclusion criteria, "
          "then add to `data/papers.tsv` or dismiss with a reason.\n")
    for r in candidates:
        venue = f" — *{r['venue']}*" if r["venue"] else ""
        print(f"- [ ] [{r['title']}]({r['url']}) ({r['year']}){venue} "
              f"<sub>{r['src']}, query: `{r['query']}`</sub>")

    if FAILED_FETCHES:
        print(f"\n> ⚠️ **Partial sweep**: {len(FAILED_FETCHES)} API request(s) "
              "failed after retries — results above are incomplete. "
              "Re-run the sweep before treating this month as covered.")
        print(f"partial sweep: {len(FAILED_FETCHES)} failed fetches", file=sys.stderr)
        sys.exit(3)  # signal "completed but incomplete" to the workflow


if __name__ == "__main__":
    main()
