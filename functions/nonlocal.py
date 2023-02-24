def main_function_1():
    a = "a"
    b = "b"

    def nested_function():
        c = "c"
        b = "Value change"

        print(a)
        print(b)
        print(id(b))

    nested_function()
    print(b)
    print(id(b))

main_function_1()


def main_function_2():
    a = "a"
    b = "b"

    def nested_function():
        c = "c"

        nonlocal b
        b = "Value change"

        print(a)
        print(b)
        print(id(b))

    nested_function()
    print(b)
    print(id(b))

main_function_2()