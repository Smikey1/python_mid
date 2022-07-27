"""
------------>  Closure  <------------
------------------------------------------
--> First class function / closure
--> it make unique python and many lecturer skip this topic

"""

# 0) Intro  -------------------------------->
import re


def square(a):
	return a**2

s = square  # not calling function only assigning

print(s(7)) # but we can call and treat s as a square function
print(s.__name__)
print(square.__name__)

# 1) pass function as a argumnet    ------------->
# --> for eg: map function 
any_list = [1,2,3]
print(list(map(lambda a:a**2, any_list)))


any_list2 = [4,5,6]

def my_own_map(func,list):  # create using list comprehension
	new_list = []
	for item in list:
		new_list.append(func(item))
	return new_list


def cube(num):
    return num**3


print(list(map(cube,[1,2,3])))

def mero_aafnai_map(fun,list):
    new_list=[]
    for ele in list:
        new_list.append(fun(ele))
    return new_list

def sq(a):
    return a**2


print(mero_aafnai_map(cube,[4,5,6] ))


# 2) function return function  ---------------->

def out_func():
	def in_func():
		print("Hello done")
	return in_func

any_var = out_func()
any_var() # calling second function


def out_func(value1):
	def in_func(value2):
		print(f"Hello done any-->{value1} and ok --> {value2} ")
	return in_func

any_var = out_func("ok1")
any_var("any1") # calling second function

# practice 1: 
def cube_off(num):
	def calc_power(n):
		return num**n
	return calc_power

to_power = cube_off(4)
print(to_power(3))
