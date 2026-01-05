# Cleaning

# Write a program that takes a string from the user and performs the following operations:
# Removes spaces at the beginning and end of the string using the strip() method.
# Converts all characters of the string to lowercase using the lower() method.
# Converts all characters of the string to uppercase using the upper() method.
# Prints the results of each operation.

my_string = input("insert a string: ")
no_space = my_string.strip()
lower_case= my_string.lower()
upper_case = my_string.upper()
print(no_space)
print(lower_case)
print(upper_case)
