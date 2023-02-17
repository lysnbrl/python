def average(listing):
    return sum(listing) / len(listing)

result = average([6, 7, 8, 9, 10])
print(result)


def average(*listing):

    print(listing)
    print(type(listing))

    return sum(listing) / len(listing)

result = average(6, 7, 8, 9, 10)
print(result)


def average(*args):
    return sum(args) / len(args)

result = average(6, 7, 8, 9, 10)
print(result)


def combination(p1, p2, *args, p4=100):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combination(1, 2, 10, 20, p4=30)