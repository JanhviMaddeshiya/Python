#   Print the reverse order series  using a while loop

a = 10

while a >= 1:
    print(a)
    a -= 1

# Create a code that describe the use of break statement in while loop

count = 0

while True:
    count += 2
    print("Counter:", count)

    if count == 10:
        print("Counter has reached 5. Exiting the loop.")
        break  


# Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.

text = "Python"

i = 0

length = len(text)

while i < length:
    print(text[i])
    i += 1

print("Length of the string:", length)

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