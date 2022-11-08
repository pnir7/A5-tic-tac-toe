# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board 
from logic import get_winner
from logic import other_player

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    cur_player = 'X'
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        for row in board:
            print(*row)

        # TODO: Input a move from the player.
        a = input('please input row')
        try:
            a = int(a)
        except ValueError:
            print('shit, this is not a fucking number!!!!')
        if int(a) >= 0 and int(a) < 3:
            b = input('please input clo')
            try:
                b = int(b)
            except ValueError:
	            print ('shit, this is not a fucking number!!!!')

            if int(b) >= 0 and int(b) < 3 and board[int(a)][int(b)] == None:
                # TODO: Update the board.
                board[int(a)][int(b)] = cur_player
            else:
                print('please input again')
                continue
        else:
            print('please input again')
            continue
        

        # TODO: Update who's turn it is.
        cur_player = other_player(cur_player)

        winner = get_winner(board)  
    
    print(winner, 'Win')