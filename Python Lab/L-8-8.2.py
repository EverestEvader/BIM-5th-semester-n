#lab 8/ 8.2
#WAP that implements method overloading in python
from multipledispatch import dispatch
class mathOps:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b
    
    @dispatch(float, float)
    def add(self, a, b):
        return a + b
    
    @dispatch(int,float)
    def add(self, a, b):
        return a + b
    
    @dispatch(float, int)
    def add(self, a, b):
        return a + b
    
    #object
mathsops = mathOps()
result_int = mathsops.add(1 , 2)
print (f"Addition of two integer : {result_int}")
print()

result_float = mathsops.add(5.5 , 4.5)
print (f"Addition of two float : {result_float}")
print()

result_int_float = mathsops.add(10 , 20.5)
print (f"Addition of integer and float : {result_int_float}")
print()

result_float_int = mathsops.add(10.123 , 20)
print (f"Addition of float and integer : {result_float_int}") 

