# Maximalist

# Write a function find_max(a, b) that takes two numbers as arguments and returns the greater of them.
# If the numbers are equal, the function should return either.
# Then write a program that prompts the user for two numbers, calls this function, and prints the result.

import random
def find_max(a, b):
    if a == b:
        return random.choice([a, b])
    return a if a > b else b
a = int(input("Insert number a: "))
b = int(input("Insert number b: "))
print("Maximum is:", find_max(a, b))

