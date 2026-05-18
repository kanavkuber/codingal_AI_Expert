import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try:
    movie_df = pd.read_csv("imdb_top_1000.csv")

except FileNotFoundError:

    print(
        Fore.RED +
        "Error: Could not find the file 'imdb_top_1000.csv'."
    )

    raise SystemExit

genres = sorted({
    g.strip()
    for xs in movie_df["Genre"].dropna().str.split(", ")
    for g in xs
})

def loading_effect():

    for _ in range(3):

        print(
            Fore.YELLOW + ".",
            end="",
            flush=True
        )

        time.sleep(0.5)

def senti(p):

    return (
        "Positive 😊" if p > 0
        else "Negative 😞" if p < 0
        else "Neutral 😐"
    )

def recommend(genre=None, mood=None, rating=None, n=5):

    data = movie_df

    if genre:

        data = data[
            data["Genre"].str.contains(
                genre,
                case=False,
                na=False
            )
        ]

    if rating is not None:

        data = data[
            data["IMDB_Rating"] >= rating
        ]

    if data.empty:

        return "Sorry, no movie recommendations matched your choices."

    data = data.sample(frac=1).reset_index(drop=True)

    need_positive = bool(mood)

    results = []

    for _, row in data.iterrows():

        overview = row.get("Overview")

        if pd.isna(overview):

            continue

        polarity = TextBlob(
            overview
        ).sentiment.polarity

        if (not need_positive) or polarity >= 0:

            results.append(
                (
                    row["Series_Title"],
                    polarity
                )
            )

            if len(results) == n:

                break

    return (
        results
        if results
        else "Sorry, no movie recommendations matched your choices."
    )

def show(recs, name):

    print(
        Fore.YELLOW +
        f"\n🍿 Movie Suggestions for {name}:"
    )

    for i, (title, polarity) in enumerate(recs, 1):

        print(
            f"{Fore.CYAN}{i}. 🎥 {title} "
            f"(Polarity: {polarity:.2f}, {senti(polarity)})"
        )

def get_genre():

    print(Fore.GREEN + "Available Genres: ", end="")

    for i, g in enumerate(genres, 1):

        print(f"{Fore.CYAN}{i}. {g}")

    print()

    while True:

        x = input(
            Fore.YELLOW +
            "Enter a genre number or type the genre name: "
        ).strip()

        if x.isdigit() and 1 <= int(x) <= len(genres):

            return genres[int(x) - 1]

        x = x.title()

        if x in genres:

            return x

        print(
            Fore.RED +
            "That genre isn't available. Please try again.\n"
        )

def get_rating():

    while True:

        x = input(
            Fore.YELLOW +
            "Choose a minimum IMDB rating (7.6-9.3) or type 'skip': "
        ).strip()

        if x.lower() == "skip":

            return None

        try:

            r = float(x)

            if 7.6 <= r <= 9.3:

                return r

            print(
                Fore.RED +
                "Please choose a rating between 7.6 and 9.3.\n"
            )

        except ValueError:

            print(
                Fore.RED +
                "Invalid input. Enter a valid number.\n"
            )

print(
    Fore.BLUE +
    "🎥 Welcome to the Movie Recommendation Assistant! 🎥\n"
)

name = input(
    Fore.YELLOW +
    "What's your name? "
).strip()

print(
    f"\n{Fore.GREEN}Nice to meet you, {name}!\n"
)

print(
    Fore.BLUE +
    "\n🔍 Let's find a great movie for you!\n"
)

genre = get_genre()

mood = input(
    Fore.YELLOW +
    "How are you feeling today? "
).strip()

print(
    Fore.BLUE +
    "\nAnalyzing your mood",
    end="",
    flush=True
)

loading_effect()

mp = TextBlob(
    mood
).sentiment.polarity

md = (
    "positive 😊" if mp > 0
    else "negative 😞" if mp < 0
    else "neutral 😐"
)

print(
    f"\n{Fore.GREEN}"
    f"Your mood seems {md} "
    f"(Polarity: {mp:.2f}).\n"
)

rating = get_rating()

print(
    Fore.BLUE +
    f"\nLooking for movies for {name}",
    end="",
    flush=True
)

loading_effect()

recs = recommend(
    genre=genre,
    mood=mood,
    rating=rating,
    n=5
)

if isinstance(recs, str):

    print(Fore.RED + recs + "\n")

else:

    show(recs, name)

while True:

    answer = input(
        Fore.YELLOW +
        "\nWould you like more movie suggestions? (yes/no): "
    ).strip().lower()

    if answer == "no":

        print(
            Fore.GREEN +
            f"\nEnjoy your movies, {name}! 🎬🍿\n"
        )

        break

    if answer == "yes":

        recs = recommend(
            genre=genre,
            mood=mood,
            rating=rating,
            n=5
        )

        if isinstance(recs, str):

            print(Fore.RED + recs + "\n")

        else:

            show(recs, name)

    else:

        print(
            Fore.RED +
            "Please enter either yes or no.\n"
        )