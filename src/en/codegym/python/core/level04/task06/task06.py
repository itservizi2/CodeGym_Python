# Random Average
# Write a program that generates 10 random numbers in the range from 1 to 100 using the random library.
# Then calculate their average value and print it on the screen.

import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
average_value = sum(numbers) / len(numbers)
print(f"average value of random numbers is : {average_value} ")
