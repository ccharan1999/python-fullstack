products = [
    {"id": 101, "name": "Wireless Mouse",
     "price": 599.0, "category": "Accessories",
     "stock": 10},
    # ... 4 more products
]
by_id = {p["id"]: p for p in products}
cart = {}   # product id -> quantity

pid, qty = int(pid), int(qty)
product = by_id.get(pid)   # None if unknown
if product is None:
    print("Unknown product ID.")
elif qty > product["stock"]:
    print(f"Only {product['stock']} left in stock.")
else:
    cart[pid] = cart.get(pid, 0) + qty
    product["stock"] -= qty
    
categories = sorted({p["category"] for p in products})
wanted = input("Category: ").strip().title()
if wanted in categories:
    for p in products:
        if p["category"] == wanted:
            print(ROW.format(**p))
            
found = [p for p in products
         if keyword in p["name"].lower()]
subtotal = sum(
    by_id[pid]["price"] * qty
    for pid, qty in cart.items())
