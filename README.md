# Awesome LLM Agents for Technology & Innovation Management

<div align="center">

**Hand-picked research papers applying LLMs, LLM agents, and multi-agent systems (MAS) to technology & innovation management (TIM).**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-91-blue)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

patent analytics · technology forecasting · scientometrics · literature screening · R&D & innovation management · market simulation

</div>

### Papers over time

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/trend-dark.svg">
  <img alt="Stacked bar chart of journal and preprint papers per quarter" src="assets/trend-light.svg" width="100%">
</picture>

*Quarterly counts, dated by first public appearance (arXiv posting or journal online date). Blue = journals & conferences, red = preprints (arXiv/SSRN).*

### Which areas peak when

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/fields-dark.svg">
  <img alt="Heatmap of papers per research area per quarter" src="assets/fields-light.svg" width="100%">
</picture>

*Papers per research area per quarter — the hot cells show each cluster's peak period.*

<!-- AUTOGEN:VENUES BEGIN (generated from data/papers.tsv) -->

### Where these papers appear

| Venue | Papers |
|---|---:|
| arXiv (preprints) | 48 |
| ACL | 3 |
| Scientometrics | 3 |
| World Patent Information | 3 |
| ICLR | 2 |
| Journal of Product Innovation Management | 2 |
| NAACL | 2 |
| Nature | 2 |
| NeurIPS | 2 |
| SIGIR | 2 |
| SSRN (working papers) | 2 |
| Technological Forecasting and Social Change | 2 |
| Others (1 each): AAAI 2026, Advanced Engineering Informatics, AgentScen @ IJCAI 2025, Artificial Intelligence Review, EMNLP 2024, Engineering Applications of Artificial Intelligence, ICML, IEEE Engineering Management Review, JASIST, Journal of Computer Languages, LREC-COLING, Nature Machine Intelligence, Organization Science, Research Synthesis Methods, SIGDIAL 2025, Science Advances, Strategy Science, UIST | 18 |

<!-- AUTOGEN:VENUES END -->

## Why this list exists

Most agent paper lists collect research *on* agent architectures (memory, planning, coordination). This list collects the complement: research that *uses* agents on real TIM tasks — the papers that end up scattered across *TFSC*, *Scientometrics*, *World Patent Information*, management journals, and application tracks, and therefore rarely appear in ML-centric lists.

**Inclusion criteria**: peer-reviewed papers or public preprints (arXiv/SSRN) where an LLM or LLM-agent system is applied to and evaluated on a TIM task. Tools without papers, blog posts, and pure architecture papers are out of scope.

Maintained with a human-in-the-loop pipeline: a monthly GitHub Action sweeps OpenAlex and Semantic Scholar for candidates and opens a review issue; humans curate (see [CONTRIBUTING.md](CONTRIBUTING.md)). The list itself lives in `data/papers.tsv`; the contents and papers sections below are generated from it.

<!-- AUTOGEN:PAPERS BEGIN (edit data/papers.tsv, not this section) -->

## Contents

- **Patent & IP Analytics**
  - [Patent Classification & Screening](#patent-classification--screening) (3)
  - [Patent Landscaping & Technology Intelligence](#patent-landscaping--technology-intelligence) (6)
  - [Prior-Art Search & Patent Retrieval](#prior-art-search--patent-retrieval) (3)
  - [Patent Drafting & Claim Generation](#patent-drafting--claim-generation) (7)
  - [Patent Quality, Novelty & Valuation](#patent-quality-novelty--valuation) (3)
  - [IP Benchmarks & Evaluation](#ip-benchmarks--evaluation) (6)
  - [IP Domain Models & Surveys](#ip-domain-models--surveys) (2)
- [Technology Forecasting & Foresight](#technology-forecasting--foresight) (8)
- **Scientometrics & Literature Analysis**
  - [Literature Screening & Systematic Reviews](#literature-screening--systematic-reviews) (6)
  - [Novelty & Impact Prediction of Research](#novelty--impact-prediction-of-research) (6)
  - [Scientometrics & Science of Science](#scientometrics--science-of-science) (5)
  - [Automated Survey Writing & Paper Search](#automated-survey-writing--paper-search) (5)
- **R&D & Innovation Management**
  - [Idea Generation & Creativity in Innovation](#idea-generation--creativity-in-innovation) (11)
  - [New Product Development & R&D Management](#new-product-development--rd-management) (2)
- **Simulation, Strategy & Discovery**
  - [Market & Consumer Simulation](#market--consumer-simulation) (6)
  - [Strategy & Decision-Making](#strategy--decision-making) (1)
  - [Scientific Discovery Agents](#scientific-discovery-agents) (7)
- [Adjacent: General MAS Frameworks & Finance](#adjacent-general-mas-frameworks--finance) (4)
- [Related lists](#related-lists)

## Papers

`MAS` badge marks explicitly multi-agent systems. Newest first within each section.

### Patent & IP Analytics

<details open>
<summary><h4>Patent Classification & Screening</h4></summary>

*Assigning patents to taxonomies (CPC/IPC or custom schemes) and screening for relevance.*

| Paper | Link |
|---|---|
| **[Large Language Models for Patent Classification: Strengths, Trade-offs, and the Long Tail Effect](https://arxiv.org/abs/2601.23200)** — Emer et al., 2026, *arXiv:2601.23200*. Compares LLMs vs BERT on CPC; LLMs win on rare subclasses | <a href="https://arxiv.org/abs/2601.23200"><img src="https://img.shields.io/badge/arXiv-2601.23200-b31b1b.svg" alt="arXiv" /></a> |
| **[Patent Figure Classification using Large Vision-language Models](https://arxiv.org/abs/2501.12751)** — Awale et al., 2025, *arXiv:2501.12751*. LVLMs classify patent figures; PatFigVQA/PatFigCLS datasets | <a href="https://arxiv.org/abs/2501.12751"><img src="https://img.shields.io/badge/arXiv-2501.12751-b31b1b.svg" alt="arXiv" /></a> |
| **[Do large language models understand patents? Enhancing patent classification through AI-generated summaries](https://doi.org/10.1016/j.wpi.2025.102353)** — Yoshikawa et al., 2025, *World Patent Information*. AI-generated summaries boost LLM patent classification accuracy | <a href="https://doi.org/10.1016/j.wpi.2025.102353"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102353-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Patent Landscaping & Technology Intelligence</h4></summary>

*Mapping technology domains from patent corpora; competitive and R&D intelligence.*

| Paper | Link |
|---|---|
| **[Evaluating the value of LLMs in patent-based technology intelligence: Toward increasing efficiency and reducing expert dependency](https://doi.org/10.1016/j.techfore.2025.124375)** — Park et al., 2026, *Technological Forecasting and Social Change*. Evaluates LLMs replacing expert judgment in patent-based technology intelligence | <a href="https://doi.org/10.1016/j.techfore.2025.124375"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.techfore.2025.124375-blue.svg" alt="DOI" /></a> |
| **[Generative AI-based intelligent patent summarization for intellectual property knowledge communication and cooperation](https://doi.org/10.1016/j.wpi.2025.102410)** — Trappey et al., 2025, *World Patent Information*. GenAI patent summarization for IP knowledge communication and cooperation | <a href="https://doi.org/10.1016/j.wpi.2025.102410"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102410-blue.svg" alt="DOI" /></a> |
| **[Integrating Generative Artificial Intelligence techniques into technology function matrix analysis](https://doi.org/10.1016/j.wpi.2025.102352)** — Wang et al., 2025, *World Patent Information*. GenAI automates technology-function matrix construction for patent analysis | <a href="https://doi.org/10.1016/j.wpi.2025.102352"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102352-blue.svg" alt="DOI" /></a> |
| **[Automotive innovation landscaping using LLM](https://arxiv.org/abs/2409.14436)** — Gorain et al., 2024, *arXiv:2409.14436*. Prompt-based LLM patent landscaping for fuel-cell innovation mapping | <a href="https://arxiv.org/abs/2409.14436"><img src="https://img.shields.io/badge/arXiv-2409.14436-b31b1b.svg" alt="arXiv" /></a> |
| **[Towards Automated Patent Workflows: AI-Orchestrated Multi-Agent Framework for Intellectual Property Management and Analysis](https://arxiv.org/abs/2409.19006)** — Srinivas et al., 2024, *OWA Workshop @ NeurIPS 2024*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> PatExpert meta-agent orchestrates end-to-end patent analysis workflows | <a href="https://arxiv.org/abs/2409.19006"><img src="https://img.shields.io/badge/arXiv-2409.19006-b31b1b.svg" alt="arXiv" /></a> |
| **[EvoPat: A Multi-LLM-based Patents Summarization and Analysis Agent](https://arxiv.org/abs/2412.18100)** — Wang et al., 2024, *arXiv:2412.18100*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Multi-LLM agent summarizes patents and tracks innovation evolution | <a href="https://arxiv.org/abs/2412.18100"><img src="https://img.shields.io/badge/arXiv-2412.18100-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>Prior-Art Search & Patent Retrieval</h4></summary>

*Finding and matching prior art; patent-specific embeddings and retrieval.*

| Paper | Link |
|---|---|
| **[Enhancing the Patent Matching Capability of Large Language Models via the Memory Graph](https://arxiv.org/abs/2504.14845)** — Xiong et al., 2025, *SIGIR 2025*. MemGraph entity/ontology memory boosts LLM patent matching | <a href="https://arxiv.org/abs/2504.14845"><img src="https://img.shields.io/badge/arXiv-2504.14845-b31b1b.svg" alt="arXiv" /></a> |
| **[PaECTER: Patent-level Representation Learning using Citation-informed Transformers](https://arxiv.org/abs/2402.19411)** — Ghosh et al., 2024, *arXiv:2402.19411*. Citation-informed patent embeddings for prior-art similarity search | <a href="https://arxiv.org/abs/2402.19411"><img src="https://img.shields.io/badge/arXiv-2402.19411-b31b1b.svg" alt="arXiv" /></a> |
| **[Large Language Model Informed Patent Image Retrieval](https://arxiv.org/abs/2404.19360)** — Lo et al., 2024, *PatentSemTech @ SIGIR 2024*. LLM-generated captions improve patent drawing retrieval | <a href="https://arxiv.org/abs/2404.19360"><img src="https://img.shields.io/badge/arXiv-2404.19360-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>Patent Drafting & Claim Generation</h4></summary>

*Generating and refining patent text: claims, abstracts, full specifications.*

| Paper | Link |
|---|---|
| **[Can Large Language Models Generate High-quality Patent Claims?](https://arxiv.org/abs/2406.19465)** — Jiang et al., 2025, *Findings of NAACL 2025*. Evaluates claim generation quality from descriptions across LLMs | <a href="https://arxiv.org/abs/2406.19465"><img src="https://img.shields.io/badge/arXiv-2406.19465-b31b1b.svg" alt="arXiv" /></a> |
| **[PAP2PAT: Benchmarking Outline-Guided Long-Text Patent Generation with Patent-Paper Pairs](https://arxiv.org/abs/2410.07009)** — Knappich et al., 2025, *Findings of ACL 2025*. Paper-to-patent drafting via chunk-based outline-guided generation | <a href="https://arxiv.org/abs/2410.07009"><img src="https://img.shields.io/badge/arXiv-2410.07009-b31b1b.svg" alt="arXiv" /></a> |
| **[Large Language Model for Patent Concept Generation](https://arxiv.org/abs/2409.00092)** — Ren et al., 2025, *Advanced Engineering Informatics*. Knowledge fine-tuned PatentGPT for inventive patent concept generation | <a href="https://arxiv.org/abs/2409.00092"><img src="https://img.shields.io/badge/arXiv-2409.00092-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentWriter: A Benchmarking Study for Patent Drafting with LLMs](https://arxiv.org/abs/2507.22387)** — Shomee et al., 2025, *arXiv:2507.22387*. Benchmarks LLM patent abstract drafting from claims | <a href="https://arxiv.org/abs/2507.22387"><img src="https://img.shields.io/badge/arXiv-2507.22387-b31b1b.svg" alt="arXiv" /></a> |
| **[ToC: Tree-of-Claims Search with Multi-Agent Language Models](https://arxiv.org/abs/2511.16972)** — Yu et al., 2025, *AAAI 2026*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> MCTS editor/examiner agents optimize claims for novelty and scope | <a href="https://arxiv.org/abs/2511.16972"><img src="https://img.shields.io/badge/arXiv-2511.16972-b31b1b.svg" alt="arXiv" /></a> |
| **[ClaimBrush: A Novel Framework for Automated Patent Claim Refinement Based on Large Language Models](https://arxiv.org/abs/2410.05575)** — Kawano et al., 2024, *arXiv:2410.05575*. Rewrites claims via fine-tuned LLM with preference optimization | <a href="https://arxiv.org/abs/2410.05575"><img src="https://img.shields.io/badge/arXiv-2410.05575-b31b1b.svg" alt="arXiv" /></a> |
| **[AutoPatent: A Multi-Agent Framework for Automatic Patent Generation](https://arxiv.org/abs/2412.09796)** — Wang et al., 2024, *arXiv:2412.09796*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Planner/writer/examiner agents draft full patents from drafts | <a href="https://arxiv.org/abs/2412.09796"><img src="https://img.shields.io/badge/arXiv-2412.09796-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>Patent Quality, Novelty & Valuation</h4></summary>

*Assessing novelty, predicting examiner outcomes, automated quality assurance.*

| Paper | Link |
|---|---|
| **[Towards Automated Quality Assurance of Patent Specifications: A Multi-Dimensional LLM Framework](https://arxiv.org/abs/2510.25402)** — Chai et al., 2025, *arXiv:2510.25402*. Industry LLM framework auto-checking patent specification quality | <a href="https://arxiv.org/abs/2510.25402"><img src="https://img.shields.io/badge/arXiv-2510.25402-b31b1b.svg" alt="arXiv" /></a> |
| **[Can AI Examine Novelty of Patents?: Novelty Evaluation Based on the Correspondence between Patent Claim and Prior Art](https://arxiv.org/abs/2502.06316)** — Ikoma et al., 2025, *arXiv:2502.06316*. LLM novelty assessment aligning claims with prior art | <a href="https://arxiv.org/abs/2502.06316"><img src="https://img.shields.io/badge/arXiv-2502.06316-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentEdits: Framing Patent Novelty as Textual Entailment](https://arxiv.org/abs/2411.13477)** — Lee et al., 2024, *arXiv:2411.13477*. Predicts examiner-driven claim edits as an entailment task | <a href="https://arxiv.org/abs/2411.13477"><img src="https://img.shields.io/badge/arXiv-2411.13477-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>IP Benchmarks & Evaluation</h4></summary>

*Benchmarks and metrics for LLM performance on intellectual-property tasks.*

| Paper | Link |
|---|---|
| **[Towards Better Evaluation for Generated Patent Claims](https://arxiv.org/abs/2505.11095)** — Jiang et al., 2025, *arXiv:2505.11095*. Patent-CE benchmark and PatClaimEval for claim evaluation | <a href="https://arxiv.org/abs/2505.11095"><img src="https://img.shields.io/badge/arXiv-2505.11095-b31b1b.svg" alt="arXiv" /></a> |
| **[IPBench: Benchmarking the Knowledge of Large Language Models in Intellectual Property](https://arxiv.org/abs/2504.15524)** — Wang et al., 2025, *arXiv:2504.15524*. Comprehensive IP-knowledge benchmark; 10 tasks, 20 IP scenarios | <a href="https://arxiv.org/abs/2504.15524"><img src="https://img.shields.io/badge/arXiv-2504.15524-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentScore: Multi-dimensional Evaluation of LLM-Generated Patent Claims](https://arxiv.org/abs/2505.19345)** — Yoo et al., 2025, *arXiv:2505.19345*. Legal-structure-aware metric scoring LLM-generated claims | <a href="https://arxiv.org/abs/2505.19345"><img src="https://img.shields.io/badge/arXiv-2505.19345-b31b1b.svg" alt="arXiv" /></a> |
| **[MoZIP: A Multilingual Benchmark to Evaluate Large Language Models in Intellectual Property](https://arxiv.org/abs/2402.16389)** — Ni et al., 2024, *LREC-COLING 2024*. Multilingual IP quiz/QA/patent-matching benchmark plus MoZi model | <a href="https://arxiv.org/abs/2402.16389"><img src="https://img.shields.io/badge/arXiv-2402.16389-b31b1b.svg" alt="arXiv" /></a> |
| **[IPEval: A Bilingual Intellectual Property Agency Consultation Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2406.12386)** — Wang et al., 2024, *arXiv:2406.12386*. Bilingual patent-agent exam benchmark for LLM IP competence | <a href="https://arxiv.org/abs/2406.12386"><img src="https://img.shields.io/badge/arXiv-2406.12386-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentEval: Understanding Errors in Patent Generation](https://arxiv.org/abs/2406.06589)** — Zuo et al., 2024, *NAACL 2024*. Error typology and human-annotated benchmark for patent generation | <a href="https://arxiv.org/abs/2406.06589"><img src="https://img.shields.io/badge/arXiv-2406.06589-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>IP Domain Models & Surveys</h4></summary>

*Domain-adapted models and surveys of NLP/LLM methods in the patent domain.*

| Paper | Link |
|---|---|
| **[Natural Language Processing in the Patent Domain: A Survey](https://arxiv.org/abs/2403.04105)** — Jiang et al., 2025, *Artificial Intelligence Review*. Survey of LLM/NLP patent tasks, datasets, and methods | <a href="https://arxiv.org/abs/2403.04105"><img src="https://img.shields.io/badge/arXiv-2403.04105-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentGPT: A Large Language Model for Intellectual Property](https://arxiv.org/abs/2404.18255)** — Bai et al., 2024, *arXiv:2404.18255*. IP-domain-trained LLM; beats GPT-4 on China patent agent exam | <a href="https://arxiv.org/abs/2404.18255"><img src="https://img.shields.io/badge/arXiv-2404.18255-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h3>Technology Forecasting & Foresight</h3></summary>

*Emerging-technology detection, weak signals, opportunity discovery, trend prediction.*

| Paper | Link |
|---|---|
| **[Anticipating Innovation Using Large Language Models](https://arxiv.org/abs/2605.04875)** — Fenoaltea et al., 2026, *arXiv:2605.04875*. LLMs anticipate future innovation and technology emergence | <a href="https://arxiv.org/abs/2605.04875"><img src="https://img.shields.io/badge/arXiv-2605.04875-b31b1b.svg" alt="arXiv" /></a> |
| **[Tuning into whispered frequencies: Harnessing Large Language Models to detect Weak Signals in complex socio-technical systems](https://doi.org/10.1016/j.engappai.2026.114738)** — Lombardi et al., 2026, *Engineering Applications of Artificial Intelligence*. LLM pipeline detects foresight weak signals in socio-technical texts | <a href="https://doi.org/10.1016/j.engappai.2026.114738"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.engappai.2026.114738-blue.svg" alt="DOI" /></a> |
| **[AI-driven opportunity forecasting for technology startup identification: Integrating graph embedding, LLMs, and informetric analysis](https://doi.org/10.1016/j.techfore.2026.124649)** — Zhai et al., 2026, *Technological Forecasting and Social Change*. Graph embedding plus LLM informetrics forecast startup technology opportunities | <a href="https://doi.org/10.1016/j.techfore.2026.124649"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.techfore.2026.124649-blue.svg" alt="DOI" /></a> |
| **[ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment](https://arxiv.org/abs/2606.00644)** — Tian et al., 2026, *arXiv:2606.00644*. Benchmark tests agent forecasts of future research directions | <a href="https://arxiv.org/abs/2606.00644"><img src="https://img.shields.io/badge/arXiv-2606.00644-b31b1b.svg" alt="arXiv" /></a> |
| **[DiTTO-LLM: Framework for Discovering Topic-based Technology Opportunities via Large Language Model](https://arxiv.org/abs/2509.09724)** — Kim et al., 2025, *arXiv:2509.09724*. LLM tracks patent topic evolution to discover technology opportunities | <a href="https://arxiv.org/abs/2509.09724"><img src="https://img.shields.io/badge/arXiv-2509.09724-b31b1b.svg" alt="arXiv" /></a> |
| **[Predicting New Research Directions in Materials Science using Large Language Models and Concept Graphs](https://arxiv.org/abs/2506.16824)** — Marwitz et al., 2025, *arXiv:2506.16824*. LLM concept extraction plus graph model predicts unexplored combinations | <a href="https://arxiv.org/abs/2506.16824"><img src="https://img.shields.io/badge/arXiv-2506.16824-b31b1b.svg" alt="arXiv" /></a> |
| **[WISDOM: An AI-powered framework for emerging research detection using weak signal analysis and advanced topic modeling](https://arxiv.org/abs/2409.15340)** — Ebadi et al., 2024, *arXiv:2409.15340*. Weak-signal analysis plus topic modeling detects emerging research themes | <a href="https://arxiv.org/abs/2409.15340"><img src="https://img.shields.io/badge/arXiv-2409.15340-b31b1b.svg" alt="arXiv" /></a> |
| **[Forecasting high-impact research topics via machine learning on evolving knowledge graphs](https://arxiv.org/abs/2402.08640)** — Gu et al., 2024, *arXiv:2402.08640*. Evolving knowledge graph forecasts high-impact topics; LLM-benchmarked | <a href="https://arxiv.org/abs/2402.08640"><img src="https://img.shields.io/badge/arXiv-2402.08640-b31b1b.svg" alt="arXiv" /></a> |

</details>

### Scientometrics & Literature Analysis

<details open>
<summary><h4>Literature Screening & Systematic Reviews</h4></summary>

*LLMs as screeners in systematic reviews — structurally the same include/exclude task as valid-patent selection.*

| Paper | Link |
|---|---|
| **[Systematic Literature Reviews With Two Multi-Agentic Systems And Human-In-The-Loop](https://arxiv.org/abs/2607.21920)** — Ren et al., 2026, *arXiv:2607.21920*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Persona agents with cross-review reproduce a published meta-analysis | <a href="https://arxiv.org/abs/2607.21920"><img src="https://img.shields.io/badge/arXiv-2607.21920-b31b1b.svg" alt="arXiv" /></a> |
| **[LatteReview: A Multi-Agent Framework for Systematic Review Automation Using Large Language Models](https://arxiv.org/abs/2501.05468)** — Rouzrokh et al., 2025, *arXiv:2501.05468*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Modular reviewer agents automate screening and data extraction | <a href="https://arxiv.org/abs/2501.05468"><img src="https://img.shields.io/badge/arXiv-2501.05468-b31b1b.svg" alt="arXiv" /></a> |
| **[The Promise and Challenges of Using LLMs to Accelerate the Screening Process of Systematic Reviews](https://arxiv.org/abs/2404.15667)** — Huotala et al., 2024, *arXiv:2404.15667*. GPT-3.5/4 vs humans on title-abstract screening; prompt strategies compared | <a href="https://arxiv.org/abs/2404.15667"><img src="https://img.shields.io/badge/arXiv-2404.15667-b31b1b.svg" alt="arXiv" /></a> |
| **[Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](https://doi.org/10.1002/jrsm.1715)** — Khraisha et al., 2024, *Research Synthesis Methods*. GPT-4 screening and data extraction across languages and literature types | <a href="https://doi.org/10.1002/jrsm.1715"><img src="https://img.shields.io/badge/DOI-10.1002%2Fjrsm.1715-blue.svg" alt="DOI" /></a> |
| **[High-performance automated abstract screening with large language model ensembles](https://arxiv.org/abs/2411.02451)** — Sanghera et al., 2024, *arXiv:2411.02451*. LLM ensembles match/exceed human accuracy on Cochrane review screening | <a href="https://arxiv.org/abs/2411.02451"><img src="https://img.shields.io/badge/arXiv-2411.02451-b31b1b.svg" alt="arXiv" /></a> |
| **[Screening articles for systematic reviews with ChatGPT](https://doi.org/10.1016/j.cola.2024.101287)** — Syriani et al., 2024, *Journal of Computer Languages*. Large-scale evaluation of ChatGPT as a systematic review screener | <a href="https://doi.org/10.1016/j.cola.2024.101287"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.cola.2024.101287-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Novelty & Impact Prediction of Research</h4></summary>

*Scoring the novelty of papers and predicting their scientific impact.*

| Paper | Link |
|---|---|
| **[Are Large Language Models able to Predict Highly Cited Papers? Evidence from Statistical Publications](https://arxiv.org/abs/2601.13627)** — Ye et al., 2026, *arXiv:2601.13627*. Tests LLM citation-impact prediction on statistics publications | <a href="https://arxiv.org/abs/2601.13627"><img src="https://img.shields.io/badge/arXiv-2601.13627-b31b1b.svg" alt="arXiv" /></a> |
| **[Can small and reasoning large language models score journal articles for research quality and do averaging and few-shot help?](https://doi.org/10.1007/s11192-026-05585-2)** — Thelwall & Mohammadi, 2026, *Scientometrics*. Small/reasoning LLMs score research quality; averaging across queries helps | <a href="https://doi.org/10.1007/s11192-026-05585-2"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05585--2-blue.svg" alt="DOI" /></a> |
| **[Automated Novelty Evaluation of Academic Paper: A Collaborative Approach Integrating Human and Large Language Model Knowledge](https://doi.org/10.1002/asi.70005)** — Wu et al., 2025, *JASIST*. Human-LLM knowledge fusion predicts method novelty of papers | <a href="https://doi.org/10.1002/asi.70005"><img src="https://img.shields.io/badge/DOI-10.1002%2Fasi.70005-blue.svg" alt="DOI" /></a> |
| **[Evaluating the predictive capacity of ChatGPT for academic peer review outcomes across multiple platforms](https://doi.org/10.1007/s11192-025-05287-1)** — Thelwall & Yaghi, 2025, *Scientometrics*. ChatGPT predicts peer-review outcomes across three publishing platforms | <a href="https://doi.org/10.1007/s11192-025-05287-1"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--025--05287--1-blue.svg" alt="DOI" /></a> |
| **[Evaluating and Enhancing Large Language Models for Novelty Assessment in Scholarly Publications](https://arxiv.org/abs/2409.16605)** — Lin et al., 2024, *AISD @ ACL 2025*. SchNovel benchmark and RAG-Novelty for scholarly novelty assessment | <a href="https://arxiv.org/abs/2409.16605"><img src="https://img.shields.io/badge/arXiv-2409.16605-b31b1b.svg" alt="arXiv" /></a> |
| **[From Words to Worth: Newborn Article Impact Prediction with LLM](https://arxiv.org/abs/2408.03934)** — Zhao et al., 2024, *arXiv:2408.03934*. Fine-tuned LLM predicts article impact from title and abstract | <a href="https://arxiv.org/abs/2408.03934"><img src="https://img.shields.io/badge/arXiv-2408.03934-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>Scientometrics & Science of Science</h4></summary>

*Agentic and LLM-based tools for bibliometric and science-of-science analysis.*

| Paper | Link |
|---|---|
| **[Large language models for scientometric mapping of scientific controversy: A validated hybrid AI–Human framework](https://doi.org/10.1007/s11192-026-05681-3)** — Susnjak et al., 2026, *Scientometrics*. Validated hybrid LLM-human framework maps scientific controversy stances | <a href="https://doi.org/10.1007/s11192-026-05681-3"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05681--3-blue.svg" alt="DOI" /></a> |
| **[AI-Augmented Bibliometric Framework: A Paradigm Shift with Agentic AI for Dynamic, Snippet-Based Research Analysis](https://arxiv.org/abs/2511.21745)** — Bara et al., 2025, *arXiv:2511.21745*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agentic AI replaces static bibliometric keyword analysis | <a href="https://arxiv.org/abs/2511.21745"><img src="https://img.shields.io/badge/arXiv-2511.21745-b31b1b.svg" alt="arXiv" /></a> |
| **[The Empowerment of Science of Science by Large Language Models: New Tools and Methods](https://arxiv.org/abs/2511.15370)** — Liang et al., 2025, *arXiv:2511.15370*. Survey of LLM tools for scientometrics and research front detection | <a href="https://arxiv.org/abs/2511.15370"><img src="https://img.shields.io/badge/arXiv-2511.15370-b31b1b.svg" alt="arXiv" /></a> |
| **[SciSciGPT: Advancing Human-AI Collaboration in the Science of Science](https://arxiv.org/abs/2504.05559)** — Shao et al., 2025, *arXiv:2504.05559*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Specialist agents automate science-of-science analytics workflows | <a href="https://arxiv.org/abs/2504.05559"><img src="https://img.shields.io/badge/arXiv-2504.05559-b31b1b.svg" alt="arXiv" /></a> |
| **[AgentReview: Exploring Peer Review Dynamics with LLM Agents](https://arxiv.org/abs/2406.12708)** — Jin et al., 2024, *EMNLP 2024*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Reviewer/author/AC agents simulate peer-review dynamics | <a href="https://arxiv.org/abs/2406.12708"><img src="https://img.shields.io/badge/arXiv-2406.12708-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>Automated Survey Writing & Paper Search</h4></summary>

*Agents that search, synthesize, and write literature reviews.*

| Paper | Link |
|---|---|
| **[PaSa: An LLM Agent for Comprehensive Academic Paper Search](https://arxiv.org/abs/2501.10120)** — He et al., 2025, *arXiv:2501.10120*. RL-trained LLM agent for comprehensive scholarly paper retrieval | <a href="https://arxiv.org/abs/2501.10120"><img src="https://img.shields.io/badge/arXiv-2501.10120-b31b1b.svg" alt="arXiv" /></a> |
| **[Agentic AutoSurvey: Let LLMs Survey LLMs](https://arxiv.org/abs/2509.18661)** — Liu et al., 2025, *arXiv:2509.18661*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Four agents search, cluster, write, and evaluate literature surveys | <a href="https://arxiv.org/abs/2509.18661"><img src="https://img.shields.io/badge/arXiv-2509.18661-b31b1b.svg" alt="arXiv" /></a> |
| **[SurveyG: A Multi-Agent LLM Framework with Hierarchical Citation Graph for Automated Survey Generation](https://arxiv.org/abs/2510.07733)** — Nguyen et al., 2025, *arXiv:2510.07733*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Citation-graph-guided multi-agent survey generation | <a href="https://arxiv.org/abs/2510.07733"><img src="https://img.shields.io/badge/arXiv-2510.07733-b31b1b.svg" alt="arXiv" /></a> |
| **[Accelerating Scientific Research Through a Multi-LLM Framework](https://arxiv.org/abs/2502.07960)** — Ramirez-Medina et al., 2025, *arXiv:2502.07960*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Four-agent pipeline retrieves, filters, and synthesizes literature | <a href="https://arxiv.org/abs/2502.07960"><img src="https://img.shields.io/badge/arXiv-2502.07960-b31b1b.svg" alt="arXiv" /></a> |
| **[AutoSurvey: Large Language Models Can Automatically Write Surveys](https://arxiv.org/abs/2406.10252)** — Wang et al., 2024, *NeurIPS 2024*. End-to-end LLM pipeline for automatic literature survey writing | <a href="https://arxiv.org/abs/2406.10252"><img src="https://img.shields.io/badge/arXiv-2406.10252-b31b1b.svg" alt="arXiv" /></a> |

</details>

### R&D & Innovation Management

<details open>
<summary><h4>Idea Generation & Creativity in Innovation</h4></summary>

*LLMs vs humans/crowds in generating product and research ideas.*

| Paper | Link |
|---|---|
| **[Multi-agent AI systems outperform human teams in creativity](https://arxiv.org/abs/2605.17885)** — Hu et al., 2026, *arXiv:2605.17885*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> LLM agent teams beat human teams on judged creativity | <a href="https://arxiv.org/abs/2605.17885"><img src="https://img.shields.io/badge/arXiv-2605.17885-b31b1b.svg" alt="arXiv" /></a> |
| **[The Role of Artificial Intelligence in the Ideation Process](https://doi.org/10.1111/jpim.12791)** — Pescher et al., 2025, *Journal of Product Innovation Management*. AI's role across ideation stages in product innovation | <a href="https://doi.org/10.1111/jpim.12791"><img src="https://img.shields.io/badge/DOI-10.1111%2Fjpim.12791-blue.svg" alt="DOI" /></a> |
| **[Agent Ideate: Multi-Agent Framework for Product Business Idea Generation from Patents](https://arxiv.org/abs/2507.01717)** — Kanumolu et al., 2025, *AgentScen @ IJCAI 2025*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agents mine patents to generate product business ideas | <a href="https://arxiv.org/abs/2507.01717"><img src="https://img.shields.io/badge/arXiv-2507.01717-b31b1b.svg" alt="arXiv" /></a> |
| **[Exploring Design of Multi-Agent LLM Dialogues for Research Ideation](https://arxiv.org/abs/2507.08350)** — Ueda et al., 2025, *SIGDIAL 2025*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agent roles, cohort size, depth shape idea novelty | <a href="https://arxiv.org/abs/2507.08350"><img src="https://img.shields.io/badge/arXiv-2507.08350-b31b1b.svg" alt="arXiv" /></a> |
| **[Deep Ideation: Designing LLM Agents to Generate Novel Research Ideas on Scientific Concept Network](https://arxiv.org/abs/2511.02238)** — Zhao et al., 2025, *arXiv:2511.02238*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Explore-expand-evolve agents mine concept networks for ideas | <a href="https://arxiv.org/abs/2511.02238"><img src="https://img.shields.io/badge/arXiv-2511.02238-b31b1b.svg" alt="arXiv" /></a> |
| **[The Crowdless Future? Generative AI and Creative Problem-Solving](https://doi.org/10.1287/orsc.2023.18430)** — Boussioux et al., 2024, *Organization Science*. GPT-4 solutions vs crowdsourced solutions in an innovation challenge | <a href="https://doi.org/10.1287/orsc.2023.18430"><img src="https://img.shields.io/badge/DOI-10.1287%2Forsc.2023.18430-blue.svg" alt="DOI" /></a> |
| **[Generative AI enhances individual creativity but reduces the collective diversity of novel content](https://doi.org/10.1126/sciadv.adn5290)** — Doshi et al., 2024, *Science Advances*. LLM ideas boost individual creativity, shrink collective diversity | <a href="https://doi.org/10.1126/sciadv.adn5290"><img src="https://img.shields.io/badge/DOI-10.1126%2Fsciadv.adn5290-blue.svg" alt="DOI" /></a> |
| **[Comparing the Ideation Quality of Humans With Generative Artificial Intelligence](https://ieeexplore.ieee.org/document/10398283)** — Joosten et al., 2024, *IEEE Engineering Management Review*. Human vs GPT-4 ideation quality comparison for innovation management | <a href="https://ieeexplore.ieee.org/document/10398283"><img src="https://img.shields.io/badge/IEEE-Xplore-00629B.svg" alt="IEEE Xplore" /></a> |
| **[Prompting Diverse Ideas: Increasing AI Idea Variance](https://arxiv.org/abs/2402.01727)** — Meincke et al., 2024, *arXiv:2402.01727*. Prompt strategies to raise diversity of LLM-generated product ideas | <a href="https://arxiv.org/abs/2402.01727"><img src="https://img.shields.io/badge/arXiv-2402.01727-b31b1b.svg" alt="arXiv" /></a> |
| **[Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers](https://arxiv.org/abs/2409.04109)** — Si et al., 2024, *ICLR 2025*. LLM-generated research ideas judged more novel than experts' | <a href="https://arxiv.org/abs/2409.04109"><img src="https://img.shields.io/badge/arXiv-2409.04109-b31b1b.svg" alt="arXiv" /></a> |
| **[Ideas are Dimes a Dozen: Large Language Models for Idea Generation in Innovation](https://doi.org/10.2139/ssrn.4526071)** — Girotra et al., 2023, *SSRN Working Paper*. GPT-4 vs students: LLM ideas dominate top-quality product ideas | <a href="https://doi.org/10.2139/ssrn.4526071"><img src="https://img.shields.io/badge/DOI-10.2139%2Fssrn.4526071-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>New Product Development & R&D Management</h4></summary>

*LLM augmentation of NPD teams and product-concept evaluation.*

| Paper | Link |
|---|---|
| **[An Interactive Multi-Agent System for Evaluation of New Product Concepts](https://arxiv.org/abs/2603.05980)** — Xuan et al., 2026, *arXiv:2603.05980*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Specialized LLM agents deliberate to evaluate product concepts | <a href="https://arxiv.org/abs/2603.05980"><img src="https://img.shields.io/badge/arXiv-2603.05980-b31b1b.svg" alt="arXiv" /></a> |
| **[Augmenting human innovation teams with artificial intelligence: Exploring transformer-based language models](https://doi.org/10.1111/jpim.12656)** — Bouschery et al., 2023, *Journal of Product Innovation Management*. GPT-3 augmenting NPD teams; AI-augmented double diamond framework | <a href="https://doi.org/10.1111/jpim.12656"><img src="https://img.shields.io/badge/DOI-10.1111%2Fjpim.12656-blue.svg" alt="DOI" /></a> |

</details>

### Simulation, Strategy & Discovery

<details open>
<summary><h4>Market & Consumer Simulation</h4></summary>

*Generative agents simulating consumers, markets, and economies for management research.*

| Paper | Link |
|---|---|
| **[MALLES: A Multi-agent LLMs-based Economic Sandbox with Consumer Preference Alignment](https://arxiv.org/abs/2603.17694)** — Wu et al., 2026, *arXiv:2603.17694*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Preference-aligned agent sandbox simulates consumer purchasing | <a href="https://arxiv.org/abs/2603.17694"><img src="https://img.shields.io/badge/arXiv-2603.17694-b31b1b.svg" alt="arXiv" /></a> |
| **[EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities](https://arxiv.org/abs/2310.10436)** — Li et al., 2024, *ACL 2024*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> LLM agents reproduce macroeconomic dynamics | <a href="https://arxiv.org/abs/2310.10436"><img src="https://img.shields.io/badge/arXiv-2310.10436-b31b1b.svg" alt="arXiv" /></a> |
| **[LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals](https://arxiv.org/abs/2411.10109)** — Park et al., 2024, *arXiv:2411.10109*. Interview-grounded generative agents simulate 1,000 real individuals | <a href="https://arxiv.org/abs/2411.10109"><img src="https://img.shields.io/badge/arXiv-2411.10109-b31b1b.svg" alt="arXiv" /></a> |
| **[CompeteAI: Understanding the Competition Dynamics in Large Language Model-based Agents](https://arxiv.org/abs/2310.17512)** — Zhao et al., 2024, *ICML 2024*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Competing restaurant agents simulate market competition dynamics | <a href="https://arxiv.org/abs/2310.17512"><img src="https://img.shields.io/badge/arXiv-2310.17512-b31b1b.svg" alt="arXiv" /></a> |
| **[Using LLMs for Market Research](https://doi.org/10.2139/ssrn.4395751)** — Brand et al., 2023, *SSRN / HBS Working Paper*. GPT elicits realistic consumer preferences and willingness-to-pay | <a href="https://doi.org/10.2139/ssrn.4395751"><img src="https://img.shields.io/badge/DOI-10.2139%2Fssrn.4395751-blue.svg" alt="DOI" /></a> |
| **[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)** — Park et al., 2023, *UIST 2023*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> 25 LLM agents show emergent social behavior; landmark work | <a href="https://arxiv.org/abs/2304.03442"><img src="https://img.shields.io/badge/arXiv-2304.03442-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>Strategy & Decision-Making</h4></summary>

*LLMs in strategic decision-making and entrepreneurship.*

| Paper | Link |
|---|---|
| **[Artificial Intelligence and Strategic Decision-Making: Evidence from Entrepreneurs and Investors](https://doi.org/10.1287/stsc.2024.0190)** — Csaszar et al., 2024, *Strategy Science*. GPT-4 business strategies rival human founders per investor evaluations | <a href="https://doi.org/10.1287/stsc.2024.0190"><img src="https://img.shields.io/badge/DOI-10.1287%2Fstsc.2024.0190-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Scientific Discovery Agents</h4></summary>

*Autonomous research agents with direct relevance to R&D processes.*

| Paper | Link |
|---|---|
| **[Towards an AI co-scientist](https://arxiv.org/abs/2502.18864)** — Gottweis et al., 2025, *arXiv:2502.18864*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Gemini multi-agent system generates validated research hypotheses | <a href="https://arxiv.org/abs/2502.18864"><img src="https://img.shields.io/badge/arXiv-2502.18864-b31b1b.svg" alt="arXiv" /></a> |
| **[The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://doi.org/10.1038/s41586-025-09442-9)** — Swanson et al., 2025, *Nature*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> AI researcher agents run meetings, design validated nanobodies | <a href="https://doi.org/10.1038/s41586-025-09442-9"><img src="https://img.shields.io/badge/DOI-10.1038%2Fs41586--025--09442--9-blue.svg" alt="DOI" /></a> |
| **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)** — Schmidgall et al., 2025, *arXiv:2501.04227*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Autonomous agent pipeline runs literature-to-report research workflows | <a href="https://arxiv.org/abs/2501.04227"><img src="https://img.shields.io/badge/arXiv-2501.04227-b31b1b.svg" alt="arXiv" /></a> |
| **[AgentRxiv: Towards Collaborative Autonomous Research](https://arxiv.org/abs/2503.18102)** — Schmidgall & Moor, 2025, *arXiv:2503.18102*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agent labs share preprints to accelerate collaborative research | <a href="https://arxiv.org/abs/2503.18102"><img src="https://img.shields.io/badge/arXiv-2503.18102-b31b1b.svg" alt="arXiv" /></a> |
| **[Augmenting large language models with chemistry tools](https://doi.org/10.1038/s42256-024-00832-8)** — Bran et al., 2024, *Nature Machine Intelligence*. ChemCrow: LLM agent with 18 tools for synthesis and discovery | <a href="https://doi.org/10.1038/s42256-024-00832-8"><img src="https://img.shields.io/badge/DOI-10.1038%2Fs42256--024--00832--8-blue.svg" alt="DOI" /></a> |
| **[The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292)** — Lu et al., 2024, *arXiv:2408.06292*. End-to-end autonomous research agent writes papers for ~$15 | <a href="https://arxiv.org/abs/2408.06292"><img src="https://img.shields.io/badge/arXiv-2408.06292-b31b1b.svg" alt="arXiv" /></a> |
| **[Autonomous chemical research with large language models](https://doi.org/10.1038/s41586-023-06792-0)** — Boiko et al., 2023, *Nature*. Coscientist agent autonomously plans and executes chemistry experiments | <a href="https://doi.org/10.1038/s41586-023-06792-0"><img src="https://img.shields.io/badge/DOI-10.1038%2Fs41586--023--06792--0-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>Adjacent: General MAS Frameworks & Finance</h3></summary>

*Landmark frameworks and finance MAS often cited by TIM applications.*

| Paper | Link |
|---|---|
| **[MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352)** — Hong et al., 2024, *ICLR 2024*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> SOP-encoded agent roles simulate a software company workflow | <a href="https://arxiv.org/abs/2308.00352"><img src="https://img.shields.io/badge/arXiv-2308.00352-b31b1b.svg" alt="arXiv" /></a> |
| **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)** — Xiao et al., 2024, *arXiv:2412.20138*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Analyst/trader/risk agents emulate a trading firm; landmark | <a href="https://arxiv.org/abs/2412.20138"><img src="https://img.shields.io/badge/arXiv-2412.20138-b31b1b.svg" alt="arXiv" /></a> |
| **[TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://arxiv.org/abs/2412.14161)** — Xu et al., 2024, *arXiv:2412.14161*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Benchmark: agents perform professional tasks in a simulated company | <a href="https://arxiv.org/abs/2412.14161"><img src="https://img.shields.io/badge/arXiv-2412.14161-b31b1b.svg" alt="arXiv" /></a> |
| **[FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743)** — Yu et al., 2023, *arXiv:2311.13743*. LLM trading agent with layered memory outperforms benchmarks | <a href="https://arxiv.org/abs/2311.13743"><img src="https://img.shields.io/badge/arXiv-2311.13743-b31b1b.svg" alt="arXiv" /></a> |

</details>

<!-- AUTOGEN:PAPERS END -->

## Related lists

Architecture- and methods-centric collections, complementary to this one:

* [awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) — agent engineering, memory, evaluation, workflows
* [Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) — methodology, applications, challenges survey companion
* [awesome-agents4science](https://github.com/OSU-NLP-Group/awesome-agents4science) — LLMs/agents for scientific R&D
* [Awesome-LLM-Agents-Scientific-Discovery](https://github.com/zhoujieli/Awesome-LLM-Agents-Scientific-Discovery) — biomedical research agents
* [LLM_MultiAgents_Survey_Papers](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers) — MAS survey papers

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Edit `data/papers.tsv`, run `python scripts/build_readme.py`, and open a PR.

## License

[CC0 1.0](LICENSE) — public domain dedication.
