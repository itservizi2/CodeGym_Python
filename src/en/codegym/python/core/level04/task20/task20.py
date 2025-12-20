# Using a nonlocal variable

# Write a program with a nested function.
# The outer function outer_function() should declare a variable x and assign it the value 10.
# The inner function inner_function() should increase the value of the variable x by 5 using
# the nonlocal statement.
# Then call the inner function and print the value of the variable x in the outer function.

def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x += 5
        return x
    inner_function()
    print(x)
outer_function()



