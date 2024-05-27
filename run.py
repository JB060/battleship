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

    #Allows new game to start







