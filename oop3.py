
'''
--> #4 Multilevel Inheritance,MRO,Method Overriding
--> print(isinstance(phone1,Phone))
--> print(issubclass(SmartPhone,Phone))

'''

class Phone: # super class, parent class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    
    def full_spec(self):
        print(f"The full spec of this phone is: {self.brand} {self.model} and price is: {self.price}")

class SmartPhone(Phone): #derived class, child class
    def __init__(self,brand,model,price,ram,memory,camera):
        super().__init__(brand,model,price)
        self.ram=ram
        self.memory=memory
        self.camera=camera
    
    def full_spec(self):
        print(f"The full spec of this phone is: {self.brand} {self.model} and price is: {self.price}")

class FlagshipPhone(SmartPhone):
    def __init__(self,brand,model,price,ram,memory,camera,security):
        super().__init__(brand,model,price,ram,memory,camera)
        self.security=security



phone1 = Phone("Maharshi","Landline",4500)
sp = SmartPhone("mi","note 5",45000,"3GB","64GB","20MP")
fp = FlagshipPhone("Samsung","S10+",45000,"8GB","256GB","100MP","Khatra Xa")
print(fp.full_spec())
# print(help(FlagshipPhone))
# print(FlagshipPhone.mro())

print(isinstance(sp,FlagshipPhone))
print(issubclass(FlagshipPhone,FlagshipPhone))