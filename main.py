from game import TicTacToeGame
from cmd import Cmd


class TicTacToeMain(Cmd):
	"""Simulates main menu of game."""

	def __init__(self):
		super().__init__()
		self.game = None
		self.do_print_instructions(None)


	def do_print_instructions(self, args):
		"""Prints instructions."""
		print("Welcome to Tic-Tac-Toe!!!")
		print()
		print("How to use: ")
		print("Enter 'start' to begin a new game.")
		print("Enter 'exit' to exit application.")
		print("In game, to select a cell to place a marker on, enter in " +
			"the format '<row>,<col>' (without the quotes), where <row>" +
			" and <col> are integers between 1 and 3 inclusive.")
		print("<row> and <col> refer to the row and column indices, " +
			"respectively, where row 1 is the topmost row, " +
			"and col 1 is the leftmost column.")
		print("For example, placing an X on (2, 3) will result in: ")

		example_grid = [["_" for _ in range(3)] for _ in range(3)]
		example_grid[1][2] = "X"
		print()
		print('\n'.join(''.join(*zip(*row)) for row in example_grid))
		print()

	def do_start(self, args):
		"""Starts a new game."""
		self.game = TicTacToeGame()
		self.game.gameLoop()

	def do_exit(self, args):
		"""Exits application."""
		print("Exiting. Thanks for playing!")
		raise SystemExit


if __name__ == '__main__':
	main = TicTacToeMain()
	main.prompt = '> '
	main.cmdloop()
		