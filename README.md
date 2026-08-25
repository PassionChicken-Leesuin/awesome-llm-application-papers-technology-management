# Awesome LLM Agents for Technology & Innovation Management

> A curated list of papers applying **LLMs, LLM agents, and multi-agent systems (MAS) to downstream tasks in technology & innovation management (TIM)** — patent analytics, technology forecasting, scientometrics, literature screening, R&D and innovation management, and market simulation for management research.

Most agent paper lists collect research *on* agent architectures (memory, planning, coordination). This list collects the complement: research that *uses* agents on real TIM tasks — the papers that end up scattered across *TFSC*, *Scientometrics*, *World Patent Information*, management journals, and application tracks, and therefore rarely appear in ML-centric lists.

**Inclusion criteria**: peer-reviewed papers or public preprints (arXiv/SSRN) where an LLM or LLM-agent system is applied to and evaluated on a TIM task. Tools without papers, blog posts, and pure architecture papers are out of scope.

Maintained with a human-in-the-loop pipeline: a monthly GitHub Action sweeps OpenAlex and Semantic Scholar for candidates and opens a review issue; humans curate (see [CONTRIBUTING.md](CONTRIBUTING.md)). The list itself lives in `data/papers.tsv`; the section below is generated from it.

## Contents

* [Patent & IP Analytics](#patent-classification--screening)
* [Technology Forecasting & Foresight](#technology-forecasting--foresight)
* [Scientometrics & Literature Analysis](#literature-screening--systematic-reviews)
* [R&D & Innovation Management](#idea-generation--creativity-in-innovation)
* [Simulation, Strategy & Discovery](#market--consumer-simulation)
* [Adjacent Landmarks](#adjacent-general-mas-frameworks--finance)
* [Related lists](#related-lists)

## Papers

<!-- AUTOGEN:PAPERS BEGIN (edit data/papers.tsv, not this section) -->

71 papers. Newest first within each section. `MAS` marks explicitly multi-agent systems.

### Patent Classification & Screening

Assigning patents to taxonomies (CPC/IPC or custom schemes) and screening for relevance.

* [Large Language Models for Patent Classification: Strengths, Trade-offs, and the Long Tail Effect](https://arxiv.org/abs/2601.23200) — Emer et al., 2026, arXiv:2601.23200. Compares LLMs vs BERT on CPC; LLMs win on rare subclasses
* [Patent Figure Classification using Large Vision-language Models](https://arxiv.org/abs/2501.12751) — Awale et al., 2025, arXiv:2501.12751. LVLMs classify patent figures; PatFigVQA/PatFigCLS datasets

### Patent Landscaping & Technology Intelligence

Mapping technology domains from patent corpora; competitive and R&D intelligence.

* [Automotive innovation landscaping using LLM](https://arxiv.org/abs/2409.14436) — Gorain et al., 2024, arXiv:2409.14436. Prompt-based LLM patent landscaping for fuel-cell innovation mapping
* [Towards Automated Patent Workflows: AI-Orchestrated Multi-Agent Framework for Intellectual Property Management and Analysis](https://arxiv.org/abs/2409.19006) — Srinivas et al., 2024, OWA Workshop @ NeurIPS 2024. `MAS` PatExpert meta-agent orchestrates end-to-end patent analysis workflows
* [EvoPat: A Multi-LLM-based Patents Summarization and Analysis Agent](https://arxiv.org/abs/2412.18100) — Wang et al., 2024, arXiv:2412.18100. `MAS` Multi-LLM agent summarizes patents and tracks innovation evolution

### Prior-Art Search & Patent Retrieval

Finding and matching prior art; patent-specific embeddings and retrieval.

* [Enhancing the Patent Matching Capability of Large Language Models via the Memory Graph](https://arxiv.org/abs/2504.14845) — Xiong et al., 2025, SIGIR 2025. MemGraph entity/ontology memory boosts LLM patent matching
* [PaECTER: Patent-level Representation Learning using Citation-informed Transformers](https://arxiv.org/abs/2402.19411) — Ghosh et al., 2024, arXiv:2402.19411. Citation-informed patent embeddings for prior-art similarity search
* [Large Language Model Informed Patent Image Retrieval](https://arxiv.org/abs/2404.19360) — Lo et al., 2024, PatentSemTech @ SIGIR 2024. LLM-generated captions improve patent drawing retrieval

### Patent Drafting & Claim Generation

Generating and refining patent text: claims, abstracts, full specifications.

* [Can Large Language Models Generate High-quality Patent Claims?](https://arxiv.org/abs/2406.19465) — Jiang et al., 2025, Findings of NAACL 2025. Evaluates claim generation quality from descriptions across LLMs
* [PAP2PAT: Benchmarking Outline-Guided Long-Text Patent Generation with Patent-Paper Pairs](https://arxiv.org/abs/2410.07009) — Knappich et al., 2025, Findings of ACL 2025. Paper-to-patent drafting via chunk-based outline-guided generation
* [Large Language Model for Patent Concept Generation](https://arxiv.org/abs/2409.00092) — Ren et al., 2025, Advanced Engineering Informatics. Knowledge fine-tuned PatentGPT for inventive patent concept generation
* [PatentWriter: A Benchmarking Study for Patent Drafting with LLMs](https://arxiv.org/abs/2507.22387) — Shomee et al., 2025, arXiv:2507.22387. Benchmarks LLM patent abstract drafting from claims
* [ClaimBrush: A Novel Framework for Automated Patent Claim Refinement Based on Large Language Models](https://arxiv.org/abs/2410.05575) — Kawano et al., 2024, arXiv:2410.05575. Rewrites claims via fine-tuned LLM with preference optimization
* [AutoPatent: A Multi-Agent Framework for Automatic Patent Generation](https://arxiv.org/abs/2412.09796) — Wang et al., 2024, arXiv:2412.09796. `MAS` Planner/writer/examiner agents draft full patents from drafts

### Patent Quality, Novelty & Valuation

Assessing novelty, predicting examiner outcomes, automated quality assurance.

* [Towards Automated Quality Assurance of Patent Specifications: A Multi-Dimensional LLM Framework](https://arxiv.org/abs/2510.25402) — Chai et al., 2025, arXiv:2510.25402. Industry LLM framework auto-checking patent specification quality
* [Can AI Examine Novelty of Patents?: Novelty Evaluation Based on the Correspondence between Patent Claim and Prior Art](https://arxiv.org/abs/2502.06316) — Ikoma et al., 2025, arXiv:2502.06316. LLM novelty assessment aligning claims with prior art
* [PatentEdits: Framing Patent Novelty as Textual Entailment](https://arxiv.org/abs/2411.13477) — Lee et al., 2024, arXiv:2411.13477. Predicts examiner-driven claim edits as an entailment task

### IP Benchmarks & Evaluation

Benchmarks and metrics for LLM performance on intellectual-property tasks.

* [Towards Better Evaluation for Generated Patent Claims](https://arxiv.org/abs/2505.11095) — Jiang et al., 2025, arXiv:2505.11095. Patent-CE benchmark and PatClaimEval for claim evaluation
* [IPBench: Benchmarking the Knowledge of Large Language Models in Intellectual Property](https://arxiv.org/abs/2504.15524) — Wang et al., 2025, arXiv:2504.15524. Comprehensive IP-knowledge benchmark; 10 tasks, 20 IP scenarios
* [PatentScore: Multi-dimensional Evaluation of LLM-Generated Patent Claims](https://arxiv.org/abs/2505.19345) — Yoo et al., 2025, arXiv:2505.19345. Legal-structure-aware metric scoring LLM-generated claims
* [MoZIP: A Multilingual Benchmark to Evaluate Large Language Models in Intellectual Property](https://arxiv.org/abs/2402.16389) — Ni et al., 2024, LREC-COLING 2024. Multilingual IP quiz/QA/patent-matching benchmark plus MoZi model
* [IPEval: A Bilingual Intellectual Property Agency Consultation Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2406.12386) — Wang et al., 2024, arXiv:2406.12386. Bilingual patent-agent exam benchmark for LLM IP competence
* [PatentEval: Understanding Errors in Patent Generation](https://arxiv.org/abs/2406.06589) — Zuo et al., 2024, NAACL 2024. Error typology and human-annotated benchmark for patent generation

### IP Domain Models & Surveys

Domain-adapted models and surveys of NLP/LLM methods in the patent domain.

* [Natural Language Processing in the Patent Domain: A Survey](https://arxiv.org/abs/2403.04105) — Jiang et al., 2025, Artificial Intelligence Review. Survey of LLM/NLP patent tasks, datasets, and methods
* [PatentGPT: A Large Language Model for Intellectual Property](https://arxiv.org/abs/2404.18255) — Bai et al., 2024, arXiv:2404.18255. IP-domain-trained LLM; beats GPT-4 on China patent agent exam

### Technology Forecasting & Foresight

Emerging-technology detection, weak signals, opportunity discovery, trend prediction.

* [Anticipating Innovation Using Large Language Models](https://arxiv.org/abs/2605.04875) — Fenoaltea et al., 2026, arXiv:2605.04875. LLMs anticipate future innovation and technology emergence
* [Tuning into whispered frequencies: Harnessing Large Language Models to detect Weak Signals in complex socio-technical systems](https://doi.org/10.1016/j.engappai.2026.114738) — Lombardi et al., 2026, Engineering Applications of Artificial Intelligence. LLM pipeline detects foresight weak signals in socio-technical texts
* [DiTTO-LLM: Framework for Discovering Topic-based Technology Opportunities via Large Language Model](https://arxiv.org/abs/2509.09724) — Kim et al., 2025, arXiv:2509.09724. LLM tracks patent topic evolution to discover technology opportunities
* [Predicting New Research Directions in Materials Science using Large Language Models and Concept Graphs](https://arxiv.org/abs/2506.16824) — Marwitz et al., 2025, arXiv:2506.16824. LLM concept extraction plus graph model predicts unexplored combinations
* [WISDOM: An AI-powered framework for emerging research detection using weak signal analysis and advanced topic modeling](https://arxiv.org/abs/2409.15340) — Ebadi et al., 2024, arXiv:2409.15340. Weak-signal analysis plus topic modeling detects emerging research themes
* [Forecasting high-impact research topics via machine learning on evolving knowledge graphs](https://arxiv.org/abs/2402.08640) — Gu et al., 2024, arXiv:2402.08640. Evolving knowledge graph forecasts high-impact topics; LLM-benchmarked

### Literature Screening & Systematic Reviews

LLMs as screeners in systematic reviews — structurally the same include/exclude task as valid-patent selection.

* [The Promise and Challenges of Using LLMs to Accelerate the Screening Process of Systematic Reviews](https://arxiv.org/abs/2404.15667) — Huotala et al., 2024, arXiv:2404.15667. GPT-3.5/4 vs humans on title-abstract screening; prompt strategies compared
* [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data](https://doi.org/10.1002/jrsm.1715) — Khraisha et al., 2024, Research Synthesis Methods. GPT-4 screening and data extraction across languages and literature types
* [High-performance automated abstract screening with large language model ensembles](https://arxiv.org/abs/2411.02451) — Sanghera et al., 2024, arXiv:2411.02451. LLM ensembles match/exceed human accuracy on Cochrane review screening
* [Screening articles for systematic reviews with ChatGPT](https://doi.org/10.1016/j.cola.2024.101287) — Syriani et al., 2024, Journal of Computer Languages. Large-scale evaluation of ChatGPT as a systematic review screener

### Novelty & Impact Prediction of Research

Scoring the novelty of papers and predicting their scientific impact.

* [Are Large Language Models able to Predict Highly Cited Papers? Evidence from Statistical Publications](https://arxiv.org/abs/2601.13627) — Ye et al., 2026, arXiv:2601.13627. Tests LLM citation-impact prediction on statistics publications
* [Automated Novelty Evaluation of Academic Paper: A Collaborative Approach Integrating Human and Large Language Model Knowledge](https://doi.org/10.1002/asi.70005) — Wu et al., 2025, JASIST. Human-LLM knowledge fusion predicts method novelty of papers
* [Evaluating and Enhancing Large Language Models for Novelty Assessment in Scholarly Publications](https://arxiv.org/abs/2409.16605) — Lin et al., 2024, AISD @ ACL 2025. SchNovel benchmark and RAG-Novelty for scholarly novelty assessment
* [From Words to Worth: Newborn Article Impact Prediction with LLM](https://arxiv.org/abs/2408.03934) — Zhao et al., 2024, arXiv:2408.03934. Fine-tuned LLM predicts article impact from title and abstract

### Scientometrics & Science of Science

Agentic and LLM-based tools for bibliometric and science-of-science analysis.

* [AI-Augmented Bibliometric Framework: A Paradigm Shift with Agentic AI for Dynamic, Snippet-Based Research Analysis](https://arxiv.org/abs/2511.21745) — Bara et al., 2025, arXiv:2511.21745. `MAS` Agentic AI replaces static bibliometric keyword analysis
* [The Empowerment of Science of Science by Large Language Models: New Tools and Methods](https://arxiv.org/abs/2511.15370) — Liang et al., 2025, arXiv:2511.15370. Survey of LLM tools for scientometrics and research front detection
* [SciSciGPT: Advancing Human-AI Collaboration in the Science of Science](https://arxiv.org/abs/2504.05559) — Shao et al., 2025, arXiv:2504.05559. `MAS` Specialist agents automate science-of-science analytics workflows

### Automated Survey Writing & Paper Search

Agents that search, synthesize, and write literature reviews.

* [PaSa: An LLM Agent for Comprehensive Academic Paper Search](https://arxiv.org/abs/2501.10120) — He et al., 2025, arXiv:2501.10120. RL-trained LLM agent for comprehensive scholarly paper retrieval
* [Agentic AutoSurvey: Let LLMs Survey LLMs](https://arxiv.org/abs/2509.18661) — Liu et al., 2025, arXiv:2509.18661. `MAS` Four agents search, cluster, write, and evaluate literature surveys
* [SurveyG: A Multi-Agent LLM Framework with Hierarchical Citation Graph for Automated Survey Generation](https://arxiv.org/abs/2510.07733) — Nguyen et al., 2025, arXiv:2510.07733. `MAS` Citation-graph-guided multi-agent survey generation
* [Accelerating Scientific Research Through a Multi-LLM Framework](https://arxiv.org/abs/2502.07960) — Ramirez-Medina et al., 2025, arXiv:2502.07960. `MAS` Four-agent pipeline retrieves, filters, and synthesizes literature
* [AutoSurvey: Large Language Models Can Automatically Write Surveys](https://arxiv.org/abs/2406.10252) — Wang et al., 2024, NeurIPS 2024. End-to-end LLM pipeline for automatic literature survey writing

### Idea Generation & Creativity in Innovation

LLMs vs humans/crowds in generating product and research ideas.

* [The Role of Artificial Intelligence in the Ideation Process](https://doi.org/10.1111/jpim.12791) — Pescher et al., 2025, Journal of Product Innovation Management. AI's role across ideation stages in product innovation
* [The Crowdless Future? Generative AI and Creative Problem-Solving](https://doi.org/10.1287/orsc.2023.18430) — Boussioux et al., 2024, Organization Science. GPT-4 solutions vs crowdsourced solutions in an innovation challenge
* [Generative AI enhances individual creativity but reduces the collective diversity of novel content](https://doi.org/10.1126/sciadv.adn5290) — Doshi et al., 2024, Science Advances. LLM ideas boost individual creativity, shrink collective diversity
* [Comparing the Ideation Quality of Humans With Generative Artificial Intelligence](https://ieeexplore.ieee.org/document/10398283) — Joosten et al., 2024, IEEE Engineering Management Review. Human vs GPT-4 ideation quality comparison for innovation management
* [Prompting Diverse Ideas: Increasing AI Idea Variance](https://arxiv.org/abs/2402.01727) — Meincke et al., 2024, arXiv:2402.01727. Prompt strategies to raise diversity of LLM-generated product ideas
* [Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers](https://arxiv.org/abs/2409.04109) — Si et al., 2024, ICLR 2025. LLM-generated research ideas judged more novel than experts'
* [Ideas are Dimes a Dozen: Large Language Models for Idea Generation in Innovation](https://doi.org/10.2139/ssrn.4526071) — Girotra et al., 2023, SSRN Working Paper. GPT-4 vs students: LLM ideas dominate top-quality product ideas

### New Product Development & R&D Management

LLM augmentation of NPD teams and product-concept evaluation.

* [An Interactive Multi-Agent System for Evaluation of New Product Concepts](https://arxiv.org/abs/2603.05980) — Xuan et al., 2026, arXiv:2603.05980. `MAS` Specialized LLM agents deliberate to evaluate product concepts
* [Augmenting human innovation teams with artificial intelligence: Exploring transformer-based language models](https://doi.org/10.1111/jpim.12656) — Bouschery et al., 2023, Journal of Product Innovation Management. GPT-3 augmenting NPD teams; AI-augmented double diamond framework

### Market & Consumer Simulation

Generative agents simulating consumers, markets, and economies for management research.

* [EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities](https://arxiv.org/abs/2310.10436) — Li et al., 2024, ACL 2024. `MAS` LLM agents reproduce macroeconomic dynamics
* [LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals](https://arxiv.org/abs/2411.10109) — Park et al., 2024, arXiv:2411.10109. Interview-grounded generative agents simulate 1,000 real individuals
* [CompeteAI: Understanding the Competition Dynamics of Large Language Model-based Agents](https://arxiv.org/abs/2310.17512) — Zhao et al., 2024, ICML 2024. `MAS` Competing restaurant agents simulate market competition dynamics
* [Using LLMs for Market Research](https://doi.org/10.2139/ssrn.4395751) — Brand et al., 2023, SSRN / HBS Working Paper. GPT elicits realistic consumer preferences and willingness-to-pay
* [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — Park et al., 2023, UIST 2023. `MAS` 25 LLM agents show emergent social behavior; landmark work

### Strategy & Decision-Making

LLMs in strategic decision-making and entrepreneurship.

* [Artificial Intelligence and Strategic Decision-Making: Evidence from Entrepreneurs and Investors](https://doi.org/10.1287/stsc.2024.0190) — Csaszar et al., 2024, Strategy Science. GPT-4 business strategies rival human founders per investor evaluations

### Scientific Discovery Agents

Autonomous research agents with direct relevance to R&D processes.

* [Towards an AI co-scientist](https://arxiv.org/abs/2502.18864) — Gottweis et al., 2025, arXiv:2502.18864. `MAS` Gemini multi-agent system generates validated research hypotheses
* [The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://doi.org/10.1038/s41586-025-09442-9) — Swanson et al., 2025, Nature. `MAS` AI researcher agents run meetings, design validated nanobodies
* [Augmenting large language models with chemistry tools](https://doi.org/10.1038/s42256-024-00832-8) — Bran et al., 2024, Nature Machine Intelligence. ChemCrow: LLM agent with 18 tools for synthesis and discovery
* [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) — Lu et al., 2024, arXiv:2408.06292. End-to-end autonomous research agent writes papers for ~$15
* [Autonomous chemical research with large language models](https://doi.org/10.1038/s41586-023-06792-0) — Boiko et al., 2023, Nature. Coscientist agent autonomously plans and executes chemistry experiments

### Adjacent: General MAS Frameworks & Finance

Landmark frameworks and finance MAS often cited by TIM applications.

* [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) — Hong et al., 2024, ICLR 2024. `MAS` SOP-encoded agent roles simulate a software company workflow
* [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138) — Xiao et al., 2024, arXiv:2412.20138. `MAS` Analyst/trader/risk agents emulate a trading firm; landmark
* [TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://arxiv.org/abs/2412.14161) — Xu et al., 2024, arXiv:2412.14161. `MAS` Benchmark: agents perform professional tasks in a simulated company
* [FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743) — Yu et al., 2023, arXiv:2311.13743. LLM trading agent with layered memory outperforms benchmarks

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
