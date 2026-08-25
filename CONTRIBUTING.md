# Contributing

Thanks for helping curate this list. The list is data-driven: **`data/papers.tsv` is the source of truth**, and the papers section of `README.md` is generated from it. Never edit the README between the `AUTOGEN:PAPERS` markers by hand.

## Adding a paper

1. Check the [inclusion criteria](README.md): peer-reviewed papers or public preprints (arXiv/SSRN) where an LLM or LLM-agent system is **applied to and evaluated on** a technology & innovation management (TIM) task. Tools without papers, blog posts, and pure agent-architecture papers are out of scope.
2. Add one row to `data/papers.tsv` (tab-separated, UTF-8). Columns:

   | column | meaning |
   |---|---|
   | `section` | one of the section names listed in `scripts/build_readme.py` (`SECTIONS`) |
   | `title` | full paper title, no trailing period |
   | `authors` | `Lastname et al.` |
   | `year` | publication year of the cited version |
   | `venue` | journal/conference, or `arXiv:XXXX.XXXXX` for unpublished preprints |
   | `url` | DOI link preferred; otherwise arXiv abstract page |
   | `mas` | `yes` if the paper presents an explicitly multi-agent system, else `no` |
   | `summary` | one clause, ≤ 12 words, telegraphic style matching existing entries |

   Row order within a year is preserved, and sections are sorted newest-first by year, so place your row where it should appear among same-year entries.
3. Regenerate the README and verify:

   ```bash
   python scripts/build_readme.py
   python scripts/build_readme.py --check
   ```

4. Open a PR with both the TSV change and the regenerated `README.md`. One paper per PR is easiest to review; batches are fine if they share a theme.

## Adding a section

Add the section name and a one-line description to `SECTIONS` in `scripts/build_readme.py`, in the position where it should appear. Update the `Contents` links in `README.md` if the new section starts a top-level group.

## Monthly candidate sweep

A GitHub Action (`.github/workflows/monthly-sweep.yml`) runs on the first day of each month. It queries OpenAlex and Semantic Scholar for recent papers matching TIM × LLM-agent keywords, drops anything already in `data/papers.tsv`, and opens a review issue listing the candidates. Triage that issue like a PR review: for each candidate, either add it via the steps above or dismiss it with a one-line reason. The sweep is recall-oriented — expect false positives.

You can also run the sweep locally:

```bash
python scripts/sweep_candidates.py            # prints candidates to stdout
```

## Removing or correcting entries

Corrections (venue updates when a preprint gets published, fixed links, better summaries) are very welcome — same workflow: edit the TSV, rebuild, PR.
