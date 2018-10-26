import math


def addition(x, y):
    """Add two number"""
    return x + y


def carry(x, y):
    """Counting carries"""
    carries = 0
    carry = 0
    while(x != 0 or y != 0):
        add = x % 10 + y % 10 + carry
        if add >= 10:
            carry = 1
            carries += 1
        else:
            carry = 0
        x = x // 10
        y = y // 10
    return carries


def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(number1, '+', number2, '=', addition(number1, number2))
    print("Number of carries:", carry(number1, number2))


main()
