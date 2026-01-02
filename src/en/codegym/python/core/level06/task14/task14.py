# Set Difference

# Write a program that creates two sets, each consisting of 10 random numbers.
# The first set contains random numbers in the range from 1 to 20, and the second set contains
# random numbers in the range from 10 to 30.
# The program should find the difference of the first set with the second using the difference() method.
# And the symmetric difference using the symmetric_difference() method.
# The program should print both results.

import random
set1 = {random.randint(1,20) for _ in range(10)}
set2 = {random.randint(10,30) for _ in range(10)}
sets_diff = set1.difference(set2)
sets_sim_diff = set2.symmetric_difference(set1)
print(f" diff: ", sets_diff)
print(f" sim diff: ", sets_sim_diff)
