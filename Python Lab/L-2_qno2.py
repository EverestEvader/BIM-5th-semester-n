# Input a year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year using the ternary operator
is_leap_year = "Leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a leap year"

# Display the result
print(f"{year} is a {is_leap_year}.")