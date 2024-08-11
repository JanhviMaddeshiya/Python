# Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.

def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")