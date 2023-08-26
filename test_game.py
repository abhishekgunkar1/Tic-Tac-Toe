import unittest
from person_player import *
from board import *
from game import *

class TestTicTacToe(unittest.TestCase):
    
    def test_arrange_board(self):
        b = Board()
        temp_board = ([0, 1, 2], [3, 4, 5], [6, 7, 8])
        self.assertEqual(b.arrange_board(), temp_board)

    def test_print_board(self):
        b = Board()
        # b.arrange_board()
        self.assertEqual(b.print_board(), True)

    def test_greet_user(self):
        player1 = PersonPlayer("X")
        player2 = PersonPlayer("O")
        my_board = Board()
        my_game = MainGame(my_board, player1, player2)
        self.assertEqual(my_game.greet_user(player1), True)

        

if __name__ == "__main__":
    unittest.main()