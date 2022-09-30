"""A list is a data structure, a data type that allows us to handle large amounts
of other data. There are two forms to create a list: a) using the list() function 
or b) using square brackets"""
list_one = list()
list_two = []

"""When we create a list, we can place inside the square brackets all those items 
that we want to store inside the list. Each item must be separated by a comma"""
list_three = ["Hello", 100, 3.1415, True]

"""Every item of a list must have a position within the list, starting at 0. This 
position is known as index"""
list_four = [0, 1, 2, 3, 4]

"""Lists allow us to mix the items that are going to be stored, but the 
recommended practice is to create lists that store only one data type, 
by doing so, we will be standardising our coding process"""
string_list = ["Bulbasaur", "Ivysaur", "Venusaur"]
integer_list = [100, 200, 300]
float_list = [0.1234, 2.7182, 3.1415]
boolean_list = [True, False, 10 < 20]

print(string_list)
print(integer_list)
print(float_list)
print(boolean_list)