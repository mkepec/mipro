# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research project for developing academic paper proposals for the MIPRO conference (Croatian ICT convention). The repository contains:

- Background information on the researcher's expertise (DevOps, Cloud, AWS, Observability)
- Detailed information about MIPRO conference tracks and sub-conferences
- Historical conference proceedings data (2010-2025)
- Research analysis and paper proposal ideas

## Repository Structure

```
.
├── background/              # Professional background and expertise summary
├── conference-info/         # MIPRO conference details
│   ├── README.md           # List of all conference tracks
│   ├── deadlines.md        # Submission deadlines
│   ├── fees.md             # Conference fees
│   ├── authors-instructions.md
│   └── [Track].md          # Individual conference track details (AIS, CE, CIS, etc.)
├── papers/                 # Historical MIPRO proceedings by year
│   └── [YEAR].md           # Papers from each year (2010-2025)
├── research/
│   ├── analysis/           # Analysis of papers and trends
│   │   ├── curated_papers.md      # Large curated list of relevant papers
│   │   └── phase1_summary.md      # Summary of initial analysis
│   ├── brainstorming/      # Generated paper ideas
│   │   ├── matrix_generated_ideas.md
│   │   ├── student_paper_ideas.md
│   │   └── user_paper_ideas_analysis.md
│   └── proposals/          # Refined research proposals
│       └── phase4_research_questions.md  # Final research proposals
├── temp/                   # Temporary copied text from proceedings
└── mipro_junior_papers.md  # Student paper track papers
```

## Key MIPRO Conference Tracks

The MIPRO conference includes multiple sub-conferences. The most relevant tracks based on the researcher's background are:

- **AIS** - Artificial Intelligence Systems (LLMs, XAI, Machine Learning)
- **CE** - Computers in Education (Cloud education, AWS Academy)
- **CIS** - Cyber and Information Security
- **DC-CPS** - Distributed Computing and Cyber-Physical Systems
- **SSE** - Software and Systems Engineering (DevOps, CI/CD, observability)
- **SIDE** - Smart Industries and Digital Ecosystems
- **EE** - Engineering Education

Full list and details are in `conference-info/README.md`.

## Researcher Background

Marin Kepec is a DevOps Engineer at Infobip and AWS Academy Educator with expertise in:

- Large-scale observability and centralized logging (Azure Data Explorer, Graylog, ELK)
- Infrastructure automation (Terraform, Ansible, Chef)
- Monitoring systems (Prometheus, Grafana)
- Container orchestration (Kubernetes, Docker)
- Cloud platforms (AWS, Azure)
- Education (AWS Academy, Cloud Computing courses)

Key project: Migrated 200+ Graylog clusters to centralized ADX-based logging system.

See `background/README.md` for full details.

## Research Focus Areas

The project focuses on finding intersections between:

1. **Professional expertise**: DevOps, observability, cloud infrastructure, automation
2. **Educational experience**: AWS Academy, teaching cloud computing
3. **MIPRO topics**: AI/ML, cloud-native systems, education, cybersecurity

Current refined proposals (in `research/proposals/phase4_research_questions.md`):

1. **The Cloud-Native Classroom** - IaC framework for containerized lab environments (CE/EE)
2. **The Self-Healing System** - LLM-based root cause analysis for observability (AIS/SSE)
3. **The University Digital Twin** - Digital twin of university IT for cybersecurity education (CE/EE/CIS)

## Working with Historical Papers

Papers are organized by year in `papers/[YEAR].md` files. Each file contains:
- Papers grouped by conference track
- Author names and paper titles
- Data extracted from MIPRO proceedings archives

The `research/analysis/curated_papers.md` file contains a large collection of papers relevant to the researcher's interests.

## Notes for Future Work

- The repository is not a git repository yet
- No programming code or tests - this is a research/documentation project
- Focus is on generating academically rigorous research proposals
- Papers should bridge industry experience with academic contribution
- Target publication in MIPRO 2026 or later conferences
