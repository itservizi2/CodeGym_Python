# Union and Intersection

# Write a program that creates two sets from elements entered by the user.
# The program should unite these sets using the union() method and find their intersection using
# the intersection() method.
# The program should output both results

set1 = set(input("insert some elements ").split())
set2 = set(input("insert some other elements ").split())
sets_union = set1.union(set2)
sets_intersection = set1.intersection(set2)
print("union is" , sets_union)
print("intersection  is" ,sets_intersection)
