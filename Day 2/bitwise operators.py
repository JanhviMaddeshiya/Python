# Define two integers
a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND
result_and = a & b
print("a & b:", result_and)

# Bitwise OR
result_or = a | b
print("a | b:", result_or)

# Bitwise XOR
result_xor = a ^ b
print("a ^ b:", result_xor)

# Bitwise NOT (inverts bits and adds 1 for negative value)
result_not = ~a
print("~a:", result_not)

# Bitwise LEFT SHIFT
result_left_shift = a << 2
print("a << 2:", result_left_shift)

# Bitwise RIGHT SHIFT
result_right_shift = a >> 2
print("a >> 2:", result_right_shift)