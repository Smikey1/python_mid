'''
#Dictionary

Syntax1: {append_item for loop}
Syntax2: {i: ("even" if i %2 ==0 else "odd") for loop}
0) intro--> create dictionary with one line'

'''

def square_func(num):
    new_dict={}
    for items in range(0,num+1):
        square=items**2
        if square%2==0:
            new_dict[square]="even"
        else:
            new_dict[square]="odd"
    return new_dict
print(square_func(5))

def sq_func(number):
    return{k**2:("even" if k**2%2==0 else "odd") for k in range(0,number+1)}

print(sq_func(5))


# eg: name= "Samay"

def name_count(name):
    return {char: name.lower().count(char.lower()) for char in name.lower()}

print(name_count("aryama"))



