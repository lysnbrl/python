def sum(numb1, numb2):
    result = numb1 + numb2
    return result

number_one = int(input("Enter the first integer: "))
number_two = int(input("Enter the second integer: "))

result = sum(number_one, number_two)
print(result)


def sum(numb1, numb2):
    return numb1 + numb2


def sum(numb1, numb2):
    return numb1 + numb2, "Function returns two values."

number_one = int(input("Enter the first integer: "))
number_two = int(input("Enter the second integer: "))

result, message = sum(number_one, number_two)
print("Result is:", result)
print(message)


result, _ = sum(number_one, number_two)
print("Result is:", result)