# homework1

import random
class SrtDict:

    def __init__(self, name):
        self.name = name
        self.dict = {}
        for i in name:
            self.dict[i] = random.randint(1,9)

    def present(self):
        return F"Below is the dictionary created from a string {self.name}\n {self.dict}"        

    def no_doublicate_values(self):
        return set(self.dict.values())

    def three_highest_values(self):
        return sorted(list(self.dict.values()), reverse=True)[-3:] 
        
            

dict_1 = SrtDict('python')

print(dict_1.present())
print(dict_1.no_doublicate_values())
print(dict_1.three_highest_values())






# homework2

# class Circle:

#     def __init__(self, radius):
#         self.circle_radius = radius

#     def area(self):
#         circle_area = 3.14 * self.circle_radius * self.circle_radius
#         return F"Circle area is {circle_area}"

#     def perimeter(self):
#         circle_perimeter = 3.14 * 2 * self.circle_radius 
#         return F"Circle perimeter is {circle_perimeter}"
  

# circle_1 = Circle(3)
# print(circle_1.area())
# print(circle_1.perimeter())