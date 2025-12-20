# The Fifth Element.

# Write a program that creates a list of 5 elements requested from the user.
# The program should display the list, then ask the user for an index of an element and display the value
# of the element at that index.

mylist = []
for i in range(5):
    user_input = int(input("Enter a number: "))
    mylist.append(user_input)
print("Current list:", mylist)
for j in range(5):
    el_index = int(input("Enter the index of the element you want: "))
    try:
        print(f"Element at index {el_index} is: {mylist[el_index]}")
        break
    except IndexError:
        print("Inserted index not in range")
