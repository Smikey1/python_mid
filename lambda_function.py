"""
------------>  Lambda Expressions (Anonymous Function ) <--------
-----------------------------------------------------------------
def add(a,b):
	return a+b
SYNTAX:
lambda param1,param2 : returning_values

Actually, we dont assign lambda function into variable.
We use it with built-in function --> built-in, map,reduce, filter (later we study)

"""

def add(num1,num2):
	return num1+num2

print(add(2,5))

sum_num = lambda p1,p2,p3 : p1+p2+p3
print(sum_num(1,1,2))

print(sum_num)
print(type(sum_num))

def check_even(n):
	return n % 2 ==0
