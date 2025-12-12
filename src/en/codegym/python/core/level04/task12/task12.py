# Uncertainty

# Write a program that asks the user for two numbers.
# If the user doesn't provide a value (empty string), use the default value None for that number.
# Calculate and print the sum of these numbers.

num1 = input("Enter a number (or leave blank): ")
num2 = input("Enter another number (or leave blank): ")
num1 = int(num1) if num1 else None
num2 = int(num2) if num2 else None
if num1 is None or num2 is None:
    print("Sum of the numbers is unknown")
else:
    print("The sum is:", num1 + num2)


