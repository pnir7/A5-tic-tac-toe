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
import database

def get_ranking(df_in,top_k = 3):
    # df_in : player list sorted
    assert top_k < len(df_in)
    res = []
    for i in range(top_k):
        subdf = df_in.iloc[i]
        name =  subdf["player"]
        score = subdf["win"]*3 + subdf["draw"]*1
        res.append((name,score))
    
    return res
        

if __name__ == '__main__':
    board = make_empty_board()

    winner = None
    cur_player = 'X'
    this_database=database.database()
    player_name=input('Please input your name:')
    while(True):
        mode = input('Please input mode: 1 for pvb, 0 for pvp')
        if mode.isdigit():
            mode = int(mode)
            if mode in [0,1]:
                break

    
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
            # if it's a robot's turn
            if mode == 1:
                row, col = logic.gen_num()
                while board[row][col] is not None:
                    row, col = logic.gen_num()
            
                board[row][col] = cur_player
            
            else: # pvb mode
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

        # TODO: Update who's turn it is.
        #print("TODO: take a turn!")
        cur_player = other_player(cur_player)

        # winner
        winner = get_winner(board)
    if winner=="X":
        this_database.record_game(player_name,'win')    
    elif winner=="O":
        this_database.record_game(player_name,'lose')
    
    ranking = get_ranking(this_database.get_ranking_list())

    print(winner, 'Win')
    for i,(name,score) in enumerate(ranking):
        print('World ranking {}, name: {}, score: {}'.format(i+1,name,score))


