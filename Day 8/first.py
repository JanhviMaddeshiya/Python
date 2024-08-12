string = "To change the overall look of your document. To change the look available in the gallery"

words = string.split()
print(words)

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word, count in count.items():
    print(f"{word}: {count}")



# Write a Python program to remove a newline in Python
# String = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"

new_string = string.replace('\n', '')

print(new_string)



# Write a Python program to reverse words in a string
# String = “Deeptech Python Training”




# Write a program in python to Count all letters, digits, and special
# symbols from a given string


def count_characters(string):
  letters = 0
  digits = 0
  special_symbols = 0

  for char in string:
    if char.isalpha():
      letters += 1
    elif char.isdigit():
      digits += 1
    else:
      special_symbols += 1

  return letters, digits, special_symbols

input_string = "Hello, World! 123$"
result = count_characters(input_string)
print("Letters:", result[0])
print("Digits:", result[1])
print("Special symbols:", result[2])