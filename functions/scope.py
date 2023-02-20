animal = "Lion"

def print_animal():
    print(animal)

print_animal()
print(animal)


def print_animal():

    animal = "Narwhal"

    print(animal)
    print(id(animal))

print_animal()
print(animal)
print(id(animal))


def print_animal():

    global animal
    animal = "Narwhal"

    print(animal)
    print(id(animal))

print_animal()
print(animal)
print(id(animal))
