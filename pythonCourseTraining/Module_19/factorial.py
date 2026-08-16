def factorial(x):

    """This function calculates the multiplication of all
    the numbers going from 1 all the way up to the given number i.e.
    -Factorial of a number"""

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print(f"Factorial for 0 is :{factorial(0)}")
print(f"Factorial for 1 is :{factorial(1)}")
print(f"Factorial for 2 is :{factorial(2)}")
print(f"Factorial for 5 is :{factorial(5)}")
print(f"Factorial for 10 is :{factorial(10)}")