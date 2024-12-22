#create a class 'Person' that has an instance method setname that accepts and set the name given by user also a method to display name
#create another class 'Student' that has an instance method setdetail that accepts age and class and sets to respective variable also a function to display them
#create an object of an student class and set name=Nilesh, age=22 and class=BIM and display the details
class person:
    def setname(self,name):
        self.name=name
    
    def displayname(self):
        print("Name is",self.name)
       
class student(person):
    def setdetail(self,age,classs):
        self.age=age
        self.classs=classs
    def displaydetail(self):
        print("Age is:",self.age)
        print("Class is::",self.classs)
s1=student()
a=input("Enter your name:")
s1.setname(a)
s1.displayname()
b=int(input("Enter your age:"))
c=input("Enter your Class:")
s1.setdetail(b,c)
s1.displaydetail()
