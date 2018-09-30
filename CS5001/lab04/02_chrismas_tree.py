
width = int(input("Please enter the width of base: ")) # Get width from user input
if width % 2 == 0: # Even number is not allowed here
    print("Please enter an odd number.")
else:
    height = int((width + 1) / 2)
    for i in range(height):
        if i == 0: # Print the first line
            print(" " * height + "*")
        elif i < height - 1:
            print(" "*(height - i) + "/" + " "*(2 * i - 1) + "\\")
        else: # Print the last line
            print(print(" "*(height - i) + "/" + "_"*(2 * i - 1) + "\\"))
