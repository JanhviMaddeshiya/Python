# Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.

text = "Python"

i = 0

length = len(text)

while i < length:
    print(text[i])
    i += 1

print("Length of the string:", length)