"""Simulates a game of tic-tac-toe."""


# Contains possible winning positions for each cell in grid.
# "r<#>": row #. "c<#>": col #.
# "d0": diagonal from top left to bottom right.
# "d1": opposite diagonal. 
# Each cell represented by (row, col) tuple.
POSITIONS_FOR_CELL = {
	(0, 0): ["r0", "c0", "d0"],
	(0, 1): ["r0", "c1"],
	(0, 2): ["r0", "c2", "d1"],
	(1, 0): ["r1", "c0"],
	(1, 1): ["r1", "c1", "d0", "d1"],
	(1, 2): ["r1", "c2"],
	(2, 0): ["r2", "c0", "d1"],
	(2, 1): ["r2", "c1"],
	(2, 2): ["r2", "c2", "d0"]
}

# Markers of each player.
PLAYER_MARKERS = ["O", "X"]


class TicTacToeGame():
	"""Represents a game of tic-tac-toe."""

	def __init__(self):
		"""Initalizes the game instance."""

		print("New game started.")

		self.turns_taken = 0;

		# Initalize which player goes first.
		received_valid_input = False
		while not received_valid_input:
			first_player = input("Who goes first - X or O?");
			if first_player == "X":
				self.x_turn = True
				received_valid_input = True
			elif first_player == "O":
				self.x_turn = False
				received_valid_input = True
			else:
				print("ERROR: Received invalid input - please enter either " +
						"'X' or 'O' (without quotes).")

		# Contains contents of 3 x 3 grid.
		# Each cell: "_" if empty, "x" if occupied Player X,
		# 	"o" if by Player O.
		self.grid = [["_" for _ in range(3)] for _ in range(3)]

		# Contains count of number of cells to satisfy each
		#	winning position, for Player O and X.
		# If a count (dictionary) value is 3, someone has won the game.
		self.winning_positions = [dict.fromkeys(["r0", "r1", "r2", "c0", "c1",
									"c2", "d0", "d1"], 0) for _ in range(2)]


	def printBoard(self):
		"""Prints the board."""
		print()
		print('\n'.join(''.join(*zip(*row)) for row in self.grid))
		print()


	def receiveUserInput(self, curr_marker):
		"""
		Receive and perform validity checks on user cell input.
		Returns False if input invalid, or (row, col) if input valid.
		"""

		turn = input("Player " + curr_marker + ":")

		# Check if input is able to be processed.
		try:
			turn = turn.split(",")
			row = int(turn[0]) - 1  # 0-index input
			col = int(turn[1]) - 1  # 0-index input
		except ValueError:
			print("ERROR: Received invalid input - please enter cell in " +
				"the format of '<row>, <col>' (without quotes), where <row>" +
				" and <col> are integers.")
			return False

		# Check if input row, col values are in valid range.
		if row < 0 or row >= 3 or col < 0 or col >= 3:
			print("ERROR: Received invalid input - make sure <row> and " +
				"<col> are in the range [1, 3], inclusive.")
			return False

		# Check if a marker already exists at (row, col) on grid.
		if self.grid[row][col] != "_":
			print("ERROR: Cell at (" + turn[0] + ", " + turn[1] + ")" +
				" already occupied.")
			return False

		return (row, col)


	def takeTurn(self):
		"""
		Take a turn.
		Returns bool value representing whether someone has won.
		"""

		self.printBoard()

		curr_player_index = int(self.x_turn)
		curr_marker = PLAYER_MARKERS[curr_player_index]

		received_valid_input = False
		while not received_valid_input:
			try:
				row, col = self.receiveUserInput(curr_marker)
				received_valid_input = True
			except TypeError:
				pass

		# Update board, winning position variables.
		self.grid[row][col] = curr_marker
		for pos in POSITIONS_FOR_CELL[(row, col)]:
			self.winning_positions[curr_player_index][pos] += 1

			# Check if a winning position has 3 counts.
			if self.winning_positions[curr_player_index][pos] == 3:
				self.printBoard()
				print("Player " + curr_marker + " has won!")
				return True

		# Switch turns.
		self.x_turn = not self.x_turn

		self.turns_taken += 1

		return False

	
	def gameLoop(self):
		while self.turns_taken < 9:
			if self.takeTurn():
				return
		
		self.printBoard()
		print("Game ended in tie.")