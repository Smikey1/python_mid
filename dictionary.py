"""
------------>  DICTIONARY  <--------
------------------------------------

0) intro--> it is a unordered collection of items of any data type in the form of key:value pair
	--> Because of the limitation of list, we used dictionary:
===> which is also known as JSON array, or map/Hash Map,

ex: user=["Aryama","Sharma",19,["thor","marvel"],["pizza","chowmin"],"Kathmandu"]
ex: days={"day1":"sunday","day2":"monday"}
{"key":"value"}  --> {"age":19}

"""
# 1) How to create dictionaries
# type 1
days = {"day1":"sunday","day2":"monday","day3":"Tuesday"}
print(days)
print(type(days))

#type 2
days2 = dict(day4="Wednesday",day5='Thursday',day6="Friday")
print(days2)
print(type(days2))

'''
2) How to access data from dictionary
# day2 = {'day4': 'Wednesday', 'day5': 'Thursday', 'day6': 'Friday'}
--> no indexing
--> days["day1"]
--> type function
'''
print(days2["day4"])

"""

3) Which type of data can dictionary store?
--> Anything (number,string,list,dictionary)
"""

any_dict = {
    "f_name":"Maharshi",
    "age":23,
    "fav_song":["s1","s2",11,True],
    "others":{
        "fav_game":"Footbal",
        "fav_programming":"Python"
    }
}

#Createing empty dict and add values into it
empty_dict ={}
print(empty_dict)
empty_dict["name"]="Kritika Absent"
print(empty_dict)

# print(any_dict["fav_song"][3])
# print(any_dict["others"]["fav_programming"])

# In keyword (conditional and looping statement)

'''
{
    'f_name': 'Maharshi', 'age': 23, 
    'fav_song': ['s1', 's2', 11, True], 
    'others': {'fav_game': 'Footbal', 'fav_programming': 'Python'}
}
'''
print(any_dict)

'''if "f_names" in any_dict:
    print("present")
else:
    print("Not Present")'''

# different methods hunxa --> keys(),values(),items(),copy(),clear(),get()
if "Maharshi" in any_dict.values():
    print("present")
else:
    print("Not Present")



for key,value in any_dict.items():
    print(f"The key is: {key} and values is: {value}")

any_dict2 = any_dict.copy()
print(any_dict2)

any_dict2.clear()
print(any_dict2)

'''
6) add, update, pop and popitem method in dictionary
--> days["all_days"]=["day1","day2","day3"]
--> days.update(ANOTHER_DICTIONARY) # which returned the value of pop(key)
--> days.pop("all_days") # which returned the value of pop(key)
--> days.popitem() # randomly delete one item and returned the value of pop(key)

'''

dic1 ={"day1":"Sunday","day2":"Monday"}
dic2 ={"day3":"Wednesday","day4":"Tuesday"}

dic3= dic1.copy()

# add value to dic3 
dic3["day5"]=["Nice day","Rainny Day"]
dic3["all_days"]=["day1","day2","day3"]
print(dic3)

#dic1.update(dic2) method
print(dic1)
dic1.update(dic2)
print(dic1)

#pop(key) method
popped_item=dic1.pop("day1")
print(dic1)
print(popped_item)

'''
7) fromkeys, get, clear and copy method
--> days=dict.fromkeys(["day1","day2","day3"], "unknown") # can use tuple and string too
--> get method:
ex: days["apple"] --> error but days.get("day1") --> no error and result too
--> if days.get("day1"): print present else absent
ex: if None: is treated as False else True
--> days.clear() ; days.copy() ; is vs == 
'''

#fromkeys(keys,value) method
days=dict.fromkeys(["day1","day2","day3"], "unknown")
print(days)

# print(days["day5"]) --> Error 404
print(days.get("day3")) #--> Do not give Error 404
print(days.get("day5")) #--> Do not give Error 404

if any_dict.get("address"):
    print("Present")
else:
    print("Not Present")


'''
8) More about dictionary:
--> get method:
ex: days["apple"] --> error but days.get("day7","Not Found") --> no error and result too
		  --> get method always took last/updated value when same keys are present in dictionary
'''
print(days.get("day5","Sorry! your value was not Found")) #--> Do not give Error 404

user_info = {"fname":"Arayama","lname":"Sharma","age":30,"age":17}
print(user_info.get("age"))

"""
Excercises:

1) Excercise 1:
--> ask a num to user and define a function which return the dictinary of cube to that number.
{1:1,2:8,--->n:n**3}

2)Excercise 2: 
modify and optimize word counter of your name:
"""

user_number = int(input("enter a number"))

def cube(number):
    new_dict={}
    for i in range(number+1):
        new_dict[i]=i**3
    return new_dict

print(cube(user_number))    

def countchar(name):
    new_dict={}
    for char in name:
        new_dict[char]= name.lower().count(char)
    return new_dict

print(countchar("aryama"))    
