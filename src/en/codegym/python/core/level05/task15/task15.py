# Sorting

# Write a program that creates a list of 10 random numbers in the range from 1 to 100.
# Then sort it in ascending and descending order.
# The program should print the original list, the sorted list in ascending order,
# and the sorted list in descending order.

import random
my_list = [random.randint(1,100) for _ in range(10)]
sorted_my_list_asc = sorted(my_list)
sorted_my_list_desc = sorted(my_list, reverse=True)
print(my_list)
print(sorted_my_list_asc)
print(sorted_my_list_desc)


