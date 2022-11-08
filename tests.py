import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!
    
    def test_other_player(self):
        self.assertEqual(logic.other_player('O'), 'X')

    def test_empty_board(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]

        for x in range(len(board)):
            y = list(board[x])
            for l in range(len(y)):
                if board[x][l] != None:
                    return False
        
        self.assertEqual(logic.make_empty_board(), True)
    
    def test_get_winner(self):
        board2 = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board2), None)
    

if __name__ == '__main__':
    unittest.main()