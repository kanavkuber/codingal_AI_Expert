# 1) Take an integer input from the user.
rows = int(input("Enter the number of rows: "))

# 2) Initialize number = 1.
number = 1

# 3) Print a heading message.
print("Floyd's Triangle")

# 4) Outer loop for each row.
for i in range(1, rows + 1):

    # 5) Inner loop to print numbers in the current row.
    for j in range(1, i + 1):
        print(number, end="  ")
        number += 1

    # 6) Move to the next line.
    print()