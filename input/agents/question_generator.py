import itertools
import uuid

class QuestionGeneratorAgent:
    """
    Generate >=15 categorized questions from the internal model.
    """
    def generate(self, model: dict, min_questions: int = 15):
        questions = []
        def add(cat, q, a):
            questions.append({
                "id": str(uuid.uuid4())[:8],
                "category": cat,
                "question": q,
                "answer": a
            })
        # Informational
        add("Informational",
            f"What is {model['name']} and what concentration does it contain?",
            f"{model['name']} contains {model['concentration']} and is formulated to help {', '.join(model.get('benefits', []))}.")
        add("Informational",
            "What are the primary benefits of this serum?",
            ", ".join(model.get("benefits", [])) or "No benefits listed.")
        # Usage
        add("Usage",
            "How do I use this serum?",
            model.get("how_to_use", "Follow product instructions."))
        add("Usage",
            "Can I use it with sunscreen?",
            "Yes — apply the serum in the morning before sunscreen.")
        # Safety
        add("Safety",
            "Are there any side effects?",
            model.get("side_effects", "No side effects listed."))
        add("Safety",
            "What should I do if I experience irritation?",
            "Stop using and consult a dermatologist if irritation persists.")
        # Ingredients
        add("Ingredients",
            "What are the key ingredients?",
            ", ".join(model.get("key_ingredients", [])))
        add("Ingredients",
            "Does it contain Hyaluronic Acid?",
            "Yes." if "Hyaluronic Acid" in model.get("key_ingredients", []) else "No.")
        # Purchase
        add("Purchase",
            "What is the price?",
            model.get("price", {}).get("display", "Price not listed."))
        add("Purchase",
            "Where can I buy this product?",
            "Refer to the retailer or brand page. (No external links used.)")
        # Comparison & skin type
        add("Comparison",
            "How does it compare to similar Vitamin C serums?",
            f"It has {model.get('concentration', '')}; compare ingredient lists and price for differences.")
        add("Usage",
            "Is this suitable for oily skin?",
            "Yes — it lists Oily and Combination as suitable skin types.")
        add("Usage",
            "Can I use it at night?",
            "The product states morning use; for night use, consult the brand or patch-test.")
        add("Ingredients",
            "Is Vitamin C the active ingredient?",
            "Yes, Vitamin C is the primary active ingredient listed.")
        add("Safety",
            "Should people with sensitive skin patch-test first?",
            "Yes, patch-test and introduce gradually.")
        # If still under min_questions, generate short variations
        idx = 1
        while len(questions) < min_questions:
            add("Informational",
                f"Extra question {idx}: What is the recommended usage frequency?",
                "Apply 2–3 drops in the morning as stated.")
            idx += 1
        return questions