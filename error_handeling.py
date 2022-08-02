'''
------------>  Error Handelling <----------------
----------------------------------------------------
'''

#1 Syntax Error:
def fun():
    print("Done")

name="Kritika"

#2 Indentation Error:
def fun():
    print("sth")

#3 Name Error #--> not defined previously
ok = 0
print(ok)

#4 TypeError
print("1"+"A")


#5 Index Error
list = ["A","B"]
print(list[0])

#6 Value Error
s=8
m= "9"
print(int(m))

#7 Attribute Error # not exist in python
list = ["A","B"]
list.append("C") # haldeu("C")

#8 Key error
d={"name":"Apple"}
print(d["name"])

# --------------> RASIE ERROR 

class ChalNikalPatliGaliseError(TypeError):
    pass

def add(a,b):
    if (type(a)==int and type(b)==int):
    	return a+b
    # raise ChalNikalPatliGaliseError("Not int datatype")

print(add(2,3))
print(add("2","3")) # --> raise error for this


# Example 1:
class MobilePhone: #base class / #parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
    
    def full_spec(self):
        return f"brand name: {self.brand} and model name: {self.model_name} "
    
    def dial(self,number):
        return f"dialing... {number}"

class MobileStore: #derived class / #child class
    def __init__(self):
        self.mobiles=[]
      
    def add_mobile(self,new_mbl):
        if isinstance(new_mbl,MobilePhone):
            self.mobiles.append(new_mbl)
        else:
            raise TypeError("new mbl is not a object of mobile phone")
        print (self.mobiles)

iphone = MobilePhone("Apple","XS",100000)
my_phone="My Hello"
store=MobileStore()
store.add_mobile(iphone)


# --------------> Exception Handling
'''while True:
    try:
        age= int(input("enter your age: "))
        print(f"your age is: {age}")
        if age>18:
            print("You can play")
        else:
            print("you can not play")
        break
    except ValueError:
        print("please input int value")
    except:
        print("unexpected error ...")
'''

# Clean way 2
'''while True:
    try:
        age= int(input("enter your age: "))
    except ValueError:
        print("please input int value")
    except:
        print("unexpected error ...")
    else: # it run only try block runs
        print(f"your age is: {age}")
        break
'''

while True:
    try:
        age= int(input("enter your age: "))
    except ValueError:
        print("please input int value")
    except:
        print("unexpected error ...")
    else: # it run only try block runs
        print(f"your age is: {age}")
        break
    finally: # it always run 
        print(f"your finally block is this:...")
        break


"""
#Excersice: 
make divide fun:
print(divide(4,2)) # output: 2
print(divide(4,0)) # don't divide by zero (Zero Division error)
print(divide("4",1)) # Input int only
"""

def divide(a,b):
    try:
        a // b
    except ZeroDivisionError as zero_error_ko_msg:
        print(zero_error_ko_msg)
        raise ZeroDivisionError("Dont divide by zero")
        
    except TypeError as type_error_huda_msg:
        print(type_error_huda_msg)
        raise TypeError("Input int only")

        
    except:
        return ("Unexcepted error")

print(divide(1,0))
