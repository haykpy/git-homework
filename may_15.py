import os

# dir_  = os.getcwd()

# print(F"we are working from {dir_}")
# print(os.listdir("C:\\Users\\Gohar\\Desktop\\Python"))

# os.mkdir("os_folder1")
# os.makedirs("os_folder3/os_folder2")


file_path = "os_folder_1/os_folder_nested"
os_folder_1, os_folder_nested = file_path.split('/')[0], file_path.split('/')[0], 

list_dir = os.listdir()

if os_folder_1 in list_dir:
    check_path = os.listdir(folder1)
    if not os_folder_nested in check_path:
        print(F"created only {os_folder_nested}")
        os.mkdir(os_folder_nested)
else:
    print("created 2 folders")
    os.mkdir(file_path)        






# print(os.getcwd())

# if not "a" in os.listdir() or not os.listdir("a"):
#     os.makedirs("a/b")
#     os.makedirs("a/c")
# else:
#     list_a = os.listdir("a")
#     if not "c" in list_a:
#         os.mkdir("a/c")
#     elif not "b" in list_a:
#         os.mkdir("a/b")   


# print(os.listdir('a')) 
# print("...after creating")

# if os.listdir("a/c"):
#     print("C is not empty")
# else:
#     os.chdir("a")
#     os.rmdir("c")

# print(os.listdir("../a")) 


