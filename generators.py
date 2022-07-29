'''
------------>  Generators   <------------
------------------------------------------
--> They are iterator.
--> And they are in the form of sequence structure like list =[1,2,3,4]
--> But we have list, Then why we need generator ? As we can loop in the list too.

#LIST
#memory --> a time is required in creation of list and after creation the memory is reserved by the list.
# It is used for continuous case / frequently.
 
#Generator:
#memory --> in generator secquence, only one number is generated and stored at a time. 
# It is used for only one time.

'''

# 0) Create generator with generator function or generator comprehension:
# --> generator function:
def generate_num_upto(num):
	for i in range(1,num+1):
		yield(i)  # yield  is used for generator
print(generate_num_upto(10)) # object

#generator is called when we only demand it because it is a iterator so it has next() function.

num_generator = generate_num_upto(10)

for ele in num_generator:
    print(ele)

for ele in num_generator:
    print(ele)

print(num_generator)

'''
#generator is called when we only demand it because it is a iterator so it has next() function.

num_generator = generate_num_upto(10)

for num in num_generator:
	print(num)

but, if i again use for loop:
for num in num_generator:
	print(num)

for num in generate_num_upto(10):
	print(num)

for num in generate_num_upto(10):
	print(num)
--> because they are no longer available in memory now.

'''

# Exercise #1: Define generator function which take one num as argument and generate the sequence of even num oly.

def generate_even_num_upto(num):
	for i in range(1,num+1):
		if i %2 ==0:
			yield(i)

even_num_generator = generate_even_num_upto(20)

for i in even_num_generator:
    print(i)

for i in even_num_generator:
    print(i)
    
print(even_num_generator)


for i in generate_even_num_upto(20):
    print(i)

for i in generate_even_num_upto(20):
    print(i)

# --> generator function with generator comprehension:
square1 = [i**2 for i in range(1,21)]   # list comprehension
square2 = (i**2 for i in range(1,21))   # generator comprehension

print(square1)
print(square2)

for num in square2:
	print(num)

for num in square2:
	print(num)
#--> It will not print two times.

# 1) Create generator vs creation of list with 10 million data:
import time as t

# t1 = t.time()
# square_list = [i**2 for i in range(10000000)]
# t2= t.time()
# list_creation_total_time =t2-t1
# print(f"The total time required to create a 10M list is: {list_creation_total_time}")

t3 = t.time()
square_generator = (i**2 for i in range(10000000))
t4= t.time()
generator_creation_total_time=t3-t4
print(f"The total time required to create a 10M generator is: {generator_creation_total_time}")


print(square_generator)
# print(square_list)
