# Sorting strings by length

# Write a program that creates a list of 5 strings, entered by the user.
# Then the program should sort the list by the lengths of the strings and output the sorted list.

my_list = input("Enter 5 strings separated by spaces: ").split()
my_list = my_list[:5]
my_list.sort(key = len)
print(my_list)

