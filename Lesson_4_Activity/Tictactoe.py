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

    while True:
        move = input(Fore.GREEN + "Choose a position (1-9): " + Style.RESET_ALL)

        if move.isdigit():
            move = int(move)

            if 1 <= move <= 9:
                if board[move - 1] not in ['X', 'O']:
                    board[move - 1] = symbol
                    break
                else:
                    print(Fore.RED + "That position is already taken.")
            else:
                print(Fore.RED + "Enter a number between 1 and 9.")
        else:
            print(Fore.RED + "Invalid input. Please enter a number.")

# ==========================================================
# TODO 2: ai_move(board, ai_symbol, player_symbol)
# ==========================================================
def ai_move(board, ai_symbol, player_symbol):

    # Try to win
    for i in range(9):
        if board[i] not in ['X', 'O']:
            temp = board[:]
            temp[i] = ai_symbol

            if check_win(temp, ai_symbol):
                board[i] = ai_symbol
                return

    # Try to block player
    for i in range(9):
        if board[i] not in ['X', 'O']:
            temp = board[:]
            temp[i] = player_symbol

            if check_win(temp, player_symbol):
                board[i] = ai_symbol
                return

    # Random move
    empty_spots = []

    for i in range(9):
        if board[i] not in ['X', 'O']:
            empty_spots.append(i)

    choice = random.choice(empty_spots)
    board[choice] = ai_symbol

# ==========================================================
# TODO 3: check_win(board, symbol)
# ==========================================================
def check_win(board, symbol):

    for combo in win_conditions:
        if (
            board[combo[0]] == symbol and
            board[combo[1]] == symbol and
            board[combo[2]] == symbol
        ):
            return True

    return False

# ==========================================================
# TODO 4: check_full(board)
# ==========================================================
def check_full(board):

    for cell in board:
        if cell not in ['X', 'O']:
            return False

    return True

# ==========================================================
# MAIN GAME (NOW WITH A FEW TODOs)
# ==========================================================
def tic_tac_toe():

    print(Fore.CYAN + "Welcome to Tic-Tac-Toe!" + Style.RESET_ALL)

    # Ask player's name
    name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL).strip()

    if name == "":
        name = "Player"

    while True:

        # Initialize board
        board = ['1','2','3','4','5','6','7','8','9']

        # Get symbols
        player_symbol, ai_symbol = player_choice()

        # Decide who starts
        turn = "Player"

        while True:

            display_board(board)

            if turn == "Player":

                # Player move
                player_move(board, player_symbol)

                # Check win
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"{name} wins!" + Style.RESET_ALL)
                    break

                # Check tie
                if check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    break

                # Switch turn
                turn = "AI"

            else:

                # AI move
                print(Fore.CYAN + "AI is making a move..." + Style.RESET_ALL)
                ai_move(board, ai_symbol, player_symbol)

                # Check AI win
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI wins!" + Style.RESET_ALL)
                    break

                # Check tie
                if check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    break

                # Switch turn
                turn = "Player"

        # Play again
        again = input(
            Fore.GREEN + "Play again? (yes/no): " + Style.RESET_ALL
        ).strip().lower()

        if again != "yes":
            print(Fore.CYAN + "Thanks for playing!" + Style.RESET_ALL)
            return

if __name__ == "__main__":
    tic_tac_toe()