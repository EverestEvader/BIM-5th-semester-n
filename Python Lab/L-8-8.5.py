#LAB 8.5
#WAP to illustrate method overriding.
import math
class Shape:
    def area(self):
        return "Area not defined for generic shape"

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

#obj for shape
s1=Shape()
print("Shape Area:")
print(s1.area())

#obj for rectangle 
R1 = Rectangle(120, 20)
print("Area of rectangle:")
print(R1.area())

#obj for circle
C1 = Circle(7)
print("Area of circle:")
print(C1.area())

