course_list = ["Python", "Django", "Flask", "Ruby", "Java"]

"""To obtain an item from a list, we need to put the index of the item inside the square 
brackets of the list. We can store the value in a new variable"""
first_course = course_list[0] 
print(first_course)
second_course = course_list[1] 
print(second_course)
last_course = course_list[4]
print(last_course)

"""An interesting thing is that we can use negative numbers to work with indexes. The 
list will now be read from right to left, and the count will start at -1"""
first_course = course_list[-5] 
print(first_course)
second_course = course_list[-4] 
print(second_course)
last_course = course_list[-1]
print(last_course)

"""Just like other cases, we can print an item directly, without storing the value 
inside a new variable"""
print(course_list[0])
print(course_list[-5])

"""To update an item of a list, we need to put the index we want to update inside 
the square brackets of the list and assign it another value"""
course_list[4] = "Rust"
print(course_list)