
def triangular_number(x):
    """Return the triangular number for x"""
    sum = 0
    for i in range(1, x + 1):
        sum += i
    return sum


def main():
    inputs = input("Enter a number, or enter 'done': ")
    result_list = []  # Initialize the list of triangular number
    while(inputs != 'done'):
        print("The triangular number for", int(inputs), "is",
              triangular_number(int(inputs)))
        result_list.append(triangular_number(int(inputs)))
        inputs = input("Enter another number, or enter 'done': ")
    print(result_list)


main()
