import math

round_up = math.ceil(29.34)
round_down = math.floor(29.34)
print (f"The ceiling and floor values are {round_up} and {round_down}")


x=10
y=-15
print(f"The value of x after copysign is {str(math.copysign(x,y))}")

print(math.fabs(-96), math.fabs(56))

print(math.gcd (24,56))