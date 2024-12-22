#exception handling
def divide_numbers():
    try:
        num1 =int(input("Enter any number : "))
        num2 =int(input("Enter any number : "))
        result = num1 / num2
    
    except ZeroDivisionError:
        print("::*ERROR*:: Division by zero not allowed !")
    except ValueError:
        print("::*ERROR*:: Enter valid number")
    else:
        print(f"The division of {num1} by {num2} results : {result}")
    finally:
        print("Division operation complete")

divide_numbers()