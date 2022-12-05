# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import logic
from logic import make_empty_board
from logic import get_winner
from logic import other_player
from logic import gen_num
from logic import user_input
import random

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    cur_player = 'X'
    # computer = 'O'
    while winner is None:
        print("New Loop")

        # TODO: Show the board to the user.
        for row in board:
            print(*row)

        # TODO: Input a move from the player.
        if cur_player == 'X':
            col = False
            while col is False:
                col = logic.user_input()
                if col is False:
                    print('shit, this is not a fucking number!!!!')

            row = False
            while row is False:
                row = logic.user_input()
                if row is False:
                    print('shit, this is not a fucking number!!!!')

            if board[row][col] is not None:
                print('It is not available')
                continue
            else:
                board[row][col] = cur_player
        else:
            row, col = logic.gen_num()
            while board[row][col] is not None:
                row, col = logic.gen_num()
            board[row][col] = cur_player

        # TODO: Update who's turn it is.
        #print("TODO: take a turn!")
        cur_player = other_player(cur_player)

        # winner
        winner = get_winner(board)

    print(winner, 'Win')