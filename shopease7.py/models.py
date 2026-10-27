from errors import OutOfStockError, InvalidQuantityError
 
class Product:
    ...
    def reduce_stock(self, qty):
        if not self.in_stock(qty):
            raise OutOfStockError(self, qty)      # was ValueError
        self._stock -= qty
 
    def to_dict(self):
        """Plain dict that can be saved as JSON."""
        return {"type": "physical", "id": self.pid, "name": self.name,
                "price": self.price, "category": self.category,
                "stock": self.stock}
 
    @staticmethod
    def from_dict(data):
        """Build a Product or DigitalProduct from a saved dict."""
        if data.get("type") == "digital":
            return DigitalProduct(data["id"], data["name"], data["price"],
                                  data["category"], data["download_url"])
        return Product(data["id"], data["name"], data["price"],
                       data["category"], data["stock"])
 
class Cart:
    def add(self, product, qty=1):
        if qty <= 0:
            raise InvalidQuantityError("Quantity must be at least 1")
        ...
 
class Order:
    @classmethod
    def continue_numbering(cls, existing_orders):
        """Start numbering after the orders already saved on disk."""
        cls._next_number = existing_orders + 1
 
    def to_dict(self):
        """Order summary for orders.json."""
        ...
