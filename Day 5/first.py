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
