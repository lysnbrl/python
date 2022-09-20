# ~AND~
"""All comparisons need to be true for the final result to be true, if
only one comparison is false, then the final result will be false"""
final_result = True and True and True
print(final_result)
final_result = True and False and True
print(final_result)

#When we use logical operators, we can also use relational operators
final_result = True and 10 < 20
print(final_result)
final_result = True and 10 > 20
print(final_result)

# ~OR~
#At least one comparison needs to be true for the final result to be true
final_result = True or 10 < 20
print(final_result)
final_result = True or 10 > 20
print(final_result)
final_result = False or 10 > 20
print(final_result)

"""It is possible to combine logical operators by using parentheses. Python will 
solve what is inside the parenthesis first, for example: in the following case, 
we are trying to compare True and False"""
final_result = True and (False or 5 > 10)
print(final_result)
final_result = True and (False or 5 < 10) 
print(final_result)

# ~NOT~
#It allows us to negate a boolean, converts True to False and vice versa
final_result = not True
print(final_result)
final_result = not False
print(final_result)