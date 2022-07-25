'''
------------>  Enumerate Functions<--------
------------------------------------------
--> We use it with for loop to track the postion of our item in iterable or loop

'''
# 0) Track the position with-out enumerate function:


list_of_name=["kritika","arayama","rushav","samay"]

for loc,name in enumerate(list_of_name):
    print(f"The name {name} is in {loc} position ")


# Excersice: #1
# A list contain many strings name and fine the position of one target string from the list. (dynamically)

def find_position_of_given_name(name_list,target_name):
    for position,name in enumerate(name_list):
        if name == target_name:
            print(position)
        else:
            print("Name not found")

print(find_position_of_given_name(list_of_name,"samay"))        

'''

------------>  Map Functions <-------------
------------------------------------------
It is iterators. So, we can use loop in map object but only one time:

Task #1: --> return the list of square num from the list with: --> normal way, 
list comprehension, def function with lambda ani normal;

'''

num_list = [1,2,3,4]  # iterables


k_ho = set(map(lambda a:a**2,num_list))  #iterator 

print(k_ho)

for i in k_ho:
    print(f"k_ho-->{i}")


'''
------------>  Iterator vs Iterable <-------------
--------------------------------------------------
for i in square:
	print(i)
--> how loops work in this iterator?

'''  
num_list = [1,2,3,4]  # iterables

# iter()  --> iterator ma convert garne

iterator_converted = iter(num_list)
print(next(iterator_converted))
print(next(iterator_converted))
print(next(iterator_converted))


'''------------>  Filter Functions<-------------
------------------------------------------------
It is iterators.
Task #1: --> return the list of even num from the list with: --> normal way, list comprehension, def function with lambda ani normal;
'''
num_list = [1,2,3,4,5,6,7,8]

def filter_even(list):
    even_list = []
    for ele in list:
        if ele %2==0:
            even_list.append(ele)
    return even_list

def even_func(i):
        return i%2 ==0

def filter_even2(list):
    return [i for i in list if i%2==0]

print(filter(even_func,num_list))
even_list = tuple(filter(even_func,num_list))
even_list2 = list(filter(lambda a: a%2==0,num_list))
print(even_list)
print(even_list2)

# print(filter_even(num_list))
# print(filter_even2(num_list))

'''

------------>  Zip Functions<-------------
------------------------------------------

'''


big_char_list = ["A","B","C","D"]
small_char_list = ["a","b","c","d"]
# num_list = [1,2,3,4,5,6,7,8]

print(list(zip(small_char_list,big_char_list)))  

l= list(zip(small_char_list,big_char_list))
print(l)

# for un-zip
l1,l2= zip(*l)
print(l1)
print(l2)

'''
Challange Excerise:
1) Ask a num with user: filter odd or even and store in list --> zip it --> and add max value into new list from pairs of tuples
and return new list

2) define a fun which take many list: (lambda function)
such as [1,2,3],[4,5,6],[7,8,9] and return avg of --> (1+4+7)/3 , (2+5+8)/3 and so on

'''

avg_calculator=lambda *args: [sum(pair)//len(pair) for pair in zip(*args)]
print(avg_calculator([1,2,3],[4,5,6],[7,8,9]))


'''

------------>  Any and All Functions<-------------
--------------------------------------------------

'''
num_list1= [2,4,6,8,10]
num_list2 = [1,3,5,7,9]



even_list = [True,True,True,True]

print(all(even_list))  # output --> True

def check_even(list):
    even_list=[]
    for i in list:
        even_list.append(i%2==0)
    return even_list

print(check_even(num_list1))

print(all([num%2==0 for num in num_list1]))


#Practice of all and any
def sum(*args):
    if all([(type(arg) == int or type(arg)==float) for arg in args]):
        total=0
        for num in args:
            total += num
        return total
    else:
	    return "Int or float are allowed only"

print(sum(1,3.0,"abc"))