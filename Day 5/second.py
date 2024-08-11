# Declare a square() function with one parameter. Then call the function ans pass one number and display the square of that number

def square(a):
    sq = a * a
    return sq

num = int(input("Enter a number: "))

print(square(num))