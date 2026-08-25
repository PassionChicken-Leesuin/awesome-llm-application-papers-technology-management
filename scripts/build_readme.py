#!/usr/bin/env python3
"""Regenerate the papers section of README.md from data/papers.tsv.

Usage:
    python scripts/build_readme.py            # rewrite README.md in place
    python scripts/build_readme.py --check    # exit 1 if README.md is stale

The generated block sits between the AUTOGEN markers in README.md.
Edit data/papers.tsv (and section metadata below), never the block itself.
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "papers.tsv"
README = ROOT / "README.md"

BEGIN = "<!-- AUTOGEN:PAPERS BEGIN (edit data/papers.tsv, not this section) -->"
END = "<!-- AUTOGEN:PAPERS END -->"

# Section order and one-line descriptions. A section appears in the README
# only if it has at least one paper in the TSV.
SECTIONS = [
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
    ("Technology Forecasting & Foresight",
     "Emerging-technology detection, weak signals, opportunity discovery, trend prediction."),
    ("Literature Screening & Systematic Reviews",
     "LLMs as screeners in systematic reviews — structurally the same include/exclude task as valid-patent selection."),
    ("Novelty & Impact Prediction of Research",
     "Scoring the novelty of papers and predicting their scientific impact."),
    ("Scientometrics & Science of Science",
     "Agentic and LLM-based tools for bibliometric and science-of-science analysis."),
    ("Automated Survey Writing & Paper Search",
     "Agents that search, synthesize, and write literature reviews."),
    ("Idea Generation & Creativity in Innovation",
     "LLMs vs humans/crowds in generating product and research ideas."),
    ("New Product Development & R&D Management",
     "LLM augmentation of NPD teams and product-concept evaluation."),
    ("Market & Consumer Simulation",
     "Generative agents simulating consumers, markets, and economies for management research."),
    ("Strategy & Decision-Making",
     "LLMs in strategic decision-making and entrepreneurship."),
    ("Scientific Discovery Agents",
     "Autonomous research agents with direct relevance to R&D processes."),
    ("Adjacent: General MAS Frameworks & Finance",
     "Landmark frameworks and finance MAS often cited by TIM applications."),
]


def load_papers():
    with TSV.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    known = {name for name, _ in SECTIONS}
    for row in rows:
        if row["section"] not in known:
            sys.exit(f"papers.tsv: unknown section {row['section']!r} "
                     f"(add it to SECTIONS in {Path(__file__).name})")
    return rows


def entry_line(row):
    badge = "`MAS` " if row["mas"].strip().lower() == "yes" else ""
    return (f"* [{row['title']}]({row['url']}) — {row['authors']}, "
            f"{row['year']}, {row['venue']}. {badge}{row['summary']}")


def render(rows):
    out = [BEGIN, "",
           f"{len(rows)} papers. Newest first within each section. "
           "`MAS` marks explicitly multi-agent systems.", ""]
    for name, desc in SECTIONS:
        papers = [r for r in rows if r["section"] == name]
        if not papers:
            continue
        papers.sort(key=lambda r: -int(r["year"]))  # stable: TSV order within a year
        out += [f"### {name}", "", desc, ""]
        out += [entry_line(r) for r in papers]
        out.append("")
    out.append(END)
    return "\n".join(out)


def main():
    rows = load_papers()
    text = README.read_text(encoding="utf-8")
    try:
        head, rest = text.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
    except ValueError:
        sys.exit("README.md: AUTOGEN markers not found")
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
