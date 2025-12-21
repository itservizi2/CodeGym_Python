# First Out

# Write a program that creates a list of 5 elements, asks the user for an element to delete,
# and removes the first found element from the list using the remove() method.
# The program should output the updated list.

my_list = [1,2,3,4,5]
user_input = int(input("insert element to delete : "))
my_list.remove(user_input)
print(my_list)
