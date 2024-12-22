#Lab 8.3
#WAP to illustrate the concept of creating a basic inheritance using any program.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display(self):
        super().display()
        print(f"No of doors: {self.doors}")
#object for vehicle
V1=Vehicle("Toyota", "Supra")
print("Vehicle Information:")
V1.display()

#object for car
C1=Car("Honda" ,"Civic", 4)
print("\nCar Information: ")
C1.display()