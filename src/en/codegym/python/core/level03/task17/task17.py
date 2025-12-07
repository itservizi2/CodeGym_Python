# Odd

# Write a program that prints numbers from 1 to 100, skipping even numbers.
# Use a while loop and the continue statement to skip even numbers.

number = 0
while number <= 99:
    number += 1
    if number % 2 == 0:
        continue
    print(number)


