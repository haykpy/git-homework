# Homework
class Shape:
	def __init__(self, name):
		self.name = name 

	def present_shape(self):
		print(F"This is {self.name}")

class Triangle(Shape):
	def __init__(self, name, side1, side2, base, height):
		self.side1 = side1
		self.side2 = side2
		self.base = base
		self.height = height
		Shape.__init__(self, name)

	def present(self):
		print(F"We have {self.name}, for which area and perimeter should be calculated")

	def area(self):
		triangle_area = (self.base * self.height) / 2
		print(F"Area for {self.name} is {triangle_area}")

	def perimeter(self):
		triangle_perimeter = self.side1 + self.side2 + self.base
		print(F"Perimeter for {self.name} is {triangle_perimeter}")	


import math 
class Square(Shape):
	def __init__(self, name, side1, side2):
		self.side1 = side1
		self.side2 = side2
		Shape.__init__(self, name)

	def present(self):
		print(F"We have {self.name}, for which area, perimeter, bias should be calculated")

	def area(self):
		square_area = self.side1 * self.side2
		print(F"Area for {self.name} is {square_area}")

	def perimeter(self):
		square_perimeter = 4 * self.side1
		print(F"Perimeter for {self.name} is {square_perimeter}")

	def get_bias(self):
		square_bias = math.sqrt(2) * self.side1
		print(F"Diagonal for {self.name} is {square_bias}")


triangle1 = Triangle("triangle", 2, 3, 5, 4)	
square1 = Square("square", 4, 4)

Shape.present_shape(triangle1)
Shape.present_shape(square1)
Triangle.present(triangle1)
Triangle.area(triangle1)
Triangle.perimeter(triangle1)

Square.present(square1)
Square.area(square1)
Square.perimeter(square1)
Square.get_bias(square1)


