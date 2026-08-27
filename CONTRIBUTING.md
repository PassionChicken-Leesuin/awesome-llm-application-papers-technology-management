# Contributing

Thanks you for helping curate this list. The list is data-driven: **`data/papers.tsv` is the source of truth**, and the generated parts of `README.md` — the paper-count badge, the trend chart (`assets/trend-*.svg`), the venue table, the Contents (with per-section counts), and the Papers tables — are built from it. Never edit the README between the `AUTOGEN:PAPERS` markers by hand.

## Adding a paper

1. Check the [inclusion criteria](README.md): peer-reviewed papers or public preprints (arXiv/SSRN) where an LLM or LLM-agent system is **applied to and evaluated on** a technology & innovation management (TIM) task. Tools without papers, blog posts, and pure agent-architecture papers are out of scope.
2. Add one row to `data/papers.tsv` (tab-separated, UTF-8). Columns:

   | column | meaning |
   |---|---|
   | `section` | one of the section names listed in `scripts/build_readme.py` (`GROUPS`) |
   | `title` | full paper title, no trailing period |
   | `authors` | `Lastname et al.` |
   | `year` | publication year of the cited version |
   | `venue` | journal/conference, or `arXiv:XXXX.XXXXX` for unpublished preprints |
   | `url` | DOI link preferred; otherwise arXiv abstract page |
   | `mas` | `yes` if the paper presents an explicitly multi-agent system (adds the purple `MAS` badge), else `no` |
   | `summary` | one clause, ≤ 12 words, telegraphic style matching existing entries |
   | `month` | `YYYY-MM` of **first public appearance** (arXiv posting month from the ID, or the journal's online-first date per Crossref) — feeds the trend chart |
   | `tier` | `core` for papers applying an LLM/agent **directly to a TIM task**; `adjacent` for benchmarks, domain models, surveys, generic-domain analogues, and enabling frameworks. Only `core` counts toward the badge and charts |

   Row order within a year is preserved, and sections are sorted newest-first by year, so place your row where it should appear among same-year entries.
3. Regenerate the README and verify:

   ```bash
   python scripts/build_readme.py
   python scripts/build_readme.py --check
   ```

4. Open a PR with both the TSV change and the regenerated `README.md`. One paper per PR is easiest to review; batches are fine if they share a theme.

## Adding a section

Add the section name and a one-line description to `GROUPS` in `scripts/build_readme.py`, under the top-level group where it belongs (or as a new group). The Contents links and counts regenerate automatically.

## Monthly candidate sweep

A GitHub Action (`.github/workflows/monthly-sweep.yml`) runs on the first day of each month and opens a review issue listing candidates. It searches along **two axes**, because each one is blind to what the other catches:

| axis | what it does | what it misses |
|---|---|---|
| **keyword** | free-text TIM × LLM/agent queries against OpenAlex and Semantic Scholar, last 2 months | journal papers that phrase the same task differently — "evaluating creative output" for idea generation, "granular classification" for landscaping |
| **venue** | a named list of ~40 TIM / scientometrics / engineering-design / strategy journals, intersected with (LLM term AND TIM-task term), last 12 months | anything published outside the named venue list |

The venue axis runs on a wider window because journals lag: a paper can sit online-first for months, and issue assignment moves its date again.

Triage the issue like a PR review. For each candidate, either add it via the steps above, **or append a row to `data/dismissed.tsv`** with a reason. The sweep dedupes against both `papers.tsv` and `dismissed.tsv`, so a paper you rejected stays rejected instead of reappearing every month. Columns: `title`, `url`, `venue`, `year`, `reason`, `dismissed` (YYYY-MM-DD).

The sweep is recall-oriented — expect false positives. Leaving a candidate untriaged is fine; it resurfaces next month, which beats a rushed call.

You can also run it locally:

```bash
python scripts/sweep_candidates.py
```

```bash
python scripts/sweep_candidates.py --axis venue --venue-months 24
```

Set `SWEEP_MAILTO` to your email to use the OpenAlex polite pool.

### Adding a venue

Add its ISSN and a short label to `VENUES` in `scripts/sweep_candidates.py`, using the print ISSN where a journal has both. A venue earns a place if it has published — or would plausibly publish — an LLM-applied-to-TIM paper, not merely because it is a good journal.

## Removing or correcting entries

Corrections (venue updates when a preprint gets published, fixed links, better summaries) are very welcome — same workflow: edit the TSV, rebuild, PR.
