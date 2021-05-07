
# homework2

class Circle:

    def __init__(self, radius):
        self.circle_radius = radius

    def area(self):
        circle_area = 3.14 * self.circle_radius * self.circle_radius
        return F"Circle area is {circle_area}"

    def perimeter(self):
        circle_perimeter = 3.14 * 2 * self.circle_radius 
        return F"Circle perimeter is {circle_perimeter}"
  

circle_1 = Circle(3)
print(circle_1.area())
print(circle_1.perimeter())