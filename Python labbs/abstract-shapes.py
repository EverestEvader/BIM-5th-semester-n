from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def get_input(self):
        """Get dimensions from user"""
        pass
    
    @abstractmethod
    def calculate_area(self):
        """Calculate area of the shape"""
        pass
    
    @abstractmethod
    def display(self):
        """Display the shape's details"""
        pass

class Square(Shape):
    def __init__(self):
        self.side = 0
        self.area = 0
    
    def get_input(self):
        while True:
            try:
                self.side = float(input("Enter the side length of square: "))
                if self.side <= 0:
                    raise ValueError("Side length must be positive")
                break
            except ValueError as e:
                print(f"Invalid input! {e}")
    
    def calculate_area(self):
        self.area = self.side ** 2
    
    def display(self):
        print(f"\nSquare Details:")
        print(f"Side length: {self.side}")
        print(f"Area: {self.area:.2f} square units")

class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0
        self.area = 0
    
    def get_input(self):
        while True:
            try:
                self.length = float(input("Enter the length of rectangle: "))
                self.width = float(input("Enter the width of rectangle: "))
                if self.length <= 0 or self.width <= 0:
                    raise ValueError("Dimensions must be positive")
                break
            except ValueError as e:
                print(f"Invalid input! {e}")
    
    def calculate_area(self):
        self.area = self.length * self.width
    
    def display(self):
        print(f"\nRectangle Details:")
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area:.2f} square units")

class Triangle(Shape):
    def __init__(self):
        self.base = 0
        self.height = 0
        self.area = 0
    
    def get_input(self):
        while True:
            try:
                self.base = float(input("Enter the base of triangle: "))
                self.height = float(input("Enter the height of triangle: "))
                if self.base <= 0 or self.height <= 0:
                    raise ValueError("Dimensions must be positive")
                break
            except ValueError as e:
                print(f"Invalid input! {e}")
    
    def calculate_area(self):
        self.area = 0.5 * self.base * self.height
    
    def display(self):
        print(f"\nTriangle Details:")
        print(f"Base: {self.base}")
        print(f"Height: {self.height}")
        print(f"Area: {self.area:.2f} square units")

def display_menu():
    """Display the menu options"""
    print("\n=== Shape Area Calculator ===")
    print("1. Calculate Square Area")
    print("2. Calculate Rectangle Area")
    print("3. Calculate Triangle Area")
    print("4. Exit")

def main():
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            
            if choice == 4:
                print("Thank you for using the Shape Area Calculator!")
                break
            
            if choice not in [1, 2, 3]:
                print("Invalid choice! Please select between 1-4")
                continue
            
            # Create appropriate shape object based on choice
            shape = None
            if choice == 1:
                shape = Square()
            elif choice == 2:
                shape = Rectangle()
            elif choice == 3:
                shape = Triangle()
            
            # Process the shape
            shape.get_input()
            shape.calculate_area()
            shape.display()
            
        except ValueError:
            print("Invalid input! Please enter a valid choice (1-4)")

if __name__ == "__main__":
    main()
