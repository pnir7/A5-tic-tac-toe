import json
import threading

from flask import Flask, request

_server = Flask(__name__)
_lock = threading.Lock()

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

"http://127.0.0.1:30077/chat"


# @_server.route("/start", methods=["GET"])
# def start():
#     """162.251.61.230:30062"""
#     try:
#         return name()
#     except Exception as e:
#         print(e)
#     return 'ok'


@_server.route("/start", methods=["POST"])
def start():
    """162.251.61.230:30062"""
    global player_name
    global another_name
    global mode
    try:
        player_name = request.json("player")
        another_name = request.json("another")
        mode = request.json("mode")
        if mode != "0" and mode != "1":
            return "0 is PVP , 1 is PVE"
        if player_name is None or player_name == '':
            return "Please input Player One's Name"
        if mode == 1 and (another_name is None or another_name == ''):
            return "Please input Player Two's Name"
        return "ok"
    except Exception as e:
        print(e)
    return 'error'


@_server.route("/play", methods=["POST"])
def play():
    """162.251.61.230:30062"""
    try:
        x = request.json("x")
        y = request.json("y")

        result = check_input_num(x)
        if not result:
            return "x is invalid"

        result = check_input_num(y)
        if not result:
            return "y is invalid"

        if board[x][y] is not None:
            return "x,y num exists"

        if mode == "1":
            return play_robot(x, y)
        else:
            return play_person(x, y)
    except Exception as e:
        print(e)
    return 'error'


@_server.route("/rank", methods=["POST"])
def rank():
    """162.251.61.230:30062"""
    try:
        # read CSV 
        return result
    except Exception as e:
        print(e)
    return 'error'


def play_person(x, y):
    """162.251.61.230:30062"""
    global cur_player
    try:
        if cur_player is None:
            cur_player = "X"

        board[x][y] = cur_player

        if checkWinner():
            return board, "finish"
        else:
            return board

    except Exception as e:
        print(e)
    return 'error'


def play_robot(x, y):
    """162.251.61.230:30062"""
    try:
        board[x][y] = "X"

        if checkWinner():
            return board, "finish"

        # robot play
        row, col = logic.gen_num()
        while board[row][col] is not None:
            row, col = logic.gen_num()

        board[row][col] = "O"

        if checkWinner():
            return board, "finish"
        else:
            return board

    except Exception as e:
        print(e)
    return 'error'


def check_input_num(x):
    if x.isdigit():
        num = int(x)
        if 0 <= num <= 2:
            return True
    return False


def checkWinner():
    winner = get_winner(board)
    if winner == "X":
        this_database.record_game(player_name, 'win')
        this_database.record_game("anqi", 'lose')
        return True
    elif winner == "O":
        this_database.record_game(player_name, 'lose')
        this_database.record_game("anqi", 'win')
        return True
    return False


if __name__ == '__main__':
    _server.run(host='0.0.0.0', port=30077, debug=False)
