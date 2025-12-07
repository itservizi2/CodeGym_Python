# Ternary Operator

# Write a program that asks the user for a number and uses the ternary operator to check whether it is even or odd.
# Display the appropriate message.

print("insert a number :")
number = int(input())
number_type = "even" if number % 2 == 0 else "odd"
print(f"Number {number} is {number_type}.")

