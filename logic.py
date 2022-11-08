# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


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