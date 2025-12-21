# Clear List

# Write a program that creates a list of 10 integers.
# Using a for loop, replace all even elements of the list with the string "even".
# The program should output the updated list.

my_list = [1,2,3,4,5,25,62,654,92,121]
for index, element in enumerate(my_list):
    if element % 2 == 0:
        my_list[index] = "even"
print(my_list)
