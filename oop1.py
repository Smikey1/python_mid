'''

------------>  OOP Part 1 <---------------------
------------------------------------------------
--> It is a just way or style to write a code
--> It is very helpful in creation of real world programs
--> CLASS, OBJECT(Instance),method

1) Create your first class
class, init method/constructor, attributes , instance variable and create object

'''


class Person:
    # init method/constructor
    def __init__(self,name,age,address):   # name,age,address --> attribute
        print("My beautiful init method called")
        # instance variable
        self.name=name
        self.age=age
        self.address=address
        self.gender = "M"
    
    # create method
    def user_info(self):
        print(f"Your name is: {self.name} and your age is: {self.age} ")


p1 = Person("Samay",21,"Ktm")
p2 = Person("Rushub",21,"Ktm")

print(p1.gender)

print(p1.user_info())
print(p1.__dict__)


"""
3) Class Variable vs instance variable
--> class variable is shared between every function and methods insode the class

"""

class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius = radius
    
    def calc_area(self):
        return self.pi*(self.radius**2)
    
    def calc_circumference(self):
        return 2*self.pi*self.radius

# In conclusion: --> self is used if class variable are meant to be changed in future.

c2 = Circle(14) # 615.44
# c2.pi=6.28

c1 = Circle(7)

print(c1.calc_circumference())
print(c2.calc_area())


# Excercise 3: Count the total no of laptop (object) are available in the shop.


'''
3) Class methods vs instance method
--> generally we dont use class method but we use more instance/object method
--> It is done with the help of decorator. --> @classmethod
'''

'''
class Laptop:
    count_total_laptop = 0
    def __init__(self,brand):
        Laptop.count_total_laptop += 1
        self.brand=brand
	
    # class method creation
    @classmethod
    def count_all_laptop(own_class):
        return f"You have total {own_class.count_total_laptop} laptos are available in your {own_class.__name__} Store "

print(Laptop.count_all_laptop()) # class method calling
'''

# 3) Class methods as constructor
class Laptop:
    count_total_laptop = 0
    def __init__(self,brand,model_name,price):
        Laptop.count_total_laptop += 1
        self.brand=brand
        self.model_name=model_name
        self.price=price
	
    # class method creation
    @classmethod
    def count_all_laptop(own_class):
        return f"You have total {own_class.count_total_laptop} laptos are available in your {own_class.__name__} Store "
    
    #static method as constructor
    @staticmethod
    def my_func():
        print("Hello World")

    # class method  as constructor
    @classmethod 
    def with_new_feature(own_class,brand_name, model_name,price):
        return own_class(brand_name, model_name,price)

# print(Laptop("dell","i5",50000)) # class method calling to create same laptop type
print(Laptop.with_new_feature("laveno","i7",70000)) # class method as constructor calling

new_laptop = Laptop.with_new_feature("laveno","i7",70000)

print(new_laptop.brand)
print(new_laptop.my_func())


'''
4) Static methods as constructor
# class method has relation with class
# self method has relation with instances/object
# but static methos has no relation with either class or object/instance.
# it is created with @staticmethod decorator.
'''


