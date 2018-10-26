def luhn_algo(number):
    """Check if a number is valid or not"""
    digits = [int(digit) for digit in number]
    sum_digits = 0
    for i in range(len(digits) - 2, -1, -2):
        digits[i] = digits[i] * 2
        if (digits[i] > 9):
            one = digits[i] % 10
            two = digits[i] // 10
            digits[i] = one + two
    for i in range(len(digits)):
        sum_digits += digits[i]
    if (sum_digits % 10 == 0):
        print("The given number", number, "is valid")
    else:
        print("The given number", number, "is not valid")


def main():
    number = input("Enter a number:")
    luhn_algo(number)


main()
