import random
from PIL import Image
from puzzle import *
from roller import *
# Some function calls that you can try out:

for i in range(100):
    print(roll('JS_logo'))
# Image.open(io.BytesIO(urllib.request.urlopen(url).read())).show()

# size = 100
# url_py_logo = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/Python.png?raw=true'
# py = Puzzle(url_py_logo, size, 'python_logo')
# py.savePieces('../../../images/')
# f = open('../../../images/python_logo/metadata.txt', 'w')
# ls = [str(py.getFullPuzzle().size[0])+','+str(py.getFullPuzzle().size[1]),'',str(len(py.pieces)),'']
# dx,dy = py.pieces[0].coords[0], py.pieces[0].coords[1]
# for piece in py.pieces:
#     ls.append(str(piece.num))
#     ls.append(str(piece.coords[0]-dx)+','+str(piece.coords[1]-dy)+','+str(piece.coords[2]-dx)+','+str(piece.coords[3]-dy))
#     ls.append(str(piece.rarity))
#     ls.append('')

# f.writelines("\n".join(ls))
# f.close()

# url_hu_logo = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/husky.png?raw=true'
# hu = Puzzle(url_hu_logo, size, 'husky_logo')
# hu.savePieces('../../../images/husky_logo/')
# f = open('../../../images/husky_logo/metadata.txt', 'w')
# ls = [str(hu.getFullPuzzle().size[0])+','+str(hu.getFullPuzzle().size[1]),'',str(len(hu.pieces)),'']
# dx,dy = hu.pieces[0].coords[0], hu.pieces[0].coords[1]
# for piece in hu.pieces:
#     ls.append(str(piece.num))
#     ls.append(str(piece.coords[0]-dx)+','+str(piece.coords[1]-dy)+','+str(piece.coords[2]-dx)+','+str(piece.coords[3]-dy))
#     ls.append(str(piece.rarity))
#     ls.append('')

# f.writelines("\n".join(ls))
# f.close()

# url_js_logo = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/JS.png?raw=true'
# js = Puzzle(url_js_logo, size, 'JS_logo')
# js.savePieces('../../../images/JS_logo/')
# f = open('../../../images/JS_logo/metadata.txt', 'w')
# ls = [str(js.getFullPuzzle().size[0])+','+str(js.getFullPuzzle().size[1]),'',str(len(js.pieces)),'']
# dx,dy = js.pieces[0].coords[0], js.pieces[0].coords[1]
# for piece in js.pieces:
#     ls.append(str(piece.num))
#     ls.append(str(piece.coords[0]-dx)+','+str(piece.coords[1]-dy)+','+str(piece.coords[2]-dx)+','+str(piece.coords[3]-dy))
#     ls.append(str(piece.rarity))
#     ls.append('')

# f.writelines("\n".join(ls))
# f.close()

# img = Image.open(puzzlePath)
# img.show()
# p.getFullPuzzle().show()
# print(p.getFullPuzzle().size)
# print('Is ' + str(len(p.pieces)) + ' = ' + str((p.getFullPuzzle().size[0] / size) * (p.getFullPuzzle().size[1] / size)) + ' true?')
# p.showPieces(1,15)
# p.showPieces(16,17)
# p.savePieces()
# p.saveFullPuzzle()
# i = 0
# n = 0
# r = 0
# sr = 0
# ssr = 0
# while i < 1000000:
#     piece = random.choice(p.getPieces())
#     if piece.getRarity() == 'N':
#     	n += 1
#     if piece.getRarity() == 'R':
#     	r += 1
#     if piece.getRarity() == 'SR':
#     	sr += 1
#     if piece.getRarity() == 'SSR':
#     	ssr += 1
#     i += 1
# print(str([n,r,sr,ssr]))
# print(str(p.rarityPool))