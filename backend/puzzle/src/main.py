import random
from puzzleCreator import *

# Some function calls that you can try out:
size = 30
p = Puzzle('../../images/Python_(programming_language).png', size, 'test')
# # # p.getFullPuzzle().show()
# # # print(p.getFullPuzzle().size)
# # # print('Is ' + str(len(p.pieces)) + ' = ' + str((p.getFullPuzzle().size[0] / size) * (p.getFullPuzzle().size[1] / size)) + ' true?')
# # # p.showPieces(1,15)
# # # p.showPieces(16,17)
# # # p.savePieces()
# # # p.saveFullPuzzle()
i = 0
n = 0
r = 0
sr = 0
ssr = 0
while i < 1000000:
    piece = random.choice(p.getPieces())
    if piece.getRarity() == 'N':
    	n += 1
    if piece.getRarity() == 'R':
    	r += 1
    if piece.getRarity() == 'SR':
    	sr += 1
    if piece.getRarity() == 'SSR':
    	ssr += 1
    i += 1
print(str([n,r,sr,ssr]))
# print(str(p.rarityPool))