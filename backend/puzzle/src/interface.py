from puzzle import *
from roller import *

def newPuzzle(URL, name, size):
	p = Puzzle(URL, size, name)
	return p.saveFullPuzzle()
