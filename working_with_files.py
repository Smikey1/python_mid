'''
------------>  Working with TXT Files <----------------
-------------------------------------------------------
'''
#all Methods
#1) readFile
#2) open function --> takes path
#3) read method()
#4) seek method() # change the position of cursor
#5) tell method() # to find the position of cursor

from pyparsing import line


poem_path = r"python-poem.txt"

rf = open(poem_path) # open method open files in --> bydefault read mode
'''print(f"Before reading, cursor position--> {rf.tell()}")
print(rf.read())
print(f"After reading, cursor position--> {rf.tell()}")
print("------------------------------------------")
rf.seek(0)
print(rf.read())'''


#6) readline method() 
'''print(f"next line -->: {rf.readline()}",end="")
print(f"next line -->: {rf.readline()}",end="")
print(f"next line -->: {rf.readline()}",end="")
print(f"next line -->: {rf.readline()}",end="")'''

#7) readlines method() # add all lines into one list
'''all_lines= rf.readlines()
for line in all_lines:
    print(f"The line is:-->{line}",end="")
print(all_lines)'''
rf.close()


# use of with block:
with open(poem_path,"r") as rf:  # default read mode --> "r"
    print(rf.read())
    

# ------------> Write data in file (w,a,r+) mode-----------
#1) write mode
# delete all data and write with new data by creating new file| it override
with open("kritika.txt","w") as wf:
    wf.write("Ok, I am fine")

#2) append mode
with open("samaya.txt","a") as af: # not delete all data and write with new data in last or by creating new file
	af.write("Hello aaryamana")

#3) r+ mode
with open("samaya.txt","r+") as rpf: # read and write data, and don't create new file and override char 
	rpf.write("write r+ mode")

with open("file.txt","r+") as rpf: # read and write data, and don't create new file and override char 
	rpf.seek(len(rpf.read()))
	rpf.write("   write r+ mode")

#4 read and write 
with open(poem_path,"r") as rf:
    with open("samay.txt","w") as wf:
        wf.write(rf.read())


#5 read love story:
with open("love_story.txt","r",encoding="utf-8") as rf:
    print(rf.encoding)
    print(rf.read())


#Challenge Excercise 
with open("ok.txt","r") as rf:
    with open("samayi.txt","w") as wf:
        for line in rf.readlines():
            name,salary = line.split(",")
            wf.write(f"{name}'s your salary is {salary}")