'''
------------>  OOP Part 2 <---------------------
------------------------------------------------

#1
Excapsulation --> write all the methods and function in one place which are going to perform 
in object data.
Abstraction  --> For eg. lst.sort() # make function and method use for easy to user. 
for eg: tim sort, merge sort, bubble sort etc. To hide all the complexitivity from user.

Special naming convension: --> bydefault all public in python but one naming convension for private --> _brand.
Name Mangling: __init__ (name as magic method or dunder method)

In ex: laptop1.__price # output: no attribute
	laptop1.__desc__  # changed by python itself (more in inheritance)

'''
class Laptop1:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.__price=price  # private (for naming convension)

new_laptop = Laptop1("laveno","i7",70000)
new_laptop._Laptop__price=50000
# print(new_laptop.__dict__)
# print(new_laptop._Laptop__price)


#2 Getter and setter
class Laptop:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.full_spec = f"The brand is {brand} and price is {price}"
        self._price = max(price,0) #problem 1 and 2 solved
    
    @property
    def full_specs(self):
        return f"The brand is {self.brand} and price is {self._price}"
    
    @property  # getter
    def price(self):
        return self._price
    
    @price.setter  # setter
    def price(self,new_price):
        self._price = max(new_price,0)
 
    
new_laptop = Laptop("laveno","i7",-70000)
new_laptop.price=-50000
# print(new_laptop._price)
print(new_laptop.full_specs)
print(new_laptop.price)


#2 Inheritance:

class Phone: #base class / #parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
    
    def full_spec(self):
        return f"brand name: {self.brand} and model name: {self.model_name} "
    
    def dial(self,number):
        return f"dialing... {number}"

p1= Phone("Apple","XS",10000)
p2= Phone("MI","Note 10",90000)
print(p1.dial(9841509543))
print(p2.full_spec())



class SmartPhone(Phone): #derived class / #child class
    def __init__(self,brand,model_name,price,ram,memory,camera):
        # two way
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.memory=memory
        self.camera=camera
      
    def open_browser(self,browser_name):
        return f"Opening {browser_name} browser"

iphone = SmartPhone("Apple","XS",100000,"2GB","64GB","2MP")
redmi = SmartPhone("Redmi","Note 4",80000,"3GB","128GB","20MP")
print(redmi.full_spec())


'''
class SmartPhone(Phone): #base class / #parent class
    def __init__(self,brand,model_name,price,ram,memory,camera):
        #two ways
        Phone.__init__(self,brand,model_name,price) # un-common way
        super().__init__(brand,model_name,price) # common way
        self.ram=ram
        self.memory=memory
        self.camera=camera
        
    def open_browser(self,browser_name):
        return f"Opening {browser_name} browser"
'''

