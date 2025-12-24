import re

class ParserAgent:
    """
    Normalize raw product JSON -> internal model dict
    """
    def parse(self, raw: dict) -> dict:
        model = {}
        model["name"] = raw.get("name", "").strip()
        model["concentration"] = raw.get("concentration", "").strip()
        # normalize skin types into list
        skin = raw.get("skin_type", "") or raw.get("skin_types", "")
        if isinstance(skin, list):
            model["skin_types"] = skin
        else:
            model["skin_types"] = [s.strip() for s in str(skin).split(",")] if skin else []
        model["key_ingredients"] = raw.get("key_ingredients", [])
        model["benefits"] = raw.get("benefits", [])
        model["how_to_use"] = raw.get("how_to_use", "")
        model["side_effects"] = raw.get("side_effects", "")
        # price normalization: extract numeric amount if possible
        price_raw = str(raw.get("price", ""))
        digits = re.sub(r"[^\d]", "", price_raw)
        try:
            amount = int(digits) if digits else None
        except:
            amount = None
        model["price"] = {"display": price_raw, "amount": amount, "currency": "INR"}
        return model
