class Move(object):
	def __init__(self, board, player):
		self.board = board
		self.player = player

	def ask_for_move(self):
		flag = False 
		possible_moves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

		while (flag != True):
			move = input("Please enter the number where you wanna move your " + self.player.symbol + ":")
			
			#check to see if user entered a number 0-8, if so, convert to int.
			#try to refactor this out
			if move in possible_moves:
				move = int(move)
			else:
				print ("Please enter valid move")
				return self.ask_for_move()

			#check to see if tile user wants to use is empty, or if someone has already played a piece there.
			#try to refactor this out
			if move != self.board.tiles[move]:
				print ("Someone has already moved to that spot. Please move to an open tile.")
				return self.ask_for_move()

			return move