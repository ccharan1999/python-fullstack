
class Product:
    GST = 0.20
    def __init__(self,pid,name,price,catagory,stock =0,):
        self.pid = pid
        self.name = name
        self.price = price
        self.catagory = catagory
        self.stock = stock
        
        
    def CheckProduct(self,pid):
        if self.pid() == pid() :
            print("Product Details")
            print("pid:",self.pid)
            print("Name:",self.name)
            print("Price:",self.price)
            print("catagory:",self.catagory)
            print("stock:",self.stock)
            print("GST:",self.GST)
        else :
            print("no such product")
            
    def CheckProductPrice(self,name) :
        if self.name() == name():
            return self.price()
        else:
            print("no such product")
            
    def ReduceStock(self,qty):
        if self.stock > qty :
            self.stock =- self.stock
        else :
            print("not enough stock")
            
    def RestockStock(self,qty) :
        self.stock =+ qty
        
    def CheckStock(self) :
        return self.stock()
    
    def CheckProduct(self):
        return self.name()
    
class DigitalProduct(Product) :
    GST = 0.0
    
    def __init__(self, pid, name, price, catagory, stock=0):
        super().__init__(pid, name, price, catagory, stock)
    
    
    
    
    

        