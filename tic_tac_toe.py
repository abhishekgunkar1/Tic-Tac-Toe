
from person_player import *
from board import *
from game import *

				

player1 = PersonPlayer("X")

player2 = PersonPlayer("O")

my_board = Board()

my_game = MainGame(my_board, player1, player2)

my_game.play()