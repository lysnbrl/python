"""We can zip items to generate tuples. To do this, we need to use the zip() function, with that
function we'll be able to combine values (lists, tuples or both). We can store the result inside 
a new variable"""
list_one = [1, 2, 3]
tuple_one = (10, 20, 30)

"""In the argument we must place the values to be compressed. The zip() function will return a 
zip type object, so we will need to convert that object to a tuple. It is better to convert 
the object to a tuple rather than to a list, for the immutability of tuples"""
result = zip(list_one, tuple_one)
result = tuple(result)

"""When we generate the tuple, we will see that the tuple stores subtuples. Each one of them 
is the combination of the items of the first and the second value (we can place n number of 
values for the function zip). The order of combinations will depend on which variable we 
place first"""
print(result)

"""If any argument doesn't have the same number of items as others, the remaining items will 
not be taken into account to generate subtuples. The combination must be exact. If any value 
has extra items, they will be omitted. Tuples will always have the same length"""
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_one = (10, 20, 30, 40, 50)

result = zip(list_one, tuple_one)
result = tuple(result)
print(result)