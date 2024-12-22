class Person:
    def __init__(self, name, age):
        self._name = name  # Protected member
        self.__age = age   # Private member

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self.__age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name (from parent class): {self._name}")

        # Accessing private member will result in an error
        try:
            print(f"Age (from parent class): {self.__age}")
        except AttributeError:
            print("Cannot access private member directly in Student class")

# Creating an instance of Person
person = Person("Nilesh", 22)
person.display_info()

# Creating an instance of Student
student = Student("Ram", 20, "S1")
student.display_student_info()

