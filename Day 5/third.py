# Using max() and min() functions display the maximum and minimum of 5 random numbers

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))

max_value = max(num1, num2, num3, num4, num5)
min_value = min(num1, num2, num3, num4, num5)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
