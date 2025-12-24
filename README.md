# Kasparro — Agentic Content Generation System
Author: Janavi (MCA Student)

Hi — I’m Janavi. This repo shows a small agent-based pipeline I built for the Kasparro Applied AI assignment. I focused on simple, maintainable code and machine-readable outputs that follow a clear data flow.

What this repo contains
- docs/projectdocumentation.md — problem, design, assumptions, agent boundaries
- outputs/faq.json — FAQ page (machine-readable)
- outputs/product_page.json — Product page (machine-readable)
- outputs/comparison_page.json — Comparison page (GlowBoost vs fictional Product B)

How I worked
- I used a pipeline approach: parse input → generate questions & content blocks → render templates → export JSON.
- Agents are designed as separate, single-responsibility components to keep the system modular and easy to extend.
- I used only the provided GlowBoost product data and a fictional Product B for comparison.

How to submit (what I will do now)
1. Copy this repo URL and paste it into the Google Form: https://forms.gle/c4GasigTr5hutF4H8
2. Reply to Kasparro email with my name and confirmation that I’m attempting the assignment.

If you want to run or extend this later
- I can add a minimal Python runner (src/) that demonstrates the agents and regenerates the outputs.

Thanks — Janavi
