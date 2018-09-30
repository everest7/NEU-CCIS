import sys
import math

radius = int(sys.argv[1]) # Get the radius from command line
for x in range(radius * 2 + 1):
    for y in range(radius * 2 + 1):
        horizontal = abs(x - radius) # Calculate the horizontal distance from current location to the center of circle
        vertical = abs(y - radius) # Calculate the vertical distance from the current location to the center of circle
        dist = math.sqrt(horizontal ** 2 + vertical ** 2) # Calculate the actual distance
        if dist < radius: # Print 'o' if the location is within the radius of circle, otherwise print space
            print("o",end="")
        else:
            print(" ",end="")
    print()