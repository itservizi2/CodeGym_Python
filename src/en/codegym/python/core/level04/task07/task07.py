# Round Math Wizard

# Write a program that asks the user for a floating-point number and rounds it down (using math.floor()),
# up (using math.ceil()), and to the nearest whole number (using round()).
# Display the results of all three roundings.

import math
number = float(input("INSERT A NUMBER  "))
number_rounded_down = math.floor(number)
print(f"number rounded down is {number_rounded_down}")
number_rounded_up = math.ceil(number)
print(f"number rounded up is {number_rounded_up}")
round_number = round(number)
print(f"round number is {round_number}")
