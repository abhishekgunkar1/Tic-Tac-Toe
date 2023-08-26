
import sys

class Board(object):
	#has a list of tiles
	def __init__(self):
		self.tiles = [x for x in range(9)]

	def arrange_board(self):
		board = [self.tiles[0], self.tiles[1], self.tiles[2]], [self.tiles[3], self.tiles[4], self.tiles[5]], [self.tiles[6], self.tiles[7], self.tiles[8]]
		return board

	def print_board(self):
		board = self.arrange_board()
		for row in board:
			sys.stdout.write("|")
			for tile in row:
				sys.stdout.write(str(tile) + "|")
			sys.stdout.write("\n")
		return True