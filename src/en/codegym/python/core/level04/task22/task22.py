# Cat Profile

# Write a function create_cat_profile(name: str, age: int, **kwargs: str) -> None,
# which takes the name and age of a cat as required parameters,
# as well as an arbitrary number of named parameters (such as breed, color, etc.).
# The function should print the cat's profile, including all passed parameters.

def create_cat_profile(name: str, age: int, **kwargs: str) -> None:
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_cat_profile("Murzik", 3, breed="Siamese", color="Black")
create_cat_profile("Barsik", 5, country="China", hobby="Catching mice")
