"""Every item inside a tuple has an index, starting at 0. With indexes we will be able 
to consult each item within a tuple"""
courses = ("Python", "Flask", "Django", "Rails", "Swift")

"""To obtain an item from a tuple, we need to put the index of the item inside the 
parenthesis of the tuple; we can store the value in a new variable"""
#Note: We can also work with negative numbers
first_course = courses[0]
print(first_course)
last_course = courses[-1]
print(last_course)

"""To generate subtuples, we need to change the parentheses of our initial tuple 
for square brackets, then we need to put inside the square brackets, separated 
by a colon, the initial index and the final index of the sublist that we want 
to generate; we can store that value in a new variable""" 
#Note: Work with suptuples is like work with sublists
subtuple = courses[0:3]
print(subtuple)
subtuple = courses[:3]
print(subtuple)
subtuple = courses[:]
print(subtuple)
