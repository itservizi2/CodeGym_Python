# Eraser

# Write a program that creates a list of 10 elements, then replaces the elements from the third to
# the fifth with a single value requested from the user.
# The program should output the updated list.

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
user_input = input("enter an element : ")
my_list[2:5] = [user_input]
print(my_list)
