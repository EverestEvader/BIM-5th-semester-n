class BaseClass:
    def __init__(self):
        self._protected_member = "I am a protected member"
        self.__private_member = "I am a private member"
    
    def display_members(self):
        print("Inside BaseClass")
        print("Protected Member:", self._protected_member)
        print("Private Member:", self.__private_member)


class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        # Accessing protected member
        print("Accessing protected member in DerivedClass:", self._protected_member)
        
        # Accessing private member will result in an error
        try:
            print("Accessing private member in DerivedClass:", self.__private_member)
        except AttributeError:
            print("Cannot access private member directly in DerivedClass")

    def access_private_member(self):
        # Accessing private member using name mangling
        print("Accessing private member using name mangling in DerivedClass:", self._BaseClass__private_member)

# Creating an instance of BaseClass
base_instance = BaseClass()
base_instance.display_members()

# Creating an instance of DerivedClass
derived_instance = DerivedClass()
derived_instance.access_private_member()

# Accessing protected member from outside the class
print("Accessing protected member from outside:", base_instance._protected_member)

# Attempting to access private member from outside the class
try:
    print("Accessing private member from outside:", base_instance.__private_member)
except AttributeError:
    print("Cannot access private member directly from outside")

# Accessing private member using name mangling
print("Accessing private member using name mangling from outside:", base_instance._BaseClass__private_member)
