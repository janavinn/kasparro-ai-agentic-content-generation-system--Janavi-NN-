import datetime
import json

class TemplateEngineAgent:
    """
    Render simple JSON templates by composing content blocks and model data.
    """
    def render_faq(self, product_name, questions):
        return {
            "page_type": "faq",
            "product": product_name,
            "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
            "questions": questions
        }

    def render_product_page(self, model, blocks):
        hero = {
            "short": f"{model.get('concentration', '')} serum — {', '.join(model.get('benefits', []))}.",
            "highlights": [
                model.get("concentration", ""),
                ", ".join(model.get("key_ingredients", [])),
                "Suitable for " + ", ".join(model.get("skin_types", [])),
                "Price: " + model.get("price", {}).get("display", "")
            ]
        }
        return {"page_type": "product_page", "product": model, "hero_summary": hero, "content_blocks": blocks}

    def render_comparison(self, left, right, comparison_rows, recommendation):
        return {"page_type": "comparison_page", "left_product": left, "right_product": right, "comparison_table": {"rows": comparison_rows}, "summary_recommendation": {"tl;dr": recommendation}}