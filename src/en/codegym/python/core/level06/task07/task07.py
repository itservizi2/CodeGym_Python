# Random Sets

# Write a program that generates:
# One list of random elements from 0 to 99.
# A second list of random elements from 50 to 125.
# Then convert the lists into sets.
# Add the first set to the second.
# Display the number of elements in the resulting set on the screen.

import random
first_list = [random.randint(0, 99) for _ in range(10)]
second_list = [random.randint(50, 125) for _ in range (10)]
first_set = set(first_list)
second_set = set(second_list)
combined_set = first_set | second_set
print(f"number of combined elements: {len(combined_set)}")
