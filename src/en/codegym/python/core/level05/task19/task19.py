# Simple and complex at the same time

# Create 5 tuples with different lengths: 0 elements, 1 element, 5 elements, 100 elements, 1000 elements.
# Print them on the screen.

tuple0 = ()
tuple1 = (1,)
tuple2 = (1,2,3,4,5)
tuple3 = tuple(range(1, 101))
tuple4 = tuple(range(1, 1001))
print("Tuple0 (length:", len(tuple0), "):", tuple0)
print("Tuple1 (length:", len(tuple1), "):", tuple1)
print("Tuple2 (length:", len(tuple2), "):", tuple2)
print("Tuple3 (length:", len(tuple3), "):", tuple3)
print("Tuple4 (length:", len(tuple4), "):", tuple4)


