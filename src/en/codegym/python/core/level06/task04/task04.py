# Detective

# Write a function set_detector that iterates over the list (tuple) of its arguments and determines
# whether there is a set among them.
# Call the function set_detector with different sets of parameters (with and without a set).

def set_detector(*args):
    for arg in args:
        if isinstance(arg, set):
            return True
    return False
# Case 1: Arguments include a set
print(set_detector(1, 2, {3, 4}, "hello"))
# Case 2: Arguments do not include a set
print(set_detector(1, 2, [3, 4], "hello"))
# Case 3: Multiple sets
print(set_detector({1}, {2, 3}, "test"))
# Case 4: No arguments at all
print(set_detector())

