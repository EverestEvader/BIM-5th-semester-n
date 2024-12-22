#operator overloading in python 
class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,o):
        return self.a + o.a

o1 = A(10)
o2 = A(20)
o3 = A("Python")
o4 = A("_Programming")

print(o1 + o2)
print(o3 + o4)