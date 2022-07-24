'''
------------>  Flexible Functions<--------
------------------------------------------

*operator or *args or **kwargs

*ARGS

'''

from unicodedata import name


def sum(a,b):
    return a+b

# P-->A
def another_sum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

list = [3,4,5,6]  
print(another_sum(*list))    # unpacking of list


print(sum(3,4))

def to_power(num,*args):
	if args:
		return [i**num for i in args]
	else:
		return "Your didnot pass any args"

'''
**KWARGS

0) intro

--> about the problem and solution of function for *kwargs (convensions)

'''

def sum_all_num(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key,value in kwargs.items():
        return f"Your First name is: {value}"


print(sum_all_num(first_name="Aaryama", last_name="Sharma"))


def your_details(**kwargs):
	print(kwargs)
	for key,value in kwargs.items():
		print(f"{key}:{value}")

print(your_details(first_nmae="Kritika",last_name="Deo"))



def another_sum(**kwargs):
    sum = 0
    for num in kwargs.values():
        sum += num
    return sum

dict ={"a":1,"b":2,"c":3}
print(another_sum(**dict))    # unpacking of list



# 3) Function with all type of parameter   PADK
def user_info(name,*args,address="unknown",**kwargs):
    print(name) 
    print(args) 
    print(address) 
    print(kwargs)

user_info("maharshi",1,2,4,address="ktm",p=12,q=13)


is_reverse=False
# Excersice1:
# -->make the first letter as the capital letter of list and if reverse_string = True mean list also reverse
# 	--> FIY: you can use list comprehension


list_of_name=["kritika","arayama",'rushav',"samay"]

def any(name_list,**kwargs):
    ''' To reverse you must give {is_reverse=True} either True or False'''  # doc string
    if kwargs.get("is_reverse"):
        return [name[-1::-1].title() for name in name_list]
    else:
        return [name.title() for name in name_list]

print(any(list_of_name))
print(any.__doc__)

