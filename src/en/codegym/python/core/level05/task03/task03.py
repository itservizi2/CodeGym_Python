# Random Program

# Write a program that creates a list of random elements, prints the length of the list, and then the first and last
# elements of the list.
import random
mylist = [random.randint(1, 25) for _ in range(5)]
print(f" list length is : {len(mylist)}")
print(f" first element in list is: {mylist[0]}" )
print(f" last element in list is: {mylist[-1]}" )
