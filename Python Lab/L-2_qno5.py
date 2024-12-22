# Get a number from the user
number = int(input("Enter a number greater than 1: "))

# Check if the number is prime or composite
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is a composite number.")
            #print(f"It is divisible by {i}.")
            #break
    else:
        print(f"{number} is a prime number.")
else:
    print("Please enter a number greater than 1.")