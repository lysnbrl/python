number_one = 1
number_two = 2
number_three = 3

"""
There are six relational operators:
< - Less than
> - Greater than
<= - Less than or equal to
>= - Greater than or equal to
== - Equal to
!= - Not equal to
"""

"""Whenever we use relational operators, Python will return a boolean, for example: in the following 
case, the value of the variable result will be False, because 10 is less than 20"""
result = number_one > number_two
print(result)

result = number_one < number_two
print(result)

result = number_one >= number_two
print(result)

result = number_two <= number_three
print(result)

result = number_one == number_three
print(result)

result = number_one != number_three
print(result)