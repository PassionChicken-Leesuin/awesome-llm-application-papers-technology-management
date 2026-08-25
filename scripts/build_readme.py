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
        ("Trademark & Non-Patent IP",
         "IP tasks beyond patents: trademark similarity, opposition, and clearance."),
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
        ("LLM-Assisted Peer Review",
         "LLMs writing, checking, or auditing manuscript reviews — the review act itself."),
        ("Research & R&D Evaluation",
         "LLM scores as institutional evaluation signals: journal quality, research value, funding assessment."),
    ]),
    ("R&D & Innovation Management", [
        ("Idea Generation & Creativity in Innovation",
         "LLMs vs humans/crowds in generating product and research ideas."),
        ("New Product Development & R&D Management",
         "LLM augmentation of NPD teams and product-concept evaluation."),
        ("Engineering & Conceptual Design",
         "LLMs in the design front end: concept generation, TRIZ, bio-inspired design, requirements."),
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
        if row.get("tier") not in ("core", "adjacent"):
            sys.exit(f"papers.tsv: tier must be 'core' or 'adjacent' for {row['title'][:50]!r}")
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


def quarter_of(month):
    y, m = int(month[:4]), int(month[5:7])
    return (y, (m - 1) // 3 + 1)


def q_label(q):
    return f"{q[0]} Q{q[1]}"


def quarter_range(rows):
    qs = [quarter_of(r["month"]) for r in rows]
    lo, hi = min(qs), max(qs)
    out, q = [], lo
    while True:
        out.append(q)
        if q == hi:
            break
        q = (q[0] + 1, 1) if q[1] == 4 else (q[0], q[1] + 1)
    return out


def is_preprint(r):
    return r["venue"].startswith("arXiv:") or "SSRN" in r["venue"]


CHART = {
    "light": {"journal": "#2a78d6", "preprint": "#e34948", "ink2": "#52514e",
              "muted": "#898781", "grid": "#e1e0d9", "axis": "#c3c2b7"},
    "dark":  {"journal": "#3987e5", "preprint": "#e66767", "ink2": "#c3c2b7",
              "muted": "#898781", "grid": "#2c2c2a", "axis": "#383835"},
}

FONT = 'font-family="system-ui,-apple-system,Segoe UI,sans-serif"'


def render_chart(rows, mode):
    """Quarterly stacked bars: journal/conference (blue) + preprint (red)."""
    c = CHART[mode]
    bins = quarter_range(rows)
    jn = {b: 0 for b in bins}
    pp = {b: 0 for b in bins}
    for r in rows:
        (pp if is_preprint(r) else jn)[quarter_of(r["month"])] += 1
    totals = [jn[b] + pp[b] for b in bins]
    vmax = max(totals)
    peak = totals.index(vmax)
    n = len(bins)

    W, H = 900, 250
    ml, mr, mt, mb = 34, 12, 30, 32
    pw, ph = W - ml - mr, H - mt - mb
    slot = pw / n
    bw = min(44, slot * 0.62)
    step = max(1, -(-vmax // 4))
    ticks = list(range(0, vmax + step, step))
    scale_max = max(ticks[-1], vmax)
    y = lambda v: mt + ph * (1 - v / scale_max)

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" role="img" aria-label="Stacked bars of '
         f'journal and preprint papers per quarter, {q_label(bins[0])} to {q_label(bins[-1])}">']
    for t in ticks:
        if t > scale_max:
            break
        p.append(f'<line x1="{ml}" y1="{y(t):.1f}" x2="{W-mr}" y2="{y(t):.1f}" '
                 f'stroke="{c["grid"]}" stroke-width="1"/>')
        p.append(f'<text x="{ml-6}" y="{y(t)+3.5:.1f}" text-anchor="end" '
                 f'{FONT} font-size="11" fill="{c["muted"]}">{t}</text>')
    # legend (top-right)
    lx = W - mr - 330
    p.append(f'<rect x="{lx}" y="{mt-22}" width="10" height="10" rx="2" fill="{c["journal"]}"/>')
    p.append(f'<text x="{lx+15}" y="{mt-13}" {FONT} font-size="11" '
             f'fill="{c["ink2"]}">Journals &amp; conferences</text>')
    p.append(f'<rect x="{lx+165}" y="{mt-22}" width="10" height="10" rx="2" fill="{c["preprint"]}"/>')
    p.append(f'<text x="{lx+180}" y="{mt-13}" {FONT} font-size="11" '
             f'fill="{c["ink2"]}">Preprints (arXiv/SSRN)</text>')

    base = mt + ph
    for i, b in enumerate(bins):
        x = ml + i * slot + (slot - bw) / 2
        j, a = jn[b], pp[b]
        # journal segment (blue, bottom), square top
        if j:
            p.append(f'<rect x="{x:.1f}" y="{y(j):.1f}" width="{bw:.1f}" '
                     f'height="{base - y(j):.1f}" fill="{c["journal"]}"/>')
        # preprint segment (red, top), 2px surface gap, rounded top
        if a:
            top = y(j + a)
            bot = y(j) - (2 if j else 0)
            h = max(bot - top, 1.5)
            r = min(4.0, h)
            p.append(f'<path d="M{x:.1f},{bot:.1f} v{-(h - r):.1f} '
                     f'q0,{-r} {r},{-r} h{bw - 2*r:.1f} q{r},0 {r},{r} '
                     f'v{h - r:.1f} z" fill="{c["preprint"]}"/>')
        elif j:  # journal-only bar gets the rounded cap instead
            pass
        if i == peak or i == n - 1:
            t = j + a
            p.append(f'<text x="{x + bw/2:.1f}" y="{y(t)-6:.1f}" text-anchor="middle" '
                     f'{FONT} font-size="11" font-weight="600" fill="{c["ink2"]}">{t}</text>')
        lbl = q_label(b) if b[1] == 1 or i == 0 else f"Q{b[1]}"
        p.append(f'<text x="{x + bw/2:.1f}" y="{H-mb+16}" text-anchor="middle" '
                 f'{FONT} font-size="10.5" fill="{c["muted"]}">{lbl}</text>')
    p.append(f'<line x1="{ml}" y1="{base}" x2="{W-mr}" y2="{base}" '
             f'stroke="{c["axis"]}" stroke-width="1"/>')
    p.append("</svg>")
    return "\n".join(p) + "\n"


# Sequential blue ramps for the field heatmap (low -> high).
HEAT = {
    "light": ["#cde2fb", "#9ec5f4", "#5598e7", "#2a78d6", "#184f95"],
    "dark":  ["#184f95", "#1c5cab", "#2a78d6", "#5598e7", "#9ec5f4"],
}
# ink that clears each ramp step (indexes match HEAT)
HEAT_INK = {
    "light": ["#0b0b0b", "#0b0b0b", "#ffffff", "#ffffff", "#ffffff"],
    "dark":  ["#ffffff", "#ffffff", "#ffffff", "#0b0b0b", "#0b0b0b"],
}
GROUP_SHORT = {
    "Patent & IP Analytics": "Patent & IP",
    "Technology Forecasting & Foresight": "Tech Forecasting",
    "Scientometrics & Literature Analysis": "Scientometrics & Lit",
    "R&D & Innovation Management": "R&D & Innovation",
    "Simulation, Strategy & Discovery": "Simulation & Strategy",
    "Adjacent Landmarks": "Adjacent (MAS/Finance)",
}


def render_heatmap(rows, mode):
    """Groups x quarters heatmap: which research cluster peaks when."""
    c = CHART[mode]
    sec2group = {name: g for g, secs in GROUPS for name, _ in secs}
    bins = quarter_range(rows)
    live_groups = {sec2group[r["section"]] for r in rows}
    groups = [g for g, _ in GROUPS if g in live_groups]
    counts = {(g, b): 0 for g in groups for b in bins}
    for r in rows:
        counts[(sec2group[r["section"]], quarter_of(r["month"]))] += 1
    vmax = max(counts.values())

    lw = 150                     # row-label gutter
    cw, ch, gap = 52, 30, 3      # cell size and spacing
    W = lw + len(bins) * (cw + gap) + 12
    H = 26 + len(groups) * (ch + gap) + 26

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" role="img" '
         f'aria-label="Heatmap of papers per research area per quarter">']
    for gi, g in enumerate(groups):
        yy = 26 + gi * (ch + gap)
        label = GROUP_SHORT[g].replace("&", "&amp;")
        p.append(f'<text x="{lw-8}" y="{yy + ch/2 + 3.5}" text-anchor="end" '
                 f'{FONT} font-size="11" fill="{c["ink2"]}">{label}</text>')
        for bi, b in enumerate(bins):
            x = lw + bi * (cw + gap)
            v = counts[(g, b)]
            if v == 0:
                p.append(f'<rect x="{x}" y="{yy}" width="{cw}" height="{ch}" rx="4" '
                         f'fill="none" stroke="{c["grid"]}" stroke-width="1"/>')
                continue
            step = min(4, int(4 * (v - 1) / max(vmax - 1, 1) + 0.9999)) if vmax > 1 else 4
            p.append(f'<rect x="{x}" y="{yy}" width="{cw}" height="{ch}" rx="4" '
                     f'fill="{HEAT[mode][step]}"/>')
            p.append(f'<text x="{x + cw/2}" y="{yy + ch/2 + 4}" text-anchor="middle" '
                     f'{FONT} font-size="11.5" font-weight="600" '
                     f'fill="{HEAT_INK[mode][step]}">{v}</text>')
    for bi, b in enumerate(bins):
        x = lw + bi * (cw + gap) + cw / 2
        lbl = q_label(b) if b[1] == 1 or bi == 0 else f"Q{b[1]}"
        p.append(f'<text x="{x}" y="{H-8}" text-anchor="middle" {FONT} '
                 f'font-size="10.5" fill="{c["muted"]}">{lbl}</text>')
    p.append(f'<text x="{lw}" y="14" {FONT} font-size="10.5" fill="{c["muted"]}">'
             f'papers per quarter — darker (light mode) / brighter (dark mode) = more</text>')
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


ADJ_HEADING = "Adjacent & enabling methods"
ADJ_INTRO = ("Benchmarks, domain models, surveys, generic-domain analogues "
             "(e.g. medical systematic-review screening), and landmark frameworks "
             "that TIM applications build on. Kept for reference — "
             "**not counted in the headline paper count or charts**.")


def render(core, adj):
    by_sec = {}
    for r in core:
        by_sec.setdefault(r["section"], []).append(r)
    adj_by_sec = {}
    for r in adj:
        adj_by_sec.setdefault(r["section"], []).append(r)

    toc, body = [], ["## Papers", "",
                     f"{len(core)} core papers. `MAS` badge marks explicitly "
                     "multi-agent systems. Newest first within each section.", ""]
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

    if adj:
        toc.append(f"- [{ADJ_HEADING}](#{gh_anchor(ADJ_HEADING)}) ({len(adj)})")
        body += [f"## {ADJ_HEADING}", "", ADJ_INTRO, ""]
        for group, secs in GROUPS:
            for name, desc in secs:
                if adj_by_sec.get(name):
                    body += section_block(name, desc, adj_by_sec[name], level=3)
    toc.append("- [Related lists](#related-lists)")

    return "\n".join([BEGIN, "", "## Contents", ""] + toc + [""] + body + [END])


def main():
    rows = load_papers()
    core = [r for r in rows if r["tier"] == "core"]
    adj = [r for r in rows if r["tier"] == "adjacent"]
    text = README.read_text(encoding="utf-8")
    try:
        head, rest = text.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
    except ValueError:
        sys.exit("README.md: AUTOGEN:PAPERS markers not found")
    head = re.sub(r"papers-\d+-blue", f"papers-{len(core)}-blue", head)
    head = re.sub(r"adjacent-\d+-lightgrey", f"adjacent-{len(adj)}-lightgrey", head)
    if V_BEGIN in head:
        try:
            v_head, v_rest = head.split(V_BEGIN, 1)
            _, v_tail = v_rest.split(V_END, 1)
        except ValueError:
            sys.exit("README.md: AUTOGEN:VENUES markers malformed")
        head = v_head + render_venues(core) + v_tail
    new = head + render(core, adj) + tail
    charts = {}
    for m in ("light", "dark"):
        charts[ROOT / "assets" / f"trend-{m}.svg"] = render_chart(core, m)
        charts[ROOT / "assets" / f"fields-{m}.svg"] = render_heatmap(core, m)
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
