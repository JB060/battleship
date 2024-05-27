from random import randint

game_board = []

player_one = {
    "name": "player 1",
    "wins": 0,
    "ships": []
}

computer = {
    "name": "computer",
    "wins": 0,
    "ships": []
}

colors = {
    "reset": "\033[00m",
    "red": "\033[91m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
}

ship_sizes = [6, 5, 4, 3, 2]

# Building our 10x10 board
def build_game_board(board):
    for _ in range(10):
        board.append(["0"] * 10)

def show_board(board):
    for row in board:
        print(" ".join(row))

# Define ship placement by players
def place_ships(player, board, is_computer=False):
    ships = []
    for size in ship_sizes:
        while True:
            try:
                if is_computer:
                    start_row = randint(0, 9)
                    start_col = randint(0, 9)
                    orientation = "H" if randint(0, 1) == 0 else "V"
                else:
                    print(f"{player['name']}, place your ship of size {size}")
                    start_row = int(input("Start Row (1-10): ")) - 1
                    start_col = int(input("Start Col (1-10): ")) - 1
                    orientation = input("Orientation (H for horizontal, V for vertical): ").upper()

                if orientation == "H":
                    end_row = start_row
                    end_col = start_col + size - 1
                else:
                    end_row = start_row + size - 1
                    end_col = start_col

                if end_row >= 10 or end_col >= 10:
                    if not is_computer:
                        print("Ship placement is out of bounds. Try again.")
                    continue

                valid_placement = True
                for r in range(start_row, end_row + 1):
                    for c in range(start_col, end_col + 1):
                        if board[r][c] != "0":
                            valid_placement = False

                if not valid_placement:
                    if not is_computer:
                        print("Invalid placement, ship overlaps another ship. Try again.")
                    continue

                ships.append([(r, c) for r in range(start_row, end_row + 1) for c in range(start_col, end_col + 1)])
                for r in range(start_row, end_row + 1):
                    for c in range(start_col, end_col + 1):
                        board[r][c] = "S"
                break

            except ValueError:
                if not is_computer:
                    print("Invalid input. Enter numbers only for rows and columns.")
                continue

    player['ships'] = ships
    if not is_computer:
        print(f"{player['name']}'s board:")
        show_board(board)
        for r in range(10):
            for c in range(10):
                if board[r][c] == "S":
                    board[r][c] = "0"  # Reset the board to hide ships
        print("\n" * 5)  # Clear screen for the next player's placement

def player_turns(total_turns):
    if total_turns % 2 == 0:
        return player_one
    return computer

def play_again():
    positive = ["yes", "y"]
    negative = ["no", "n"]

    while True:
        answer = input("Play again? [yes/no]: ").lower().strip()
        if answer in positive:
            main()
            break
        elif answer in negative:
            print("Thanks for playing!")
            exit()

def input_check(player, opponent, board):
    if player == computer:
        guess_row, guess_col = computer_guess(board)
    else:
        while True:
            try:
                guess_row = int(input("Guess Row (1-10): ")) - 1
                guess_col = int(input("Guess Col (1-10): ")) - 1
            except ValueError:
                print("Enter a number only: ")
                continue
            else:
                break

    not_on_game_board = (guess_row < 0 or guess_row >= 10) or (guess_col < 0 or guess_col >= 10)

    if not_on_game_board:
        if player == computer:
            return False
        else:
            print("Oops, that's not even in the ocean! :P.")
    elif board[guess_row][guess_col] in ["X", "Y"]:
        if player == computer:
            return False
        else:
            print("You've already guessed that location.")
    else:
        hit = False
        for ship in opponent['ships']:
            if (guess_row, guess_col) in ship:
                ship.remove((guess_row, guess_col))
                if not ship:
                    opponent['ships'].remove(ship)
                    print("You sunk a ship!")
                else:
                    print("You hit a ship! Take another shot!")
                hit = True
                break

        if hit:
            if player == player_one:
                board[guess_row][guess_col] = "X"
            else:
                board[guess_row][guess_col] = "Y"
            return True
        else:
            print("You missed!")
            board[guess_row][guess_col] = "M"
        
        print(colors["cyan"])
        show_board(game_board)
        print(colors["reset"])

        if not opponent['ships']:
            player["wins"] += 1
            print(f"Congratulations! {player['name']} wins!")
            print('The current match score is %d : %d (Player1 : Computer)' % (player_one["wins"], computer["wins"]))
            play_again()

    return False

def computer_guess(board):
    while True:
        guess_row = randint(0, 9)
        guess_col = randint(0, 9)
        if board[guess_row][guess_col] not in ["X", "Y", "M"]:
            return guess_row, guess_col

def main():
    print("WELCOME TO BATTLESHIP")
    print("Find & sink the other player's ships")
    print("THIS IS A PLAYER VS COMPUTER GAME")

    del game_board[:]
    build_game_board(game_board)
    print("Player 1, place your ships.")
    place_ships(player_one, game_board)
    print("Computer is placing its ships.")
    place_ships(computer, game_board, is_computer=True)

    turns = 0
    while True:
        current_player = player_turns(turns)
        opponent_player = player_one if current_player == computer else computer
        print(f"{current_player['name']}'s turn")
        another_shot = input_check(current_player, opponent_player, game_board)
        
        if not another_shot:
            turns += 1

if __name__ == "__main__":
    main()


