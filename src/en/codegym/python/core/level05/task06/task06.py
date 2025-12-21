# String Search

# Write a program that creates a list of 10 elements.
# The program asks the user to enter a string and then checks if it is in the list.

my_list = [1, 2, 3, "a","s","d","g","o","p","n"]
element = input("enter a string : ")
if element in my_list:
    print(f"{element} is in the list")
else:
    print(f"{element} is not in the list")

