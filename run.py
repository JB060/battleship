from random import randint

game_board -[]

player_one = {
    "name": "player 1",
    "wins": 0,
}

player_two = {
    "name": "player 2"
    "wins" : 0,
}

colors - {
    "reset":"\033[00m",
    "red":"\033[91m",
    "blue":"\033[94m",
    "cyan":"\033[96m",
}

#Building our 6X6 Board
def build_game_board(board):
    for item in range(6):
        board.append(["0" * 6])

def show_board(board):
    for row in board:
        print("".join (row))

#defining ships location
def load_game(board):
    print("WELCOME TO BATTLESHIP")
    print("Find & sink the other players ships")
    print("THIS IS A 2 PLAYER GAME ")
    del board[:]
    build_game_board(board):
    print(colors['blue'])
    show_board(board)
    print(colors['reset'])
    ship_col = randint(1, len(board))
    ship_row = randint(1, len(board[0]))
    return{
        'ship_col': ship_col,
        'ship_row': ship_row,
    }

    ship_points = load_game(game_board)

    #Players will alternate turns.
    def player_turns(total_turns):

        if total_turns % 2 == 0
           total_turns += 1
           return player_one

        return player_two

    #Allows new game to start.abs
    def play_again():

        positive = ["yes","y"]
        negative = ["no""n"]

        global ship_points

        while True:
            answer = input("play again?[yes/no]:").lower().strip()
            if answer in positive:
                ship_points = load_game(game_board)
                main()
                break

            elif answer in negative:
                print("Thanks for Playing!")
                exit()
        
    # what happens with players guesses.
    def input_check(ship_row, ship_col, player, board):
        guess_col = 0
        guess_row = 0
        while True:

            try:
                 guess_row int(input("Guess Row:")) - 1
                 guess_col int(input("Guess Col:")) - 1
            except ValueError:

                print("Enter a number only: ")
                continue
            else:

                break
        match = guess_row == ship_row - 1 and guess_col == ship_col - 1
        not_on_game_board = (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6)

        if match:
            player["wins"] += 1
            print("Congradulations! you sunk my battleShip! ")
            print('The current match score is %d : %d (Player1 : Player2)'% (player_one["wins"], player_two["wins"]))
            print("Thanks for Playing!")
            play_again()

        elif not match:
            if not_on_game_board
                print("Oops, that's not even in the ocean! :P.")
            
            elif board[guess_row][guess_col] = "X" or board[guess_row][guess_col] == "Y":
                 print("You've Already guessed that location.")

            else:
                 print ("You Missed my battleShip!")
                 if player == player_one:
                    board[guess_row][guess_col] = "X"
                else:
                    board[guess_row][guess_col] = "Y"

            print(colors["cyan"])
            show_board(game_board)
            print(colors ["reset"])

        else:
            return 0
    
    def main():

        for turns in range(10):
            












