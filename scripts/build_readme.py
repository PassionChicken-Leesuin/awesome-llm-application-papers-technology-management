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
V_BEGIN = "<!-- AUTOGEN:VENUES BEGIN (generated from data/papers.tsv) -->"
V_END = "<!-- AUTOGEN:VENUES END -->"

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
        if not re.fullmatch(r"20\d\d-(0[1-9]|1[0-2])", row.get("month") or ""):
            sys.exit(f"papers.tsv: missing/invalid month for {row['title'][:50]!r} "
                     "(expected YYYY-MM — first public appearance)")
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


def bin_of(month):
    """'YYYY-MM' -> bin key: half-yearly through 2025, monthly from 2026."""
    y, m = int(month[:4]), int(month[5:7])
    if y <= 2025:
        return (y, 1 if m <= 6 else 2, "H")
    return (y, m, "M")


def bin_label(b):
    y, v, kind = b
    if kind == "H":
        return f"{y} H{v}"
    return f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][v-1]} {y}"


def next_bin(b):
    y, v, kind = b
    if kind == "H":
        if v == 1:
            return (y, 2, "H")
        return (y + 1, 1, "M") if y + 1 >= 2026 else (y + 1, 1, "H")
    return (y, v + 1, "M") if v < 12 else (y + 1, 1, "M")


CHART = {
    "light": {"bar": "#2a78d6", "ink2": "#52514e", "muted": "#898781",
              "grid": "#e1e0d9", "axis": "#c3c2b7"},
    "dark":  {"bar": "#3987e5", "ink2": "#c3c2b7", "muted": "#898781",
              "grid": "#2c2c2a", "axis": "#383835"},
}


def render_chart(rows, mode):
    """Single-series bar chart of papers per time bin, as an SVG string."""
    c = CHART[mode]
    counts = {}
    for r in rows:
        counts[bin_of(r["month"])] = counts.get(bin_of(r["month"]), 0) + 1
    lo, hi = min(counts), max(counts)
    bins, b = [], lo
    while True:
        bins.append(b)
        if b == hi:
            break
        b = next_bin(b)
    vals = [counts.get(b, 0) for b in bins]
    vmax = max(vals)
    peak = vals.index(vmax)

    W, H = 900, 240
    ml, mr, mt, mb = 34, 12, 18, 34
    pw, ph = W - ml - mr, H - mt - mb
    n = len(bins)
    slot = pw / n
    bw = min(46, slot * 0.62)
    ticks = list(range(0, vmax + 1, max(1, (vmax + 3) // 4)))
    y = lambda v: mt + ph * (1 - v / (ticks[-1] if ticks[-1] >= vmax else vmax))

    font = 'font-family="system-ui,-apple-system,Segoe UI,sans-serif"'
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" role="img" '
         f'aria-label="Papers per period, {bin_label(lo)} to {bin_label(hi)}">']
    for t in ticks:
        p.append(f'<line x1="{ml}" y1="{y(t):.1f}" x2="{W-mr}" y2="{y(t):.1f}" '
                 f'stroke="{c["grid"]}" stroke-width="1"/>')
        p.append(f'<text x="{ml-6}" y="{y(t)+3.5:.1f}" text-anchor="end" '
                 f'{font} font-size="11" fill="{c["muted"]}">{t}</text>')
    # divider between half-yearly and monthly zones
    for i, b in enumerate(bins):
        if b[2] == "M":
            xd = ml + i * slot
            p.append(f'<line x1="{xd:.1f}" y1="{mt-6}" x2="{xd:.1f}" y2="{mt+ph}" '
                     f'stroke="{c["axis"]}" stroke-width="1" stroke-dasharray="3 4"/>')
            p.append(f'<text x="{xd-5:.1f}" y="{mt+2}" text-anchor="end" {font} '
                     f'font-size="10" fill="{c["muted"]}">half-yearly</text>')
            p.append(f'<text x="{xd+5:.1f}" y="{mt+2}" {font} '
                     f'font-size="10" fill="{c["muted"]}">monthly</text>')
            break
    for i, (b, v) in enumerate(zip(bins, vals)):
        x = ml + i * slot + (slot - bw) / 2
        if v:
            top, base, r = y(v), mt + ph, 4
            h = base - top
            r = min(r, h)
            p.append(f'<path d="M{x:.1f},{base:.1f} v{-(h - r):.1f} '
                     f'q0,{-r} {r},{-r} h{bw - 2*r:.1f} q{r},0 {r},{r} '
                     f'v{h - r:.1f} z" fill="{c["bar"]}"/>')
        if i == peak or i == n - 1:
            p.append(f'<text x="{x + bw/2:.1f}" y="{y(v)-6:.1f}" text-anchor="middle" '
                     f'{font} font-size="11" font-weight="600" fill="{c["ink2"]}">{v}</text>')
        p.append(f'<text x="{x + bw/2:.1f}" y="{H-mb+16}" text-anchor="middle" '
                 f'{font} font-size="10.5" fill="{c["muted"]}">{bin_label(b)}</text>')
    p.append(f'<line x1="{ml}" y1="{mt+ph}" x2="{W-mr}" y2="{mt+ph}" '
             f'stroke="{c["axis"]}" stroke-width="1"/>')
    p.append("</svg>")
    return "\n".join(p) + "\n"


def venue_group(venue):
    """Normalize a venue string to a display group for the venue table."""
    if venue.startswith("arXiv:"):
        return "arXiv (preprints)"
    if "SSRN" in venue:
        return "SSRN (working papers)"
    for conf in ("NAACL", "ACL", "SIGIR", "NeurIPS", "ICLR", "ICML",
                 "LREC-COLING", "UIST"):
        if conf in venue:
            return conf
    return venue


def render_venues(rows):
    counts = {}
    for r in rows:
        g = venue_group(r["venue"])
        counts[g] = counts.get(g, 0) + 1
    multi = sorted(((n, v) for v, n in counts.items() if n >= 2),
                   key=lambda x: (-x[0], x[1]))
    singles = sorted(v for v, n in counts.items() if n == 1)
    out = [V_BEGIN, "", "### Where these papers appear", "",
           "| Venue | Papers |", "|---|---:|"]
    out += [f"| {v} | {n} |" for n, v in multi]
    if singles:
        out.append(f"| Others (1 each): {', '.join(singles)} | {len(singles)} |")
    out += ["", V_END]
    return "\n".join(out)


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
        sys.exit("README.md: AUTOGEN:PAPERS markers not found")
    head = re.sub(r"papers-\d+-blue", f"papers-{len(rows)}-blue", head)
    if V_BEGIN in head:
        try:
            v_head, v_rest = head.split(V_BEGIN, 1)
            _, v_tail = v_rest.split(V_END, 1)
        except ValueError:
            sys.exit("README.md: AUTOGEN:VENUES markers malformed")
        head = v_head + render_venues(rows) + v_tail
    new = head + render(rows) + tail
    charts = {ROOT / "assets" / f"trend-{m}.svg": render_chart(rows, m)
              for m in ("light", "dark")}
    if "--check" in sys.argv:
        stale = new != text or any(
            not f.exists() or f.read_text(encoding="utf-8") != svg
            for f, svg in charts.items())
        if stale:
            sys.exit("README.md/assets are stale — run: python scripts/build_readme.py")
        print(f"README.md and trend charts are up to date ({len(rows)} papers).")
        return
    README.write_text(new, encoding="utf-8")
    (ROOT / "assets").mkdir(exist_ok=True)
    for f, svg in charts.items():
        f.write_text(svg, encoding="utf-8")
    print(f"README.md and trend charts regenerated ({len(rows)} papers).")


if __name__ == "__main__":
    main()
