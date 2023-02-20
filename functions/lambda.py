degrees_function = lambda degrees : degrees * 1.8 + 32
print(degrees_function(25))

no_parameters = lambda : True
print(no_parameters())

default_parameters = lambda one=10, two=20, three=30 : one + two + three
print(default_parameters())

asterisk = lambda *args, **kwargs : len(args) + len(kwargs)
print(asterisk(1, 2, 3, Cuatro=4, Cinco=5))