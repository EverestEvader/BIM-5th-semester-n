#WAp using functions to """"""
#1 Accepts number from user and add them
print ("Accepts number from user and add them")
def add(x,y):
    return x+y
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print (f"The sum of {x} and {y} is:", add(x,y))

#accept any string from user and check either a is in the string
print ("accept any string from user and check either a is in the string")
s=input("Enter any string value:")
def check_stri(s):
    if 'a' in s:
        print ("a is present in the string")
    else:
        print ("a is not present in the string")
check_stri(s)

#Wap to add two numbers and print the sum by returning the value to function call
print ("Wap to add two numbers and print the sum by returning the value to function call")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
def sum(a,b):
    print (a+b)
sum(a,b)


#WAP to find factorial of number
print ("#WAP to find factorial of number")
n=int(input("Enter any number to find factorial"))
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n - 1) 
print (f"Factorial of {n} is",factorial(n))