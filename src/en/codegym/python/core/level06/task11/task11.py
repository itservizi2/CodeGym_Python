# Indexing

# Write a program that creates a set of random numbers ranging from 1 to 50.
# Then the program should output all elements of the set along with their "indexes" using the enumerate() function.

import random
my_set = {random.randint(1,50) for _ in range(12)}
for index, element in enumerate(my_set):
    print(f"Index: {index}, Element: {element}")
