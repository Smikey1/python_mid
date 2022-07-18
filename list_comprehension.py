"""
------------>  List Comprehension <--------
-------------------------------------------
Syntax1: [append_item for loop]
Syntax2: [append_item for loop if (condition)]
Syntax3: [append_item if (condition) else -i for loop]

"""

def square(n):
    square_list = []
    for i in range(1,n+1):
        square_list.append(i**2)
    return square_list

def same_square(n):
    return [i**2 for i in range(1,n+1)]

print(square(10))
print(same_square(10))

def first_char(any_list):
    first_char=[]
    for i in any_list:
        first_char.append(i[0])
    return first_char

print(first_char(["abc","def","ghi"]))

def filter_even(num):
    return [i for i in range(num+1) if (i%2==0)]
print(filter_even(10))

def fun1(num):
    return [ i*2 if(i % 2==0) else -i for i in range(num+1)]
print(fun1(10))

# Nested Loop
example = [[1,2,3],[1,2,3],[1,2,3]]
def nested_loop(num):
    return [ f"k{k}--> {[m for m in range(1,num+1)]}" for k in range(1,num+1)]

print(nested_loop(3))
