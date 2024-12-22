#a = int(input("Enter any number:"))
#b = int(input("Enter any number:"))

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a / b

