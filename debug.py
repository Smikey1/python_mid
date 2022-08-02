#Python Dbugger
'''--> What is dbugging?
--> Why python dugging?
--> importing python module pdb
--> use debugging by 2steps: 1) --> set-trace() function and 2) --> executing line by line:
--> important command --> ncl (next line, continue, line list)
'''
# Example: 
import pdb as debug
debug.set_trace()
name = input("Please, enter your name: ")
age = input("Please, enter your age: ")
print(f"Your name is: {name} and your age: {age}")
new_age = int(age) + 5
print(new_age)
