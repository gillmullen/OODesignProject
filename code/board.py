COLUMNS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"]
ROWS = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", "10 ", "11 ", "12 ", "13 ", "14 ", "15 ", "16 ", "17 ", "18 ", "19 "]

class Board:
	def __init__(self, size):
		'''Initialises board
		   size: Size of board required (int)
		   return None
		'''
		self.board = [["╔"] + ["╦" for x in range(size-2)] + ["╗"]] + \
					 [["╠"] + ["╬" for x in range(size-2)] + ["╣"] for x in range(size-2)] + \
					 [["╚"] + ["╩" for x in range(size-2)] + ["╝"]]

	def is_valid_move(self, piece, move):
		'''Determines whether a move is valid
		   piece: Piece being moved on board (str)
		   move: Move user is making ((int, int))
		   return bool
		'''
		pass

	def place_stone(self, piece, move):
		'''Makes user's move
		   piece: Piece being moved on board (str)
		   move: Move user is making ((int, int))
		   return None
		'''
		self.board[move[0]][move[1]] = piece
		return

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

	def __str__(self):
		'''return str representation of board'''
		s = "   " + "  ".join(COLUMNS[:len(self.board)]) + ("\n")
		for i in range(len(self.board) - 1):
			s += ROWS[i] + "══".join(self.board[i]) + ("\n")
			s += "   " + "║  " * len(self.board) + ("\n")
		s += ROWS[i+1] + "══".join(self.board[-1]) + ("\n")
		return s
