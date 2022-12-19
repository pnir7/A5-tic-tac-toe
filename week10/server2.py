import random
from flask import Flask, request, make_response, render_template, redirect

_server = Flask(__name__)

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def gen_num():
    candidates = []
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                candidates.append((row, col))
    if not candidates:
        return
    return random.choice(candidates)


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

board = make_empty_board()

@_server.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        resp = make_response()
        resp.set_cookie('name', name)
        board[:] = make_empty_board()
        return redirect('/play')
    return render_template('index.html')

@_server.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        x = int(request.form.get('x'))
        y = int(request.form.get('y'))
        if not board[x][y]:
            board[x][y] = 'X'
            winner = get_winner(board)
            if not winner:
                result = gen_num()
                if result:
                    row, col = result
                    board[row][col] = 'O'
                    winner = get_winner(board)
                else:
                    winner = 'draw'
        else:
            winner = get_winner(board)
    else:
        winner = get_winner(board)

    return render_template('play.html', board=board, winner=winner)


if __name__ == '__main__':
    _server.run(host='0.0.0.0', port=30077, debug=True)
