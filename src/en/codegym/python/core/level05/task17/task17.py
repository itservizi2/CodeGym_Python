# Sorting Without Sorting

# Write a program that creates a list of 10 random numbers ranging from 1 to 100.
# Then, the program should create a copy of this list and sort the copy in ascending order without
# modifying the original list.
# The program should output both the original and the sorted lists.

import random
import copy
my_list = [random.randint(1,100) for _ in range(10)]
new_my_list = copy.deepcopy(my_list)
print(my_list)
print(sorted(new_my_list))
