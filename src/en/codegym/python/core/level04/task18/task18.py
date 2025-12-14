# Found a Cat

# Write a function create_cat_profile(name, age, breed="Unknown") that takes a name, age, and an optional
# parameter "breed" (default is "Unknown").
# The function should print the cat's profile in the format "Name: [name], Age: [age], Breed: [breed]".
# Then write a program that calls this function with various parameters.

def create_cat_profile(name, age, breed="Unknown"):
    print(f"Name: {name}, Age: {age}, Breed: {breed}")

create_cat_profile("Alice", 2, "munckin")
create_cat_profile("John", 3, "british")
create_cat_profile("Jessica", 1)
