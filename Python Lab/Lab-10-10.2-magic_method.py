#implementation of magic methods
class Points:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self,o):
        return Points(self.x + o.x , self.y + o.y)
    
    def __eq__(self,o):
        return self.x == o.x and self.y == o.y
    
    def __mul__(self,s):
        return Points(self.x * s, self.y * s)

#instances
p1 = Points(2 , 3)
p2 = Points(4 , 6)

#magic methods usage
print("POINTS:")
print(p1.__str__())
print(p2.__str__())

print("\nADDITION:")
print(p1.__add__(p2))

print("\n Are P1 and P2 equal ?")
print(p1.__eq__(p2))

print("\n Scalar Multiplication of P1 by 3")
print(p1.__mul__(3))



