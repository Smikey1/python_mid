'''
------------>  OS Module <----------------
------------------------------------------
'''
import os

print(os.getcwd())
orginal_path = r"C:\Users\Smikey\Desktop\test test\python_mid"

# os.mkdir("any2")
# os.mkdir("any2")
# os.rmdir("any2")

print(os.path.exists("any2"))

if os.path.exists("any3"):
    print("Already Exist")
else:
    os.mkdir("any3")

#open or make new file
open("file.png","a").close() # a--> append mode

list_dir_path= r"C:\Users\Smikey\Desktop\test test\python_mid\any3"
print(os.listdir(list_dir_path))

# change directry
change_dir_path= r"C:\Users\Smikey\Desktop\test test\python_mid\any3"
# 1)--> os.chdir(r"F:\abc")
# 2) --> os.mkdir(r"F:\abc\abc")

os.chdir(change_dir_path)
print(os.getcwd())
os.chdir(orginal_path)
print(os.getcwd())


# to find the path of files:
for item in os.listdir():
	file_path= os.path.join(os.getcwd(),item)
	# print(f"The path of this item file {item} is: --> {file_path}")
	print(f"Any")


# to walk in the path of files:
orginal_agile_path=r"C:\Users\Smikey\Desktop\Agile T"
print(os.walk(orginal_agile_path)) # iterator
file_walk= os.walk(orginal_agile_path) #--> give three important things
for current_path,folder_names,file_name in file_walk:
	print(f"The current_path is: --> {current_path}")
	print(f"The folder_names is: --> {folder_names}")
	print(f"The file_name is: --> {file_name}")



# ------------>  shutil <-------------------------
# --------------------------------------------------

import shutil
print(os.getcwd())

# os.rmdir("any3")
# shutil.rmtree("any3") # pernamently delete


# any3_path= orginal_path +r"\any3"
# copy_garne_path= orginal_path + r"\any2\any3"
# shutil.copytree(any3_path,copy_garne_path)

# file_path = orginal_path +r"\file.txt"
# file_ko_copy_garne_path= orginal_path + r"\any2\file.txt"
# shutil.copy(file_path,file_ko_copy_garne_path)


# move_file_path = orginal_path +r"\file.png"
# file_ko_move_garne_path= orginal_path + r"\any2\file.png"
# shutil.move(move_file_path,file_ko_move_garne_path)


