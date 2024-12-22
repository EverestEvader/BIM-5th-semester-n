##LAB 8.5
#WAP to illustrate use of protected and private data members.
class BaseClass:
    def __init__(self):
        self._protected_member = "I am protected"
        self.__private_member = "I am private"
    def display(self):
        print("Inside base class")
        print("Protected Member: ", self._protected_member)
        print("Private member: ", self.__private_member)
class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        #accessing protected member in derived class
        print("Accessing Protected Member in derived class: ",self._protected_member)

        #accessing private member in derived class
        try:
            print("Accessing Private Member in derived class: ", self.__private_member)
        except AttributeError:
            print("Cannot access Private Member directly in derived class")

#instance for Base Class
BC = BaseClass()
BC.display()

#instance for Derived Class
DC = DerivedClass()
DC.display()