"""We can assign variables to the items of a tuple (or a list), we just have to assign the tuple to 
the variables at the moment of creating them. By assigning the tuple to the variables, Python will 
assign each one of the items within the tuple to each one of the variables. The first item will be 
assigned to the first variable and so on. This is known as unpacking"""
#Note: Variables must be equal in number to items
numbers = (1, 2, 3)
one, two, tree = numbers
print(one)
print(two)
print(tree)

"""If we don't know the number of items within a tuple and we use variables, we will get an error 
that will indicate us that there are too many items to unpack. To avoid this, we can declare a 
final variable which starts with an asterisk. By doing so, we tell Python that, starting from 
the penultimate variable, the rest of the items will be stored in the last variable"""
#Whenever we see an asterisk as a prefix, it means that the variable is a list
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
one, two, tree, *remaining_numbers = numbers

#If we print the last variable, we will get a list that store the items that weren't unpacked 
print(remaining_numbers)

"""If we do not want to store the rest of the items in a variable, we can place an asterisk 
followed by an underscore, this will omit the items"""
one, two, *_ = numbers
print(one)
print(two)

"""If we want to omit certain items, but we also want to get the last ones, we need to 
place a comma after having omitted certain items with the asterisk and the underscore, 
then we can place the variables that will store the last items"""
one, two, *_, nine, ten = numbers
print(one)
print(two)
print(nine)
print(ten)

"""If we want to omit only one item, we just need to place an underscore in the 
position of that item"""
one, _, tree, *_, eight, _, ten = numbers
print(one)
print(tree)
print(eight)
print(ten)