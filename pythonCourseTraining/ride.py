print("Select which ride you want: ")
print("1. Bike")
print("2. Car")

choice1 = int( input("Enter your choice: (1/2)") )

if( choice1 == 1 ):
    print( "what type of bike? " )
    print("1.Scooter\n")
    print("2.Motorcycle\n")

    choice2=int(input("Enter you bike choice: "))
    if choice2==1:
        print("you have selected a Scooter")
    else:
        print("you have selected a Motorcycle")

elif( choice1 == 2 ): 
    print( "what type of car?" )
    print("1.Sedan")
    print("2.SUV")

    choice3=int(input("enter your car choice: "))

    if choice3==1:
        print("you have selected sedan")
    else:
        print("you have selected SUV")
else: 
    print("Wrong choice!")