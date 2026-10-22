

class Bank :
    def __init__ (self, name ,pin, balance =0) :
        self.name = name
        self.__pin = pin
        self._balance = balance

    def addbalance(self,__pin,_balance) :
        if __pin != self.__pin :
            print("wrong pin")
        else :
            print("correct pin \n Welcom")
            self._balance += _balance
            
    def accountbalance(self) :
        return self._balance

client1 = Bank ("charan","7894",500)
client1.addbalance("7894",500)
print(client1.name,client1.accountbalance())
    

