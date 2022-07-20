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
dic1 ={"day3":"Wednesday","day4":"Tuesday"}

