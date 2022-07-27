'''
------------>  Advance min() and max() Functions<-------------
--------------------------------------------------------------
'''

def any_fun(name):
	return len(name)

names=["Apple","joy","om","ram kumar"]

# print(max(names,key=any_fun))

# print(max(names,key= lambda name: len(name)))

#1 find the name of highest marks: 
student1 = [
    {"name":"Ram","score":60,"age":19},
    {"name":"kiran","score":70,"age":20},
    {"name":"om","score":80,"age":21}
    ]

print(min(student1, key= lambda dict_item: dict_item.get("score"))["name"])

student2 = {
    "Ram":{"score":60,"age":19},
    "kiran":{"score":70,"age":20},
    "om":{"score":80,"age":21}
    }

print(max(student2,key=lambda item: student2[item]["score"]))

'''
------------>  Advance sorted() Functions<-------------
--------------------------------------------------------
'''

name1=["Apple","joy","om","ram kumar"]
name2=("Apple","joy","om","ram kumar")

#sort method
name1.sort()
print(name1)

# but in case of tuple and sets
# name2.sort() # immutable --> ERROR
sorted_list= sorted(name2) # sorted function sort and return in list
print(sorted_list) 
print(name2) # immutable


#1 find the sorted according to highest marks:
student1 = [
    {"name":"kiran","score":70,"age":19},
    {"name":"Ram","score":60,"age":21},
    {"name":"om","score":80,"age":21}
    ]

sorted_list= sorted(student1, key= lambda item: item["score"],reverse=True)
print(sorted_list)

'''------------>  Doc-String in more about Functions<-------------
---------------------------------------------------------------'''
#len,sum,max,min,sorted

def add(a,b):
	''' This function takes 2 value and return their sum '''
	return a+b

print(add.__doc__)
print(help(sum))

