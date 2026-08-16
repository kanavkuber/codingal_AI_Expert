# 1) Print a heading message.
print("Half Pyramid Pattern")

# 2) Take an integer input.
n = int(input("Enter the number of rows: "))

# 3) Outer loop for each row.
for i in range(n):

    # 4) Inner loop to print stars.
    for j in range(i + 1):
        print("* ", end="")

    # 5) Move to the next line.
    print()