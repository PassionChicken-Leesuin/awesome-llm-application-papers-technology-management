#!/usr/bin/env python3
"""Monthly candidate sweep for the awesome list.

Two independent search axes, because they miss different things:

  keyword axis  free-text TIM x LLM/agent queries against OpenAlex and
                Semantic Scholar. Good at catching arXiv preprints early;
                blind to journal papers whose abstracts phrase the task
                differently.
  venue  axis   a named list of TIM / scientometrics / engineering-design /
                strategy journals, intersected with (LLM term AND TIM-task
                term). Good at catching journal papers the keyword axis
                phrases past; blind to venues not on the list.

Both drop anything already in data/papers.tsv (matched by normalized title
or DOI/arXiv id) and print the survivors as a markdown checklist (used as
the body of the review issue).

No API keys required; both APIs are public. Recall-oriented by design --
expect false positives, humans triage.

Usage:
    python scripts/sweep_candidates.py                    # both axes
    python scripts/sweep_candidates.py --axis venue       # one axis only
    python scripts/sweep_candidates.py --months 2 --venue-months 12
"""

import argparse
import csv
import json
import os
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
DISMISSED = ROOT / "data" / "dismissed.tsv"

# Polite-pool contact for OpenAlex. Override with SWEEP_MAILTO in CI.
MAILTO = os.environ.get("SWEEP_MAILTO", "openalex@example.org")

# ---------------------------------------------------------------- keyword axis

# Each query pairs an LLM/agent term with a TIM task term.
QUERIES = [
    '"large language model" patent',
    '"LLM" "patent classification"',
    '"LLM agent" patent',
    '"multi-agent" patent analysis',
    '"large language model" "prior art"',
    '"LLM" "patent claim" generation',
    '"large language model" trademark',
    '"large language model" "technology forecasting"',
    '"large language model" "technology opportunity"',
    '"LLM" "emerging technology" detection',
    '"large language model" "weak signal" OR "horizon scanning"',
    '"LLM agents" Delphi OR foresight',
    '"LLM" scientometrics',
    '"large language model" bibliometric',
    '"large language model" "science of science"',
    '"LLM" "research evaluation"',
    '"large language model" "peer review"',
    '"LLM" "systematic review" screening',
    '"large language model" "idea generation" innovation',
    '"LLM agents" "research idea" generation',
    '"generative AI" "new product development"',
    '"large language model" "concept generation" design',
    '"LLM" TRIZ OR "inventive problem"',
    '"large language model" "engineering design" ideation',
    '"LLM agents" "market simulation"',
    '"LLM agents" conjoint OR "willingness to pay"',
    '"large language model" "competitive intelligence"',
    '"large language model" "innovation management"',
    '"large language model" "technology roadmap"',
    '"large language model" "technology transfer" OR "IP licensing"',
    '"LLM" "R&D portfolio" OR "R&D project management"',
    '"large language model" standards OR regulation "technology management"',
    '"LLM" commercialization OR "startup scouting"',
    '"generative AI" "digital prototyping"',
]

# ------------------------------------------------------------------ venue axis

# ISSN -> display label. Venues that publish LLM-applied-to-TIM work.
VENUES = {
    # innovation & technology management
    "0048-7333": "Research Policy",
    "0166-4972": "Technovation",
    "0040-1625": "Technological Forecasting and Social Change",
    "0018-9391": "IEEE Trans. Engineering Management",
    "0033-6807": "R&D Management",
    "0923-4748": "Journal of Engineering and Technology Management",
    "0953-7325": "Technology Analysis & Strategic Management",
    "0024-6301": "Long Range Planning",
    "0963-1690": "Creativity and Innovation Management",
    "1363-9196": "International Journal of Innovation Management",
    "0737-6782": "Journal of Product Innovation Management",
    "0960-6491": "Industrial and Corporate Change",
    "0160-791X": "Technology in Society",
    "1367-3270": "Journal of Knowledge Management",
    # scientometrics, informetrics & IP
    "0138-9130": "Scientometrics",
    "1751-1577": "Journal of Informetrics",
    "2641-3337": "Quantitative Science Studies",
    "0958-2029": "Research Evaluation",
    "2330-1635": "JASIST",
    "0306-4573": "Information Processing & Management",
    "0172-2190": "World Patent Information",
    "2096-157X": "Journal of Data and Information Science",
    # applied AI venues that carry TIM applications
    "0957-4174": "Expert Systems with Applications",
    "1474-0346": "Advanced Engineering Informatics",
    "0952-1976": "Engineering Applications of AI",
    # engineering design & manufacturing
    "0142-694X": "Design Studies",
    "1050-0472": "Journal of Mechanical Design",
    "0954-4828": "Journal of Engineering Design",
    "2053-4701": "Design Science",
    "0890-0604": "AI EDAM",
    "0007-8506": "CIRP Annals",
    "0278-6125": "Journal of Manufacturing Systems",
    # strategy, management & IS
    "0143-2095": "Strategic Management Journal",
    "0025-1909": "Management Science",
    "1047-7039": "Organization Science",
    "0001-4273": "Academy of Management Journal",
    "0276-7783": "MIS Quarterly",
    "1047-7047": "Information Systems Research",
    "0883-9026": "Journal of Business Venturing",
    "1932-4391": "Strategic Entrepreneurship Journal",
    "0148-2963": "Journal of Business Research",
    # broad-audience science
    "2397-3374": "Nature Human Behaviour",
}

VENUE_LLM = (
    '("large language model" OR "large language models" OR LLM OR LLMs OR "GPT-4" '
    'OR ChatGPT OR "generative AI" OR "generative artificial intelligence" '
    'OR "foundation model" OR "LLM agent" OR "LLM agents" OR "agentic AI" '
    'OR "retrieval-augmented generation")'
)
VENUE_TIM = (
    '(patent OR patents OR "intellectual property" OR "technology forecasting" '
    'OR "technology management" OR "innovation management" OR "new product development" '
    'OR scientometric OR bibliometric OR "prior art" OR roadmapping '
    'OR "technology intelligence" OR "idea generation" OR ideation '
    'OR "systematic review" OR "literature review" OR "scientific discovery" '
    'OR "peer review" OR "research evaluation" OR "emerging technology" '
    'OR "technology opportunity" OR "concept generation" OR "engineering design" '
    'OR TRIZ OR trademark OR "R&D")'
)


def norm_title(t):
    t = unicodedata.normalize("NFKD", t or "").lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


FAILED_FETCHES = []  # sweep is only complete if this stays empty
COUNTS = {"listed": 0, "dismissed": 0}


def get_json(url, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": f"awesome-tm-sweep (mailto:{MAILTO})"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 -- best-effort sweep
            if i == tries - 1:
                print(f"WARN: giving up on {url}: {e}", file=sys.stderr)
                FAILED_FETCHES.append(url)
                return None
            time.sleep(2 * (i + 1))


def _ident(title, url):
    """Keys a paper is recognized by: normalized title, plus DOI/arXiv id."""
    out = [norm_title(title)]
    m = re.search(r"(?:doi\.org/|arxiv\.org/abs/)(.+)$", url or "")
    if m:
        out.append(m.group(1).lower())
    return [k for k in out if k]


def known_keys():
    """Papers the sweep should not re-surface: already listed, or already dismissed.

    Without the dismissed ledger every triaged-and-rejected paper reappears in
    next month's issue, which the wide venue-axis window makes unmanageable.
    """
    keys = set()
    with TSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            keys.update(_ident(row["title"], row["url"]))
            COUNTS["listed"] += 1

    if DISMISSED.exists():
        with DISMISSED.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                keys.update(_ident(row["title"], row.get("url", "")))
                COUNTS["dismissed"] += 1
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
            "axis": "keyword",
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
            "axis": "keyword",
            "query": query,
        }


def venue_axis(since):
    """Walk the named-venue list in ISSN batches, cursor-paginating each batch."""
    issns = list(VENUES)
    for start in range(0, len(issns), 15):
        batch = issns[start:start + 15]
        cursor = "*"
        while cursor:
            url = ("https://api.openalex.org/works?"
                   + urllib.parse.urlencode({
                       "filter": (f"primary_location.source.issn:{'|'.join(batch)},"
                                  f"from_publication_date:{since},"
                                  f"title_and_abstract.search:{VENUE_LLM} AND {VENUE_TIM}"),
                       "per-page": 200,
                       "cursor": cursor,
                       "mailto": MAILTO,
                       "select": "id,doi,display_name,publication_year,primary_location",
                   }))
            data = get_json(url)
            if not data:
                break
            for w in data.get("results", []):
                doi = (w.get("doi") or "").replace("https://doi.org/", "")
                src = (w.get("primary_location") or {}).get("source") or {}
                label = next((VENUES[i] for i in (src.get("issn") or []) if i in VENUES),
                             src.get("display_name") or "")
                yield {
                    "title": w.get("display_name") or "",
                    "year": w.get("publication_year"),
                    "url": w.get("doi") or w.get("id"),
                    "venue": label,
                    "id": doi.lower(),
                    "src": "OpenAlex",
                    "axis": "venue",
                    "query": label,
                }
            cursor = data.get("meta", {}).get("next_cursor")
            time.sleep(0.4)


def months_ago(n):
    today = date.today()
    total = today.year * 12 + (today.month - 1) - n
    y, m0 = divmod(total, 12)
    return date(y, m0 + 1, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--months", type=int, default=2,
                    help="keyword-axis look-back window in months")
    ap.add_argument("--venue-months", type=int, default=12,
                    help="venue-axis look-back; journals lag, so this runs wider")
    ap.add_argument("--axis", choices=["keyword", "venue", "all"], default="all")
    ap.add_argument("--per-query", type=int, default=25)
    args = ap.parse_args()

    since = months_ago(args.months)
    venue_since = months_ago(args.venue_months)

    known = known_keys()
    seen, candidates = set(), []

    def absorb(rows):
        for r in rows:
            key = norm_title(r["title"])
            if not key or key in known or key in seen or (r["id"] and r["id"] in known):
                continue
            seen.add(key)
            candidates.append(r)

    if args.axis in ("keyword", "all"):
        for q in QUERIES:
            absorb(openalex(q, since.isoformat(), args.per_query))
            absorb(semantic_scholar(q, since.year, args.per_query))
            time.sleep(1)  # be nice to both APIs

    if args.axis in ("venue", "all"):
        absorb(venue_axis(venue_since.isoformat()))

    candidates.sort(key=lambda r: (r["axis"], -(r["year"] or 0), r["title"]))

    today = date.today()
    print(f"## Candidate sweep {today.isoformat()}\n")
    kw = [c for c in candidates if c["axis"] == "keyword"]
    vn = [c for c in candidates if c["axis"] == "venue"]
    print(f"{len(candidates)} candidates "
          f"({len(kw)} keyword axis since {since}, "
          f"{len(vn)} venue axis since {venue_since} across {len(VENUES)} named venues), "
          f"deduplicated against {COUNTS['listed']} listed "
          f"and {COUNTS['dismissed']} previously dismissed papers. "
          "Triage per [CONTRIBUTING.md](../CONTRIBUTING.md): check inclusion criteria, "
          "then add to `data/papers.tsv`, or record it in `data/dismissed.tsv` "
          "with a reason so it stops resurfacing.\n")

    for label, group in (("Keyword axis", kw), ("Venue axis", vn)):
        if not group:
            continue
        print(f"### {label}\n")
        for r in group:
            venue = f" — *{r['venue']}*" if r["venue"] else ""
            print(f"- [ ] [{r['title']}]({r['url']}) ({r['year']}){venue} "
                  f"<sub>{r['src']}, {r['axis']}: `{r['query']}`</sub>")
        print()

    if FAILED_FETCHES:
        print(f"\n> ⚠️ **Partial sweep**: {len(FAILED_FETCHES)} API request(s) "
              "failed after retries — results above are incomplete. "
              "Re-run the sweep before treating this month as covered.")
        print(f"partial sweep: {len(FAILED_FETCHES)} failed fetches", file=sys.stderr)
        sys.exit(3)  # signal "completed but incomplete" to the workflow


if __name__ == "__main__":
    main()
