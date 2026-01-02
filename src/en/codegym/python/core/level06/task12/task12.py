# Replacement

# Write a program that creates a set containing names of several fruits.
# The program should output the fruits to the screen.
# Then the program should ask the user for the index (considering the order of output to the screen)
# and a new fruit name for replacement.
# Then find the fruit by its index, replace it with the new name, and output the updated set.

my_set = {"apple", "banana", "cherry", "orange", "strawberry"}
my_list = list(my_set)   # convert to list for indexing

print("Available fruits:")
for idx, fruit in enumerate(my_list):
    print(f"{idx}: {fruit}")

while True:
    user_input_index = int(input(f"Insert an index (0 to {len(my_list)-1}): "))    # Ask for index only
    if 0 <= user_input_index < len(my_list):
        user_input_fruit = input("Insert a fruit: ")
        my_list[user_input_index] = user_input_fruit
        my_set = set(my_list)   # convert back to set
        print(" Updated set:", my_set)
        break
    else:
        print(" Invalid index! Please try again.")
