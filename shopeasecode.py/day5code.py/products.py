PRODUCTS = [
    {"id": 101, "name": "Wireless Mouse", "price": 599.0,
     "category": "Accessories", "stock": 10},
    # ... 4 more products
]
_BY_ID = {p["id"]: p for p in PRODUCTS}
def find_product(product_id):
    """Return the product dict, or None."""
    return _BY_ID.get(product_id)
def search(keyword):
    keyword = keyword.strip().lower()
    return [p for p in PRODUCTS if keyword in p["name"].lower()]

def categories():
    return sorted(
        {p["category"] for p in PRODUCTS})
def by_category(category):
    return [p for p in PRODUCTS
            if p["category"] == category]
def print_table(items): ...
