# Cat Frenzy

# Write a program that maintains a set of the 5 most popular cat names.
# The user must try to guess them. When they guess a cat's name, it is removed from the set.
# The goal of the game is to guess all the cat names in as few attempts as possible.

cat_name_set = {"snejok", "pushok", "markiz", "baron", "barsik"}
counter = 0
while cat_name_set:
    user_input = input("Enter a name: ")
    counter += 1
    if user_input in cat_name_set:
        cat_name_set.remove(user_input)
        print(f"Correct! '{user_input}' removed. Remaining names: {len(cat_name_set)}")
    else:
        print("Not found, try again.")
print("All names guessed!")
print("Number of attempts:", counter)
