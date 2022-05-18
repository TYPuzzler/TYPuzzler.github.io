import urllib.request
# This script contains all the utilily classes and functions

# Base case exception.
class PuzzleException(Exception):
	pass

class PuzzlePieceException(PuzzleException):
	pass

# Raised when user ask for a non-existing piece.
class NoSuchPieceException(PuzzlePieceException):
	pass

def writeRarity(nameOfPuzzle):
	meta = open('../../images/' + nameOfPuzzle + '/metadata.txt', 'r')
	ml = meta.readlines()
	nL = []
	rL = []
	srL = []
	ssrL = []
	for i in range(4, len(ml), 4):
		num = ml[i].splitlines()[0]
		rarity = str(ml[i + 2]).splitlines()[0]
		if rarity == 'N':
			nL.append(num)
		elif rarity == 'R':
			rL.append(num)
		elif rarity == 'SR':
			srL.append(num)
		elif rarity == 'SSR':
			ssrL.append(num)

	f = open('../../images/' + nameOfPuzzle + '/N.txt', 'w')
	f.writelines("\n".join(nL))
	f.close
	f = open('../../images/' + nameOfPuzzle + '/R.txt', 'w')
	f.writelines("\n".join(rL))
	f.close
	f = open('../../images/' + nameOfPuzzle + '/SR.txt', 'w')
	f.writelines("\n".join(srL))
	f.close
	f = open('../../images/' + nameOfPuzzle + '/SSR.txt', 'w')
	f.writelines("\n".join(ssrL))
	f.close