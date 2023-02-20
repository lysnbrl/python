def operation():
    def deposit(balance, amount):
        return balance + amount


    def withdrawal(balance, amount):
        if amount <= balance:
            return balance - amount
        else:
            return None

    print("Your bank account now has $", deposit(100, 50))
    print("Your bank account now has $", withdrawal(100, 50))

operation()


def operation(amount, balance, typeof="Deposit"):
    def deposit(amount, balance):
        return balance + amount


    def withdrawal(amount, balance):
        if amount <= balance:
            return balance - amount
        else:
            return None

    if typeof == "Deposit":
        return deposit(amount, balance)
    elif typeof == "Withdrawal":
        return withdrawal(amount, balance)

result = operation(50, 100)
print(result)