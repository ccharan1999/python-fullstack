import csv

import json

from pathlib import Path

from models import Product

DATA_DIR = Path(__file__).parent / "data"
PRODUCT_FILE = DATA_DIR / "product.json"
ORDERS_FILE = DATA_DIR / "order.json"

DEFAULT_PRODUCT = [{"type": "physical", "id": 101, "name": "Wireless Mouse", "price": 599.0,
     "category": "Accessories", "stock": 10},
    {"type": "physical", "id": 102, "name": "USB Keyboard", "price": 899.0,
     "category": "Accessories", "stock": 5},
    {"type": "physical", "id": 103, "name": "Laptop Stand", "price": 1499.0,
     "category": "Furniture", "stock": 3},
    {"type": "physical", "id": 104, "name": "HD Webcam", "price": 2199.0,
     "category": "Electronics", "stock": 4},
    {"type": "physical", "id": 105, "name": "USB-C Hub", "price": 1299.0,
     "category": "Electronics", "stock": 8},
      {"type": "digital", "id": 201, "name": "Python eBook", "price": 499.0,
     "category": "eBooks", "download_url": "https://shopease.in/dl/py"},


    
]

def _read_json(path,default) :
    """return json in file or default"""
    try :
        with open(path,encoding="utf-8") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return default
    
    except json.JSONDecodeError:
        print(f"WARNING: {path.name}the path is damaged ")
        return default
    
def _write_json(path,data) :
    path.parent.mkdir(parents = True , exist_ok = True)
    with open(path ,"w",encoding="utf-8") as f:
        json.dump(data, f, indent = 2)
        
def load_products(path = PRODUCT_FILE):
    return [Product.from_dict(d) for d in _read_json(path, DEFAULT_PRODUCT)]

def save_products(product,path =PRODUCT_FILE):
    _write_json(path, [p.to_dict() for p in product])
    
def load_orders(path = ORDERS_FILE) :
    return _read_json(path,[])

def save_orders(order, path =ORDERS_FILE) :
    orders = load_orders(path)
    orders.append(order.to_dict())
    _write_json(path, orders)
    
def export_orders_csv(csv_path, orders_path = ORDERS_FILE) :
    orders = load_orders(orders_path)
    with open(csv_path, "w",newline="",encoding="utf-8") as f :
        writer = csv.writer(f)
        writer.writerow(["number","data","customer","item","total"])
        for o in orders:
            units = sum(item["qty"] for item in o["item"])
            writer.writerow([o["number"],o["data"],o["customer"],units,o["item"],o["total"]])
    return len(orders)
    
        
          