#lab 8.4
#WAP that illustrates multilevel inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id
    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")
class Manager(Employee):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age, emp_id)
        self.department = department
    def display(self):
        super().display()
        print(f"Department: {self.department}")
#instance for manager 
M1=Manager("Aakriti", 21, "EMP2002", "IT")
print("Manager Information:")
M1.display()