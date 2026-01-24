# Dictionary.

# Write a program that creates a dictionary with information about a person (e.g., name, age, and city)
# in three different ways:
# Using curly braces {}.
# Using the dict() function with a sequence of key-value pairs.
# Using the dict() function with named arguments.
# The program should print all three dictionaries.

person_dict_braces = {"name" : "Bob",
                    "age" : 25,
                    "job" : "engineer"}

person_key_value  = dict([("name", "Peter"), ("age", 20), ("job", "Dj")])
person_named_arguments = dict(name="Trevis", age=28, job="mechanic")

print(person_dict_braces)
print(person_key_value)
print(person_named_arguments)
