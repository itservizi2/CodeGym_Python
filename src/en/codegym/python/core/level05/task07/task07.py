# Who wants more?

# Write a program that creates an empty list, then prompts the user for 5 elements and adds them to the list
# using the append() method.
# After that, the program should output the final list.

my_list =[]
for i in range(5):
    element = input("enter an element : ")
    my_list.append(element)
print(my_list)
