import sys

def main():
    height = int(sys.argv[1])
    isEven = 0 # Determine if the height is even number. If yes, add a duplicate line
    if height % 2 == 0:
        half = int(height / 2)
        isEven = 1
    else:
        half = int(height / 2 + 1)
    # Print the upper half
    for row in range(1,half + isEven):
        for _ in range(half - row):
            print(end=" ")
        for _ in range(2 * row - 1):
            print("*",end="")
        print()
    # Print the lower half
    for row in range(half):
        for _ in range(row):
            print(end=" ")
        for _ in range(2 * (half - row) - 1):
            print("*",end="")
        print()

main()