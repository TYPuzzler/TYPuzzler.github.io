# This script contains all the utilily classes and functions

# Base case exception.
class PuzzlePieceException(Exception):
	pass

# Raised when user ask for a non-existing piece.
class NoSuchPieceException(PuzzlePieceException):
	pass