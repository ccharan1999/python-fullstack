"""catalog.py — the product objects ShopEase sells."""
from models import Product, DigitalProduct
PRODUCTS = [
 Product(101, "Wireless Mouse", 599, "Accessories", 10),
 Product(102, "USB Keyboard", 899, "Accessories", 5),
 Product(103, "Laptop Stand", 1499, "Furniture", 3),
 Product(104, "HD Webcam", 2199, "Electronics", 4),
 Product(105, "USB-C Hub", 1299, "Electronics", 8),
 DigitalProduct(201, "Python eBook", 499, "eBooks",
 "https://shopease.in/dl/py"),
]
_BY_ID = {p.pid: p for p in PRODUCTS}
def find(pid):
 return _BY_ID.get(pid)
def search(keyword):
 keyword = keyword.strip().lower()
 return [p for p in PRODUCTS if keyword in p.name.lower()]
def print_table(items):
 print(f"{'ID':<5}{'Product':<16}{'Category':<13}{'Price':>9}{'Stock':>7}")
 for p in items:
     print(p) # calls Product.__str__