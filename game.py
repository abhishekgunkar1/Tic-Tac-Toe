from move import *


class MainGame(object):
	def __init__(self, board, player1, player2):
		self.board = board
		self.players = [player1, player2]
		self.turn = 0

	def greet_user(self, currplayer):
		print ("It's your turn player " + currplayer.symbol)
		return True

	def play(self):
		flag = False
		
		while flag == False:
			#GAME NEEDS TO GET BOARD.. HOW DO I DO THIS!!!!
			#set first player to first element in self.players list
			currplayer = self.players[self.turn]
			#print board
			self.board.print_board()
			#great user
			self.greet_user(currplayer)
			#ask for move
			move = Move(self.board, currplayer)
			player_move = move.ask_for_move()
			#move - switch board number to player symbol
			self.board.tiles[player_move] = currplayer.symbol
			#checks for a win
			winner = self.check_win(currplayer.symbol)
			#if win, declare win and break loop
			if winner != False:
				self.game_over(winner)
				flag = True
			#else, switch turns by flipping index in self.players array
			else:
				self.turn = 1 - self.turn
		return True

	def check_win(self, player_symbol):
		tiles = self.board.tiles

		for i in range(3):
			if tiles[i] == player_symbol and tiles[i+3] == player_symbol and tiles[i+6] == player_symbol: #check for vertical win
				return player_symbol
			elif tiles[(i*3)] == player_symbol and tiles[(i*3) + 1] == player_symbol and tiles[(i*3) + 2] == player_symbol: #check for horizontal win
				return player_symbol

			#check for diagonal wins
			if tiles[0] == player_symbol and tiles[4] == player_symbol and tiles[8] == player_symbol:
				return player_symbol
			elif tiles[2] == player_symbol and tiles[4] == player_symbol and tiles[6] == player_symbol:
				return player_symbol

    #if no wins, return false
		return False

	def game_over(self, player_symbol):
			print ("It's over! Player " + player_symbol + "wins!")