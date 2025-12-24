def generate_benefits_block(model):
    bullets = []
    for b in model.get("benefits", []):
        if "bright" in b.lower():
            bullets.append("Brightening — helps improve skin radiance")
        else:
            bullets.append(b)
    return {"title": "Benefits", "bullets": bullets, "summary": " / ".join(model.get("benefits", []))}

def generate_ingredients_block(model):
    items = []
    for ing in model.get("key_ingredients", []):
        role = "Active ingredient" if "Vitamin" in ing else "Support ingredient"
        if "Hyaluronic" in ing:
            role = "Hydration and plumping"
        items.append({"name": ing, "role": role})
    return {"title": "Key Ingredients", "items": items}

def generate_usage_block(model):
    return {"title": "How to Use", "instructions": model.get("how_to_use", ""), "notes": "Apply before sunscreen in the morning."}

def generate_safety_block(model):
    return {"title": "Safety & Side Effects", "text": model.get("side_effects", "") or "No side effects listed."}