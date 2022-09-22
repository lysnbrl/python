#A variable can store different types of data at different times
value = 22
value = 3.14
value = True
value = "Jade"

"""In the following case, the value that is going to be printed 
is the last value taken by the variable at the moment of using 
the print() function. In this case it is the string"""
print(value)

value = 22
print(value) 

value = 3.14
print(value) 

value = True
print(value) 

"""If we want to know what data type a variable is storing, we
can make use of the type() function. This function will return
the data type that the variable is storing"""
value = "Jade"
print(type(value))