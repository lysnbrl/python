"""Sometimes we will need to ask the user to enter values from keyboard, in that
cases we will need to make use of the input() function. This function pauses 
program execution until enter is pressed, it can also display a message"""
input("Enter your name: ")

"""Input() is going to return everything the user typed before pressing enter,
and we can store such value in a variable. It will always return a string"""
full_name = input("Enter your full name: ")

"""If we want to work with an int or with a float, we must generate new values      
from strings. For this, we will make use of the int() and float() functions"""
age = input("Enter your age: ")
age = int(age)

height = input("Enter your height: ")
height = float(height)

#If we want to work with a boolean, we must use relational operators
authorization = input("Do you authorize the storage of your data? Yes/No: ")
authorization = authorization == "Yes"

print(full_name)
print(age)
print(height)
print(authorization)

"""We can also execute int() and float() directly with the input() function,
this is way more practical and it saves us a few lines of code"""
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
authorization = input("Do you authorize the storage of your data? Yes/No: ") == "Yes"
print(full_name)
print(age)
print(height)
print(authorization)
