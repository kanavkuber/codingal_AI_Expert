# 1) Ask the user to enter a number.
num = int(input("Enter a number: "))

# 2) Set sum to 0.
sum = 0

# 3) Copy num into temp.
temp = num

# 4) Repeat while temp is greater than 0.
while temp > 0:
    # a) Find the last digit.
    digit = temp % 10

    # b) Add the cube of the digit to sum.
    sum += digit * digit * digit

    # c) Remove the last digit.
    temp = temp // 10

# 5) Compare num and sum.
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")