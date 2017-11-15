class Game:
	def __init__(self, user1, user2, size):
		'''Initialises a game
		   user1: First user (User)
		   user2: Second user (User)
		   size: Size of board required (int)
		   return None
		'''
		pass

	def determine_whose_move(self):
		'''Determines whose move is next
		   Returns True if it's user1's move otherwise False
		   return bool 
		'''
		pass

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
		pass

	def place_stone(self, user, move):
		'''Makes players move
		   user: User making move (User)
		   move: Players chosen move ((int, int))
		   return None 
		'''
		pass

	def pass_turn(self, user):
		'''Passes users turn
		   user: User passing turn (User)
		   return None
		'''
		pass

	def forfeit_game(self, user):
		'''Forfeits user from game
		   user: User forfeiting game (User)
		   return None
		'''
		pass
