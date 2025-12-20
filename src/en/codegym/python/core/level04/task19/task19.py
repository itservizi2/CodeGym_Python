# Using a Global Variable

# Write a program that has a global variable counter, initially set to 0.
# Write a function increment_counter() that increments this variable by 1 every time it's called.
# Then, call this function several times and print the value of the global variable counter.

counter = 0
def increment_counter():
    global counter
    counter += 1
    return counter
increment_counter()
print(increment_counter())
print(increment_counter())


