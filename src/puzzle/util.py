import urllib.request
from PIL import Image 
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
	f.close()
	f = open('../../images/' + nameOfPuzzle + '/R.txt', 'w')
	f.writelines("\n".join(rL))
	f.close()
	f = open('../../images/' + nameOfPuzzle + '/SR.txt', 'w')
	f.writelines("\n".join(srL))
	f.close()
	f = open('../../images/' + nameOfPuzzle + '/SSR.txt', 'w')
	f.writelines("\n".join(ssrL))
	f.close()

def write_sql_inserts(nameOfPuzzle):
	meta = open('../../images/' + nameOfPuzzle + '/metadata.txt', 'r')
	ml = meta.readlines()
	meta.close()
	f = open('sql.txt', 'w')
	lines = []
	for i in range(4, len(ml), 4):
		num = ml[i].splitlines()[0]
		rarity = str(ml[i + 2]).splitlines()[0]
		x = str(ml[i + 1]).splitlines()[0].split(',')[0]
		y = str(ml[i + 1]).splitlines()[0].split(',')[1]
		line = 'insert into ' + nameOfPuzzle + ' values(' + num + ', \'https://raw.githubusercontent.com/TYPuzzler/TYPuzzler.github.io/main/images/' + nameOfPuzzle + '/' + nameOfPuzzle + '_piece_' + num + '.png\', \'' + rarity + '\', ' + x + ', ' + y + ');'
		lines.append(line)
	f.writelines('\n'.join(lines))
	f.close()

def write_sql_updates_for_trans(nameOfPuzzle):
	meta = open('../../images/' + nameOfPuzzle + '/metadata.txt', 'r')
	ml = meta.readlines()
	meta.close()
	f = open('sql.txt', 'w')
	lines = []
	for i in range(4, len(ml), 4):
		num = ml[i].splitlines()[0]
		rarity = str(ml[i + 2]).splitlines()[0]
		x = str(ml[i + 1]).splitlines()[0].split(',')[0]
		y = str(ml[i + 1]).splitlines()[0].split(',')[1]
		line = 'update ' + nameOfPuzzle + ' set trans_url = \'https://raw.githubusercontent.com/TYPuzzler/TYPuzzler.github.io/main/images/' + nameOfPuzzle + '/trans_piece_' + num + '.png\' where piece_num = ' + num + ';'
		lines.append(line)
	f.writelines('\n'.join(lines))
	f.close()

def add_new_to_piece(nameOfPuzzle):
	meta = open('../../images/' + nameOfPuzzle + '/metadata.txt', 'r')
	ml = meta.readlines()
	meta.close()
	num = int(ml[2].splitlines()[0])
	for i in range(num):
		n = i + 1
		img = Image.open('../../images/' + nameOfPuzzle + '/' + nameOfPuzzle + '_piece_' + str(n) + '.png')
		new = Image.open('../../images/new.png')
		img.paste(new, (0,0), new)
		img.save('../../images/' + nameOfPuzzle + '/new_piece_' + str(n) + '.png')

def write_sql_updates_for_news(nameOfPuzzle):
	meta = open('../../images/' + nameOfPuzzle + '/metadata.txt', 'r')
	ml = meta.readlines()
	meta.close()
	f = open('sql.txt', 'w')
	lines = []
	for i in range(4, len(ml), 4):
		num = ml[i].splitlines()[0]
		rarity = str(ml[i + 2]).splitlines()[0]
		x = str(ml[i + 1]).splitlines()[0].split(',')[0]
		y = str(ml[i + 1]).splitlines()[0].split(',')[1]
		line = 'update ' + nameOfPuzzle + ' set new_url = \'https://raw.githubusercontent.com/TYPuzzler/TYPuzzler.github.io/main/images/' + nameOfPuzzle + '/new_piece_' + num + '.png\' where piece_num = ' + num + ';'
		lines.append(line)
	f.writelines('\n'.join(lines))
	f.close()








