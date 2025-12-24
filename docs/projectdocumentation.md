# Kasparro — Applied AI Agentic Content Generation System
Author: Janavi (MCA student)

## Problem Statement
I need to build a small, modular agentic system that takes one product JSON (GlowBoost Vitamin C Serum) and automatically generates three machine-readable pages: FAQ, Product Page, and Comparison Page. The system should show clear agent boundaries, reusable content logic blocks, a template engine I design, and output valid JSON files.

## Short Solution Overview (in my words)
I built a simple pipeline of small agents. Each agent does one job and returns a clean output. The main idea: parse the input → make reusable content blocks → assemble pages from templates → export JSON. This proves I can design automation flows and produce structured outputs, not just write text.

## Scopes & Assumptions
- Input: only the provided GlowBoost product data. No external web research or new facts about GlowBoost.
- Comparison uses a fictional Product B (structured fields only).
- Agents are deterministic, stateless functions (input → output).
- Focus is system design and JSON correctness over fancy marketing copy.

## System Design (mandatory, most important)
High-level components:
1. ParserAgent
   - Input: raw product JSON
   - Output: canonical internal model
     { name, concentration, skin_types[], ingredients[], benefits[], usage, side_effects, price }

2. QuestionGeneratorAgent
   - Input: internal model
   - Output: >=15 categorized questions (Informational, Usage, Safety, Purchase, Comparison, Ingredients)

3. ContentBlockAgents (reusable)
   - generate_benefits_block(model) → bullets + short summary
   - extract_usage_block(model) → instructions + notes
   - generate_safety_block(model) → side-effect guidance
   - summarize_ingredients_block(model) → structured ingredient list
   - compare_ingredients_block(modelA, modelB) → diffs for comparison

4. TemplateEngineAgent
   - Template = JSON spec with fields, rules, and block dependencies
   - Renders page JSON by plugging content blocks into the template
   - Ensures consistent keys and machine-readable structure

5. Orchestrator
   - Runs the DAG in order:
     ParserAgent -> QuestionGeneratorAgent
                -> ContentBlockAgents
     TemplateEngineAgent consumes blocks -> writes outputs/*.json
   - No hidden state; orchestrator just wires agents together.

Agent I/O examples:
- ParserAgent.parse(raw) => InternalModel
- QuestionGeneratorAgent.generate(model) => [{id, category, question, answer}]
- TemplateEngine.render(template, blocks) => JSON object

DAG summary:
ParserAgent
  ├→ QuestionGeneratorAgent → FAQ Template → faq.json
  └→ ContentBlockAgents → Product Template → product_page.json
ParserAgent + ProductB → compare_ingredients_block → Comparison Template → comparison_page.json

## Templates (brief)
- FAQ Template: title, product, generated_at, questions[]
- Product Page Template: product, hero_summary, content_blocks (benefits, ingredients, usage, safety, price)
- Comparison Template: left_product, right_product, comparison_table, recommendation

## What I deliver
- docs/projectdocumentation.md (this file)
- outputs/faq.json (>=5 Q&As, >=15 generated questions internal)
- outputs/product_page.json
- outputs/comparison_page.json
- (Optional) small Python runner that demonstrates agents as separate modules

## Diagrams (quick sketch)
- DAG: Parser → {QuestionGenerator, ContentBlocks} → TemplateEngine → JSON outputs
- Each arrow is data-passing (no global state)

Notes: I’m an MCA student — I focused on clarity, modularity, and simple reproducible code. This repo shows I can think in terms of interfaces, small services, and clean outputs.
