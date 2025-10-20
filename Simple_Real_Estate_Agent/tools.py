from agents import function_tool

properties = [
    {"id": 1, "city": "Karachi", "type": "House", "listing": "sale", "price": "15,000,000 PKR"},
    {"id": 2, "city": "Lahore", "type": "Apartment", "listing": "rent", "price": "45,000 PKR/month"},
    {"id": 3, "city": "Islamabad", "type": "Villa", "listing": "sale", "price": "25,000,000 PKR"},
    {"id": 4, "city": "Karachi", "type": "Apartment", "listing": "rent", "price": "60,000 PKR/month"},
]

@function_tool
def list_properties(city: str = None, listing: str = None):
    results = properties

    if city:
        result = [p for p in results if p["city"].lower() == city.lower()]
    if listing:
        result = [p for p in results if p["listing"].lower() == listing.lower()]

    if not result:
        return "no matching properties found"

    summary = [f"{p['id']}: {p['type']} in {p['city']} ({p['listing']}) - {p['price']}" for p in results]
    return "\n".join(summary)

@function_tool
def get_property(id: int):
    """Get full details of a property by id"""
    for p in properties:
        if p["id"] == id:
            return f"Property {p['id']}: {p['type']} in {p['city']} for {p['listing']} — Price: {p['price']}"
