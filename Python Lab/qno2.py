#WAP that accepts string from user and checks either there are letter 'y' and 't' on the input string or not
# Input a string from the user
input_st = input("Enter a string: ")

# Convert the string to lowercase for case-insensitive comparison
input_st = input_st.lower()

# Check if 'y' and 't' are in the string
y_in = 'y' in input_st
t_in = 't' in input_st

# Display the results
if y_in and t_in:
    print("Both 'y' and 't' are present in the string.")
elif y_in:
    print("Only 'y' is present in the string.")
elif t_in:
    print("Only 't' is present in the string.")
else:
    print("Neither 'y' nor 't' is present in the string.")