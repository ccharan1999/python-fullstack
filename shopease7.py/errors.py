
class shoperror(Exception) :
    pass
class OutOfStock(shoperror):
    def __init__(self,product,requested):
        self.product = product
        self.requested = requested
        super().__init__(f"Only{product.stock}{product.name} are left" f"(you asked for {requested})")

class InvalidQuantityError(shoperror) :
    pass
    
class ProductNotFoundError(shoperror) :
    pass