def first_part(size):
    """Print the first part"""
    for i in range(size//2 + 2):
        print(' ' * (size // 2 + 1 - i), end="")
        if(i == 0):
            print('+'+'-' * (2 * size), end="+")
        elif(i == size // 2 + 1):
            print('+'+'-' * (2 * size) + '+' + ' ' * (i-1), end='|')
        else:
            print('/'+' ' * (2 * size) + '/' + ' ' * (i-1), end='|')
        print()


def second_part(size):
    """Print the second part"""
    for i in range(size, size + size//2):
        if(i == size + size // 2 - 1):
            print('|' + ' ' * (2 * size) + '|' + ' ' * (size // 2), end='+')
        else:
            print('|' + ' ' * (2 * size) + '|' + ' ' * (size // 2), end='|')
        print()


def third_part(size):
    """Print the third part"""
    for i in range(size + size//2, 2 * size + 1):
        if(i == 2 * size):
            print('+' + '-' * (2 * size), end='+')
        else:
            print('|' + ' ' * (2 * size) + '|' +
                  ' ' * (2 * size - i - 1), end='/')
        print()


def main():
    '''
    Break the whole cube into three parts.
    Print three parts respectively.
        +------------+ ------------
       /            /|
      /            / |  First part
     /            /  |
    +------------+   | ------------
    |            |   |
    |            |   |  Second part
    |            |   + ------------
    |            |  /
    |            | /    Third part
    |            |/
    +------------+     ------------
    '''
    size = int(input("Input cube size (multiple of 2):"))
    while (size % 2 != 0):
        print("Please enter the right size.")
        size = int(input("Input cube size (multiple of 2):"))
    first_part(size)
    second_part(size)
    third_part(size)


main()
