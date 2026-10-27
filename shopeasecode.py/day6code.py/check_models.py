"""check_models.py — checks for the ShopEase classes.
Run: python check_models.py
"""

from models import Product, DigitalProduct, Customer, Cart, Order


# Create products
mouse = Product(1, "Mouse", 599, "Accessories", 5)
ebook = DigitalProduct(2, "eBook", 499, "eBooks", "https://example.com")


# Check GST calculations and inheritance
assert mouse.price_with_gst() == 706.82
assert ebook.price_with_gst() == 499.0  # Digital: no GST
assert isinstance(ebook, Product)


# Test cart operations
cart = Cart()
cart.add(mouse, 2)
cart.add(ebook, 1)

assert len(cart) == 3
assert mouse.stock == 3


# Check insufficient stock
try:
    cart.add(mouse, 10)
    assert False, "Should have raised ValueError"
except ValueError:
    pass


# Check negative price validation
try:
    Product(3, "Bad", -1, "X")
    assert False, "Negative price should fail"
except ValueError:
    pass


# Test order calculations
order = Order(Customer("priya", "PRIYA@MAIL.COM"), cart)

assert order.subtotal == 1697.0
assert order.rate == 0.05

assert round(order.total, 2) == round(
    1697 * 0.95 + 1198 * 0.95 * 0.18,
    2
)


# Test discount rate
assert Order.discount_rate(5001) == 0.10


# Success message
print("All model checks passed.")