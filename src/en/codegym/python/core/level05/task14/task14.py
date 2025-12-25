# Filtering

# Write a program that creates a list of 20 random numbers in the range from 1 to 100 using List Comprehension.
# Then, using List Comprehension, create a new list containing only the even numbers from the original list.
# The program should output both lists.

from random import randrange
my_list = [randrange(1,100) for i in range(20)]
my_list_even = [element for element in my_list if element % 2 == 0]
print(my_list)
print(my_list_even)
