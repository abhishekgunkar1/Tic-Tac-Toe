
from player import *

class PersonPlayer(Player):
	#an instance of the player class

	def __init__(self, symbol):
		self.symbol = symbol

	def get_move(self):
		move = 0
		while (move == 0):
			print("It's your move player " + self.symbol)