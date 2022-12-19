import random
from flask import Flask, request, make_response, render_template, redirect

from database import database

db = database()

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
        if not name:
            return render_template('index.html', error='Please enter your name')
        mode = request.form.get('mode')
        resp = make_response(redirect('/play'))
        resp.set_cookie('name', name)
        resp.set_cookie('mode', mode)
        board[:] = make_empty_board()
        return resp
    
    name = request.cookies.get('name', '')
    return render_template('index.html', name=name)

@_server.route('/play', methods=['GET', 'POST'])
def play():
    name = request.cookies.get('name')
    mode = request.cookies.get('mode')
    if not name or not mode:
        return redirect('/')

    player = request.form.get('player', 'X')
    if request.method == 'POST':
        x = int(request.form.get('x'))
        y = int(request.form.get('y'))
        if not board[x][y]:
            board[x][y] = player
            winner = get_winner(board)
            if not winner:
                if mode == '1':
                    result = gen_num()
                    if result:
                        row, col = result
                        board[row][col] = 'O'
                        winner = get_winner(board)
                    else:
                        winner = 'draw'
                else:
                    player = 'O' if player == 'X' else 'X'
        else:
            winner = get_winner(board)
        
        if mode == '1' and winner:
            if winner == 'draw':
                db.record_game(name, 'draw')
            elif winner == 'X':
                db.record_game(name, 'win')
            else:
                db.record_game(name, 'lose')
    else:
        winner = get_winner(board)
    
    return render_template('play.html', mode=mode, board=board, player=player, winner=winner)



@_server.route('/stats')
def stats():
    ranking_list = db.get_ranking_list()
    print(ranking_list)
    return render_template('stats.html', ranking_list=ranking_list)


if __name__ == '__main__':
    _server.run(host='0.0.0.0', port=30077, debug=True)
