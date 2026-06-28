# 1) Ask the user to enter a number (greater than 1).
n = int(input("Enter a number greater than 1: "))

# 2) Print a message.
print("Numbers from", n, "down to 1:")

# 3) Use a for loop from n down to 1.
for i in range(n, 0, -1):
    # 4) Print the current value of i.
    print(i)