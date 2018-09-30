print("Enter a magic number: ")
number1 = input()
number2 = input()
number3 = input()
# Convert a string of number into array
line1 = [int(x) for x in number1]
line2 = [int(x) for x in number2]
line3 = [int(x) for x in number3]
square = [line1,line2,line3] # Converge three arrays into one two-dimension array
isMagic = True # Set isMagic's default as True

# Check each row to see if their sum is equal to 15
for i in range(len(square)):
    horizontal = 0
    for j in range(len(square[0])):
        horizontal += square[i][j]
    if horizontal != 15:
        isMagic = False
        break

# Check each column to see if their sum is equal to 15
for j in range(len(square[0])):
    vertical = 0
    for i in range(len(square)):
        vertical += square[i][j]
    if vertical != 15:
        isMagic = False
        break
        
# Check if the diagonal sum is equal to 15
diag1 = 0 # The sum of values in the diagonal line from top-left to bottom-right
diag2 = 0 # The sum of values in the diagonal line from top-right to botton-left
for i in range(len(square)):
    for j in range(len(square[0])):
        if i == j:
            diag1 += square[i][j]
        if i + j == 2:
            diag2 += square[i][j]
if diag1 != 15 or diag2 != 15:
    isMagic = False

# Print out the result
if isMagic == True:
    print("This is a magic square!")
else:
    print("Not a magic square!")