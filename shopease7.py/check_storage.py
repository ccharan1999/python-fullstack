"""check_storage.py — checks for saving and loading. Run: python check_storage.py"""
import json
import tempfile
from pathlib import Path
 
import storage
from errors import OutOfStockError, InvalidQuantityError
from models import Product, Customer, Cart, Order
 
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    products_file = tmp / "products.json"
    orders_file = tmp / "orders.json"
 
    # Missing file -> default products
    products = storage.load_products(products_file)
    assert len(products) == 6
 
    # Save and load keeps the data, including the digital product
    products[0].reduce_stock(4)
    storage.save_products(products, products_file)
    again = storage.load_products(products_file)
    assert again[0].stock == products[0].stock == 6
    assert again[-1].to_dict()["type"] == "digital"
 
    # Damaged file -> warning and defaults instead of a crash
    products_file.write_text("{ not json")
    assert len(storage.load_products(products_file)) == 6
 
    # Orders append to the file and export to CSV
    cart = Cart()
    cart.add(Product(1, "Pen", 50, "Stationery", 5), 2)
    storage.save_order(Order(Customer("arun", "a@b.c"), cart), orders_file)
    storage.save_order(Order(Customer("kavi", "k@b.c"), cart), orders_file)
    assert len(json.loads(orders_file.read_text())) == 2
    rows = storage.export_orders_csv(tmp / "out.csv", orders_file)
    assert rows == 2
    assert (tmp / "out.csv").read_text().startswith("number,date,customer")
 
# Custom exceptions
mouse = Product(9, "Mouse", 599, "Accessories", 1)
try:
    Cart().add(mouse, 5)
    assert False
except OutOfStockError as error:
    assert error.requested == 5
try:
    Cart().add(mouse, 0)
    assert False
except InvalidQuantityError:
    pass
 
print("All storage checks passed.")