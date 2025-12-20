# Waiting for stop

# Write a program that creates an empty list using square brackets [] and adds elements to it, requested from the user.
# The input of elements should continue until the user enters the word "stop". Then the program should print
# the final list.

mylist = []
user_input = input("Enter a number or letter: ")
while user_input != "stop":
    mylist.append(user_input)
    user_input = input("Enter a number or letter: ")
print(mylist)

