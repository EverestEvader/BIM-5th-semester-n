#operator overriding
"""1.	A class named Vector that represents a 2D vector with x and y coordinates.
2.	Implement operator overloading for the + operator using the __add__(self, other) method. This method should allow two vectors to be added together.
3.	Also, overload the * operator using the __mul__(self, scalar) method to allow scalar multiplication of a vector.
4.	Implement a method __str__(self) to return a string representation of the vector in the form Vector(x, y).
5.	Create two instances of the Vector class, add them together, and perform scalar multiplication to demonstrate operator overloading.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,o):
        return Vector(self.x + o.x, self.y + o.y)
    
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

V1 = Vector(2 , 3)
V2 = Vector(4 , 1)
V3 = V1 * 3
V4 = V2 * 3

print(V1.__str__())
print(V2.__str__())
print()

print(f"Addition of vectors {V1} + {V2} : {V1 + V2}")
print()

print(f"Scalar multiplication of vector {V1} with scalar {3} : {V3}")
print()

print(f"Scalar multiplication of vector {V2} with scalar {3} : {V4}")
print()

