# This script contains all the utilily classes and functions

# Base case exception.
class PuzzleException(Exception):
	pass

class PuzzlePieceException(PuzzleException):
	pass

# Raised when user ask for a non-existing piece.
class NoSuchPieceException(PuzzlePieceException):
	pass