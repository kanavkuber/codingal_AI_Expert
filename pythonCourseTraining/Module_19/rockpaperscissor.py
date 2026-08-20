import random

while True:
    choice = input("Choose rock paper or scissors: ")
    num=random.randint(1,3)
    if num==1:
        comp = "rock"
    elif num==2:
        comp = "paper"
    else:
        comp = "scissors"

    print (f"Player chose {choice} and Computer chose {comp}")

    if choice == comp:
        print ("Its a tie")

    elif choice == "rock":
        if comp == "paper":
            print ("Computer wins")
        elif comp == "scissors":
            print ("Player wins")

    elif choice == "paper":
        if comp == "scissors":
                print ("Computer wins")
        elif comp == "rock":
                print ("Player wins")

    elif choice == "scissors":
        if comp == "rock":
                print ("Computer wins")
        elif comp == "paper":
                print ("Player wins")

    ask = input ("Do you want to play again? (y/n)")

    if ask != "y":
        break
