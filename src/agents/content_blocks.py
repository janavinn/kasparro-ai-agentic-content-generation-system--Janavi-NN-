def generate_benefits_block(model):
    bullets = []
    for b in model.get("benefits", []):
        text = b
        if "bright" in b.lower():
            text = "Brightening — helps improve skin radiance"
        bullets.append(text)
    return {"title": "Benefits", "bullets": bullets, "summary": " / ".join(model.get("benefits", []))}

def generate_ingredients_block(model):
    items = []
    for ing in model.get("key_ingredients", []):
        if "Vitamin" in ing:
            role = "Active brightening ingredient"
        elif "Hyaluronic" in ing:
            role = "Hydration and plumping"
        else:
            role = "Support ingredient"
        items.append({"name": ing, "role": role})
    return {"title": "Key Ingredients", "items": items}

def generate_usage_block(model):
    return {"title": "How to Use", "instructions": model.get("how_to_use", ""), "notes": "Apply before sunscreen in the morning. Patch-test if unsure."}

def generate_safety_block(model):
    return {"title": "Safety & Side Effects", "text": model.get("side_effects", "") or "No side effects listed. Stop use if irritation occurs."}
