#WAP that implements all the bitwise operator of python. You must take required inputs from user
# Input two integers from the user
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Bitwise AND
and_ = a & b
print(f"Bitwise AND ({a} & {b}): {and_}")
#print(f"Binary: {a:08b} & {b:08b} = {and_:08b}")

# Bitwise OR
or_ = a | b
print(f"Bitwise OR ({a} | {b}): {or_}")
#print(f"Binary: {a:08b} | {b:08b} = {or_:08b}")

# Bitwise XOR
xor_ = a ^ b
print(f"Bitwise XOR ({a} ^ {b}): {xor_}")
#print(f"Binary: {a:08b} ^ {b:08b} = {xor_:08b}")

# Bitwise NOT
not_a = ~a
not_b = ~b
print(f"Bitwise NOT of {a}: {not_a}")
#print(f"Binary: ~{a:08b} = {not_a:08b}")
print(f"Bitwise NOT of {b}: {not_b}")
#print(f"Binary: ~{b:08b} = {not_b:08b}")

# Left shift
left_shift_a = a << 2
left_shift_b = b << 2
print(f"Left shift {a} by 2: {left_shift_a}")
#print(f"Binary: {a:08b} << 2 = {left_shift_a:08b}")
print(f"Left shift {b} by 2: {left_shift_b}")
#print(f"Binary: {b:08b} << 2 = {left_shift_b:08b}")

# Right shift
right_shift_a = a >> 2
right_shift_b = b >> 2
print(f"Right shift {a} by 2: {right_shift_a}")
#print(f"Binary: {a:08b} >> 2 = {right_shift_a:08b}")
print(f"Right shift {b} by 2: {right_shift_b}")
#print(f"Binary: {b:08b} >> 2 = {right_shift_b:08b}")