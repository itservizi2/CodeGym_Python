# Characters in a string

# Write a program that takes a string input from the user, prints its length,
# and then prompts the user for an index.
# The program should print the character of the string at that index.
# If the index is out of bounds, the program should print an appropriate message.

my_string = input("enter your string :")
print(f" string length is : ", len(my_string))
my_input = int(input(f" insert an index: "))
if  0<= my_input < len(my_string):
    print(f" the character at position {my_input} is: ", my_string[my_input])
else:
    print(f" index out of range ")
