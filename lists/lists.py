#With indexes, we will be able to obtain and update items within a list
course_list = ["Python", "Django", "Flask", "Ruby", "Java"]

"""To obtain an element through its index, we need to put the 
index inside the square brackets of the list and store the 
value in a new variable"""
first_course = course_list[0] 
print(first_course)
second_course = course_list[1] 
print(second_course)
last_course = course_list[4]
print(last_course)

"""We can also work with indexes using negative numbers, the 
list will now be read from right to left, and the count will 
start at -1"""
first_course = course_list[-5] 
print(first_course)
second_course = course_list[-4] 
print(second_course)
last_course = course_list[-1]
print(last_course)

"""Just like other cases, we can print an element directly, 
without storing the value inside a new variable"""
print(course_list[0])
print(course_list[-5])

"""To update an item of a list, we just need to put inside 
the square brackets the index we want to update and assign 
it another value"""
course_list[4] = "Rust"
print(course_list)