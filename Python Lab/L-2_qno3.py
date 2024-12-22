a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if b>a and c>a:
    print(f"{a} is smallest among the three")
elif a>b and c>b:
    print(f"{b} is smallest among the three")
else:
    print(f"{c} is smallest among the three")
