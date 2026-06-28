a = 100
b = 150
c = 150

print(not (a == b))

print(not (b == c))

a = "python"
b = "coding"

if not (a == b):
    print(a, 'and', b, 'are different.')

a = 40
b = 50

if not ((a == 10) == (b == 50)):
    print('Hello')

a = int(input("Enter a number: "))

if not (a % 2 == 0):
    print(a, "is an odd number.")