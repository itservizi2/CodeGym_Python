# A Word and a Link

# Write a program that creates two lists, assigns one of them to another variable, and checks if both
# variables point to the same object.
# Use the is operator to check the references.

list1 = [1 ,2, 3]
list2 = list1
print(list1 is list2)
