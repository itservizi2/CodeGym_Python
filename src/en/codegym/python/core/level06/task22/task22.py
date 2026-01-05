# Reordering.

# Write a program that takes a string of several words separated by commas from the user.
# The program should:
# Split the string into a list of words using the split() method.
# Join this list of words into a single string using the join() method, separating the words with spaces.
# Print the results of each operation.

my_string = input("Enter some strings separated by commas: ")
my_string_split = my_string.split(',')
my_string_join = ' '.join(my_string_split)
print(my_string_split)
print(my_string_join)
