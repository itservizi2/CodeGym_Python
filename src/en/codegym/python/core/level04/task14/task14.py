# Random Argument

# Write a function print_random(a, b, c) that prints a randomly selected argument passed to it.
import random
def print_random(a, b, c):
    random_arg = random.choice([a, b, c])
    print(random_arg)
print_random(1,2,3)
