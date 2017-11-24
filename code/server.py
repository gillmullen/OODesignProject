from game import Game
from user import User
class Server:
	def __init__(self, user_list=[], wait_list=[]):
		'''Initialises server
		   user_list: Contains users known to server
		   wait_list: Contains users waiting for a game
		   return None
		'''
		self.user_list = user_list
		self.wait_list = wait_list

	def _add_user(self, username):
		'''Adds new user to system
		   username: Username the user chooses (str)
		   return None
		'''
		pass


	def join_server(self, username):
		'''Logs user onto server, creating a new account if necessary
		   username: Username the user chooses (str)
		   return None
		'''
		if username not in self.user_list:
			self._add_user(username)

	def join_game(self, username, size):
		'''Adds user to game
		   username: Username for user (str)
		   size: Size user wants for game (int)
		   return player number and piece (str)
		'''
		pass 

	def generate_game(self, user1, user2, size=9):
		'''Generates a game for two users
		   user1: First user (User)
		   user2: Second user (User)
		   size: Size of board required for game (int)
		   return None
		'''
		pass

	def pair_waiting_players(self):
		'''Checks wait list. If there's more than one user in
		   the wait list generate a game
		   return None
		'''
		pass

	def request_move(self, user):
		'''Requests a user to make their next move
		   user: User to make move (User)
		   return None
		'''
		pass

	def user_play(self, user, command):
		'''Calls the Game with the users command
		   user: User making command (User)
		   command: Play user wants to make (list)
		   return bool determining if an error occured
		'''
		pass

	def _game_over(self, game, user1, user2):
		'''Game has ended. Increments win_count for winner.
		   game: Game which has ended (Game)
		   user1: First user (User)
		   user2: Second user (User)
		   return win/lose message (str)
		'''
		pass