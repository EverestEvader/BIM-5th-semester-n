"""LAB 7:
Create a class car that has :
1. Class attribute country Nepal
2. Initialize a instance method 'setdetail' that accepts b and m as attributes and
    sets brand=b and model=m
3. Define a instance method 'changecountry' that accepts 'c' and sets the
    Country=c for particular object.
4. Define a class method 'chgcoun' that modifies the country attribute for all the
    Objects as 'USA'.
5. Write a function 'show' to display the country, brand, model of object.
6. Create an object car1 and car2.
7. Set the brand and model of car1 to 'BMW' and 'coupe' respectively and 
    display them
8. Repeat step 7 for car2 also.
9. Change the country of car2 to Germany and display it.
10.Change the country variable of all the objects to USA and print
"""
class Car:
    country = "Nepal"  # Class attribute

    def setdetail(self, b, m):
        self.brand = b
        self.model = m

    def changecountry(self, c):
        self.country = c

    @classmethod
    def chgcoun(cls):
        cls.country = "USA"

    def show(self):
        print(f"Country: {self.country}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print()

# Create objects car1 and car2
car1 = Car()
car2 = Car()

# Set details for car1
car1.setdetail("BMW", "coupe")
print("Car 1 details:")
car1.show()

# Set details for car2
car2.setdetail("Toyota", "Camry")
print("Car 2 details:")
car2.show()

# Change country of car2 to Germany
car2.changecountry("Germany")
print("Car 2 after changing country:")
car2.show()

# Change country for all objects to USA
Car.chgcoun()
print("Car 1 after changing country for all objects:")
car1.show()
print("Car 2 after changing country for all objects:")
car2.show()