import sys

symbol = str(input("Input the symbol of rectangle: "))
width = int(input("Enter the width of rectangle: "))
height = int(input("Enter the height of rectangle: "))

if width < 2 or height < 2: # Determine if the value is too small
    print("The value is too small.")
else:
    for i in range(height):
        for j in range(width): # Print symbol on the four side of the rectangle, otherwise print space
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                print(symbol,end="")
            else:
                print(end=" ")
        print()