def users(**kwargs):
    print(kwargs)
    print(type(kwargs))

users(Jade=[10, 10, 10], Mauri=[10, 10, 8])


def combination(*args, **kwargs):
    print(args)
    print(kwargs)

combination(1, 2, 3, 4, 5, Foxy="Perro", Chetto="Gato")