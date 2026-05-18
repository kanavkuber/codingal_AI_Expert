import random
from colorama import init, Fore, Style

init(autoreset=True)

# =========================================
# CONSTANTS (DO NOT EDIT)
# =========================================
win_conditions = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def display_board(board):
    """Prints the Tic-Tac-Toe board in color."""
    print()

    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    """Asks player to choose X or O and returns (player_symbol, ai_symbol)."""
    symbol = ''

    while symbol not in ['X', 'O']:
        symbol = input(
            Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL
        ).strip().upper()

    return ('X', 'O') if symbol == 'X' else ('O', 'X')

# ==========================================================
# TODO 1: player_move(board, symbol)
# ==========================================================
def player_move(board, symbol):

    choice = -1

    while choice not in range(1, 10) or not board[choice - 1].isdigit():

        try:

            choice = int(input(
                Fore.GREEN + "Choose your spot (1-9): " + Style.RESET_ALL
            ))

            if choice not in range(1, 10) or not board[choice - 1].isdigit():

                print(
                    Fore.RED + "That move isn't available. Try again."
                    + Style.RESET_ALL
                )

        except ValueError:

            print(
                Fore.RED + "Please enter a valid number from 1 to 9."
                + Style.RESET_ALL
            )

    board[choice - 1] = symbol

# ==========================================================
# TODO 2: ai_move(board, ai_symbol, player_symbol)
# ==========================================================
def ai_move(board, ai_symbol, player_symbol):

    # Try winning first
    for position in range(9):

        if board[position].isdigit():

            temp_board = board.copy()

            temp_board[position] = ai_symbol

            if check_win(temp_board, ai_symbol):

                board[position] = ai_symbol

                return

    # Try blocking the player
    for position in range(9):

        if board[position].isdigit():

            temp_board = board.copy()

            temp_board[position] = player_symbol

            if check_win(temp_board, player_symbol):

                board[position] = ai_symbol

                return

    # Pick a random available spot
    available_positions = [
        position for position in range(9)
        if board[position].isdigit()
    ]

    selected_position = random.choice(available_positions)

    board[selected_position] = ai_symbol

# ==========================================================
# TODO 3: check_win(board, symbol)
# ==========================================================
def check_win(board, symbol):

    for pattern in win_conditions:

        if (
            board[pattern[0]] ==
            board[pattern[1]] ==
            board[pattern[2]] ==
            symbol
        ):

            return True

    return False

# ==========================================================
# TODO 4: check_full(board)
# ==========================================================
def check_full(board):

    return all(not spot.isdigit() for spot in board)

# ==========================================================
# MAIN GAME (NOW WITH A FEW TODOs)
# ==========================================================
def tic_tac_toe():

    print(Fore.CYAN + "Welcome to Tic-Tac-Toe!" + Style.RESET_ALL)

    player_name = input(
        Fore.GREEN + "Enter your name: " + Style.RESET_ALL
    ).strip()

    if player_name == "":
        player_name = "Player"

    while True:

        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        player_symbol, ai_symbol = player_choice()

        turn = 'Player'

        game_active = True

        while game_active:

            display_board(board)

            if turn == 'Player':

                player_move(board, player_symbol)

                if check_win(board, player_symbol):

                    display_board(board)

                    print(
                        Fore.GREEN +
                        f"Great job {player_name}! You won the game!"
                        + Style.RESET_ALL
                    )

                    game_active = False

                else:

                    if check_full(board):

                        display_board(board)

                        print(
                            Fore.YELLOW + "It's a tie!" + Style.RESET_ALL
                        )

                        break

                    else:

                        turn = 'AI'

            else:

                print(
                    Fore.CYAN + "AI is making its move..."
                    + Style.RESET_ALL
                )

                ai_move(board, ai_symbol, player_symbol)

                if check_win(board, ai_symbol):

                    display_board(board)

                    print(
                        Fore.RED + "AI won this round!"
                        + Style.RESET_ALL
                    )

                    game_active = False

                else:

                    if check_full(board):

                        display_board(board)

                        print(
                            Fore.YELLOW + "It's a tie!" + Style.RESET_ALL
                        )

                        break

                    else:

                        turn = 'Player'

        play_again = input(
            Fore.GREEN +
            "Would you like to play again? (yes/no): "
            + Style.RESET_ALL
        ).lower()

        if play_again != 'yes':

            print(
                Fore.CYAN + "Thanks for playing!" + Style.RESET_ALL
            )

            break

if __name__ == "__main__":

            tic_tac_toe()