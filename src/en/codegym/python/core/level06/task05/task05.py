# Clear but random

# Write a program that creates a set of 10 random numbers in the range from 1 to 100.
# The program should get the subset of all even numbers from this set and print it.

import random
my_set = {random.randint(1,100) for _ in range(10)}
print(my_set)
even_set  = set(filter(lambda x: x % 2 == 0, my_set))
print(even_set)
