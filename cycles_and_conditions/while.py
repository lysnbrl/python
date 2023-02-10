number = 2023
digit_counter = 0

while number >= 1:
    digit_counter += 1

    number = number / 10
else:
    print(digit_counter)
    print("End of while loop.")