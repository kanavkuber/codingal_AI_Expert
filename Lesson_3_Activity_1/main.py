import re
import random
from colorama import Fore, init

# Initialize colorama with automatic reset
init(autoreset=True)

# Vacation categories and destinations
travel_options = {
    "beaches": ["Bora Bora", "Seychelles", "Goa"],
    "mountains": ["Andes", "Mount Fuji", "Dolomites"],
    "cities": ["London", "Singapore", "Dubai"]
}

# Fun travel-related jokes
funny_lines = [
    "Why did the tourist bring a ladder? To reach new heights!",
    "Why do computers love vacations? They get to reboot!",
    "Why was the suitcase always calm? Because it had emotional baggage under control!"
]

# Clean and standardize user input
def clean_text(user_text):
    return re.sub(r"\s+", " ", user_text.strip().lower())

# Recommend destinations recursively until user is satisfied
def suggest_destination():
    print(Fore.CYAN + "VoyageBot: What kind of trip are you planning? Beaches, mountains, or cities?")
    
    travel_choice = input(Fore.YELLOW + "You: ")
    travel_choice = clean_text(travel_choice)

    if travel_choice in travel_options:
        selected_place = random.choice(travel_options[travel_choice])

        print(Fore.GREEN + f"VoyageBot: You might enjoy visiting {selected_place}!")
        print(Fore.CYAN + "VoyageBot: Does that sound good? (yes/no)")

        feedback = input(Fore.YELLOW + "You: ").lower()

        if feedback == "yes":
            print(Fore.GREEN + f"VoyageBot: Fantastic! Hope you have an amazing time in {selected_place}!")
        
        elif feedback == "no":
            print(Fore.RED + "VoyageBot: No worries, let me suggest something else.")
            suggest_destination()
        
        else:
            print(Fore.RED + "VoyageBot: I didn't catch that, so I'll suggest another place.")
            suggest_destination()

    else:
        print(Fore.RED + "VoyageBot: I currently only suggest beaches, mountains, or cities.")
        suggest_destination()

# Provide packing guidance
def travel_checklist():
    print(Fore.CYAN + "VoyageBot: Which destination are you traveling to?")
    destination_name = clean_text(input(Fore.YELLOW + "You: "))

    print(Fore.CYAN + "VoyageBot: How long will your trip be (in days)?")
    trip_length = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"VoyageBot: Here are some packing suggestions for {trip_length} days in {destination_name}:")
    print(Fore.GREEN + "- Carry comfortable and reusable outfits.")
    print(Fore.GREEN + "- Keep chargers and travel documents handy.")
    print(Fore.GREEN + "- Check local weather updates before departure.")

# Display a random joke
def share_joke():
    print(Fore.YELLOW + f"VoyageBot: {random.choice(funny_lines)}")

# Show available commands
def display_commands():
    print(Fore.MAGENTA + "\nHere’s what I can help you with:")
    print(Fore.GREEN + "- Recommend travel destinations (type 'recommendation')")
    print(Fore.GREEN + "- Share packing advice (type 'packing')")
    print(Fore.GREEN + "- Tell travel jokes (type 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' whenever you want to quit.\n")

# Main chatbot interaction loop
def start_chat():
    print(Fore.CYAN + "Greetings! I’m VoyageBot, your travel assistant.")

    visitor_name = input(Fore.YELLOW + "May I know your name? ")

    print(Fore.GREEN + f"Welcome aboard, {visitor_name}!")

    display_commands()

    while True:
        message = input(Fore.YELLOW + f"{visitor_name}: ")
        message = clean_text(message)

        if "recommend" in message or "suggest" in message:
            suggest_destination()

        elif "pack" in message or "packing" in message:
            travel_checklist()

        elif "joke" in message or "funny" in message:
            share_joke()

        elif "help" in message:
            display_commands()

        elif "exit" in message or "bye" in message:
            print(Fore.CYAN + "VoyageBot: Wishing you safe and happy travels. Goodbye!")
            break

        else:
            print(Fore.RED + "VoyageBot: I’m not equipped enough to understood that. Could you try wording it differently?")

# Run chatbot
if __name__ == "__main__":
    start_chat()