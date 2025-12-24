import json

class ParserAgent:
    """
    Single responsibility: normalize raw product JSON -> internal model dict
    """
    def parse(self, raw: dict) -> dict:
        model = {}
        model["name"] = raw.get("name", "").strip()
        model["concentration"] = raw.get("concentration", "").strip()
        # normalize skin types into list
        skin = raw.get("skin_type", "")
        model["skin_types"] = [s.strip() for s in skin.split(",")] if skin else []
        model["key_ingredients"] = raw.get("key_ingredients", [])
        model["benefits"] = raw.get("benefits", [])
        model["how_to_use"] = raw.get("how_to_use", "")
        model["side_effects"] = raw.get("side_effects", "")
        # price normalization: try extract numbers
        price_raw = raw.get("price", "")
        amount = None
        try:
            amount = int(''.join(ch for ch in price_raw if ch.isdigit()))
        except:
            amount = None
        model["price"] = {"display": price_raw, "amount": amount, "currency": "INR"}
        return model