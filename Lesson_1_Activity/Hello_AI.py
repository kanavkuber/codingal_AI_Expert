# Welcome message
print("Hello! Welcome to AI Bot :) What's your name? : ")

username = input()

# Respond to the user's name
print(f"Pleased to meet you {username}!")

# Ask a question
print("How's your mood today? (good/bad/neutral) : ")

mood = input().lower()

# Use conditional statements to respond based on input

if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
elif mood == "netural": 
    print ("Could be better could be worse huh!")
else:
    print("Hmm. Can't find proper words to express ourselves today :D")

# End the conversation
print(f"It was nice chatting with you {username}. Goodbye!")