# Substring extraction.

# Write a program that takes a string from the user and extracts substrings using slices.
# The program should:
# Extract the substring from the 3rd to the 8th character (index) inclusive.
# Extract the substring from the 5th character (index) to the end of the string.
# Print both substrings.

my_string = input("Enter a string: ")
subst1 = my_string[2:9]
subst2 = my_string[4::1]
print(f" substring from the 3rd to the 8th character (index) inclusive: " , subst1)
print(f" substring from the 5th character to the end : " , subst2)
