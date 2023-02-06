dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}

print(dictionary)

print(dictionary["d"])

print(dictionary.get("d"))
print(dictionary.get("e"))
print(dictionary.get("e", "La llave no existe."))
print(dictionary.get("d", "La llave no existe."))

print(dictionary.setdefault("e", 5))

print(dictionary)