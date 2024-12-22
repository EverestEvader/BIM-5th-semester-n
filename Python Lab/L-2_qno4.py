# Display the menu
print("Menu Options:")
print("1. Login")
print("2. Forgot Password")
print("3. Sign Up")
print("4. Exit")

# Get user's choice
choice = int(input("\nEnter your choice (1-4): "))

# Use match-case (Python 3.10+)
match choice:
    case 1:
        print("You chose to login.")
    case 2:
        print("You chose to reset your password.")
    case 3:
        print("You chose to create a new account.")
    case 4:
        print("You chose to exit. Goodbye!")
    case _:
        print("Invalid choice. Please try again.")