class Student:
    clgname = 'BMC'
    
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print("Name: ", self.name)
        print("College Name: ", self.clgname)
    
    @classmethod
    def change_clgname(cls, new_clgname):
        cls.clgname = new_clgname

# Creating an instance of Student
s1 = Student("Nilesh")
s1.display()

# Changing the college name using class method
Student.change_clgname("BKT")
s1.display()
