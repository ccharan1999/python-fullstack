from cart import cart_lines, item_count
GST_RATE = 0.18
def discount_rate(subtotal):
    if subtotal > 5000:
        return 0.10
    if subtotal > 1000:
        return 0.05
    return 0.0
def calculate_bill(cart, gst_rate=GST_RATE):
    subtotal = sum(t for _, _, t in cart_lines(cart))
    rate = discount_rate(subtotal)
    discount = subtotal * rate
    gst = (subtotal - discount) * gst_rate
    return {
        "items": item_count(cart),
        "subtotal": subtotal,
        "rate": rate,
        "discount": discount,
        "gst": gst,
        "total": subtotal - discount + gst,
    }
    
def print_bill(bill):
    print(f"{'Items':<18}{bill['items']}")
    print(f"{'Subtotal':<18}Rs "
          f"{bill['subtotal']:>10,.2f}")
    # discount, GST and TOTAL follow
