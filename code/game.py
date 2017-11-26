from board import Board, COLUMNS, ROWS

class Game:
	def __init__(self, user1, user2, size):
		'''Initialises a game
		   user1: First user (User)
		   user2: Second user (User)
		   size: Size of board required (int)
		   return None
		'''
		self.user1 = user1
		self.user2 = user2
		self.size = size
		self.turn = user1
		self.board = Board(size)

	def change_turn(self, user):
		'''Changes turn to opposite user
		   user: User who's current turn it is
		   return None
		'''
		if user == self.user1:
			self.turn = self.user2
		else:
			self.turn = self.user1

	def determine_whose_move(self):
		'''Determines whose move is next
		   Returns True if it's user1's move otherwise False
		   return bool 
		'''
		return self.turn == self.user1

	def check_game_finished(self):
		'''Checks if game has ended
		   Returns True if game has ended
		   return bool
		'''
		pass

	def user_action(self, user, command):
		'''Determines which play the user wants to make
		   eg. Forfeit game, make move, pass turn
		   user: User making command (User)
		   command: Play user wants to make (list)
		   return None
		'''
		if command == "forfeit":
			self.forfeit_game(user)
		elif command == "pass":
			self.pass_turn(user)
		else:
			self.make_move(user, command)

	def make_move(self, user, move):
		'''Makes players move
		   user: User making move (User)
		   move: Players chosen move ((int, int))
		   return None 
		'''
		move = (int(move[1])-1, COLUMNS.index(move[0]))
		if self.user1 == user:
			piece = "X"
		else:
			piece = "O"

		if self.board.is_valid_move(piece, move):
			self.board.place_stone(piece, move)
			self.change_turn(user)
		else:
			#Error function, invalid move
			pass

	def pass_turn(self, user):
		'''Passes users turn
		   user: User passing turn (User)
		   return None
		'''
		self.change_turn(user)

	def forfeit_game(self, user):
		'''Forfeits user from game
		   user: User forfeiting game (User)
		   return None
		'''
		pass
