# 1) Ask the user to enter the number of terms.
n = int(input("Enter the number of terms: "))

# 2) Initialize sum to 0.
sum = 0

# 3) Initialize i to 1.
i = 1

# 4) Repeat while i is less than or equal to n.
while i <= n:
    # a) Add i to sum.
    sum += i

    # b) Increase i by 1.
    i += 1

# 5) Print the final value of sum.
print("The sum is:", sum)