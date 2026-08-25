# Awesome LLM Application Papers for Technology & Innovation Management

<div align="center">

**Hand-picked research papers applying LLMs, LLM agents, and multi-agent systems (MAS) to technology & innovation management (TIM).**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-161-blue)
![Adjacent](https://img.shields.io/badge/adjacent-56-lightgrey)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

patent analytics · technology forecasting · scientometrics · R&D & innovation management · market simulation

</div>

### Papers over time

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/trend-dark.svg">
  <img alt="Stacked bar chart of journal and preprint papers per quarter" src="assets/trend-light.svg" width="100%">
</picture>

*Core list only. Quarterly counts, dated by first public appearance (arXiv posting or journal online date). Blue = journals & conferences, red = preprints (arXiv/SSRN).*

### Which areas peak when

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/fields-dark.svg">
  <img alt="Heatmap of papers per research area per quarter" src="assets/fields-light.svg" width="100%">
</picture>

*Core papers per research area per quarter — the hot cells show each cluster's peak period.*

<!-- AUTOGEN:VENUES BEGIN (generated from data/papers.tsv) -->

### Where these papers appear

| Venue | Papers |
|---|---:|
| arXiv (preprints) | 27 |
| Scientometrics | 23 |
| World Patent Information | 21 |
| J. Engineering Design | 13 |
| Advanced Engineering Informatics | 9 |
| Information Processing & Management | 9 |
| J. Mechanical Design | 6 |
| Design Science | 4 |
| Quantitative Science Studies | 4 |
| ACL | 3 |
| Technological Forecasting and Social Change | 3 |
| Technovation | 3 |
| CIRP Annals | 2 |
| Creativity and Innovation Management | 2 |
| Engineering Applications of Artificial Intelligence | 2 |
| Expert Systems with Applications | 2 |
| ICML | 2 |
| Information Systems Research | 2 |
| JASIST | 2 |
| Journal of Product Innovation Management | 2 |
| Organization Science | 2 |
| SIGIR | 2 |
| SSRN (working papers) | 2 |
| Others (1 each): AAAI 2026, AgentScen @ IJCAI 2025, EMNLP 2024, ICLR, IEEE Engineering Management Review, J. Data and Information Science, J. Informetrics, Management Science, NAACL, NeurIPS, Research Evaluation, Research Policy, SIGDIAL 2025, Strategy Science | 14 |

<!-- AUTOGEN:VENUES END -->

## Why this list exists

Most agent paper lists collect research *on* agent architectures (memory, planning, coordination). This list collects the complement: research that *uses* agents on real TIM tasks — the papers that end up scattered across *TFSC*, *Scientometrics*, *World Patent Information*, management journals, and application tracks, and therefore rarely appear in ML-centric lists.

**Inclusion criteria — two tiers.** The **core list** collects peer-reviewed papers or public preprints (arXiv/SSRN) where an LLM or LLM-agent system is applied to and evaluated on a TIM task *directly* — patents and IP, technology foresight, innovation and R&D management, and market simulation for management research. A separate **[Adjacent & enabling methods](#adjacent--enabling-methods)** tier collects benchmarks, domain models, surveys, generic-domain analogues (e.g. medical systematic-review screening), and landmark agent frameworks that TIM applications build on; these are excluded from the headline count and charts. Tools without papers, blog posts, and pure architecture papers are out of scope entirely.

Maintained with a human-in-the-loop pipeline: a monthly GitHub Action sweeps OpenAlex and Semantic Scholar for candidates and opens a review issue; humans curate (see [CONTRIBUTING.md](CONTRIBUTING.md)). The list itself lives in `data/papers.tsv`; the contents and papers sections below are generated from it.

<!-- AUTOGEN:PAPERS BEGIN (edit data/papers.tsv, not this section) -->

## Contents

- **Patent & IP Analytics**
  - [Patent Classification & Screening](#patent-classification--screening) (5)
  - [Patent Landscaping & Technology Intelligence](#patent-landscaping--technology-intelligence) (17)
  - [Prior-Art Search & Patent Retrieval](#prior-art-search--patent-retrieval) (5)
  - [Patent Drafting & Claim Generation](#patent-drafting--claim-generation) (11)
  - [Patent Quality, Novelty & Valuation](#patent-quality-novelty--valuation) (9)
  - [Trademark & Non-Patent IP](#trademark--non-patent-ip) (2)
- [Technology Forecasting & Foresight](#technology-forecasting--foresight) (10)
- **Scientometrics & Literature Analysis**
  - [Literature Screening & Systematic Reviews](#literature-screening--systematic-reviews) (2)
  - [Novelty & Impact Prediction of Research](#novelty--impact-prediction-of-research) (8)
  - [Scientometrics & Science of Science](#scientometrics--science-of-science) (18)
  - [LLM-Assisted Peer Review](#llm-assisted-peer-review) (8)
  - [Research & R&D Evaluation](#research--rd-evaluation) (5)
- **R&D & Innovation Management**
  - [Idea Generation & Creativity in Innovation](#idea-generation--creativity-in-innovation) (18)
  - [New Product Development & R&D Management](#new-product-development--rd-management) (7)
  - [Engineering & Conceptual Design](#engineering--conceptual-design) (29)
- **Simulation, Strategy & Discovery**
  - [Market & Consumer Simulation](#market--consumer-simulation) (6)
  - [Strategy & Decision-Making](#strategy--decision-making) (1)
- [Adjacent & enabling methods](#adjacent--enabling-methods) (56)
- [Related lists](#related-lists)

## Papers

161 core papers. `MAS` badge marks explicitly multi-agent systems. Newest first within each section.

### Patent & IP Analytics

<details open>
<summary><h4>Patent Classification & Screening</h4></summary>

*Assigning patents to taxonomies (CPC/IPC or custom schemes) and screening for relevance.*

| Paper | Link |
|---|---|
| **[Large Language Models for Patent Classification: Strengths, Trade-offs, and the Long Tail Effect](https://arxiv.org/abs/2601.23200)** — Emer et al., 2026, *arXiv:2601.23200*. Compares LLMs vs BERT on CPC; LLMs win on rare subclasses | <a href="https://arxiv.org/abs/2601.23200"><img src="https://img.shields.io/badge/arXiv-2601.23200-b31b1b.svg" alt="arXiv" /></a> |
| **[Patent Figure Classification using Large Vision-language Models](https://arxiv.org/abs/2501.12751)** — Awale et al., 2025, *arXiv:2501.12751*. LVLMs classify patent figures; PatFigVQA/PatFigCLS datasets | <a href="https://arxiv.org/abs/2501.12751"><img src="https://img.shields.io/badge/arXiv-2501.12751-b31b1b.svg" alt="arXiv" /></a> |
| **[Do large language models understand patents? Enhancing patent classification through AI-generated summaries](https://doi.org/10.1016/j.wpi.2025.102353)** — Yoshikawa et al., 2025, *World Patent Information*. AI-generated summaries boost LLM patent classification accuracy | <a href="https://doi.org/10.1016/j.wpi.2025.102353"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102353-blue.svg" alt="DOI" /></a> |
| **[Improved multi-label hierarchical patent classification using LLMs](https://doi.org/10.1016/j.wpi.2025.102356)** — Rafieian & Vázquez, 2025, *World Patent Information*. LLMs improve hierarchical multi-label patent classification | <a href="https://doi.org/10.1016/j.wpi.2025.102356"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102356-blue.svg" alt="DOI" /></a> |
| **[Scalable multi-label patent classification via iterative large language model-assisted active learning](https://doi.org/10.1016/j.wpi.2025.102380)** — Xiong et al., 2025, *World Patent Information*. Iterative LLM-assisted active learning scales multi-label patent classification | <a href="https://doi.org/10.1016/j.wpi.2025.102380"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102380-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Patent Landscaping & Technology Intelligence</h4></summary>

*Mapping technology domains from patent corpora; competitive and R&D intelligence.*

| Paper | Link |
|---|---|
| **[Evaluating the value of LLMs in patent-based technology intelligence: Toward increasing efficiency and reducing expert dependency](https://doi.org/10.1016/j.techfore.2025.124375)** — Park et al., 2026, *Technological Forecasting and Social Change*. Evaluates LLMs replacing expert judgment in patent-based technology intelligence | <a href="https://doi.org/10.1016/j.techfore.2025.124375"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.techfore.2025.124375-blue.svg" alt="DOI" /></a> |
| **[Patent technology knowledge recommendation by integrating large language models and knowledge graphs](https://doi.org/10.1016/j.engappai.2026.114176)** — Yang et al., 2026, *Engineering Applications of Artificial Intelligence*. Couples LLMs with patent knowledge graphs for technology recommendation | <a href="https://doi.org/10.1016/j.engappai.2026.114176"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.engappai.2026.114176-blue.svg" alt="DOI" /></a> |
| **[A multimodal framework for patent survival and commercialization prediction](https://doi.org/10.1016/j.ipm.2026.104626)** — Sun et al., 2026, *Information Processing & Management*. Multimodal model predicts patent survival and commercialization outcomes | <a href="https://doi.org/10.1016/j.ipm.2026.104626"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2026.104626-blue.svg" alt="DOI" /></a> |
| **[Pioneering exploration in patent landscape studies: leveraging large language models and in-context learning for deeper insights](https://doi.org/10.1007/s11192-026-05537-w)** — Yang et al., 2026, *Scientometrics*. In-context learning deepens LLM patent landscape analysis | <a href="https://doi.org/10.1007/s11192-026-05537-w"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05537--w-blue.svg" alt="DOI" /></a> |
| **[RoCoMAP: A Role-Based Collaborative Multi-Agent Framework for Patent Supply–Demand Matching](https://doi.org/10.1007/s11192-026-05777-w)** — He et al., 2026, *Scientometrics*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Role-based multi-agent framework matches patent supply with demand | <a href="https://doi.org/10.1007/s11192-026-05777-w"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05777--w-blue.svg" alt="DOI" /></a> |
| **[Towards efficient patent analysis: A large language model and BERT-refined methodology for keyphrase extraction](https://doi.org/10.1016/j.wpi.2026.102435)** — Mu et al., 2026, *World Patent Information*. LLM and BERT-refined keyphrase extraction for efficient patent analysis | <a href="https://doi.org/10.1016/j.wpi.2026.102435"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102435-blue.svg" alt="DOI" /></a> |
| **[Global innovation landscape of Ganoderma mushrooms: Integrating patent mapping, technological life cycle modeling, and an LLM keyword extraction](https://doi.org/10.1016/j.wpi.2026.102458)** — Foffano et al., 2026, *World Patent Information*. Patent mapping, life-cycle modelling, LLM keywords chart Ganoderma innovation | <a href="https://doi.org/10.1016/j.wpi.2026.102458"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102458-blue.svg" alt="DOI" /></a> |
| **[Patent intelligence in the age of AI: Unlocking strategic insights through granular classification](https://doi.org/10.1016/j.wpi.2026.102454)** — Giuntelli et al., 2026, *World Patent Information*. AI granular classification produces analyst-facing patent matrices and trajectories | <a href="https://doi.org/10.1016/j.wpi.2026.102454"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102454-blue.svg" alt="DOI" /></a> |
| **[Agentic cognitive orchestration for cross-lingual patent intelligence: A modular workflow automation approach](https://doi.org/10.1016/j.wpi.2026.102483)** — Wang & Ke, 2026, *World Patent Information*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Modular agent workflow automates cross-lingual patent intelligence | <a href="https://doi.org/10.1016/j.wpi.2026.102483"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102483-blue.svg" alt="DOI" /></a> |
| **[Generative AI-based intelligent patent summarization for intellectual property knowledge communication and cooperation](https://doi.org/10.1016/j.wpi.2025.102410)** — Trappey et al., 2025, *World Patent Information*. GenAI patent summarization for IP knowledge communication and cooperation | <a href="https://doi.org/10.1016/j.wpi.2025.102410"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102410-blue.svg" alt="DOI" /></a> |
| **[Integrating Generative Artificial Intelligence techniques into technology function matrix analysis](https://doi.org/10.1016/j.wpi.2025.102352)** — Wang et al., 2025, *World Patent Information*. GenAI automates technology-function matrix construction for patent analysis | <a href="https://doi.org/10.1016/j.wpi.2025.102352"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102352-blue.svg" alt="DOI" /></a> |
| **[Generative AI approach for inventive process visualisation – enhancing human-AI hybrid understanding and comparing of patents](https://doi.org/10.1080/09544828.2025.2518657)** — Trappey et al., 2025, *J. Engineering Design*. Extracts and visualises patent inventive processes for hybrid comparison | <a href="https://doi.org/10.1080/09544828.2025.2518657"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2025.2518657-blue.svg" alt="DOI" /></a> |
| **[Meeting companies’ innovative requirements on online technology trading platforms: A novel large language model-based framework](https://doi.org/10.1016/j.ipm.2025.104392)** — Xu et al., 2025, *Information Processing & Management*. LLM framework matches company technology needs on trading platforms | <a href="https://doi.org/10.1016/j.ipm.2025.104392"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2025.104392-blue.svg" alt="DOI" /></a> |
| **[Automotive innovation landscaping using LLM](https://arxiv.org/abs/2409.14436)** — Gorain et al., 2024, *arXiv:2409.14436*. Prompt-based LLM patent landscaping for fuel-cell innovation mapping | <a href="https://arxiv.org/abs/2409.14436"><img src="https://img.shields.io/badge/arXiv-2409.14436-b31b1b.svg" alt="arXiv" /></a> |
| **[Towards Automated Patent Workflows: AI-Orchestrated Multi-Agent Framework for Intellectual Property Management and Analysis](https://arxiv.org/abs/2409.19006)** — Srinivas et al., 2024, *OWA Workshop @ NeurIPS 2024*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> PatExpert meta-agent orchestrates end-to-end patent analysis workflows | <a href="https://arxiv.org/abs/2409.19006"><img src="https://img.shields.io/badge/arXiv-2409.19006-b31b1b.svg" alt="arXiv" /></a> |
| **[EvoPat: A Multi-LLM-based Patents Summarization and Analysis Agent](https://arxiv.org/abs/2412.18100)** — Wang et al., 2024, *arXiv:2412.18100*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Multi-LLM agent summarizes patents and tracks innovation evolution | <a href="https://arxiv.org/abs/2412.18100"><img src="https://img.shields.io/badge/arXiv-2412.18100-b31b1b.svg" alt="arXiv" /></a> |
| **[Patent litigation mining using a large language model—Taking unmanned aerial vehicle development as the case domain](https://doi.org/10.1016/j.wpi.2024.102332)** — Trappey et al., 2024, *World Patent Information*. LLM mines patent litigation records in UAV technology domain | <a href="https://doi.org/10.1016/j.wpi.2024.102332"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2024.102332-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Prior-Art Search & Patent Retrieval</h4></summary>

*Finding and matching prior art; patent-specific embeddings and retrieval.*

| Paper | Link |
|---|---|
| **[LLM-powered Real-time Patent Citation Recommendation for Financial Technologies](https://arxiv.org/abs/2601.16775)** — Deng et al., 2026, *arXiv:2601.16775*. Real-time LLM-embedding citation recommendation over growing patent corpus | <a href="https://arxiv.org/abs/2601.16775"><img src="https://img.shields.io/badge/arXiv-2601.16775-b31b1b.svg" alt="arXiv" /></a> |
| **[Enhancing the Patent Matching Capability of Large Language Models via the Memory Graph](https://arxiv.org/abs/2504.14845)** — Xiong et al., 2025, *SIGIR 2025*. MemGraph entity/ontology memory boosts LLM patent matching | <a href="https://arxiv.org/abs/2504.14845"><img src="https://img.shields.io/badge/arXiv-2504.14845-b31b1b.svg" alt="arXiv" /></a> |
| **[Advancing patent law with generative AI: Human-in-the-loop systems for AI-assisted drafting, prior art search, and multimodal IP protection](https://doi.org/10.1016/j.wpi.2025.102341)** — Bui, 2025, *World Patent Information*. Human-in-the-loop generative AI for drafting, prior-art search, multimodal IP | <a href="https://doi.org/10.1016/j.wpi.2025.102341"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102341-blue.svg" alt="DOI" /></a> |
| **[Designing tailored patent search approaches – A case study on nursing care technology](https://doi.org/10.1016/j.wpi.2025.102420)** — Waterstraat & Walter, 2025, *World Patent Information*. Design-theory multi-perspective keyword search for fuzzy technology fields | <a href="https://doi.org/10.1016/j.wpi.2025.102420"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102420-blue.svg" alt="DOI" /></a> |
| **[Large Language Model Informed Patent Image Retrieval](https://arxiv.org/abs/2404.19360)** — Lo et al., 2024, *PatentSemTech @ SIGIR 2024*. LLM-generated captions improve patent drawing retrieval | <a href="https://arxiv.org/abs/2404.19360"><img src="https://img.shields.io/badge/arXiv-2404.19360-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>Patent Drafting & Claim Generation</h4></summary>

*Generating and refining patent text: claims, abstracts, full specifications.*

| Paper | Link |
|---|---|
| **[Experimenting with a prompt-based AI examiner for inventive step determination: A rule-based framework toward harmonized patent examination](https://doi.org/10.1016/j.wpi.2026.102463)** — Yamazaki, 2026, *World Patent Information*. Prompt-based AI examiner applies rules to inventive-step determination | <a href="https://doi.org/10.1016/j.wpi.2026.102463"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102463-blue.svg" alt="DOI" /></a> |
| **[Can Large Language Models Generate High-quality Patent Claims?](https://arxiv.org/abs/2406.19465)** — Jiang et al., 2025, *Findings of NAACL 2025*. Evaluates claim generation quality from descriptions across LLMs | <a href="https://arxiv.org/abs/2406.19465"><img src="https://img.shields.io/badge/arXiv-2406.19465-b31b1b.svg" alt="arXiv" /></a> |
| **[PAP2PAT: Benchmarking Outline-Guided Long-Text Patent Generation with Patent-Paper Pairs](https://arxiv.org/abs/2410.07009)** — Knappich et al., 2025, *Findings of ACL 2025*. Paper-to-patent drafting via chunk-based outline-guided generation | <a href="https://arxiv.org/abs/2410.07009"><img src="https://img.shields.io/badge/arXiv-2410.07009-b31b1b.svg" alt="arXiv" /></a> |
| **[Large Language Model for Patent Concept Generation](https://arxiv.org/abs/2409.00092)** — Ren et al., 2025, *Advanced Engineering Informatics*. Knowledge fine-tuned PatentGPT for inventive patent concept generation | <a href="https://arxiv.org/abs/2409.00092"><img src="https://img.shields.io/badge/arXiv-2409.00092-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentWriter: A Benchmarking Study for Patent Drafting with LLMs](https://arxiv.org/abs/2507.22387)** — Shomee et al., 2025, *arXiv:2507.22387*. Benchmarks LLM patent abstract drafting from claims | <a href="https://arxiv.org/abs/2507.22387"><img src="https://img.shields.io/badge/arXiv-2507.22387-b31b1b.svg" alt="arXiv" /></a> |
| **[ToC: Tree-of-Claims Search with Multi-Agent Language Models](https://arxiv.org/abs/2511.16972)** — Yu et al., 2025, *AAAI 2026*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> MCTS editor/examiner agents optimize claims for novelty and scope | <a href="https://arxiv.org/abs/2511.16972"><img src="https://img.shields.io/badge/arXiv-2511.16972-b31b1b.svg" alt="arXiv" /></a> |
| **[Evaluating application of large language models to biomedical patent claim generation](https://doi.org/10.1016/j.wpi.2025.102339)** — Chen & Pan, 2025, *World Patent Information*. Evaluates LLM generation of biomedical patent claims | <a href="https://doi.org/10.1016/j.wpi.2025.102339"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102339-blue.svg" alt="DOI" /></a> |
| **[Generating patent claims with semantic novelty](https://doi.org/10.1016/j.wpi.2025.102404)** — Lee, 2025, *World Patent Information*. Generates patent claims optimised for semantic novelty | <a href="https://doi.org/10.1016/j.wpi.2025.102404"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102404-blue.svg" alt="DOI" /></a> |
| **[ClaimBrush: A Novel Framework for Automated Patent Claim Refinement Based on Large Language Models](https://arxiv.org/abs/2410.05575)** — Kawano et al., 2024, *arXiv:2410.05575*. Rewrites claims via fine-tuned LLM with preference optimization | <a href="https://arxiv.org/abs/2410.05575"><img src="https://img.shields.io/badge/arXiv-2410.05575-b31b1b.svg" alt="arXiv" /></a> |
| **[AutoPatent: A Multi-Agent Framework for Automatic Patent Generation](https://arxiv.org/abs/2412.09796)** — Wang et al., 2024, *arXiv:2412.09796*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Planner/writer/examiner agents draft full patents from drafts | <a href="https://arxiv.org/abs/2412.09796"><img src="https://img.shields.io/badge/arXiv-2412.09796-b31b1b.svg" alt="arXiv" /></a> |
| **[Patent claim generation by fine-tuning OpenAI GPT-2](https://doi.org/10.1016/j.wpi.2020.101983)** — Lee & Hsiang, 2020, *World Patent Information*. Pioneer work: GPT-2 fine-tuned to draft patent claims | <a href="https://doi.org/10.1016/j.wpi.2020.101983"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2020.101983-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Patent Quality, Novelty & Valuation</h4></summary>

*Assessing novelty, predicting examiner outcomes, automated quality assurance.*

| Paper | Link |
|---|---|
| **[ERA: Aligning semantic models with revealed economic preference for real-time and explainable patent valuation](https://doi.org/10.1016/j.ipm.2026.104898)** — Yoo et al., 2026, *Information Processing & Management*. Aligns patent semantics with revealed economic preference for explainable valuation | <a href="https://doi.org/10.1016/j.ipm.2026.104898"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2026.104898-blue.svg" alt="DOI" /></a> |
| **[Perception to Cognition: Patent Value Assessment Based on Large Language Model Semantic Enhancement and Ensemble Learning](https://doi.org/10.1515/jdis-2025-0455)** — Xi et al., 2026, *J. Data and Information Science*. Virtual-assessor LLM semantics plus ensemble learning identify high-value patents | <a href="https://doi.org/10.1515/jdis-2025-0455"><img src="https://img.shields.io/badge/DOI-10.1515%2Fjdis--2025--0455-blue.svg" alt="DOI" /></a> |
| **[Structured LLM-based patent comparison across three evaluation dimensions](https://doi.org/10.1016/j.wpi.2026.102430)** — Choi & Park, 2026, *World Patent Information*. Structured LLM comparison of patents across three evaluation dimensions | <a href="https://doi.org/10.1016/j.wpi.2026.102430"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102430-blue.svg" alt="DOI" /></a> |
| **[Towards Automated Quality Assurance of Patent Specifications: A Multi-Dimensional LLM Framework](https://arxiv.org/abs/2510.25402)** — Chai et al., 2025, *arXiv:2510.25402*. Industry LLM framework auto-checking patent specification quality | <a href="https://arxiv.org/abs/2510.25402"><img src="https://img.shields.io/badge/arXiv-2510.25402-b31b1b.svg" alt="arXiv" /></a> |
| **[Can AI Examine Novelty of Patents?: Novelty Evaluation Based on the Correspondence between Patent Claim and Prior Art](https://arxiv.org/abs/2502.06316)** — Ikoma et al., 2025, *arXiv:2502.06316*. LLM novelty assessment aligning claims with prior art | <a href="https://arxiv.org/abs/2502.06316"><img src="https://img.shields.io/badge/arXiv-2502.06316-b31b1b.svg" alt="arXiv" /></a> |
| **[Disentangling patent quality: using a large language model for a systematic literature review](https://doi.org/10.1007/s11192-024-05206-w)** — Schmitt, 2025, *Scientometrics*. LLM-run systematic review builds multidimensional patent quality framework | <a href="https://doi.org/10.1007/s11192-024-05206-w"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--024--05206--w-blue.svg" alt="DOI" /></a> |
| **[Assessing the standard-essentiality of 5G technology patents by means of generative artificial intelligence](https://doi.org/10.1016/j.wpi.2025.102363)** — Herzberg, 2025, *World Patent Information*. Generative AI screens declared 5G patents for standard-essentiality | <a href="https://doi.org/10.1016/j.wpi.2025.102363"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2025.102363-blue.svg" alt="DOI" /></a> |
| **[PatentEdits: Framing Patent Novelty as Textual Entailment](https://arxiv.org/abs/2411.13477)** — Lee et al., 2024, *arXiv:2411.13477*. Predicts examiner-driven claim edits as an entailment task | <a href="https://arxiv.org/abs/2411.13477"><img src="https://img.shields.io/badge/arXiv-2411.13477-b31b1b.svg" alt="arXiv" /></a> |
| **[A novel approach to measuring the scope of patent claims based on probabilities obtained from (large) language models](https://doi.org/10.1016/j.wpi.2024.102321)** — Ragot, 2024, *World Patent Information*. Measures patent claim scope from language-model token probabilities | <a href="https://doi.org/10.1016/j.wpi.2024.102321"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2024.102321-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Trademark & Non-Patent IP</h4></summary>

*IP tasks beyond patents: trademark similarity, opposition, and clearance.*

| Paper | Link |
|---|---|
| **[A large language model-based method for trademark similarity analysis in the Brazilian context](https://doi.org/10.1016/j.wpi.2026.102436)** — Reis et al., 2026, *World Patent Information*. LLM-based trademark similarity assessment for Brazilian filings | <a href="https://doi.org/10.1016/j.wpi.2026.102436"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102436-blue.svg" alt="DOI" /></a> |
| **[Automatic similarity detection for trademark](https://doi.org/10.1016/j.wpi.2026.102452)** — Le Nir et al., 2026, *World Patent Information*. Predicts EUIPO goods/services conflict decisions from 107,570 opposition records | <a href="https://doi.org/10.1016/j.wpi.2026.102452"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102452-blue.svg" alt="DOI" /></a> |

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
| **[MPCoT: explainable identification in technology opportunity analysis via metapaths and multi-perspective chain-of-thought reasoning](https://doi.org/10.1016/j.eswa.2026.133318)** — Li et al., 2026, *Expert Systems with Applications*. Metapaths and multi-perspective chain-of-thought explain technology opportunities | <a href="https://doi.org/10.1016/j.eswa.2026.133318"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.eswa.2026.133318-blue.svg" alt="DOI" /></a> |
| **[Signals of innovation online: Identifying innovative firms by combining website mining and evidence producing LLMs](https://doi.org/10.1016/j.techfore.2026.124695)** — Grybauskas et al., 2026, *Technological Forecasting and Social Change*. Website mining plus evidence-producing LLMs identify innovative firms | <a href="https://doi.org/10.1016/j.techfore.2026.124695"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.techfore.2026.124695-blue.svg" alt="DOI" /></a> |
| **[Prescriptive technology intelligence for technology opportunity discovery: An LLM-based automated framework for narrating promising technology concepts](https://doi.org/10.1016/j.technovation.2026.103584)** — Yoo et al., 2026, *Technovation*. LLM framework narrates promising technology concepts for opportunity discovery | <a href="https://doi.org/10.1016/j.technovation.2026.103584"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.technovation.2026.103584-blue.svg" alt="DOI" /></a> |
| **[DiTTO-LLM: Framework for Discovering Topic-based Technology Opportunities via Large Language Model](https://arxiv.org/abs/2509.09724)** — Kim et al., 2025, *arXiv:2509.09724*. LLM tracks patent topic evolution to discover technology opportunities | <a href="https://arxiv.org/abs/2509.09724"><img src="https://img.shields.io/badge/arXiv-2509.09724-b31b1b.svg" alt="arXiv" /></a> |
| **[Predicting New Research Directions in Materials Science using Large Language Models and Concept Graphs](https://arxiv.org/abs/2506.16824)** — Marwitz et al., 2025, *arXiv:2506.16824*. LLM concept extraction plus graph model predicts unexplored combinations | <a href="https://arxiv.org/abs/2506.16824"><img src="https://img.shields.io/badge/arXiv-2506.16824-b31b1b.svg" alt="arXiv" /></a> |
| **[Technology opportunity analysis for creating innovative solutions: A framework for cross-field insights using patent data](https://doi.org/10.1016/j.aei.2025.104116)** — Kim et al., 2025, *Advanced Engineering Informatics*. Cross-field patent framework surfaces technology opportunities for solutions | <a href="https://doi.org/10.1016/j.aei.2025.104116"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2025.104116-blue.svg" alt="DOI" /></a> |

</details>

### Scientometrics & Literature Analysis

<details open>
<summary><h4>Literature Screening & Systematic Reviews</h4></summary>

*LLMs as screeners in systematic reviews — structurally the same include/exclude task as valid-patent selection.*

| Paper | Link |
|---|---|
| **[Scientific hypothesis prediction based on large language models and causal graphs](https://doi.org/10.1016/j.ipm.2026.104894)** — Ba et al., 2026, *Information Processing & Management*. Predicts scientific hypotheses from LLMs and causal graphs | <a href="https://doi.org/10.1016/j.ipm.2026.104894"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2026.104894-blue.svg" alt="DOI" /></a> |
| **[SocLitGen: An LLM-assisted framework for automated literature review in social sciences](https://doi.org/10.1016/j.ipm.2026.104885)** — Hu et al., 2026, *Information Processing & Management*. LLM-assisted framework automates social-science literature reviews | <a href="https://doi.org/10.1016/j.ipm.2026.104885"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2026.104885-blue.svg" alt="DOI" /></a> |

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
| **[Can ChatGPT be used to predict citation counts, readership, and social media interaction? An exploration among 2222 scientific abstracts](https://doi.org/10.1007/s11192-024-04939-y)** — de Winter, 2024, *Scientometrics*. ChatGPT predicts citations, readership, altmetrics across 2,222 abstracts | <a href="https://doi.org/10.1007/s11192-024-04939-y"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--024--04939--y-blue.svg" alt="DOI" /></a> |
| **[The use of ChatGPT for identifying disruptive papers in science: a first exploration](https://doi.org/10.1007/s11192-024-05176-z)** — Bornmann et al., 2024, *Scientometrics*. ChatGPT identifies disruptive papers without publication or citation counts | <a href="https://doi.org/10.1007/s11192-024-05176-z"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--024--05176--z-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Scientometrics & Science of Science</h4></summary>

*Agentic and LLM-based tools for bibliometric and science-of-science analysis.*

| Paper | Link |
|---|---|
| **[Large language models for scientometric mapping of scientific controversy: A validated hybrid AI–Human framework](https://doi.org/10.1007/s11192-026-05681-3)** — Susnjak et al., 2026, *Scientometrics*. Validated hybrid LLM-human framework maps scientific controversy stances | <a href="https://doi.org/10.1007/s11192-026-05681-3"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05681--3-blue.svg" alt="DOI" /></a> |
| **[Knowledge graphs and large language models for prompt-based scientometric inquiry](https://doi.org/10.1016/j.ipm.2026.104882)** — Correia et al., 2026, *Information Processing & Management*. Knowledge graphs plus LLMs answer scientometric questions from prompts | <a href="https://doi.org/10.1016/j.ipm.2026.104882"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2026.104882-blue.svg" alt="DOI" /></a> |
| **[An embedding-based approach for measuring science–technology topic linkages using LLMs](https://doi.org/10.1016/j.ipm.2026.104983)** — Hu et al., 2026, *Information Processing & Management*. LLM embeddings measure topic linkage between science and technology | <a href="https://doi.org/10.1016/j.ipm.2026.104983"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2026.104983-blue.svg" alt="DOI" /></a> |
| **[Turning Citation Networks Inside Out: Studying Science Using Content-Based Knowledge Graphs from LLM-Derived Taxonomies](https://doi.org/10.1162/qss.a.506)** — Kim et al., 2026, *Quantitative Science Studies*. LLM-induced taxonomies rebuild field structure from content, not citations | <a href="https://doi.org/10.1162/qss.a.506"><img src="https://img.shields.io/badge/DOI-10.1162%2Fqss.a.506-blue.svg" alt="DOI" /></a> |
| **[Assessing scientific knowledge in patents: A large language model approach](https://doi.org/10.1162/qss.a.493)** — Waterstraat, 2026, *Quantitative Science Studies*. LLM measure of patent science-relatedness beyond nonpatent references | <a href="https://doi.org/10.1162/qss.a.493"><img src="https://img.shields.io/badge/DOI-10.1162%2Fqss.a.493-blue.svg" alt="DOI" /></a> |
| **[Why grounded large language models fail without domain-specialized retrieval: an experimental scientometric study in solar physics](https://doi.org/10.1007/s11192-026-05784-x)** — Insardi & Gradvohl, 2026, *Scientometrics*. Retrieval infrastructure systematically shapes LLM scientometric outputs | <a href="https://doi.org/10.1007/s11192-026-05784-x"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05784--x-blue.svg" alt="DOI" /></a> |
| **[A framework for measuring scientific innovation integrating LLM-driven semantic reasoning and bibliometric analysis](https://doi.org/10.1007/s11192-026-05770-3)** — Shang et al., 2026, *Scientometrics*. Combines LLM semantic reasoning with bibliometrics to measure innovation | <a href="https://doi.org/10.1007/s11192-026-05770-3"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05770--3-blue.svg" alt="DOI" /></a> |
| **[Evidence access design for llm-based scientometrics: graph-based evidence augmentation over semantic retrieval](https://doi.org/10.1007/s11192-026-05729-4)** — Lee et al., 2026, *Scientometrics*. Graph-based evidence augmentation beats semantic retrieval for scientometrics | <a href="https://doi.org/10.1007/s11192-026-05729-4"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05729--4-blue.svg" alt="DOI" /></a> |
| **[LLMs as complementary tools for innovation surveys research: pattern replication and contextual relevance](https://doi.org/10.1007/s11192-026-05571-8)** — Park & Yang, 2026, *Scientometrics*. LLMs replicate innovation-survey response patterns and add contextual depth | <a href="https://doi.org/10.1007/s11192-026-05571-8"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05571--8-blue.svg" alt="DOI" /></a> |
| **[CiteFuncRanker: an LLM-based pairwise ranking framework for multi-functional citation analysis](https://doi.org/10.1007/s11192-026-05764-1)** — Wang et al., 2026, *Scientometrics*. LLM pairwise ranking framework for multi-functional citation analysis | <a href="https://doi.org/10.1007/s11192-026-05764-1"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05764--1-blue.svg" alt="DOI" /></a> |
| **[A scalable framework for scholarly similarity and novelty measurement with LLM-derived semantic embeddings](https://doi.org/10.1007/s11192-026-05754-3)** — Wang et al., 2026, *Scientometrics*. LLM embeddings scale scholarly similarity and novelty measurement | <a href="https://doi.org/10.1007/s11192-026-05754-3"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05754--3-blue.svg" alt="DOI" /></a> |
| **[Deepening citation understanding in scientific literature via LLM-powered context extraction](https://doi.org/10.1007/s11192-026-05637-7)** — Nguyen et al., 2026, *Scientometrics*. LLM extracts citation context to deepen citation-function understanding | <a href="https://doi.org/10.1007/s11192-026-05637-7"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05637--7-blue.svg" alt="DOI" /></a> |
| **[AI-Augmented Bibliometric Framework: A Paradigm Shift with Agentic AI for Dynamic, Snippet-Based Research Analysis](https://arxiv.org/abs/2511.21745)** — Bara et al., 2025, *arXiv:2511.21745*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agentic AI replaces static bibliometric keyword analysis | <a href="https://arxiv.org/abs/2511.21745"><img src="https://img.shields.io/badge/arXiv-2511.21745-b31b1b.svg" alt="arXiv" /></a> |
| **[The Empowerment of Science of Science by Large Language Models: New Tools and Methods](https://arxiv.org/abs/2511.15370)** — Liang et al., 2025, *arXiv:2511.15370*. Survey of LLM tools for scientometrics and research front detection | <a href="https://arxiv.org/abs/2511.15370"><img src="https://img.shields.io/badge/arXiv-2511.15370-b31b1b.svg" alt="arXiv" /></a> |
| **[SciSciGPT: Advancing Human-AI Collaboration in the Science of Science](https://arxiv.org/abs/2504.05559)** — Shao et al., 2025, *arXiv:2504.05559*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Specialist agents automate science-of-science analytics workflows | <a href="https://arxiv.org/abs/2504.05559"><img src="https://img.shields.io/badge/arXiv-2504.05559-b31b1b.svg" alt="arXiv" /></a> |
| **[Scaling research aim identification: Language models for classifying scientific and societal‐oriented studies](https://doi.org/10.1002/asi.70004)** — Wu et al., 2025, *JASIST*. Language models classify basic, applied, and societal research aims | <a href="https://doi.org/10.1002/asi.70004"><img src="https://img.shields.io/badge/DOI-10.1002%2Fasi.70004-blue.svg" alt="DOI" /></a> |
| **[AgentReview: Exploring Peer Review Dynamics with LLM Agents](https://arxiv.org/abs/2406.12708)** — Jin et al., 2024, *EMNLP 2024*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Reviewer/author/AC agents simulate peer-review dynamics | <a href="https://arxiv.org/abs/2406.12708"><img src="https://img.shields.io/badge/arXiv-2406.12708-b31b1b.svg" alt="arXiv" /></a> |
| **[Large-scale text analysis using generative language models: A case study in discovering public value expressions in AI patents](https://doi.org/10.1162/qss_a_00285)** — Pelaez et al., 2024, *Quantitative Science Studies*. GPT-4 labels public value expressions across 5.4M patent sentences | <a href="https://doi.org/10.1162/qss_a_00285"><img src="https://img.shields.io/badge/DOI-10.1162%2Fqss__a__00285-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>LLM-Assisted Peer Review</h4></summary>

*LLMs writing, checking, or auditing manuscript reviews — the review act itself.*

| Paper | Link |
|---|---|
| **[Toward better pragmatic tagging of peer review: Enhancing benchmark datasets via human-in-the-loop multi-agent collaboration](https://doi.org/10.1016/j.ipm.2026.104704)** — He et al., 2026, *Information Processing & Management*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Human-in-the-loop multi-agent tagging improves peer-review benchmark datasets | <a href="https://doi.org/10.1016/j.ipm.2026.104704"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2026.104704-blue.svg" alt="DOI" /></a> |
| **[Relationship between peer review quality and scientific impact: Insights from LLMs-assessed reviews](https://doi.org/10.1016/j.joi.2026.101801)** — Sun, 2026, *J. Informetrics*. LLM-scored review quality correlates with later citation impact | <a href="https://doi.org/10.1016/j.joi.2026.101801"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.joi.2026.101801-blue.svg" alt="DOI" /></a> |
| **[Can large language models assess the quality of peer review? An empirical study](https://doi.org/10.1007/s11192-026-05622-0)** — Tang et al., 2026, *Scientometrics*. Empirically tests whether LLMs can judge peer-review quality | <a href="https://doi.org/10.1007/s11192-026-05622-0"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05622--0-blue.svg" alt="DOI" /></a> |
| **[Impact of large language models on peer review opinions from a fine-grained perspective: evidence from top conference proceedings in AI](https://doi.org/10.1007/s11192-026-05645-7)** — Wu et al., 2026, *Scientometrics*. Fine-grained analysis of LLM influence on conference review opinions | <a href="https://doi.org/10.1007/s11192-026-05645-7"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05645--7-blue.svg" alt="DOI" /></a> |
| **[Co-Reviewer: can AI review like a human? An agentic framework for LLM-human alignment in peer review](https://doi.org/10.1007/s11192-026-05557-6)** — Bharti et al., 2026, *Scientometrics*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agentic framework aligns LLM reviews with human reviewer judgement | <a href="https://doi.org/10.1007/s11192-026-05557-6"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05557--6-blue.svg" alt="DOI" /></a> |
| **[LLM aspect prediction: reviewing academic papers from different aspects with Large Language Model](https://doi.org/10.1007/s11192-026-05771-2)** — Hu et al., 2026, *Scientometrics*. LLM reviews papers along separate evaluative aspects | <a href="https://doi.org/10.1007/s11192-026-05771-2"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05771--2-blue.svg" alt="DOI" /></a> |
| **[Fighting Fire with Fire: Infusing Artificial Intelligence into Peer Review to Sustain Quality Scholarship](https://doi.org/10.1287/mnsc.2026.00184)** — Bhargava et al., 2026, *Management Science*. Journals infuse generative AI into review to sustain quality | <a href="https://doi.org/10.1287/mnsc.2026.00184"><img src="https://img.shields.io/badge/DOI-10.1287%2Fmnsc.2026.00184-blue.svg" alt="DOI" /></a> |
| **[PaperEval: A universal, quantitative, and explainable paper evaluation method powered by a multi-agent system](https://doi.org/10.1016/j.ipm.2025.104225)** — Huang et al., 2025, *Information Processing & Management*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Multi-agent system scores papers quantitatively with explanations | <a href="https://doi.org/10.1016/j.ipm.2025.104225"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2025.104225-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Research & R&D Evaluation</h4></summary>

*LLM scores as institutional evaluation signals: journal quality, research value, funding assessment.*

| Paper | Link |
|---|---|
| **[A global south strategy for evaluating research value with ChatGPT](https://doi.org/10.1162/qss.a.460)** — Nunkoo & Thelwall, 2026, *Quantitative Science Studies*. ChatGPT research-value scoring as peer-review substitute for Global South | <a href="https://doi.org/10.1162/qss.a.460"><img src="https://img.shields.io/badge/DOI-10.1162%2Fqss.a.460-blue.svg" alt="DOI" /></a> |
| **[Evaluating LLM-assisted research: stage-sensitive asymmetries in productivity and epistemic control](https://doi.org/10.1093/reseval/rvag021)** — Kim & Park, 2026, *Research Evaluation*. Stage-sensitive productivity and epistemic-control asymmetries in LLM-assisted research | <a href="https://doi.org/10.1093/reseval/rvag021"><img src="https://img.shields.io/badge/DOI-10.1093%2Freseval%2Frvag021-blue.svg" alt="DOI" /></a> |
| **[Comparing LLM and expert assessments of journal quality](https://doi.org/10.1007/s11192-026-05644-8)** — Saarela et al., 2026, *Scientometrics*. LLM journal-quality ratings compared against Finnish JuFo expert panels | <a href="https://doi.org/10.1007/s11192-026-05644-8"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05644--8-blue.svg" alt="DOI" /></a> |
| **[Cicq: a unified framework integrating citation impact and content quality for automated literature evaluation](https://doi.org/10.1007/s11192-026-05594-1)** — Chen et al., 2026, *Scientometrics*. Unifies citation impact with fine-tuned LLM content quality | <a href="https://doi.org/10.1007/s11192-026-05594-1"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05594--1-blue.svg" alt="DOI" /></a> |
| **[Research evaluation with ChatGPT: is it age, country, length, or field biased?](https://doi.org/10.1007/s11192-025-05393-0)** — Thelwall & Kurt, 2025, *Scientometrics*. Tests ChatGPT quality scores for age, country, length, field bias | <a href="https://doi.org/10.1007/s11192-025-05393-0"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--025--05393--0-blue.svg" alt="DOI" /></a> |

</details>

### R&D & Innovation Management

<details open>
<summary><h4>Idea Generation & Creativity in Innovation</h4></summary>

*LLMs vs humans/crowds in generating product and research ideas.*

| Paper | Link |
|---|---|
| **[Multi-agent AI systems outperform human teams in creativity](https://arxiv.org/abs/2605.17885)** — Hu et al., 2026, *arXiv:2605.17885*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> LLM agent teams beat human teams on judged creativity | <a href="https://arxiv.org/abs/2605.17885"><img src="https://img.shields.io/badge/arXiv-2605.17885-b31b1b.svg" alt="arXiv" /></a> |
| **[Enhancing Research Idea Generation through Combinatorial Innovation and Multi-Agent Iterative Search Strategies](https://doi.org/10.1007/s11192-026-05654-6)** — Chen & Zhang, 2026, *Scientometrics*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Combinatorial innovation and multi-agent iterative search generate research ideas | <a href="https://doi.org/10.1007/s11192-026-05654-6"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05654--6-blue.svg" alt="DOI" /></a> |
| **[Agency Configurations in Generative AI Ideation: How Textual and Visual Idea Concretizations Shape Idea Creativity and Ideator Effort](https://doi.org/10.1287/isre.2024.0952)** — Gordetzki et al., 2026, *Information Systems Research*. Textual versus visual AI concretization shapes idea creativity and effort | <a href="https://doi.org/10.1287/isre.2024.0952"><img src="https://img.shields.io/badge/DOI-10.1287%2Fisre.2024.0952-blue.svg" alt="DOI" /></a> |
| **[The Role of Artificial Intelligence in the Ideation Process](https://doi.org/10.1111/jpim.12791)** — Pescher et al., 2025, *Journal of Product Innovation Management*. AI's role across ideation stages in product innovation | <a href="https://doi.org/10.1111/jpim.12791"><img src="https://img.shields.io/badge/DOI-10.1111%2Fjpim.12791-blue.svg" alt="DOI" /></a> |
| **[Agent Ideate: Multi-Agent Framework for Product Business Idea Generation from Patents](https://arxiv.org/abs/2507.01717)** — Kanumolu et al., 2025, *AgentScen @ IJCAI 2025*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agents mine patents to generate product business ideas | <a href="https://arxiv.org/abs/2507.01717"><img src="https://img.shields.io/badge/arXiv-2507.01717-b31b1b.svg" alt="arXiv" /></a> |
| **[Exploring Design of Multi-Agent LLM Dialogues for Research Ideation](https://arxiv.org/abs/2507.08350)** — Ueda et al., 2025, *SIGDIAL 2025*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agent roles, cohort size, depth shape idea novelty | <a href="https://arxiv.org/abs/2507.08350"><img src="https://img.shields.io/badge/arXiv-2507.08350-b31b1b.svg" alt="arXiv" /></a> |
| **[Deep Ideation: Designing LLM Agents to Generate Novel Research Ideas on Scientific Concept Network](https://arxiv.org/abs/2511.02238)** — Zhao et al., 2025, *arXiv:2511.02238*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Explore-expand-evolve agents mine concept networks for ideas | <a href="https://arxiv.org/abs/2511.02238"><img src="https://img.shields.io/badge/arXiv-2511.02238-b31b1b.svg" alt="arXiv" /></a> |
| **[SMAR + NIE IdeaGen: A knowledge graph based node importance estimation with analogical reasoning on large language model for idea generation](https://doi.org/10.1016/j.eswa.2025.127455)** — Oyelade et al., 2025, *Expert Systems with Applications*. Knowledge-graph node importance plus analogical LLM reasoning generates ideas | <a href="https://doi.org/10.1016/j.eswa.2025.127455"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.eswa.2025.127455-blue.svg" alt="DOI" /></a> |
| **[How the Ideation Process Shapes the Creative Output in Innovation Contests—An Analysis Using a Large Language Model](https://doi.org/10.1111/caim.70011)** — Moehrle et al., 2025, *Creativity and Innovation Management*. LLM traces how ideation shapes innovation-contest creative output | <a href="https://doi.org/10.1111/caim.70011"><img src="https://img.shields.io/badge/DOI-10.1111%2Fcaim.70011-blue.svg" alt="DOI" /></a> |
| **[Evaluating Creative Output With Generative Artificial Intelligence: Comparing GPT Models and Human Experts in Idea Evaluation](https://doi.org/10.1111/caim.70007)** — Kranzle & Sharratt, 2025, *Creativity and Innovation Management*. GPT models versus human experts at evaluating creative ideas | <a href="https://doi.org/10.1111/caim.70007"><img src="https://img.shields.io/badge/DOI-10.1111%2Fcaim.70007-blue.svg" alt="DOI" /></a> |
| **[The Double-Edged Roles of Generative AI in the Creative Process: Experiments on Design Work](https://doi.org/10.1287/isre.2024.0937)** — Hou et al., 2025, *Information Systems Research*. GenAI boosts ideation but hurts execution for designers | <a href="https://doi.org/10.1287/isre.2024.0937"><img src="https://img.shields.io/badge/DOI-10.1287%2Fisre.2024.0937-blue.svg" alt="DOI" /></a> |
| **[The Crowdless Future? Generative AI and Creative Problem-Solving](https://doi.org/10.1287/orsc.2023.18430)** — Boussioux et al., 2024, *Organization Science*. GPT-4 solutions vs crowdsourced solutions in an innovation challenge | <a href="https://doi.org/10.1287/orsc.2023.18430"><img src="https://img.shields.io/badge/DOI-10.1287%2Forsc.2023.18430-blue.svg" alt="DOI" /></a> |
| **[Comparing the Ideation Quality of Humans With Generative Artificial Intelligence](https://ieeexplore.ieee.org/document/10398283)** — Joosten et al., 2024, *IEEE Engineering Management Review*. Human vs GPT-4 ideation quality comparison for innovation management | <a href="https://ieeexplore.ieee.org/document/10398283"><img src="https://img.shields.io/badge/IEEE-Xplore-00629B.svg" alt="IEEE Xplore" /></a> |
| **[Prompting Diverse Ideas: Increasing AI Idea Variance](https://arxiv.org/abs/2402.01727)** — Meincke et al., 2024, *arXiv:2402.01727*. Prompt strategies to raise diversity of LLM-generated product ideas | <a href="https://arxiv.org/abs/2402.01727"><img src="https://img.shields.io/badge/arXiv-2402.01727-b31b1b.svg" alt="arXiv" /></a> |
| **[Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers](https://arxiv.org/abs/2409.04109)** — Si et al., 2024, *ICLR 2025*. LLM-generated research ideas judged more novel than experts' | <a href="https://arxiv.org/abs/2409.04109"><img src="https://img.shields.io/badge/arXiv-2409.04109-b31b1b.svg" alt="arXiv" /></a> |
| **[Generation and human-expert evaluation of interesting research ideas using knowledge graphs and large language models](https://arxiv.org/abs/2405.17044)** — Gu & Krenn, 2024, *arXiv:2405.17044*. SciMuse: knowledge-graph LLM ideas ranked by 100+ research leaders | <a href="https://arxiv.org/abs/2405.17044"><img src="https://img.shields.io/badge/arXiv-2405.17044-b31b1b.svg" alt="arXiv" /></a> |
| **[Revolution or inflated expectations? Exploring the impact of generative AI on ideation in a practical sustainability context](https://doi.org/10.1016/j.technovation.2024.103123)** — Eisenreich et al., 2024, *Technovation*. GenAI ideation versus expert workshops at BSH Home Appliances | <a href="https://doi.org/10.1016/j.technovation.2024.103123"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.technovation.2024.103123-blue.svg" alt="DOI" /></a> |
| **[Ideas are Dimes a Dozen: Large Language Models for Idea Generation in Innovation](https://doi.org/10.2139/ssrn.4526071)** — Girotra et al., 2023, *SSRN Working Paper*. GPT-4 vs students: LLM ideas dominate top-quality product ideas | <a href="https://doi.org/10.2139/ssrn.4526071"><img src="https://img.shields.io/badge/DOI-10.2139%2Fssrn.4526071-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>New Product Development & R&D Management</h4></summary>

*LLM augmentation of NPD teams and product-concept evaluation.*

| Paper | Link |
|---|---|
| **[An Interactive Multi-Agent System for Evaluation of New Product Concepts](https://arxiv.org/abs/2603.05980)** — Xuan et al., 2026, *arXiv:2603.05980*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Specialized LLM agents deliberate to evaluate product concepts | <a href="https://arxiv.org/abs/2603.05980"><img src="https://img.shields.io/badge/arXiv-2603.05980-b31b1b.svg" alt="arXiv" /></a> |
| **[Comparing human- and AI-generated system requirements: an industrial case study](https://doi.org/10.1080/09544828.2026.2683735)** — Rahmanpour et al., 2026, *J. Engineering Design*. Compares LLM- and human-written system requirements in industry | <a href="https://doi.org/10.1080/09544828.2026.2683735"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2026.2683735-blue.svg" alt="DOI" /></a> |
| **[How experience moderates the impact of AI suggestions on researchers' perceptions of their ideas](https://doi.org/10.1016/j.respol.2026.105575)** — Tröbinger et al., 2026, *Research Policy*. Researcher experience moderates how AI suggestions reshape idea perceptions | <a href="https://doi.org/10.1016/j.respol.2026.105575"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.respol.2026.105575-blue.svg" alt="DOI" /></a> |
| **[The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork](https://doi.org/10.1287/orsc.2025.20702)** — Dell’Acqua et al., 2026, *Organization Science*. Field experiment with 791 P&G professionals on AI teamwork | <a href="https://doi.org/10.1287/orsc.2025.20702"><img src="https://img.shields.io/badge/DOI-10.1287%2Forsc.2025.20702-blue.svg" alt="DOI" /></a> |
| **[Identifying Opportunities to Repurpose Decommissioned Products Using Large Language Models](https://doi.org/10.1115/1.4070518)** — Hewa Witharanage et al., 2025, *J. Mechanical Design*. LLMs identify repurposing opportunities for decommissioned products | <a href="https://doi.org/10.1115/1.4070518"><img src="https://img.shields.io/badge/DOI-10.1115%2F1.4070518-blue.svg" alt="DOI" /></a> |
| **[Bridging the maturity-expectation gap: Generative AI in strategic decision-making for public R&D interim review](https://doi.org/10.1016/j.technovation.2025.103374)** — Kim et al., 2025, *Technovation*. Generative AI supports strategic decisions in public R&D interim review | <a href="https://doi.org/10.1016/j.technovation.2025.103374"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.technovation.2025.103374-blue.svg" alt="DOI" /></a> |
| **[Augmenting human innovation teams with artificial intelligence: Exploring transformer-based language models](https://doi.org/10.1111/jpim.12656)** — Bouschery et al., 2023, *Journal of Product Innovation Management*. GPT-3 augmenting NPD teams; AI-augmented double diamond framework | <a href="https://doi.org/10.1111/jpim.12656"><img src="https://img.shields.io/badge/DOI-10.1111%2Fjpim.12656-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h4>Engineering & Conceptual Design</h4></summary>

*LLMs in the design front end: concept generation, TRIZ, bio-inspired design, requirements.*

| Paper | Link |
|---|---|
| **[A retrieval-augmented method for explainable product ideation: Unifying conceptual design knowledge graph and large language models](https://doi.org/10.1016/j.aei.2026.104770)** — Cong et al., 2026, *Advanced Engineering Informatics*. Retrieval-augmented design knowledge graph makes product ideation explainable | <a href="https://doi.org/10.1016/j.aei.2026.104770"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2026.104770-blue.svg" alt="DOI" /></a> |
| **[Analogical reasoning with large language models: a co-creative framework and benchmarking of LLMs in design ideation](https://doi.org/10.1017/dsj.2025.10044)** — Kokate & Onkar, 2026, *Design Science*. Co-creative analogical reasoning framework benchmarks LLMs on design ideation | <a href="https://doi.org/10.1017/dsj.2025.10044"><img src="https://img.shields.io/badge/DOI-10.1017%2Fdsj.2025.10044-blue.svg" alt="DOI" /></a> |
| **[Design ideation through large language model-driven design operation: a case study of architectural design using pattern language](https://doi.org/10.1017/dsj.2026.10061)** — Tanaka et al., 2026, *Design Science*. Pattern-language design operation drives LLM ideation in architectural design | <a href="https://doi.org/10.1017/dsj.2026.10061"><img src="https://img.shields.io/badge/DOI-10.1017%2Fdsj.2026.10061-blue.svg" alt="DOI" /></a> |
| **[Large language model agent as a mechanical designer](https://doi.org/10.1080/09544828.2026.2624356)** — Jadhav & Barati Farimani, 2026, *J. Engineering Design*. LLM agent iterates mechanical design against FEM performance targets | <a href="https://doi.org/10.1080/09544828.2026.2624356"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2026.2624356-blue.svg" alt="DOI" /></a> |
| **[An LLM-based multi-agent system to assist early-stage product design and evaluation](https://doi.org/10.1080/09544828.2026.2616583)** — Chen et al., 2026, *J. Engineering Design*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Multi-agent LLM system generates and feasibility-checks early product concepts | <a href="https://doi.org/10.1080/09544828.2026.2616583"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2026.2616583-blue.svg" alt="DOI" /></a> |
| **[Leveraging large language models for participatory digital personas in future-oriented design: a case study of autonomous vehicle intelligent cockpits](https://doi.org/10.1080/09544828.2026.2639927)** — Zhou et al., 2026, *J. Engineering Design*. LLM digital personas stand in for unavailable future users | <a href="https://doi.org/10.1080/09544828.2026.2639927"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2026.2639927-blue.svg" alt="DOI" /></a> |
| **[An agentic knowledge-infused reasoning framework for engineering design based on large language models](https://doi.org/10.1080/09544828.2026.2680617)** — Li et al., 2026, *J. Engineering Design*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Agentic knowledge-infused reasoning framework for LLM engineering design | <a href="https://doi.org/10.1080/09544828.2026.2680617"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2026.2680617-blue.svg" alt="DOI" /></a> |
| **[From diagnosis to design: a hybrid human–LLM framework integrating fsQCA and TRIZ for cultural service innovation](https://doi.org/10.1080/09544828.2026.2714470)** — Gilani & Lee, 2026, *J. Engineering Design*. Hybrid human-LLM framework joins fsQCA diagnosis with TRIZ solutions | <a href="https://doi.org/10.1080/09544828.2026.2714470"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2026.2714470-blue.svg" alt="DOI" /></a> |
| **[Real-time dynamic graph construction and reasoning to support human-AI collaborative product conceptual design](https://doi.org/10.1080/09544828.2026.2680619)** — Chen et al., 2026, *J. Engineering Design*. Real-time dynamic graph reasoning syncs AI with designer cognition | <a href="https://doi.org/10.1080/09544828.2026.2680619"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2026.2680619-blue.svg" alt="DOI" /></a> |
| **[Collaboration Between Two Large Language Models for Design Concept Generation](https://doi.org/10.1115/1.4072235)** — Xiao et al., 2026, *J. Mechanical Design*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Two LLMs collaborate to generate design concepts | <a href="https://doi.org/10.1115/1.4072235"><img src="https://img.shields.io/badge/DOI-10.1115%2F1.4072235-blue.svg" alt="DOI" /></a> |
| **[Explainable Artificial Intelligence in Conceptual Design: An Large Language Model–Powered Framework to Enhance Originality and Credibility](https://doi.org/10.1115/1.4071544)** — Velasco Medina & Murakami, 2026, *J. Mechanical Design*. Explainable LLM framework raises originality and credibility of concepts | <a href="https://doi.org/10.1115/1.4071544"><img src="https://img.shields.io/badge/DOI-10.1115%2F1.4071544-blue.svg" alt="DOI" /></a> |
| **[AutoTRIZ: Automating engineering innovation with TRIZ and large language models](https://doi.org/10.1016/j.aei.2025.103312)** — Jiang et al., 2025, *Advanced Engineering Informatics*. AutoTRIZ automates TRIZ inventive problem solving with LLMs | <a href="https://doi.org/10.1016/j.aei.2025.103312"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2025.103312-blue.svg" alt="DOI" /></a> |
| **[An LLM-based cross-domain knowledge retrieval augmented generation method for bio-inspired solution design](https://doi.org/10.1016/j.aei.2025.104017)** — Cui et al., 2025, *Advanced Engineering Informatics*. Cross-domain retrieval augments LLMs for bio-inspired solution design | <a href="https://doi.org/10.1016/j.aei.2025.104017"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2025.104017-blue.svg" alt="DOI" /></a> |
| **[A context-aware KG-LLM collaborated conceptual design approach for personalized products: A case in lower limbs rehabilitation assistive devices](https://doi.org/10.1016/j.aei.2025.103422)** — Pan et al., 2025, *Advanced Engineering Informatics*. Context-aware knowledge-graph LLM conceptual design for personalized assistive devices | <a href="https://doi.org/10.1016/j.aei.2025.103422"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2025.103422-blue.svg" alt="DOI" /></a> |
| **[Knowledge augmented generalizer specializer: A framework for early stage design exploration](https://doi.org/10.1016/j.aei.2025.103141)** — Sahadevan et al., 2025, *Advanced Engineering Informatics*. Generalizer-specializer framework augments knowledge for early-stage design exploration | <a href="https://doi.org/10.1016/j.aei.2025.103141"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2025.103141-blue.svg" alt="DOI" /></a> |
| **[Customization and personalization of large language models for engineering design](https://doi.org/10.1016/j.cirp.2025.03.001)** — Jiang et al., 2025, *CIRP Annals*. Customizes general-purpose LLMs into manufacturability-aware design models | <a href="https://doi.org/10.1016/j.cirp.2025.03.001"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.cirp.2025.03.001-blue.svg" alt="DOI" /></a> |
| **[How generative AI supports human in conceptual design](https://doi.org/10.1017/dsj.2025.2)** — Chen et al., 2025, *Design Science*. Maps human and generative-AI roles across conceptual design stages | <a href="https://doi.org/10.1017/dsj.2025.2"><img src="https://img.shields.io/badge/DOI-10.1017%2Fdsj.2025.2-blue.svg" alt="DOI" /></a> |
| **[Enhancing design concept diversity: multi-persona prompting strategies for large language models](https://doi.org/10.1017/dsj.2025.10037)** — Feng et al., 2025, *Design Science*. Multi-persona prompting broadens the diversity of LLM design concepts | <a href="https://doi.org/10.1017/dsj.2025.10037"><img src="https://img.shields.io/badge/DOI-10.1017%2Fdsj.2025.10037-blue.svg" alt="DOI" /></a> |
| **[A comparative study on retrieval-augmented generation and chain-of-thought applications for LLM-assisted engineering design ideation](https://doi.org/10.1080/09544828.2025.2574209)** — Jiang, 2025, *J. Engineering Design*. Compares RAG and chain-of-thought prompting across 40 design tasks | <a href="https://doi.org/10.1080/09544828.2025.2574209"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2025.2574209-blue.svg" alt="DOI" /></a> |
| **[AskNatureGPT: an LLM-driven concept generation method based on bio-inspired design knowledge](https://doi.org/10.1080/09544828.2025.2481536)** — Chen et al., 2025, *J. Engineering Design*. AskNatureGPT generates concepts from bio-inspired design knowledge | <a href="https://doi.org/10.1080/09544828.2025.2481536"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2025.2481536-blue.svg" alt="DOI" /></a> |
| **[A generation framework of conceptual solutions integrating link prediction and large language model](https://doi.org/10.1080/09544828.2025.2558333)** — Chang et al., 2025, *J. Engineering Design*. Link prediction plus LLM turns ideas into conceptual solutions | <a href="https://doi.org/10.1080/09544828.2025.2558333"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2025.2558333-blue.svg" alt="DOI" /></a> |
| **[Multilingual graph retrieval-augmented generation for product design using design knowledge](https://doi.org/10.1080/09544828.2025.2537464)** — Zhang et al., 2025, *J. Engineering Design*. Multilingual graph RAG unifies product design knowledge across languages | <a href="https://doi.org/10.1080/09544828.2025.2537464"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2025.2537464-blue.svg" alt="DOI" /></a> |
| **[Agentic Large Language Models for Conceptual Systems Engineering and Design](https://doi.org/10.1115/1.4070328)** — Massoudi & Fuge, 2025, *J. Mechanical Design*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Multi-agent LLMs handle requirements, decomposition, and executable system models | <a href="https://doi.org/10.1115/1.4070328"><img src="https://img.shields.io/badge/DOI-10.1115%2F1.4070328-blue.svg" alt="DOI" /></a> |
| **[Vision-Language Models for Design Concept Generation: An Actor–Critic Framework](https://doi.org/10.1115/1.4067619)** — Ghasemi & Moghaddam, 2025, *J. Mechanical Design*. Actor-critic vision-language framework diversifies generated design concepts | <a href="https://doi.org/10.1115/1.4067619"><img src="https://img.shields.io/badge/DOI-10.1115%2F1.4067619-blue.svg" alt="DOI" /></a> |
| **[Generating TRIZ-inspired guidelines for eco-design using Generative Artificial Intelligence](https://doi.org/10.1016/j.aei.2024.102846)** — Lee et al., 2024, *Advanced Engineering Informatics*. Generative AI produces TRIZ-inspired eco-design guidelines | <a href="https://doi.org/10.1016/j.aei.2024.102846"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2024.102846-blue.svg" alt="DOI" /></a> |
| **[AskNatureNet: A divergent thinking tool based on bio-inspired design knowledge](https://doi.org/10.1016/j.aei.2024.102593)** — Chen et al., 2024, *Advanced Engineering Informatics*. AskNatureNet supports divergent thinking with bio-inspired design analogies | <a href="https://doi.org/10.1016/j.aei.2024.102593"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2024.102593-blue.svg" alt="DOI" /></a> |
| **[Systematic synthesis of design prompts for large language models in conceptual design](https://doi.org/10.1016/j.cirp.2024.04.062)** — Tian et al., 2024, *CIRP Annals*. Classification scheme systematizes design prompts for conceptual-design LLMs | <a href="https://doi.org/10.1016/j.cirp.2024.04.062"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.cirp.2024.04.062-blue.svg" alt="DOI" /></a> |
| **[A foundation model enhanced approach for generative design in combinational creativity](https://doi.org/10.1080/09544828.2024.2356707)** — Chen et al., 2024, *J. Engineering Design*. Foundation model fuses base and additive concepts for combinational creativity | <a href="https://doi.org/10.1080/09544828.2024.2356707"><img src="https://img.shields.io/badge/DOI-10.1080%2F09544828.2024.2356707-blue.svg" alt="DOI" /></a> |
| **[Toward Controllable Generative Design: A Conceptual Design Generation Approach Leveraging the Function–Behavior–Structure Ontology and Large Language Models](https://doi.org/10.1115/1.4065562)** — Chen et al., 2024, *J. Mechanical Design*. Function-Behavior-Structure ontology makes LLM conceptual generation controllable | <a href="https://doi.org/10.1115/1.4065562"><img src="https://img.shields.io/badge/DOI-10.1115%2F1.4065562-blue.svg" alt="DOI" /></a> |

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
| **[Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://arxiv.org/abs/2208.10264)** — Aher et al., 2023, *ICML 2023*. Turing Experiments replicate classic human-subject studies with LLMs | <a href="https://arxiv.org/abs/2208.10264"><img src="https://img.shields.io/badge/arXiv-2208.10264-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h4>Strategy & Decision-Making</h4></summary>

*LLMs in strategic decision-making and entrepreneurship.*

| Paper | Link |
|---|---|
| **[Artificial Intelligence and Strategic Decision-Making: Evidence from Entrepreneurs and Investors](https://doi.org/10.1287/stsc.2024.0190)** — Csaszar et al., 2024, *Strategy Science*. GPT-4 business strategies rival human founders per investor evaluations | <a href="https://doi.org/10.1287/stsc.2024.0190"><img src="https://img.shields.io/badge/DOI-10.1287%2Fstsc.2024.0190-blue.svg" alt="DOI" /></a> |

</details>

## Adjacent & enabling methods

Benchmarks, domain models, surveys, generic-domain analogues (e.g. medical systematic-review screening), and landmark frameworks that TIM applications build on. Kept for reference — **not counted in the headline paper count or charts**.

<details open>
<summary><h3>IP Benchmarks & Evaluation</h3></summary>

*Benchmarks and metrics for LLM performance on intellectual-property tasks.*

| Paper | Link |
|---|---|
| **[Towards Better Evaluation for Generated Patent Claims](https://arxiv.org/abs/2505.11095)** — Jiang et al., 2025, *arXiv:2505.11095*. Patent-CE benchmark and PatClaimEval for claim evaluation | <a href="https://arxiv.org/abs/2505.11095"><img src="https://img.shields.io/badge/arXiv-2505.11095-b31b1b.svg" alt="arXiv" /></a> |
| **[IPBench: Benchmarking the Knowledge of Large Language Models in Intellectual Property](https://arxiv.org/abs/2504.15524)** — Wang et al., 2025, *arXiv:2504.15524*. Comprehensive IP-knowledge benchmark; 10 tasks, 20 IP scenarios | <a href="https://arxiv.org/abs/2504.15524"><img src="https://img.shields.io/badge/arXiv-2504.15524-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentScore: Multi-dimensional Evaluation of LLM-Generated Patent Claims](https://arxiv.org/abs/2505.19345)** — Yoo et al., 2025, *arXiv:2505.19345*. Legal-structure-aware metric scoring LLM-generated claims | <a href="https://arxiv.org/abs/2505.19345"><img src="https://img.shields.io/badge/arXiv-2505.19345-b31b1b.svg" alt="arXiv" /></a> |
| **[MoZIP: A Multilingual Benchmark to Evaluate Large Language Models in Intellectual Property](https://arxiv.org/abs/2402.16389)** — Ni et al., 2024, *LREC-COLING 2024*. Multilingual IP quiz/QA/patent-matching benchmark plus MoZi model | <a href="https://arxiv.org/abs/2402.16389"><img src="https://img.shields.io/badge/arXiv-2402.16389-b31b1b.svg" alt="arXiv" /></a> |
| **[IPEval: A Bilingual Intellectual Property Agency Consultation Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2406.12386)** — Wang et al., 2024, *arXiv:2406.12386*. Bilingual patent-agent exam benchmark for LLM IP competence | <a href="https://arxiv.org/abs/2406.12386"><img src="https://img.shields.io/badge/arXiv-2406.12386-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentEval: Understanding Errors in Patent Generation](https://arxiv.org/abs/2406.06589)** — Zuo et al., 2024, *NAACL 2024*. Error typology and human-annotated benchmark for patent generation | <a href="https://arxiv.org/abs/2406.06589"><img src="https://img.shields.io/badge/arXiv-2406.06589-b31b1b.svg" alt="arXiv" /></a> |
| **[Evaluating generative patent language models](https://doi.org/10.1016/j.wpi.2023.102173)** — Lee, 2023, *World Patent Information*. Autocomplete-based evaluation of generative patent language models | <a href="https://doi.org/10.1016/j.wpi.2023.102173"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2023.102173-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>IP Domain Models & Surveys</h3></summary>

*Domain-adapted models and surveys of NLP/LLM methods in the patent domain.*

| Paper | Link |
|---|---|
| **[A statistical approach of distinguishing patent abstracts written by human from those generated by ChatGPT](https://doi.org/10.1016/j.wpi.2026.102457)** — Yue et al., 2026, *World Patent Information*. Statistical test distinguishes ChatGPT-generated patent abstracts from human ones | <a href="https://doi.org/10.1016/j.wpi.2026.102457"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2026.102457-blue.svg" alt="DOI" /></a> |
| **[Natural Language Processing in the Patent Domain: A Survey](https://arxiv.org/abs/2403.04105)** — Jiang et al., 2025, *Artificial Intelligence Review*. Survey of LLM/NLP patent tasks, datasets, and methods | <a href="https://arxiv.org/abs/2403.04105"><img src="https://img.shields.io/badge/arXiv-2403.04105-b31b1b.svg" alt="arXiv" /></a> |
| **[PatentGPT: A Large Language Model for Intellectual Property](https://arxiv.org/abs/2404.18255)** — Bai et al., 2024, *arXiv:2404.18255*. IP-domain-trained LLM; beats GPT-4 on China patent agent exam | <a href="https://arxiv.org/abs/2404.18255"><img src="https://img.shields.io/badge/arXiv-2404.18255-b31b1b.svg" alt="arXiv" /></a> |
| **[Will AI solve the patent classification problem?](https://doi.org/10.1016/j.wpi.2024.102294)** — Kamateri et al., 2024, *World Patent Information*. Reviews whether AI has solved automated patent classification | <a href="https://doi.org/10.1016/j.wpi.2024.102294"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.wpi.2024.102294-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>Literature Screening & Systematic Reviews</h3></summary>

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
<summary><h3>Novelty & Impact Prediction of Research</h3></summary>

*Scoring the novelty of papers and predicting their scientific impact.*

| Paper | Link |
|---|---|
| **[How deep do large language models internalize scientific literature and citation practices?](https://doi.org/10.1162/qss.a.502)** — Algaba et al., 2026, *Quantitative Science Studies*. Compares GPT-4o reference suggestions against human citation practice | <a href="https://doi.org/10.1162/qss.a.502"><img src="https://img.shields.io/badge/DOI-10.1162%2Fqss.a.502-blue.svg" alt="DOI" /></a> |
| **[Large language models surpass human experts in predicting neuroscience results](https://doi.org/10.1038/s41562-024-02046-9)** — Luo et al., 2024, *Nature Human Behaviour*. BrainBench: LLMs beat neuroscientists at predicting experimental outcomes | <a href="https://doi.org/10.1038/s41562-024-02046-9"><img src="https://img.shields.io/badge/DOI-10.1038%2Fs41562--024--02046--9-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>Scientometrics & Science of Science</h3></summary>

*Agentic and LLM-based tools for bibliometric and science-of-science analysis.*

| Paper | Link |
|---|---|
| **[Large language models for business and management applications: A review](https://doi.org/10.1016/j.ipm.2026.104864)** — Arslan et al., 2026, *Information Processing & Management*. Bibliometric and thematic review of LLMs in business management | <a href="https://doi.org/10.1016/j.ipm.2026.104864"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.ipm.2026.104864-blue.svg" alt="DOI" /></a> |
| **[Ethical evaluation of large language models for scientometrics: a multidimensional perspective](https://doi.org/10.1007/s11192-026-05773-0)** — Shen et al., 2026, *Scientometrics*. Multidimensional ethical assessment of LLM use in scientometrics | <a href="https://doi.org/10.1007/s11192-026-05773-0"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05773--0-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>Automated Survey Writing & Paper Search</h3></summary>

*Agents that search, synthesize, and write literature reviews.*

| Paper | Link |
|---|---|
| **[PaSa: An LLM Agent for Comprehensive Academic Paper Search](https://arxiv.org/abs/2501.10120)** — He et al., 2025, *arXiv:2501.10120*. RL-trained LLM agent for comprehensive scholarly paper retrieval | <a href="https://arxiv.org/abs/2501.10120"><img src="https://img.shields.io/badge/arXiv-2501.10120-b31b1b.svg" alt="arXiv" /></a> |
| **[Agentic AutoSurvey: Let LLMs Survey LLMs](https://arxiv.org/abs/2509.18661)** — Liu et al., 2025, *arXiv:2509.18661*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Four agents search, cluster, write, and evaluate literature surveys | <a href="https://arxiv.org/abs/2509.18661"><img src="https://img.shields.io/badge/arXiv-2509.18661-b31b1b.svg" alt="arXiv" /></a> |
| **[SurveyG: A Multi-Agent LLM Framework with Hierarchical Citation Graph for Automated Survey Generation](https://arxiv.org/abs/2510.07733)** — Nguyen et al., 2025, *arXiv:2510.07733*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Citation-graph-guided multi-agent survey generation | <a href="https://arxiv.org/abs/2510.07733"><img src="https://img.shields.io/badge/arXiv-2510.07733-b31b1b.svg" alt="arXiv" /></a> |
| **[Accelerating Scientific Research Through a Multi-LLM Framework](https://arxiv.org/abs/2502.07960)** — Ramirez-Medina et al., 2025, *arXiv:2502.07960*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> Four-agent pipeline retrieves, filters, and synthesizes literature | <a href="https://arxiv.org/abs/2502.07960"><img src="https://img.shields.io/badge/arXiv-2502.07960-b31b1b.svg" alt="arXiv" /></a> |
| **[AutoSurvey: Large Language Models Can Automatically Write Surveys](https://arxiv.org/abs/2406.10252)** — Wang et al., 2024, *NeurIPS 2024*. End-to-end LLM pipeline for automatic literature survey writing | <a href="https://arxiv.org/abs/2406.10252"><img src="https://img.shields.io/badge/arXiv-2406.10252-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h3>LLM-Assisted Peer Review</h3></summary>

*LLMs writing, checking, or auditing manuscript reviews — the review act itself.*

| Paper | Link |
|---|---|
| **[When AI Becomes Its Own Biggest Fan: Self-Preference Bias in AI-Assisted Peer Review](https://doi.org/10.1109/tem.2026.3691360)** — Shi et al., 2026, *IEEE Trans. Engineering Management*. GPT-4 and LLaMA favour their own text when reviewing | <a href="https://doi.org/10.1109/tem.2026.3691360"><img src="https://img.shields.io/badge/DOI-10.1109%2Ftem.2026.3691360-blue.svg" alt="DOI" /></a> |
| **[Exploiting large language models in peer review: indirect prompt injection attacks and integrity probes](https://doi.org/10.1007/s11192-026-05695-x)** — Torrielli et al., 2026, *Scientometrics*. Hidden manuscript instructions steer LLM reviewers via prompt injection | <a href="https://doi.org/10.1007/s11192-026-05695-x"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05695--x-blue.svg" alt="DOI" /></a> |
| **[More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review](https://doi.org/10.1287/orsc.2026.ed.v37.n3)** — Gartenberg et al., 2026, *Organization Science*. AI raises submissions 42% while writing quality falls | <a href="https://doi.org/10.1287/orsc.2026.ed.v37.n3"><img src="https://img.shields.io/badge/DOI-10.1287%2Forsc.2026.ed.v37.n3-blue.svg" alt="DOI" /></a> |
| **[Large language models in peer review: challenges and opportunities](https://doi.org/10.1007/s11192-025-05440-w)** — Sun, 2025, *Scientometrics*. Surveys challenges and opportunities of LLMs in peer review | <a href="https://doi.org/10.1007/s11192-025-05440-w"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--025--05440--w-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>Research & R&D Evaluation</h3></summary>

*LLM scores as institutional evaluation signals: journal quality, research value, funding assessment.*

| Paper | Link |
|---|---|
| **[Large language models and responsible research evaluation: an extension of the Leiden Manifesto](https://doi.org/10.1007/s11192-026-05552-x)** — Thelwall, 2026, *Scientometrics*. Extends Leiden Manifesto principles to LLM-based research evaluation | <a href="https://doi.org/10.1007/s11192-026-05552-x"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05552--x-blue.svg" alt="DOI" /></a> |
| **[Opinion paper: generative AI and the future of scientometrics](https://doi.org/10.1007/s11192-026-05667-1)** — Lepori et al., 2026, *Scientometrics*. Conceptual framework comparing GenAI, bibliometrics, and human judgement | <a href="https://doi.org/10.1007/s11192-026-05667-1"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--026--05667--1-blue.svg" alt="DOI" /></a> |
| **[Research quality evaluation by AI in the era of large language models: advantages, disadvantages, and systemic effects – An opinion paper](https://doi.org/10.1007/s11192-025-05361-8)** — Thelwall, 2025, *Scientometrics*. Opinion piece on AI displacing bibliometrics in quality evaluation | <a href="https://doi.org/10.1007/s11192-025-05361-8"><img src="https://img.shields.io/badge/DOI-10.1007%2Fs11192--025--05361--8-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>Idea Generation & Creativity in Innovation</h3></summary>

*LLMs vs humans/crowds in generating product and research ideas.*

| Paper | Link |
|---|---|
| **[The hidden costs of AI-assisted ideation: empirical findings on ChatGPT’s impact on novice designers’ creative confidence and design process](https://doi.org/10.1017/dsj.2026.10060)** — Krajcer et al., 2026, *Design Science*. ChatGPT ideation dents novice designers' creative confidence and process | <a href="https://doi.org/10.1017/dsj.2026.10060"><img src="https://img.shields.io/badge/DOI-10.1017%2Fdsj.2026.10060-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>New Product Development & R&D Management</h3></summary>

*LLM augmentation of NPD teams and product-concept evaluation.*

| Paper | Link |
|---|---|
| **[The use of artificial intelligence in new product development: A systematic literature review, conceptual framework, and future research agenda](https://doi.org/10.1016/j.technovation.2026.103541)** — Vallé et al., 2026, *Technovation*. Systematic review and framework for AI in new product development | <a href="https://doi.org/10.1016/j.technovation.2026.103541"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.technovation.2026.103541-blue.svg" alt="DOI" /></a> |
| **[Future applications of generative large language models: A data-driven case study on ChatGPT](https://doi.org/10.1016/j.technovation.2024.103002)** — Chiarello et al., 2024, *Technovation*. Data-driven analysis of tasks users bring to ChatGPT | <a href="https://doi.org/10.1016/j.technovation.2024.103002"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.technovation.2024.103002-blue.svg" alt="DOI" /></a> |
| **[Natural language processing for innovation search – Reviewing an emerging non-human innovation intermediary](https://doi.org/10.1016/j.technovation.2023.102883)** — Just, 2023, *Technovation*. Reviews NLP as non-human innovation search intermediary | <a href="https://doi.org/10.1016/j.technovation.2023.102883"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.technovation.2023.102883-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>Engineering & Conceptual Design</h3></summary>

*LLMs in the design front end: concept generation, TRIZ, bio-inspired design, requirements.*

| Paper | Link |
|---|---|
| **[LLMs in industrial domains: A systematic review of adaptation techniques and applications from the product lifecycle perspective](https://doi.org/10.1016/j.aei.2026.104655)** — Yu et al., 2026, *Advanced Engineering Informatics*. Systematic review of LLM adaptation across the product lifecycle | <a href="https://doi.org/10.1016/j.aei.2026.104655"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2026.104655-blue.svg" alt="DOI" /></a> |
| **[How does contextual fidelity impact how we think, talk, and act in AI-assisted engineering design?](https://doi.org/10.1016/j.aei.2026.104456)** — Vyas et al., 2026, *Advanced Engineering Informatics*. Studies how contextual fidelity shapes AI-assisted engineering design behaviour | <a href="https://doi.org/10.1016/j.aei.2026.104456"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2026.104456-blue.svg" alt="DOI" /></a> |
| **[Generative AI-enhanced human-AI collaborative conceptual design: A systematic literature review](https://doi.org/10.1016/j.destud.2025.101300)** — Fang et al., 2025, *Design Studies*. Systematic review of GenAI-enhanced human-AI collaborative conceptual design | <a href="https://doi.org/10.1016/j.destud.2025.101300"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.destud.2025.101300-blue.svg" alt="DOI" /></a> |
| **[A survey of large language model-augmented knowledge graphs for advanced complex product design](https://doi.org/10.1016/j.jmsy.2025.04.016)** — Liang et al., 2025, *J. Manufacturing Systems*. Surveys LLM-augmented knowledge graphs for complex product design | <a href="https://doi.org/10.1016/j.jmsy.2025.04.016"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.jmsy.2025.04.016-blue.svg" alt="DOI" /></a> |
| **[Exploring Human and Language Model Alignment in Perceived Design Similarity Using Ordinal Embeddings](https://doi.org/10.1115/1.4069129)** — Keeler et al., 2025, *J. Mechanical Design*. Tests whether language models judge design similarity like humans | <a href="https://doi.org/10.1115/1.4069129"><img src="https://img.shields.io/badge/DOI-10.1115%2F1.4069129-blue.svg" alt="DOI" /></a> |
| **[A survey of emerging applications of large language models for problems in mechanics, product design, and manufacturing](https://doi.org/10.1016/j.aei.2024.103066)** — Mustapha, 2024, *Advanced Engineering Informatics*. Surveys LLM applications in mechanics, product design, and manufacturing | <a href="https://doi.org/10.1016/j.aei.2024.103066"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.aei.2024.103066-blue.svg" alt="DOI" /></a> |
| **[A Method for Synthesizing Ontology-Based Textual Design Datasets: Evaluating the Potential of Large Language Model in Domain-Specific Dataset Generation](https://doi.org/10.1115/1.4067478)** — Qiu & Jin, 2024, *J. Mechanical Design*. LLM synthesizes ontology-based textual datasets for engineering design | <a href="https://doi.org/10.1115/1.4067478"><img src="https://img.shields.io/badge/DOI-10.1115%2F1.4067478-blue.svg" alt="DOI" /></a> |

</details>

<details open>
<summary><h3>Market & Consumer Simulation</h3></summary>

*Generative agents simulating consumers, markets, and economies for management research.*

| Paper | Link |
|---|---|
| **[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)** — Park et al., 2023, *UIST 2023*. <img src="https://img.shields.io/badge/MAS-multi--agent-8A2BE2" alt="MAS" /> 25 LLM agents show emergent social behavior; landmark work | <a href="https://arxiv.org/abs/2304.03442"><img src="https://img.shields.io/badge/arXiv-2304.03442-b31b1b.svg" alt="arXiv" /></a> |

</details>

<details open>
<summary><h3>Scientific Discovery Agents</h3></summary>

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
