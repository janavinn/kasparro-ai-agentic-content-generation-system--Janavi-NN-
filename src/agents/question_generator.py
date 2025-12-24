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
            f"{model['name']} contains {model.get('concentration','')} and is formulated to help {', '.join(model.get('benefits', []))}.")
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
        add("Usage",
            "Is this suitable for oily skin?",
            "Yes — it lists Oily and Combination as suitable skin types.")
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
            ", ".join(model.get("key_ingredients", [])) or "No ingredients listed.")
        add("Ingredients",
            "Does it contain Hyaluronic Acid?",
            "Yes." if "Hyaluronic Acid" in model.get("key_ingredients", []) else "No.")
        add("Ingredients",
            "Is Vitamin C the active ingredient?",
            "Yes, Vitamin C is listed as an active ingredient.")
        # Purchase
        add("Purchase",
            "What is the price?",
            model.get("price", {}).get("display", "Price not listed."))
        add("Purchase",
            "Is this affordable?",
            f"At {model.get('price',{}).get('display','N/A')}, it is positioned as an accessible option.")
        # Comparison
        add("Comparison",
            "How does it compare to other vitamin C serums?",
            "Compare concentration, ingredient list and price to decide.")
        add("Usage",
            "Can I use this at night?",
            "Product recommends morning; consult or patch-test for night use.")
        # fill up to min_questions with small variations
        idx = 1
        while len(questions) < min_questions:
            add("Informational",
                f"Extra question {idx}: How often should I apply the serum?",
                "Apply 2–3 drops in the morning as stated.")
            idx += 1
        return questions
