#lab 8.1
#WAP to illustrate the use of parameterized constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
p1 = Person("Nilesh", 22)
p2 = Person("Ram", 32)
p1.display()
p2.display()