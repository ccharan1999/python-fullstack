from products import find_product
def add_item(cart, product_id, qty):
    product = find_product(product_id)
    if product is None:
        return False, "Unknown product ID."
    if qty <= 0:
        return False, "Quantity must be at least 1."
    if qty > product["stock"]:
        return False, f"Only {product['stock']} left."
    cart[product_id] = cart.get(product_id, 0) + qty
    product["stock"] -= qty
    return True, f"Added {qty} x {product['name']}"
def remove_item(cart, product_id):
    qty = cart.pop(product_id, 0)
    if qty:
        find_product(product_id)["stock"] += qty
    return qty
def cart_lines(cart):
    lines = []
    for pid, qty in cart.items():
        p = find_product(pid)
        total = p["price"] * qty
        lines.append((p["name"], qty, total))
    return lines
def item_count(cart):
    return sum(cart.values())