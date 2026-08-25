#!/usr/bin/env python3
"""Regenerate the generated parts of README.md from data/papers.tsv.

Usage:
    python scripts/build_readme.py            # rewrite README.md in place
    python scripts/build_readme.py --check    # exit 1 if README.md is stale

Generated: the paper-count badge in the header, and everything between the
AUTOGEN markers (Contents + Papers). Edit data/papers.tsv (and the section
metadata below), never the generated block itself.
"""

import csv
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "papers.tsv"
README = ROOT / "README.md"

BEGIN = "<!-- AUTOGEN:PAPERS BEGIN (edit data/papers.tsv, not this section) -->"
END = "<!-- AUTOGEN:PAPERS END -->"

# Top-level groups -> sections (order defines README order).
# A section appears only if it has at least one paper in the TSV.
GROUPS = [
    ("Patent & IP Analytics", [
        ("Patent Classification & Screening",
         "Assigning patents to taxonomies (CPC/IPC or custom schemes) and screening for relevance."),
        ("Patent Landscaping & Technology Intelligence",
         "Mapping technology domains from patent corpora; competitive and R&D intelligence."),
        ("Prior-Art Search & Patent Retrieval",
         "Finding and matching prior art; patent-specific embeddings and retrieval."),
        ("Patent Drafting & Claim Generation",
         "Generating and refining patent text: claims, abstracts, full specifications."),
        ("Patent Quality, Novelty & Valuation",
         "Assessing novelty, predicting examiner outcomes, automated quality assurance."),
        ("IP Benchmarks & Evaluation",
         "Benchmarks and metrics for LLM performance on intellectual-property tasks."),
        ("IP Domain Models & Surveys",
         "Domain-adapted models and surveys of NLP/LLM methods in the patent domain."),
    ]),
    ("Technology Forecasting & Foresight", [
        ("Technology Forecasting & Foresight",
         "Emerging-technology detection, weak signals, opportunity discovery, trend prediction."),
    ]),
    ("Scientometrics & Literature Analysis", [
        ("Literature Screening & Systematic Reviews",
         "LLMs as screeners in systematic reviews — structurally the same include/exclude task as valid-patent selection."),
        ("Novelty & Impact Prediction of Research",
         "Scoring the novelty of papers and predicting their scientific impact."),
        ("Scientometrics & Science of Science",
         "Agentic and LLM-based tools for bibliometric and science-of-science analysis."),
        ("Automated Survey Writing & Paper Search",
         "Agents that search, synthesize, and write literature reviews."),
    ]),
    ("R&D & Innovation Management", [
        ("Idea Generation & Creativity in Innovation",
         "LLMs vs humans/crowds in generating product and research ideas."),
        ("New Product Development & R&D Management",
         "LLM augmentation of NPD teams and product-concept evaluation."),
    ]),
    ("Simulation, Strategy & Discovery", [
        ("Market & Consumer Simulation",
         "Generative agents simulating consumers, markets, and economies for management research."),
        ("Strategy & Decision-Making",
         "LLMs in strategic decision-making and entrepreneurship."),
        ("Scientific Discovery Agents",
         "Autonomous research agents with direct relevance to R&D processes."),
    ]),
    ("Adjacent Landmarks", [
        ("Adjacent: General MAS Frameworks & Finance",
         "Landmark frameworks and finance MAS often cited by TIM applications."),
    ]),
]

MAS_BADGE = ("<img src=\"https://img.shields.io/badge/MAS-multi--agent-8A2BE2\" "
             "alt=\"MAS\" />")


def gh_anchor(text):
    """GitHub heading -> #anchor (lowercase, punctuation dropped, spaces -> '-')."""
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def shield_escape(text):
    """Escape text for a shields.io static badge path segment."""
    text = text.replace("-", "--").replace("_", "__").replace(" ", "_")
    return urllib.parse.quote(text, safe="")


def link_badge(url):
    m = re.search(r"arxiv\.org/abs/([\w.\-]+)", url)
    if m:
        img = f"https://img.shields.io/badge/arXiv-{shield_escape(m.group(1))}-b31b1b.svg"
        return f'<a href="{url}"><img src="{img}" alt="arXiv" /></a>'
    m = re.search(r"doi\.org/(.+)$", url)
    if m:
        img = f"https://img.shields.io/badge/DOI-{shield_escape(m.group(1))}-blue.svg"
        return f'<a href="{url}"><img src="{img}" alt="DOI" /></a>'
    if "ieeexplore" in url:
        return (f'<a href="{url}"><img src="https://img.shields.io/badge/'
                f'IEEE-Xplore-00629B.svg" alt="IEEE Xplore" /></a>')
    return f'<a href="{url}"><img src="https://img.shields.io/badge/link-paper-lightgrey.svg" alt="link" /></a>'


def load_papers():
    with TSV.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    known = {name for _, secs in GROUPS for name, _ in secs}
    for row in rows:
        if row["section"] not in known:
            sys.exit(f"papers.tsv: unknown section {row['section']!r} "
                     f"(add it to GROUPS in {Path(__file__).name})")
    return rows


def paper_row(r):
    mas = f"{MAS_BADGE} " if r["mas"].strip().lower() == "yes" else ""
    desc = (f"**[{r['title']}]({r['url']})** — {r['authors']}, {r['year']}, "
            f"*{r['venue']}*. {mas}{r['summary']}")
    return f"| {desc} | {link_badge(r['url'])} |"


def section_block(name, desc, papers, level):
    papers = sorted(papers, key=lambda r: -int(r["year"]))  # stable within a year
    h = f"h{level}"
    out = ["<details open>",
           f"<summary><{h}>{name}</{h}></summary>", "",
           f"*{desc}*", "",
           "| Paper | Link |",
           "|---|---|"]
    out += [paper_row(r) for r in papers]
    out += ["", "</details>", ""]
    return out


def render(rows):
    by_sec = {}
    for r in rows:
        by_sec.setdefault(r["section"], []).append(r)

    toc, body = [], ["## Papers", "",
                     "`MAS` badge marks explicitly multi-agent systems. "
                     "Newest first within each section.", ""]
    for group, secs in GROUPS:
        live = [(n, d) for n, d in secs if by_sec.get(n)]
        if not live:
            continue
        if len(live) == 1:
            name, desc = live[0]
            toc.append(f"- [{name}](#{gh_anchor(name)}) ({len(by_sec[name])})")
            body += section_block(name, desc, by_sec[name], level=3)
        else:
            toc.append(f"- **{group}**")
            body += [f"### {group}", ""]
            for name, desc in live:
                toc.append(f"  - [{name}](#{gh_anchor(name)}) ({len(by_sec[name])})")
                body += section_block(name, desc, by_sec[name], level=4)
    toc.append("- [Related lists](#related-lists)")

    return "\n".join([BEGIN, "", "## Contents", ""] + toc + [""] + body + [END])


def main():
    rows = load_papers()
    text = README.read_text(encoding="utf-8")
    try:
        head, rest = text.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
    except ValueError:
        sys.exit("README.md: AUTOGEN markers not found")
    head = re.sub(r"papers-\d+-blue", f"papers-{len(rows)}-blue", head)
    new = head + render(rows) + tail
    if "--check" in sys.argv:
        if new != text:
            sys.exit("README.md is stale — run: python scripts/build_readme.py")
        print(f"README.md is up to date ({len(rows)} papers).")
        return
    README.write_text(new, encoding="utf-8")
    print(f"README.md regenerated ({len(rows)} papers).")


if __name__ == "__main__":
    main()
