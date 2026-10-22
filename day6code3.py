

class Employee :
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def addsalary(self,amount):
        self.salary += amount
        return self.salary
    
    def checksalary(self,name):
        if self.name == name:
            return self.salary
        else:
            print("No name")
        
         
    
class Manager(Employee) :
    def __init__(self, name,age,salary,bonus = 0):
        super().__init__(name, age, salary)
        self.name = name
        self.age = age
        self.salary =salary
        self.bonus = bonus
        
    def addbonus(self,name,bonus):
        if self.name == name :
            self.salary += bonus
            print(self.salary)
        else:
            print("wrong name")

emplyee1 = Manager("charan",11,1000)
emplyee1.addbonus("charan",700)
emplyee1.checksalary("charan")
emplyee1.checksalary("varun")
    
            
        
        