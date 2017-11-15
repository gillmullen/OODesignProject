class Board:
	def __init__(self, size):
		'''Initialises board
		   size: Size of board required (int)
		   return None
		'''
		pass

	def is_valid_move(self, piece, move):
		'''Determines whether a move is valid
		   piece: Piece being moved on board (str)
		   move: Move user is making ((int, int))
		   return bool
		'''
		pass

	def place_stone(self, piece, move):
		'''Makes users move
		   piece: Piece being moved on board (str)
		   move: Move user is making ((int, int))
		   return None
		'''
		pass

	def move_possible(self, piece):
		'''Checks if it's possible for a piece to move
		   piece: Piece to check on board (str)
		   return bool
		'''
		pass

	def return_score(self, piece):
		'''Returns final score for piece on board
		   piece: Piece being moved on board (str)
		   return score (float)
		'''
		pass
        
        def remove_stone(self, position):
                '''Removes stone from the board 
                   Position: Position on the board to remove piece from ((int, int))
                   return none 
                '''
                pass

	def __str__(self):
		'''return str representation of board'''
		pass
