#exception handling example
a = int(input("Enter any number = "))
b = int(input("Enter any number = "))
try:
    c = a / b
except ZeroDivisionError:
    print("++++_ERROR_++++ Division cannot be performed by [ZERO (0)] !")
except ValueError:
    print("++++_ERROR_++++ Enter a valid number !")
else:
    print(f"Division [ {a}/{b} ] = {c}")
finally:
    print("::Division operation completed::")