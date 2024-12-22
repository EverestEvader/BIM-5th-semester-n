def add(x, y):
    """Add two numbers and return the result"""
    return x + y

def subtract(x, y):
    """Subtract second number from first number and return the result"""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result"""
    return x * y

def divide(x, y):
    """Divide first number by second number and return the result"""
    return x / y

def calculator():
    """Main calculator function that handles the menu and user input"""
    while True:
        # Display menu options
        print("\n==== Simple Calculator ====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        try:
            # Get user's choice
            choice = input("\nEnter choice (1-5): ")
            
            # Exit condition
            if choice == '5':
                print("Thank you for using the calculator!")
                break
            
            # Validate choice
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please enter a number between 1 and 5")
                continue
            
            # Get input numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on choice
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
                
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
                
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} × {num2} = {result}")
                
            elif choice == '4':
                try:
                    # Handle division by zero
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero!")
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
                except ZeroDivisionError as e:
                    print(f"\nError: {e}")
        
        except ValueError:
            # Handle invalid number inputs
            print("\nError: Please enter valid numbers!")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"\nAn unexpected error occurred: {e}")

# Start the calculator program
if __name__ == "__main__":
    calculator()
