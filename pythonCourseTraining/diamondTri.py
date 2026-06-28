# 1) Take an integer input from the user.
rowSize = int(input("Enter the number of rows: "))

# 2) Decide the number of rows in the upper half.
if rowSize % 2 == 0:
    halfDiamRow = rowSize // 2
else:
    halfDiamRow = rowSize // 2 + 1

# 3) Initialize space.
space = halfDiamRow - 1

# 4) Print the upper half.
for i in range(1, halfDiamRow + 1):

    # Print leading spaces.
    for j in range(space):
        print(" ", end="")

    # Decrease spaces for the next row.
    space -= 1

    # Start printing numbers.
    num = 1

    # Print numbers.
    for j in range(2 * i - 1):
        print(num, end="")
        num += 1

    # Move to the next line.
    print()

# 5) Reset space.
space = 1

# 6) Print the lower half.
for i in range(1, halfDiamRow):

    # Print leading spaces.
    for j in range(space):
        print(" ", end="")

    # Increase spaces for the next row.
    space += 1

    # Start printing numbers.
    num = 1

    # Print numbers.
    for j in range(2 * (halfDiamRow - i) - 1):
        print(num, end="")
        num += 1

    # Move to the next line.
    print()