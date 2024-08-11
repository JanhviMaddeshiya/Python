# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division

def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

num = float(input("Enter the numerator: "))
den = float(input("Enter the denominator: "))

result = div(num, den)
print(f"The division is: {result}")


# Declare a square() function with one parameter. Then call the function ans pass one number and display the square of that number

def square(a):
    sq = a * a
    return sq

num = int(input("Enter a number: "))

print(square(num))

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


# Accept a name from the user and display the lower case using lower() funtion

name = input("Enter your name: ")

lowercase = name.lower()

print("Your name in lowercase is:", lowercase)
