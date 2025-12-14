# Calculating Factorial

# Write a function factorial(n) that takes an integer n and returns its factorial. If n is 0,
# the function should return 1.
# The factorial of a number n is denoted as n! and is the product of all numbers from 1 to n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Insert number n: "))
print(f"factorial of {n} is ", factorial(n))
