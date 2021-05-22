import random 
import os


gen_list = []
for i in range(1,21):
    gen_numbers = random.randint(1,20)
    if gen_numbers % 2 != 0:
        gen_list.append(gen_numbers)
print(gen_list)

print(os.getcwd())
path = os.path.join(os.getcwd(), 'odd_num_list.txt')

with open(path, "w") as file:
    file.write(str(gen_list))

for i in gen_list:
    n = sum(gen_list)
print(n)

with open(path, "a") as file:
    file.write(F"\n Sum of odd numbers are {n}")