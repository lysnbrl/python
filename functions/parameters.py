def circle_area(radius, pi=3.141592):
    return pi * (radius ** 2)

result = circle_area(10)
print(result)


def circle_area(radius, pi=3.141592):
    return pi * (radius ** 2)

result = circle_area(10, 3.14)
print(result)


def circle_area(radius, pi):
    return pi * (radius ** 2)

result = circle_area(pi=3.141592, radius=10)
print(result)