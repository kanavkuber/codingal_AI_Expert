
# ------------------------------------------------------
# 1) IMPORTS & SETUP
# ------------------------------------------------------
# - Import colorama for colored text
# - Import specific color constants (e.g., Fore, Style)
# - Import textblob for sentiment analysis
# - Initialize colorama for cross-platform color support


import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()

# ------------------------------------------------------
# 2) INITIAL GREETING
# ------------------------------------------------------
# - Print a welcome message using a color (e.g., Fore.CYAN)
# - Include emojis (e.g., '👋', '🕵️') for a fun greeting


print(f"{Fore.RED} 👋 Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")

# ------------------------------------------------------
# 3) USER NAME INPUT
# ------------------------------------------------------
# - Prompt the user for their name
# - Strip extra whitespace
# - If empty, default to "Mystery Agent"

name = input(f"{Fore.CYAN} Please Enter your name:{Style.RESET_ALL}").strip()
if not name:
    name = "007"

# ------------------------------------------------------
# 4) CONVERSATION HISTORY
# ------------------------------------------------------
# - Create a structure (e.g., list) to store each user input
#   along with its polarity and sentiment type
# - For example: (user_text, polarity, sentiment_type)

convo_list = []

# ------------------------------------------------------
# 5) INSTRUCTIONS
# ------------------------------------------------------
# - Print instructions to the user describing the available
#   commands (e.g., 'reset', 'history', 'exit')

print(f"\n{Fore.RED}Hello, Agent {name}!")
print(f"Enter a sentence and I will analyze your sentences to show you the sentiment. ")
print(f"Type {Fore.YELLOW}'history' {Fore.CYAN} to check your previous conversations, {Fore.YELLOW}'reset' {Fore.CYAN}to clear your history,  "
    f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

# ------------------------------------------------------
# 6) MAIN INTERACTION LOOP
# ------------------------------------------------------
# - Use a 'while True:' loop to repeatedly prompt the user
# - Read input and strip whitespace
# - If empty, notify the user and continue

#     6.1) 'exit' COMMAND
#         - If agent_input.lower() == 'exit':
#           - Print a farewell message
#           - Break out of the loop to end the program

#     6.2) 'reset' COMMAND
#         - Clear the conversation history
#         - Print a message confirming reset

#     6.3) 'history' COMMAND
#         - If no history, print a message indicating so
#         - Otherwise, print each conversation entry
#           - Show text, polarity (formatted), and sentiment type
#           - Use color and emojis based on sentiment
#         - Continue the loop

#     6.4) SENTIMENT ANALYSIS
#         - If the input is not a command, analyze sentiment
#         - Use TextBlob(agent_input).sentiment.polarity to get a float
#           between -1.0 and +1.0
#         - Define thresholds:
#             > 0.25 -> Positive
#             < -0.25 -> Negative
#             Otherwise -> Neutral
#         - Assign color and emoji accordingly (e.g., GREEN/😊, RED/😢, YELLOW/😐)
#         - Append the tuple (text, polarity, sentiment_type) to the history
#         - Print a result message showing sentiment type and polarity


while True:
    agent_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not agent_input:
        print(f"{Fore.RED}Please enter some text to work with or you can choose one of the commands.{Style.RESET_ALL}")
        continue

    if agent_input.lower() == "exit":
        print(f"\n{Fore.BLUE}Time to say Goodbye! Until we meet again, Agent {name}! 😊{Style.RESET_ALL}")
        break

    elif agent_input.lower() == "reset":
        convo_list.clear()
        print(f"{Fore.CYAN} All of your conversation history has been wiped clean{Style.RESET_ALL}")

    elif agent_input.lower() == "history":
        if not convo_list:
            print(f"{Fore.YELLOW}Nothing to see here yet{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for index, (text, polarity, sentiment_type) in enumerate(convo_list, start=1):
                # Choose color & emoji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{index}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")

    polarity = TextBlob(agent_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    convo_list.append((agent_input, polarity, sentiment_type))

    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
        f"Polarity: {polarity:.2f}")



# ------------------------------------------------------
# END
# ------------------------------------------------------
# - The program terminates when 'exit' is typed
# - No additional code is shown beyond these comments


