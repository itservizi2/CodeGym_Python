# Negative slicing

# Write a program that takes a string from the user and
# performs the following operations using negative indices and slices:
# Extracts the last three characters of the string.
# Extracts the string excluding the last character.
# Reverses the string.
# Displays all three results.

my_string = input("Enter a string: ")
last3 = my_string[-3:]
string_excl_last = my_string[:-1]
reversed_string = my_string[::-1]
print(last3)
print(string_excl_last)
print(reversed_string)
