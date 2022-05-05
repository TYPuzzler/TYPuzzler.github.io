from puzzle import *
from roller import *

def newPuzzle(URL, name, size):
	p = Puzzle(URL, size, name)
	p.savePieces()
	return p.saveFullPuzzle()
