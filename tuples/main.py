"""A tuple is a data structure, a data type that will allow us to store different data types and will be 
useful to consult values. In contrast to lists, tuples are immutable: once we define one, it will remain 
the same for the rest of the program. To create a tuple, we need to make use of parentheses and place 
inside them the items that we want to store, separated by a comma, at the moment of defining it"""
#Note: We can store tuples inside a tuple
tuple_one = ("Hello", 10, 3.14, True, [1, 2, 3], (4, 5, 6))
print(tuple_one)

"""The main advantage of using tuples over lists is that tuples are much faster in terms of obtaining 
items. Since they are immutable, Python stores them in a memory space for reading objects"""
