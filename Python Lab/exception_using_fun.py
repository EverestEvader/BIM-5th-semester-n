#exception handling in python using function
def div_num():
    try:
        a = int(input("Enter any number : "))
        b = int(input("Enter any number : "))
        result = a / b

    except ZeroDivisionError:
        print("ERROR!!. Cannot be divided by ZERO.")
    
    except ValueError:
        print("ERROR!!. Invalid input. Please enter a valid number.")
    
    else:
        print(f"{a} / {b} = {result}")

div_num()