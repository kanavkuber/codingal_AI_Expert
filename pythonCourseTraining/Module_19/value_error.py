try:
 num=int(input("Enter the first number: "))
 print("You Entered: ",num)
except ValueError as ex:
 print("Invalid Entry: ", ex )