course_list_one = ["Python", "Django", "Flask", "Ruby", "Java"]
course_list_two = ["Rails", "PyGame", "Docker"]
number_list = [90, 349, 68, 1, 672, 1500, 4]

"""To add a new item to a list, we can make use of two different methods: a) the append() method 
and b) the insert() method. The first one will allow us to add new items to the end of our list;
the second one will help us to add new items to a particular index"""
course_list_one.append("MongoDB")
print(course_list_one)

"""The second method will receive two arguments, separated by a comma: the index where we will 
add the new element, and the new element itself"""
course_list_one.insert(3, "JavaScript")
print(course_list_one)

"""We can make a list larger using another list. For this, we can make use of the extend() 
method. This method will take as argument the list that we want to add to the list that we 
want to make larger"""
course_list_one.extend(course_list_two)
print(course_list_one)

"""To remove an item from a list, we can rely in two different ways: a) with the remove() 
method or b) using indexes with the del keyword"""
course_list_one.remove("MongoDB")
print(course_list_one)

del course_list_one[3]
print(course_list_one)

"""To sort single-type lists, we can make use of the sort() method. This method will 
allow us to sort lists in ascending order"""
#The sort() method is exclusive for lists
number_list.sort()
print(number_list)

"""In the other hand, if we want to sort in descending order, we can use the sort() 
method with the reverse parameter. To use it, we need to put reverse inside the 
sort() method's parentheses and set it to True"""
number_list.sort(reverse = True)
print(number_list)

"""To know whether or not an item is in a list, we can use the logical operator in, 
which is going to return a boolean value. In addition, we can negate the statement 
with the logical operator not"""
print(73 in number_list)
print(68 in number_list)

print(73 not in number_list)
print(68 not in number_list)

"""To obtain the smallest and largest values of a list, we can make use of the 
min() and max() functions. Min() will return the smallest value and max() the 
largest one"""
print(min(number_list))
print(max(number_list))

#To remove all the items within a list, we can make use of the clear() method
course_list_one.clear()
print(course_list_one)

#To get the index of an item, we can make use of the index() method
print(number_list.index(672))

#To know the length of a list, we can make use of the len() funtion
print(len(number_list))
