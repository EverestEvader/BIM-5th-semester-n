#LAB 8.6
#WAP to illustrate use of protected and private data members.
#create a class Person with default constructor with name and age,
#set name as protected member and age as private member
#display name and age
#Create a class student that inherits Person and new member student_id,
#try to access the protected and private members of the Base class
class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def display(self):
        print(f"Name: {self._name}")
        print(f"Age: {self.__age}")

class Student(Person):
    def __init__(self,name, age, Student_ID):
        super().__init__(name, age)
        self.Student_ID = Student_ID
    
    def displays(self):
        print(f"\nStudent ID: {self.Student_ID}")
        print(f"Name (from Parent class): {self._name}")
    
    #accessing private members will result in error so 
        try:
            print(f"Age (from parent class): {self.__age}")
        except AttributeError:
            print("Cannot access private member directly in Student class")

p1= Person("Nilesh", 22)
p1.display()
st = Student("Ram", 20, "S12")
st.displays()
