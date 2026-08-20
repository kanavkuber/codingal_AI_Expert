try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    result = num1/num2
    print("Result: ",result)

except ValueError as ex:
    print("Invalid Entry: ", ex)

except ZeroDivisionError:
    print("Invalid Entry: Division by zero is an error!")

except:
    print("Wrong Input")

else:
    print("No exceptions")

finally:
    print (" I will always show up")