# Summing all numbers

# Write a function sum_numbers(*args: int) -> int that takes any number of integers as arguments and
# returns their sum.
# Then write a program that calls this function with different sets of arguments and prints the result.

def sum_numbers(*args: int) -> int:
    suma = 0
    for numbers in args:
        suma = suma + numbers
    return suma
print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2, 3, 4))
print(sum_numbers(1, 2, 3, 5))
