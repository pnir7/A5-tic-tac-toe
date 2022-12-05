# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    for line in range(3):
        if board[line][0] == board[line][1] == board[line][2]:
            return board[line][0]
    # check for col win #
    for line in range(3):
        if board[0][line] == board[1][line] == board[2][line]:
            return board[0][line]
    # check For diagonal #
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    # check For draw #
    return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'O':
        return 'X'
    else:
        return "O"


def gen_num():
    col = random.randint(0, 2)
    row = random.randint(0, 2)
    return col, row


def user_input():
    ret = input('input a number plz')
    if ret.isdigit():
        num = int(ret)
        if 0 <= num <= 2:
            return num
    return False


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    cur_player = 'X'
    # computer = 'O'
    player_name=input('Please input your name:')
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