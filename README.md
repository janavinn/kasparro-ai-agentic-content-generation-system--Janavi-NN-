# Kasparro — Agentic Content Generation System
Author: Janavi N N (MCA Student)

Hi — I’m Janavi. This repository implements a modular, agent-based content generation pipeline built for the Kasparro Applied AI assignment. The focus is on system design, agent boundaries, orchestration flow, and clean, machine-readable outputs — not on UI or prompt engineering.

## What this repo contains
- docs/projectdocumentation.md — problem statement, system design, assumptions, and agent responsibilities
- outputs/faq.json — generated FAQ page (machine-readable)
- outputs/product_page.json — generated product description page (machine-readable)
- outputs/comparison_page.json — generated comparison page (GlowBoost vs fictional Product B)

## System approach
- The system follows a pipeline flow:
  parse input → generate questions & content blocks → apply templates → export structured JSON
- Each agent has a single responsibility and well-defined input/output.
- A central orchestrator coordinates agent execution.
- Content logic is implemented as reusable transformation blocks.
- No external data or research is used beyond the provided product dataset.

## Notes
- This is a systems design and automation project, not a UI or prompting exercise.
- The architecture is designed to be easily extensible with additional agents or templates.
