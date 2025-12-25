# Clean the list

# Write a program that creates a list of 10 random numbers in the range from 1 to 20.
# Then the program should remove all even numbers from the list using a loop.
# The program should print the original and updated lists.

import copy
import random
my_list = [random.randint(1,20) for _ in range(10)]
new_my_list = copy.deepcopy(my_list)
for item in new_my_list[:]:
    if item % 2 == 0:
        new_my_list.remove(item)
print(my_list)
print(new_my_list)
