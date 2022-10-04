"""It is better to work with lists when we don't know the number of items to store 
and/or if we know that those items may change; if we know that the items to store 
won't change and we want to keep them that way for the rest of the program, it is 
better to work with tuples"""

"""To generate a tuple from a list, we need to make use of the tuple() function. 
This function will take by argument the list from which we will generate a 
tuple; we can store the value in a new variable"""
course = ["Python", "Django", "Flask"]
course_tuple = tuple(course)
print(course_tuple)

"""To generate a list from a tuple, we need to make use of the list() function. 
This function will take by argument the tuple from which we will generate a 
list; we can store the value in a new variable"""
level = ("Basic", "Intermediate", "Advanced")
level_list = list(level)
print(level_list)

