"""In Python, we can generate sublists. To generate one, we need to put inside the square
brackets of our initial list, separated by a colon, the initial index and the final index 
of the sublist that we want to generate; we can store that value inside a new variable""" 
#Note: The final index won't be taken into account in the sublist items
course_list = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
sublist = course_list[0:3]
print(sublist)

"""To obtain the last items of a list, we just need to put the initial index (where we 
want our sublist to start) and the colon"""
sublist = course_list[3:]
print(sublist)

"""On the other hand, to obtain the first items of a list, we just need to put the 
colon and the final index (where we want our sublist to end)"""
sublist = course_list[:3]
print(sublist)

"""To generate a sublist that contains steps, we just need to add another colon 
after the final index and then the step interval"""
sublist = course_list[0:5:2]
print(sublist)

#If we put a -1 in the step interval we will get the items of the list in reverse
sublist = course_list[::-1]
print(sublist)