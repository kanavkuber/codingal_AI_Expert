import random

playing = True

num = str(random.randint(0,9))

print("*** This is a number guessing game. Guess what number I am thinking of ***")



while playing:
    guess = input("Your guess: ")
    if guess == num:
        print("You guessed it right! Wow I am amazed. Are you in my head ?")
        playing = False
    else:
        print("That wasn't it I am afraid, why don't you try again")
