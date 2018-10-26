import sys


def draw_cone(width, isEven):
    """ Draw rocket nose cone """
    half = (width + 1) // 2
    if (isEven == 1):
        print()
    for row in range(1, half):
        print(' ' * (half - row), end='')
        print('*' * (2 * row - 1 + isEven), end='')
        print()


def draw_fuselage(width, length, isEven, striped):
    """ Draw rocket fuselage """
    if (striped):
        for row in range(1, length + 1):
            for _ in range(length * 2 - 1 + isEven):
                print('_' * width)
            for _ in range(length * 2):
                print('X' * width)
    else:
        for row in range(1, width * length + 1):
            print('X' * width)


def draw_tail(width, isEven):
    """ Draw rocket tail """
    half = (width + 1) // 2
    for row in range(1, half + 1):
        print(' ' * (half - row - 1), end='')
        if (row == half):
            print('*' * width, end='')
        else:
            print('*' * (2 * row + 1 + isEven), end='')
        print()


def main():
    width = int(sys.argv[1])
    length = int(sys.argv[2])
    striped = False
    if(len(sys.argv) > 3):
        if(sys.argv[3] == 'striped'):
            striped = True
    isEven = 0  # Rockets have different tip for an odd or even width
    if (width % 2 == 0):
        isEven = 1
    draw_cone(width, isEven)
    draw_fuselage(width, length, isEven, striped)
    draw_tail(width, isEven)


main()
