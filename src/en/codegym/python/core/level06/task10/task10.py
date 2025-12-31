# Fruit Bowl  

# Write a program that creates a set containing the names of a few fruits.  
# Then the program should ask the user for the name of a fruit to remove and delete it
# from the set using the discard() method.
# The program should output the updated set.  
# If the element is not found, the program should continue execution without an error.  

fruits_set = {"apple", "banana", "cherry", "strawberry", "grapefruit"}
while True:
    user_input = input("Which fruit do you want? ")
    if user_input in fruits_set:
        fruits_set.discard(user_input)
        break
    else:
        print("Not found, try again")
print("set is ", fruits_set)
