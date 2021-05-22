import os

# os.mkdir("test")

# base_dir = os.getcwd()
# test_items = os.listdir('test')
# print(test_items)

# for item in test_items:
#   path = os.path.join(base_dir, "test", item)
#   if os.path.isfile(path):
#       print(F"removing file {path}")
#       os.remove(path)
#   else:
#       print(F"removing directory {path}")
#       os.rmdir(path)



# path = os.path.join(os.getcwd(), "test", "t.txt")
# new_path = os.path.join(os.getcwd(), "test", "updated")
# if os.path.exists(path):
#     os.rename(path, new_path)
# else:
#     print("not found")


path = os.path.join(os.getcwd(), "test", "t.txt")
new_path = os.path.join(os.getcwd(), "test", "updated")

# file = open(new_path, 'r')
# print(file)
# print(file.read())


file = open(new_path)
# file_ = open(path, 'w')


# print(file)
# print(file.read())


# print(file.readline(2))
# print(file.readline())
# print(file.readline())





# file = open(new_path)
# print(file.read(100))
# file.close()


# with open(new_path) as file:   #context mananger
#     print(file.read(100))



# with open(new_path, "w") as file:
#     file.write("hello from python")


# with open(new_path, "a") as file:
#     file.write("hello from python\n")


# class A:                          # FYI
#     def __enter__(self):
#         print("111")

#     def __exit__(self, exception_type, exception_value, traceback):
#         print("bye")    
#     pass

# with A() as a:
#     print("a")



path = os.path.join(os.getcwd(), "test", "t.txt")

# with open(path, "w") as file:
#     file.write("Gohar ")

# with open(path, "a") as file:
#     file.write("Keshishyan")

# with open(path, "r") as file:
#     print(file.read())    


                       #kam

file = open(path, "w")
file.write("Gohar ")
file.close()

file = open(path, "a")
file.write("Keshishyan")
file.close()

file = open(path, "r")
print(file.read()) 
file.close()
