"""
Run this script to regenerate outputs/faq.json, outputs/product_page.json, outputs/comparison_page.json.

To run locally:
1. Python 3.8+
2. From repo root: python -m src.run_pipeline
(If using modules, ensure package imports work. Alternatively run this file directly.)
"""
from src.orchestrator import Orchestrator

def main():
    orch = Orchestrator(input_path="src/input/product.json", out_dir="outputs")
    orch.run()

if __name__ == "__main__":
    main()