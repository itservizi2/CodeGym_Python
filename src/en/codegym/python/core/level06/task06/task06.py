# Square Generator

# Write a program that creates a set of squares of numbers from 1 to 10 using a set comprehension.
# The program should print the resulting set.

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
square_set = {x**2 for x in my_set}
print(square_set)
