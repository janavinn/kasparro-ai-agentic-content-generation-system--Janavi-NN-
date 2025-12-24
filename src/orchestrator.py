import os
import json
from src.agents.parser_agent import ParserAgent
from src.agents.question_generator import QuestionGeneratorAgent
from src.agents.content_blocks import generate_benefits_block, generate_ingredients_block, generate_usage_block, generate_safety_block
from src.agents.template_engine import TemplateEngineAgent

class Orchestrator:
    def __init__(self, input_path="src/input/product.json", out_dir="outputs"):
        self.input_path = input_path
        self.out_dir = out_dir
        os.makedirs(self.out_dir, exist_ok=True)
        self.parser = ParserAgent()
        self.qgen = QuestionGeneratorAgent()
        self.engine = TemplateEngineAgent()

    def load_input(self):
        with open(self.input_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def create_fictional_product_b(self, model):
        return {
            "name": "RadiantPure Vitamin C Serum (Fictional Product B)",
            "concentration": "12% Vitamin C",
            "key_ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": ["Brightening", "Hydration"],
            "price": {"currency": "INR", "amount": 749, "display": "₹749"},
            "skin_types": ["Dry", "Normal"]
        }

    def compare_rows(self, left_model, right_model):
        rows = []
        rows.append({"field": "Concentration", "left": left_model.get("concentration"), "right": right_model.get("concentration")})
        rows.append({"field": "Key Ingredients", "left": left_model.get("key_ingredients"), "right": right_model.get("key_ingredients")})
        rows.append({"field": "Benefits", "left": left_model.get("benefits"), "right": right_model.get("benefits")})
        rows.append({"field": "Suitable Skin Types", "left": left_model.get("skin_types"), "right": right_model.get("skin_types")})
        rows.append({"field": "Price", "left": left_model.get("price", {}).get("display"), "right": right_model.get("price", {}).get("display")})
        return rows

    def run(self):
        raw = self.load_input()
        model = self.parser.parse(raw)
        # Generate >=15 questions
        questions = self.qgen.generate(model, min_questions=15)
        # Content blocks
        benefits = generate_benefits_block(model)
        ingredients = generate_ingredients_block(model)
        usage = generate_usage_block(model)
        safety = generate_safety_block(model)
        blocks = {
            "benefits_block": benefits,
            "ingredients_block": ingredients,
            "usage_block": usage,
            "safety_block": safety,
            "purchase_block": {"title": "Price", "text": model.get("price", {}).get("display")}
        }
        # Render pages
        faq_json = self.engine.render_faq(model.get("name"), questions)
        product_json = self.engine.render_product_page(model, blocks)
        product_b = self.create_fictional_product_b(model)
        comparison_rows = self.compare_rows(model, product_b)
        recommendation = f"{model.get('name')} offers {model.get('concentration')} and hydration support at {model.get('price', {}).get('display')}. Product B has higher concentration but is pricier."
        comparison_json = self.engine.render_comparison(model, product_b, comparison_rows, recommendation)
        # Write outputs
        with open(os.path.join(self.out_dir, "faq.json"), "w", encoding="utf-8") as f:
            json.dump(faq_json, f, indent=2, ensure_ascii=False)
        with open(os.path.join(self.out_dir, "product_page.json"), "w", encoding="utf-8") as f:
            json.dump(product_json, f, indent=2, ensure_ascii=False)
        with open(os.path.join(self.out_dir, "comparison_page.json"), "w", encoding="utf-8") as f:
            json.dump(comparison_json, f, indent=2, ensure_ascii=False)
        print("Wrote outputs to", self.out_dir)
