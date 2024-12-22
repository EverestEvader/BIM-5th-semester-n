#8.7
#WAP to illustrate the use of ABC.
"""Example : Create an base class Shape with abstract method to
    calculate area of the shape and perimeter of shape
    and create derived classes Circle and Rectangle
"""
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

#class for rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    #override the area method to provide specific information
    def area(self):
        return self.length * self.breadth
    
    #override the perimeter method also to provide specific information
    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    #override as above in rectangle
    def area(self):
        return math.pi * (self.radius ** 2)
    
    #override as above dine in perimeter method
    def perimeter(self):
        return 2 * math.pi * self.radius

#object for rectangel
R1 = Rectangle(5,10)
print("Area of rectangle: " , R1.area())
print("Perimeter of rectangle: " , R1.perimeter())
#object for circle
C1 = Circle(7)
print("Area of circle: " , C1.area())
print("Perimeter of circle: " , C1.perimeter())